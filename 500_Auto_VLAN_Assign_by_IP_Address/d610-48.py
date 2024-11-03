#modVLANFinder.py - to determine VLAN ID
#VLAN_info.txt - vlan id and subnet mask

import os, cli
import modVLANFinder #import VLANFinder.py
import inspect

#
#from file name, find the port number
#d610-48.py is 48th port i.e 1/0/48
#
file_name = inspect.getfile(inspect.currentframe())
print (file_name)
file_name = file_name.split('-')
how_many = len(file_name)
print (how_many)
port_number = file_name[how_many - 1]
port_number = port_number.replace(".py","")
print ("port number", port_number)

#
# from netflow table, find the IP address
#
a = 'dohost \"show flow monitor yame-flow cache format table | include 10\.\"'
stream = os.popen(a)
output = stream.read()
print("Source IP address", type(output), output)

if "\n" in output:   #if line is there, run this line. If not, do nothing.
    print("39th line n detected")
    IP_address = output.replace("\n","").replace(" ","").replace(" ","")

    message = "line_is_detected"
    message = f'dohost \"send log \"****{message}\"\"'
    stream = os.popen(message)

    if IP_address.count('.') > 2: #if IP address is there, run thie if. If not, do nothing.
        message = "source_address_is_" + IP_address
        message = f'dohost \"send log \"****{message}\"\"'
        stream = os.popen(message)

        VLAN_ID = modVLANFinder.VLANFinder (IP_address)
        command1 = 'interface g1/0/' + port_number
        command2 = 'switch access vlan ' + VLAN_ID

        message = "VLAN_ID_is_" + VLAN_ID
        message = f'dohost \"send log \"****{message}\"\"'
        stream = os.popen(message)

        print("VLAN_APPLY_command:::", command1, command2)
        result = cli.configure([command1, command2])
        print ("Applied result ", type(result), result)

        message = result.replace("\n","_").replace("\n","_").replace("  ","_").replace("  ","_").replace(" ","_").replace(" ","_").replace(" ","_").replace(" ","_").replace(" ","_").replace(" ","_").replace(" ","_").replace(" ","_").replace(" ","_").replace(" ","_").replace(" ","_").replace(" ","_").replace(" ","_").replace(" ","_")
        print ("message is", message)
        message = f'dohost \"send log \"****{message}\"\"'
        stream = os.popen(message)
'''
event manager applet G1/0/48_up_event
 event syslog pattern "LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet1/0/48, changed state to up"
 action 1.0 cli command "send log ##### EEM started for 1/0/48 - Wait 5 sec"
 action 2.0 cli command "enable"
 action 5.0 wait 5
 action 6.0 cli command "send log ##### python code called"
 action 8.0 cli command "guestshell run python3 d610-48.py"
 action 9.0 cli command "send log ##### EEM completed for 1/0/48"
 '''