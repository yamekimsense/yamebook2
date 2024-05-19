
def AP_NAME_FINDER(AP_MAC):
    f = open("c901_ap_list.txt", 'r')
    lines = f.readlines()
    for line in lines:
        if AP_MAC in line:
            #print(line)
            AP_NAME = line
    f.close()

    AP_NAME = AP_NAME[0:34]

    for i in range(0, 35):
        AP_NAME = AP_NAME.rstrip()

    #print (AP_NAME)
    return(AP_NAME)

if __name__ == "__main__":
    AP_MAC = "345d.a8ce.2100"
    AP_NAME = AP_NAME_FINDER(AP_MAC)
    print (AP_NAME)
