import sqlite3
from PIL import Image, ImageDraw, ImageFont
import os


path = "/Users/wankim/Documents/Py/yamebook2_youtube_not_git/200-WIFI-status-map/show_tech_wirelss"
file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith(".db")]
file_list_py = sorted (file_list_py )

for db_name in file_list_py:
    conn = sqlite3.connect( path+"/"+db_name)
    cur = conn.cursor()
    floor_all = [0,0,11,15,16,16,16,16,16,16,16,16,16]
    for floor_now in range (2,10):
        floor_each = floor_all[floor_now]
        #
        # draw for each AP
        img = Image.open( 'floor-map/Slide1'+str(floor_now)+".png"  ).convert('RGB')
        color = (0, 0, 0)
        font_size = 50
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", font_size)
        draw = ImageDraw.Draw(img)
        #
        for AP_EACH in range (1, floor_each + 1):
            #print (AP_EACH)
            command = "select * from A where APNAME = \'XXX_XX_" + str(floor_now) + "F_AP" + str(AP_EACH) +"\';"
            cur.execute(command)
            rows = cur.fetchall()
            if len(rows) > 0:
                APNAME = rows[0][0]
                CHAN  = rows[0][1]
                POWER = rows[0][2]
                CLIENT = rows[0][3]
                #
                CU = rows[0][4]
                RX = rows[0][5]
                TX = rows[0][6]
                INF = rows[0][7]
                print (APNAME, CHAN, POWER, CU, CLIENT, CU, RX, TX, INF)
                #
                #location check
                f = open("location.text", 'r')
                lines = f.readlines()
                for line in lines:
                    if APNAME== line.split(",")[0]:
                        #print (APNAME, line.split(",")[1], line.split(",")[2] )
                        location_x = int (line.split(",")[1])
                        location_y = int (line.split(",")[2])
                        #print (APNAME, location_x, location_y)
                f.close()
                #
                text_pos = (location_x, location_y)
                draw.text(text_pos, CHAN+" / "+POWER+" / "+CLIENT, color, font=font)
                text_pos = (location_x, location_y+60)
                draw.text(text_pos, CU +" / "+ RX +" / "+ TX +" / "+ INF, color, font=font)

        text_pos = (400, 100)
        draw.text(text_pos, db_name, color, font=font)
        # img.show()
        print("printing ", db_name.replace(".db", "") + "_" + str(floor_now) + "F.png")
        img = img.save("floor-map-result/"+db_name.replace(".db", "") + "_" + str(floor_now) + "F.png")

    conn.close()
