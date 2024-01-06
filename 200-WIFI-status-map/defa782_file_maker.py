
import linecache

def defa782_file_maker(show_tech_file_name, show_load_info_start_line, show_load_info_end_line, show_summary_start_line, show_summary_end_line, show_ap_start_line, show_ap_end_line):

    #show_load_info
    f = open(show_tech_file_name.replace(".log","") + ".load_info.text" ,"w" )
    for line_number in range (show_load_info_start_line+4, show_load_info_end_line-1):
        print (line_number, linecache.getline(show_tech_file_name, line_number), end="")
        f.write (linecache.getline(show_tech_file_name, line_number))
    f.close()

    print ("------------------")

    # show_summary
    f = open(show_tech_file_name.replace(".log", "") + ".summary.text", "w")
    for line_number in range(show_summary_start_line + 8, show_summary_end_line - 1):
        print(line_number, linecache.getline(show_tech_file_name, line_number), end="")
        f.write(linecache.getline(show_tech_file_name, line_number))
    f.close()

    print ("------------------")

    # show_ap
    f = open(show_tech_file_name.replace(".log", "") + ".ap.text", "w")
    for line_number in range(show_ap_start_line, show_ap_end_line - 1):

        line_content = linecache.getline(show_tech_file_name, line_number)
        if "Name"  in line_content:
            print(line_number, line_content, end="")
            f.write(line_content)

        if "Util"  in line_content:
            print(line_number, line_content, end="")
            f.write(line_content)


    f.close()


if __name__ == "__main__":
    show_tech_file_name = "/Users/wankim/Documents/Py/yamebook2_youtube_not_git/200-WIFI-status-map/show_tech_wirelss/20230530_1434.log"

    show_load_info_start_line = 161888
    show_load_info_end_line = 162025

    show_summary_start_line = 141837
    show_summary_end_line = 141977

    show_ap_start_line = 124359
    show_ap_end_line = 141053

    defa782_file_maker (show_tech_file_name, show_load_info_start_line, show_load_info_end_line, show_summary_start_line, show_summary_end_line, show_ap_start_line, show_ap_end_line)
