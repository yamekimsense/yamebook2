import os
import sqlite3


path = "/Users/wankim/Documents/Py/yamebook2_youtube_not_git/200-WIFI-status-map/show_tech_wirelss"
file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith(".db")]

file_list_py = sorted (file_list_py )

for file_name in file_list_py:
    db_file_name = path + "/" + file_name
    print ("\n\n", file_name,"POWER CLIENT CU RX TX INF")

    conn = sqlite3.connect(db_file_name)
    cur = conn.cursor()

    for floor in range (2,10):
        sqlite3_command =  f"select round(avg(POWER),1), round(avg(CLIENT),1), round(avg(CU),1), round(AVG(RX),1), round(AVG(TX),1), round(AVG(INF),1) from a where APNAME LIKE \'XXX_XX_{floor}F%\';"
        #print (sqlite3_command)
        cur.execute(sqlite3_command)
        for row in cur:
            print(floor, row)
    conn.commit()








