
import linecache

def defa784_file_maker(show_tech_file_name):

    f = open(show_tech_file_name.replace(".log", "") + ".ap.text", "r")
    ff = open (show_tech_file_name.replace(".log", "") + ".ap2.text", "w")
    while True:
        lines1 = f.readline()
        if not lines1: break
        lines2 = f.readline()
        lines3 = f.readline()
        lines4 = f.readline()

        lines1 = lines1.split(":")
        lines1 = lines1[1].replace(" ", "").replace(" ", "").replace(" ", "").replace(" ", "").replace(" ", "").replace(
            "\n", "").replace("%", "")
        # print (lines1)

        lines2 = lines2.split(":")
        lines2 = lines2[1].replace(" ", "").replace(" ", "").replace(" ", "").replace(" ", "").replace(" ", "").replace(
            "\n", "").replace("%", "")
        # print (lines2)

        lines3 = lines3.split(":")
        lines3 = lines3[1].replace(" ", "").replace(" ", "").replace(" ", "").replace(" ", "").replace(" ", "").replace(
            "\n", "").replace("%", "")
        # print (lines3)

        lines4 = lines4.split(":")
        lines4 = lines4[1].replace(" ", "").replace(" ", "").replace(" ", "").replace(" ", "").replace(" ", "").replace(
            "\n", "").replace("%", "")
        # print (lines4)

        AP_NAME = lines1
        RX = lines2
        TX = lines3
        CU = lines4
        print(AP_NAME, RX, TX, CU, (int(CU) - int(TX) - int(RX)))
        context = AP_NAME+" "+RX+" "+TX+" "+CU+" "+ str(int(CU) - int(TX) - int(RX))+"\n"
        print(context)
        ff.write (context)
    print ("### end of defa784 ###")
    f.close()
    ff.close()


if __name__ == "__main__":

    show_tech_file_name = "/Users/wankim/Documents/Py/yamebook2_youtube_not_git/200-WIFI-status-map/show_tech_wirelss/20230530_1434.log"
    defa784_file_maker (show_tech_file_name)
