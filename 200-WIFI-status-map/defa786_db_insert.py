
import sqlite3

def defa786_db_insert(show_tech_file_name, show_tech_file_name_short):

    print ("### start of 786####")
    print (show_tech_file_name)
    print (show_tech_file_name_short)

    db_name = show_tech_file_name

    conn = sqlite3.connect(db_name + ".db")
    cur = conn.cursor()

    table_name = "a"

    cur.execute(
        "CREATE TABLE " + table_name + " (APNAME text, CHAN text, POWER text,  CLIENT text, CU text, RX text, TX text, INF text)")

    file_name = db_name
    summary_file_name = show_tech_file_name.replace(".log", "") + ".summary.text"
    load_file_name = show_tech_file_name.replace(".log","") + ".load_info.text"
    traffic_file_name = show_tech_file_name.replace(".log", "") + ".ap2.text"

    f = open(summary_file_name, 'r')
    for line in f:

        if line[0:7] == "XXX_XX_":
            APNAME = line[0:14].replace(" ", "").replace(" ", "").replace(" ", "").replace(" ", "").replace(" ", "")
            CHAN = line[112:120].replace("(", "").replace(")", "").replace("*", "").replace(" ", "").replace(" ",
                                                                                                             "").replace(
                " ", "").replace(" ", "")
            POWER = line[97:98].replace(" ", "").replace(" ", "").replace(" ", "").replace(" ", "").replace(" ", "")
            input_data = []
            input_data.append(APNAME)
            input_data.append(CHAN)
            input_data.append(POWER)

            print("APNAME CHAN POWER", input_data)
            cur.execute("INSERT INTO " + table_name + " (APNAME, CHAN, POWER) VALUES (?,?,?);", input_data)
            conn.commit()
    f.close()

    f = open(load_file_name, 'r')
    for line in f:
        if line[0:7] == "XXX_XX_":
            APNAME = line[0:14].replace(" ", "")
            CU = line[77:79].replace(" ", "")
            CLIENT = line[86:88].replace(" ", "")

            print("APNAME CLIENT CU", APNAME, CLIENT, CU)
            cur.execute("update " + table_name + " set CLIENT = \'" + CLIENT + "\' where APNAME = \'" + APNAME + "\';")
            cur.execute("update " + table_name + " set CU = \'" + CU + "\' where APNAME = \'" + APNAME + "\';")

            conn.commit()
    f.close()

    f = open(traffic_file_name, 'r')
    for line in f:
        if line[0:7] == "XXX_XX_":
            list = line.split(" ")
            APNAME = list[0].replace(" ", "")
            RX = list[1].replace(" ", "")
            TX = list[2].replace(" ", "")
            INF = list[4].replace(" ", "").replace("\n", "")

            print("APNAME, RX, TX, INF", APNAME, RX, TX, INF)
            cur.execute("update " + table_name + " set RX = \'" + RX + "\' where APNAME = \'" + APNAME + "\';")
            cur.execute("update " + table_name + " set TX = \'" + TX + "\' where APNAME = \'" + APNAME + "\';")
            cur.execute("update " + table_name + " set INF = \'" + INF + "\' where APNAME = \'" + APNAME + "\';")

            conn.commit()
    f.close()


if __name__ == "__main__":
    show_tech_file_name = "/Users/wankim/Documents/Py/yamebook2_youtube_not_git/200-WIFI-status-map/show_tech_wirelss/20230530_1434.log"
    show_tech_file_name_short = "20230530_1434.log"
    defa786_db_insert(show_tech_file_name, show_tech_file_name_short )