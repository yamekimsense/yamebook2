
def defa780_line_number_get(show_tech_file_name):
    show_load_info_start = "------------------ show ap dot11 5ghz load-info ------------------"
    show_load_info_end = "------------------ show ap dot11 24ghz load-info ------------------"

    show_summary_start = "------------------ show ap dot11 5ghz summary ------------------"
    show_summary_end = "------------------ show ap dot11 5ghz summary extended ------------------"

    show_ap_start = "------------------ show ap auto-rf dot11 5ghz ------------------"
    show_ap_end = "------------------ show ap dot11 24ghz bss-color ------------------"


    i = 1
    print ("###a780_module_start")


    f = open(show_tech_file_name,"r")
    lines = f.readlines()
    for line in lines:
        #print (i, line)
        if show_load_info_start in line:
            show_load_info_start_line = i

        if show_load_info_end in line:
            show_load_info_end_line = i-1

        if show_summary_start in line:
            show_summary_start_line = i

        if show_summary_end in line:
            show_summary_end_line = i-1

        if show_ap_start in line:
            show_ap_start_line = i

        if show_ap_end in line:
            show_ap_end_line = i-1

        i = i + 1
    f.close()

    print (show_load_info_start_line)
    print (show_load_info_end_line)

    print (show_summary_start_line)
    print (show_summary_end_line)

    print (show_ap_start_line)
    print (show_ap_end_line)

    print (show_load_info_start_line, show_load_info_end_line, show_summary_start_line, show_summary_end_line, show_ap_start_line, show_ap_end_line)
    print ("#### a780 module end####")
    return (show_load_info_start_line, show_load_info_end_line, show_summary_start_line, show_summary_end_line, show_ap_start_line, show_ap_end_line)

if __name__ == "__main__":
    show_tech_file_name = "show_tech_wirelss/20230530_1434.log"
    defa780_line_number_get(show_tech_file_name)