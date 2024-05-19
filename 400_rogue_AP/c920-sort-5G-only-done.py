#pip3 install netmiko

from netmiko import ConnectHandler
from ModC910FindApName import *
from ModC920MacVendorFinder import *

#
# Make the AP list from 5Ghz and 2.4Ghz
# Save as as_list.txt
#
wlc = {
    'device_type' : 'cisco_ios',
    'host' : "192.168.1.7",
    'username' : "cisco",
    'password' : "cisco"
}

net_connect = ConnectHandler(**wlc)

f = open ('c901_ap_list.txt','w')

output = net_connect.send_command ('show ap dot11 5ghz load-info')
#print (output)
f.write(output)

output = net_connect.send_command ('show ap dot11 24ghz load-info')
#print (output)
f.write(output)

f.close()



#
# Get the rogue AP List
#

f = open ('c902_rogue_AP_list.txt','w')
output = net_connect.send_command ('show wireless wps rogue ap summary')
#print (output)
f.write(output)
f.close()



f = open("c902_rogue_AP_list.txt", 'r')

i = 0
lines = f.readlines()


f = open("c903_result_for_sort.txt", 'w')

for line in lines:
    i = i + 1

    if i > 13 :
        #
        #Rogue AP MAC and vendor
        #
        AP_MAC = line[0:7].replace(".","").replace(".","")
        #print ("AP_MAC", AP_MAC)
        AP_MAC = AP_MAC.upper()
        #print("AP_MAC", AP_MAC)

        ROGUE_AP_VENDOR = MAC_VENDOR_FINDER(AP_MAC)

        #
        #Detect AP MAC and host name
        #
        AP_MAC = line[82:96]
        #print ("AP_MAC", AP_MAC)
        AP_NAME_RESULT = AP_NAME_FINDER(AP_MAC)
        #print (AP_MAC_6digit, MAC_VENDOR, AP_MAC, AP_NAME_RESULT)
        line = line.replace("\n","")
        #print (len(line))

        while len(line) < 122:
            line = line + " "

        line = line + AP_NAME_RESULT

        while len(line) < 145:
            line = line + " "
        #print ("**", len(line) )
        #print (line, ROGUE_AP_VENDOR)
        f.write(line+ROGUE_AP_VENDOR+"\n")
f.close()


f = open("c903_result_for_sort.txt", 'r')
lines = f.readlines()

#
# To sort using RSSI
#

sort = []

for line in lines:
    line = line.replace("\n","")
    RSSI = line[102:108].replace(" ", "").replace(" ", "").replace(" ", "").replace(" ", "").replace(" ", "")
    RSSI = int(RSSI)
    #print (RSSI, type(RSSI))
    each = {}
    each["RSSI"] = RSSI
    each["line"] = line

    #print (each)
    sort.append(each)

print ("MAC Address     Classification  State        #APs  #Clients  Last Heard           Highest-RSSI-Det-AP  RSSI  Channel GHz  Detect_AP_Name        Rogue_AP_Vendor")
print ("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")

data = sorted (sort, key=lambda x:x['RSSI'], reverse = True)


#
#Print Result
#

for each_line in data:
    if each_line['line'][117:118] == '5':
        print (each_line['line'])
    #if each_line['line'][117:118] == '2':
    #    print (each_line['line'])

