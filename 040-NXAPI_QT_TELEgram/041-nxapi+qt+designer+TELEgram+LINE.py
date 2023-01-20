# -*- coding: utf-8 -*-
from datetime import datetime
import socket, requests, json, inspect, time, sys
from defNXapi import *
from defTELEgram import *
from defLINE import *
from PyQt5 import QtCore, QtGui, QtWidgets

csv_file = '042-port-list.csv'
switchuser = 'admin'
switchpassword = '1234Qwer'


def lineno(): #to print line number on print
    return inspect.getlineno(inspect.getouterframes(inspect.currentframe())[-1][0])

def action1():
    print ("----- Action1 -----")
    global address, port_number
    print ("#### LINE #", lineno(), "action1 ", address, port_number)
    command = "inter e " + port_number + " ; sh"
    print("#### LINE #", lineno(), "1st command to execute ", command)
    nxapicall(address, switchuser, switchpassword, command)
    time.sleep(3)
    command = "inter e " + port_number + " ; no sh"
    print("#### LINE #", lineno(), "2nd command to execute ", command)
    nxapicall_result = nxapicall(address, switchuser, switchpassword, command)

    if nxapicall_result == 0:
        TELEgram ("Success of shut/no shut to " + address + " " + port_number )
        LINE_NAVER("Success of shut/no shut to " + address + " " + port_number)
    else:
        TELEgram("Failure of shut/no shut to " + address + " " + port_number)
        LINE_NAVER("Failure of shut/no shut to " + address + " " + port_number)

def action2():
    print ("----- Action2 -----")
    global address_target, port_target
    print (address_target, port_target)
    command = "inter e " + port_target + " ; no description"
    print("#### LINE #", lineno(), "Only One to execute ", command)
    nxapicall_result = nxapicall(address_target, switchuser, switchpassword, command)

    if nxapicall_result == 0:
        TELEgram ("Success of Remove description " + address_target + " eth " + port_target )
        LINE_NAVER("Success of Remove description " + address_target + " eth " + port_target)
    else:
        TELEgram("Failure of Remove description " + address_target + " eth " + port_target)
        LINE_NAVER("Failure of Remove description " + address_target + " eth " + port_target)



class Ui_Dialog(object):
    def setupUi(self, Dialog, address, port_number, address_target, port_target):

        Dialog.setObjectName("Dialog")
        Dialog.resize(669, 241)

        self.btn1 = QtWidgets.QPushButton(Dialog)
        self.btn1.setGeometry(QtCore.QRect(120, 30, 451, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn1.setFont(font)
        self.btn1.setObjectName("btn1")
        self.btn1.clicked.connect(action1)

        self.btn2 = QtWidgets.QPushButton(Dialog)
        self.btn2.setGeometry(QtCore.QRect(120, 110, 451, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn2.setFont(font)
        self.btn2.setObjectName("btn2")
        self.btn2.clicked.connect(action2)

        btn1_display = "Reset " + address + " eth " + port_number
        btn2_display = "Config Remove " + address_target + " eth " + port_target
        self.retranslateUi(Dialog, btn1_display, btn2_display)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog, btn1_display, btn2_display):
        _translate = QtCore.QCoreApplication.translate
        now = datetime.now()
        clock = now.strftime('%Y-%m-%d %H:%M:%S')
        Dialog.setWindowTitle(_translate("Dialog", "Error Disable Detected  " + clock))
        self.btn1.setText(_translate("Dialog", btn1_display))
        self.btn2.setText(_translate("Dialog", btn2_display))


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()

    address = ''
    port_number = ''
    address_target = ''
    port_target = ''

    # SYSLOG server
    UDP_IP = "0.0.0.0"
    UDP_PORT = 514
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        print("#### LINE #", lineno(), "----- Start of Syslog App -----")
        data, addr = sock.recvfrom(1024)
        data_string = data.decode('utf-8')
        print("#### LINE #", lineno(), "syslog printing", addr[0], data_string)

        # detect the Error Disable
        if ("IF_DOWN_ERROR_DISABLED" in data_string) and (not "repeated" in data_string):
            print("-------- ERROR DISABLE detected --------")
            port_number = data_string.split("Ethernet")[1].split(" ")[0]
            address = addr[0]
            print("#### LINE #", lineno(), "issue switch IP and port", address, port_number)

            TELEgram("Error Disabled on " + address + " eth " + port_number)
            LINE_NAVER("Error Disabled on " + address + " eth " + port_number)

            #find the paird port
            f = open(csv_file, 'r')
            lines = f.readlines()
            for line in lines:
                line_split = line.split(",")
                ip1 = line_split[0].replace("\n", "")
                port1 = line_split[1].replace("\n", "")
                ip2 = line_split[2].replace("\n", "")
                port2 = line_split[3].replace("\n", "")
                print("#### LINE #", lineno(), ".csv reading", ip1, port1, ip2, port2)

                # get the pair switch/port
                if (address == ip1) and (port_number == port1):
                    address_target = ip2
                    port_target = port2

                if (address == ip2) and (port_number == port2):
                    address_target = ip1
                    port_target = port1

                print("#### LINE #", lineno(), "pair switch and port", address_target, port_target)
            f.close()

            # to the paired port
            command = "interface e " + port_target + " ; description \"ERROR_DISABLE removed\""
            nxapicall_result = nxapicall(address_target, switchuser, switchpassword, command)

            if nxapicall_result == 0:
                TELEgram("Success of Add description " + address_target + " eth " + port_target)
                LINE_NAVER("Success of Add description " + address_target + " eth " + port_target)
            else:
                TELEgram("Failure of Add description " + address_target + " eth " + port_target)
                LINE_NAVER("Failure of Add description " + address_target + " eth " + port_target)

            ui.setupUi(Dialog, address, port_number, address_target, port_target)
            Dialog.show()
            app.exec_()
