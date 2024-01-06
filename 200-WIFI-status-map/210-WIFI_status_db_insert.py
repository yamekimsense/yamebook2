import os
from defa780_line_number_get import defa780_line_number_get
from defa782_file_maker import defa782_file_maker
from defa784_file_maker import defa784_file_maker
from defa786_db_insert import defa786_db_insert

path = "/Users/wankim/Documents/Py/yamebook2_youtube_not_git/200-WIFI-status-map/show_tech_wirelss"
file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith(".log")]


for file_name in file_list_py:
    show_tech_file_name = path + "/" + file_name
    show_tech_file_name_short = file_name
    print ("**************************************")
    print (show_tech_file_name)

    line_numbers = defa780_line_number_get(show_tech_file_name)

    show_load_info_start_line = line_numbers[0]
    show_load_info_end_line = line_numbers[1]
    show_summary_start_line = line_numbers[2]
    show_summary_end_line = line_numbers[3]
    show_ap_start_line = line_numbers[4]
    show_ap_end_line = line_numbers[5]

    print (show_tech_file_name, show_load_info_start_line, show_load_info_end_line, show_summary_start_line, show_summary_end_line, show_ap_start_line, show_ap_end_line)

    defa782_file_maker(show_tech_file_name, show_load_info_start_line, show_load_info_end_line, show_summary_start_line, show_summary_end_line, show_ap_start_line, show_ap_end_line)

    defa784_file_maker(show_tech_file_name)

    defa786_db_insert (show_tech_file_name, show_tech_file_name_short)

