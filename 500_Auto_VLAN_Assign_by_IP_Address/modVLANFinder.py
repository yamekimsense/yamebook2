
import ipaddress

def VLANFinder(IP_address):
    f = open("VLAN_info.txt", 'r')
    lines = f.readlines()
    for line in lines:
        #print(line)
        VLAN_ID = line.split(",")[0]
        NETWORK_MASK = line.split(",")[1].replace("\n","")
        #print ("#### line 8", VLAN_ID, NETWORK_MASK)

        if ipaddress.ip_address(IP_address) in ipaddress.ip_network(NETWORK_MASK) :
            print ("#### line 14", VLAN_ID, NETWORK_MASK)
            VLAN_ID_RESULT = VLAN_ID
    f.close()
    return VLAN_ID_RESULT

if __name__ == "__main__":
    IP_address = '10.1.100.2'
    VLAN_ID_RESULT = VLANFinder(IP_address)
    print ("#### line 22", VLAN_ID_RESULT)
