
def MAC_VENDOR_FINDER( AP_MAC_6digit ):
    AP_VENDOR = ""
    f = open("c900-mac-vendor.txt", 'r')
    lines = f.readlines()
    for line in lines:
        if AP_MAC_6digit in line:
            AP_VENDOR = line
    f.close()

    #print (AP_VENDOR)

    if AP_VENDOR == "":
            AP_VENDOR = "000000	unknown"
            #print ( "***c841_L15", AP_MAC_6digit, AP_VENDOR)
    AP_VENDOR = AP_VENDOR[7:].replace("\n","")

    #print (AP_VENDOR)
    return(AP_VENDOR)



if __name__ == "__main__":
    line = "0007.8930.bd84  Unclassified    Alert        2     0         06/05/2023 11:40:41  345d.a8cd.7a20       -77   6       2.4"
    AP_MAC_6digit = line[0:7].replace(".","")
    print ( MAC_VENDOR_FINDER(AP_MAC_6digit) )
