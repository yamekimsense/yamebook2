#pip install paramiko

from z100credential import *
import paramiko, time, datetime

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, username=id, password=password)

while 1>0:
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('top -b -n 1')
    msg = ssh_stdout.read().decode("euc-kr")
    msg_dict = msg.split('\n')
    print ("\n\n\n", datetime.datetime.now())
    for line_number in range (7,len(msg_dict)-1):
        CPU_UTIL = msg_dict[line_number][47:53].replace("\n","").replace(" ","").replace(" ","").replace(" ","").replace(" ","").replace(" ","").replace(" ","")
        PROCESS_NAME = msg_dict[line_number][68:].replace("\n","")
        if float(CPU_UTIL) > 30:
            print (CPU_UTIL, PROCESS_NAME)
    time.sleep(3)

'''
while 1>0:
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('top -b -n 1 | grep nginx.bin')
    #ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('top -b -n 1')
    msg = ssh_stdout.read().decode("euc-kr")
    msg_2 = msg.replace("\n", "")
    print(datetime.datetime.now(), msg_2[-32:])
    #print (msg)
    #print (msg_2)
    time.sleep(3)
'''