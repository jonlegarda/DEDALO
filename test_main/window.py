from tkinter import *
from tkinter import ttk
from tkinter.ttk import Notebook, Separator
from tkinter import messagebox as MessageBox
import utils
#csv
import csv
import os
from tkinter import filedialog as Filedialog

from shodan_handler import ShodanQuery, shodan_query_creator
from test_main.nmap_handler import scan_ip_port
from zoomeye_handler import ZoomEyeQuery, zoomeye_query_creator
import constants as var
from window_statistics import WindowStatistics
from window_history import WindowHistory
from window_about_us import WindowAboutUs
from window_vulnerabilities import WindowVulnerabilities
from window_api_configuration import WindowApiConfiguration
import time



class MainWindowHandler:
    # window is the main object that creates the window.
    window = Tk()
    window_title = var.window_title
    window_size = var.window_size

    # shodan_query is the object of Shodan
    shodan_query = ShodanQuery()
    # zoomeye_query is the object of ZoomEye
    zoomeye_query = ZoomEyeQuery()

    # Method to initialize the Object.
    def __init__(self):
        # window settings.
        self.window.geometry(self.window_size)
        self.window.title(self.window_title)

        self.notebook = Notebook(self.window)
        self.notebook.pack(padx=10, pady=10, fill="both", expand=True)

        # Main Window
        self.frame_main_nbook = Frame(self.notebook)
        self.frame_main_nbook.grid(sticky="nsew")
        # Statistics Window.
        self.frame_statistics_nbook = Frame(self.notebook)
        # API Window
        self.frame_api_nbook = Frame(self.notebook)
        # About Us
        self.frame_about_us_nbook = Frame(self.notebook)
        self.frame_history_nbook = Frame(self.notebook)

        # methods to display the windows and their elements
        self.display_nbook_main(self.frame_main_nbook)
        WindowStatistics(self.frame_statistics_nbook, self.shodan_query, self.zoomeye_query)
        WindowApiConfiguration(self.frame_api_nbook, self.shodan_query, self.zoomeye_query)
        WindowHistory(self.frame_history_nbook, self.shodan_query, self.zoomeye_query)
        WindowAboutUs(self.frame_about_us_nbook)

        # method to add the Main window and Shodan API window to the notebook.
        self.notebook.add(self.frame_main_nbook, text=var.window_main, padding=10)
        self.notebook.add(self.frame_statistics_nbook, text=var.window_statistics, padding=10)
        self.notebook.add(self.frame_history_nbook, text=var.window_history, padding=10)
        self.notebook.add(self.frame_api_nbook, text=var.window_api, padding=10)
        self.notebook.add(self.frame_about_us_nbook, text=var.window_about_us, padding=10)

    # Method to display all the elements of the Main window.
    def display_nbook_main(self, frame):

        lframe_main_search = LabelFrame(frame, text=var.main_window_search_title)
        lframe_main_search.grid(column=0, row=0)
        ##### La idea es una organización jerárquica: LabelFrame (lframe_group) -> Entry, Label, etc.
        self.lbl_ip_1 = Label(lframe_main_search, text=var.label_simpletext_1).grid(column=0, row=0,
                                                                                    padx=var.group_1_padx,
                                                                                    pady=var.group_1_pady)
        self.txt_simpletext = Entry(lframe_main_search, width=var.text_entry_size)
        self.txt_simpletext.grid(column=1, row=0, padx=var.group_1_padx, pady=var.group_1_pady)
        #lbl_ip_2 = Label(lframe_main_search, text=var.text_label_simpletext_2).grid(column=2, row=0, padx=var.group_1_padx,
        #                                                                       pady=var.group_1_pady)

        self.lbl_ip_1 = Label(lframe_main_search, text=var.label_ip_1).grid(column=0, row=1, padx=var.group_1_padx,
                                                                            pady=var.group_1_pady)
        self.txt_ip = Entry(lframe_main_search, width=var.text_entry_size)
        self.txt_ip.grid(column=1, row=1, padx=var.group_1_padx, pady=var.group_1_pady)
        #lbl_ip_2 = Label(lframe_main_search, text=var.text_label_ip_2).grid(column=2, row=1, padx=var.group_1_padx,
        #                                                               pady=var.group_1_pady)

        label_ip_net= Label(lframe_main_search, text=var.label_ip_net).grid(column=0, row=2,
                                                                                 padx=var.group_1_padx,
                                                                                 pady=var.group_1_pady)
        self.txt_ip_net = Entry(lframe_main_search, width=var.text_entry_size)
        self.txt_ip_net.grid(column=1, row=2, padx=var.group_1_padx, pady=var.group_1_pady)

        sep_1 = ttk.Separator(lframe_main_search, orient="vertical").grid(column=2, row=0, rowspan=3, sticky="ns")

        lbl_port_1 = Label(lframe_main_search, text=var.label_port_1).grid(column=3, row=0, padx=var.group_1_padx,
                                                                           pady=var.group_1_pady)
        self.txt_port = Entry(lframe_main_search, width=var.text_entry_size)
        self.txt_port.grid(column=4, row=0, padx=var.group_1_padx, pady=var.group_1_pady)
        # lbl_port_2 = Label(lframe_main_search, text=var.text_label_port_2).grid(column=6, row=3, padx=var.group_1_padx,
        #                                                                   pady=var.group_1_pady)

        lbl_protocol_1 = Label(lframe_main_search, text=var.label_protocol_1).grid(column=3, row=1,
                                                                                   padx=var.group_1_padx,
                                                                                   pady=var.group_1_pady)
        self.txt_protocol = Entry(lframe_main_search, width=var.text_entry_size)
        self.txt_protocol.grid(column=4, row=1, padx=var.group_1_padx, pady=var.group_1_pady)
        #lbl_protocol_2 = Label(lframe_main_search, text=var.text_label_protocol_2).grid(column=6, row=0,
        #                                                                           padx=var.group_1_padx,
        #                                                                           pady=var.group_1_pady)

        lbl_os_1 = Label(lframe_main_search, text=var.label_os_1).grid(column=3, row=2, padx=var.group_1_padx,
                                                                       pady=var.group_1_pady)
        self.txt_os = Entry(lframe_main_search, width=var.text_entry_size)
        self.txt_os.grid(column=4, row=2, padx=var.group_1_padx, pady=var.group_1_pady)
        #lbl_os_2 = Label(lframe_main_search, text=var.text_label_os_2).grid(column=6, row=1, padx=var.group_1_padx,
        #                                                               pady=var.group_1_pady)

        sep_2 = ttk.Separator(lframe_main_search, orient="vertical").grid(column=5, row=0, rowspan=3, sticky="ns")

        lbl_server_1 = Label(lframe_main_search, text=var.label_server_1).grid(column=6, row=0, padx=var.group_1_padx,
                                                                               pady=var.group_1_pady)
        self.txt_server = Entry(lframe_main_search, width=var.text_entry_size)
        self.txt_server.grid(column=7, row=0, padx=var.group_1_padx, pady=var.group_1_pady)
        #lbl_server_2 = Label(lframe_main_search, text=var.text_label_server_2).grid(column=6, row=2, padx=var.group_1_padx,
        #                                                                       pady=var.group_1_pady)


        lbl_city_1 = Label(lframe_main_search, text=var.label_city_1).grid(column=6, row=1, padx=var.group_1_padx,
                                                                           pady=var.group_1_pady)
        self.txt_city = Entry(lframe_main_search, width=var.text_entry_size)
        self.txt_city.grid(column=7, row=1, padx=var.group_1_padx, pady=var.group_1_pady)
        # lbl_city_2 = Label(lframe_main_search, text=var.text_label_city_2).grid(column=2, row=3, padx=var.group_1_padx,
        #                                                                   pady=var.group_1_pady)

        lbl_country_1 = Label(lframe_main_search, text=var.label_country_1).grid(column=6, row=2,
                                                                                 padx=var.group_1_padx,
                                                                                 pady=var.group_1_pady)
        self.txt_country = Entry(lframe_main_search, width=var.text_entry_size)
        self.txt_country.grid(column=7, row=2, padx=var.group_1_padx, pady=var.group_1_pady)

        #lbl_country_2 = Label(lframe_main_search, text=var.text_label_country_2).grid(column=2, row=2,
        #                                                                         padx=var.group_1_padx,
        #                                                                         pady=var.group_1_pady)

        sep_3 = ttk.Separator(lframe_main_search, orient="vertical").grid(column=8, row=0, rowspan=3, sticky="ns")

        """
        lbl_country_list_1 = Label(lframe_group1, text=self.text_label_country_list_1).grid(column=4, row=3,
                                                                                  padx=self.group_1_padx,
                                                                                  pady=self.group_1_pady)
        clicked_country = StringVar()
        clicked_country.set(country_list[0])
        self.txt_country_list = OptionMenu(lframe_group1, clicked_country, *country_list).grid(column=5, row=3,
                                                                                  padx=self.group_1_padx,
                                                                                  pady=self.group_1_pady)
        """

        #btn_execute = Button(lframe_main_search, text="Run Shodan Query!", width=20, height=2, command=self.run_shodan_query)
        #btn_execute.grid(column=0, row=4, padx=10, columnspan=7)

        btn_execute = Button(lframe_main_search, text=var.button_run_shodan_query, width=12, height=5, command=self.run_shodan_query)
        btn_execute.grid(column=10, row=0, rowspan=3, padx=5, pady=5)

        btn_execute = Button(lframe_main_search, text=var.button_run_zoomeye_query, width=12, height=5,command=self.run_zoomeye_query)
        btn_execute.grid(column=11, row=0, rowspan=3, padx=5, pady=5)

        button_both_queries = Button(lframe_main_search, text=var.button_both_queries, width=20,command=self.run_both_queries)
        button_both_queries.grid(column=12, row=0, rowspan=2, padx=5)

        button_clean_form = Button(lframe_main_search, text=var.button_clean_form, width=20, command=self.clean_form)
        button_clean_form.grid(column=12, row=2, padx=5)

        #lframe_main_search = LabelFrame(frame, text=var.main_window_search_title)

        lframe_query_summary = LabelFrame(self.frame_main_nbook, text=var.window_query_summary)
        lframe_query_summary.grid(column=0, row=1, sticky="nsew")

        """"
        self.lbl_shodanvar = Tk.StringVar()
        self.lbl_shodanvar.set(shodan_last_query)
        self.lbl_shodan = Label(lframe_query_summary, textvariable=self.lbl_shodanvar).grid(column=0, row=0, padx=var.group_1_padx,pady=var.group_1_pady)
        """

        lbl_shodan_results_txt = Label(lframe_query_summary, text=var.shodan_txt + var.last_query_results).grid(column=0, row=0, padx=var.group_1_padx,pady=var.group_1_pady)

        self.lbl_shodan_total_results_txt_value = StringVar()
        self.lbl_shodan_total_results_txt_value.set(var.empty_value)
        self.lbl_shodan_total_results = Label(lframe_query_summary, textvariable=self.lbl_shodan_total_results_txt_value).grid(column=1, row=0,padx=var.group_1_padx,pady=var.group_1_pady)

        lbl_shodan_elapsed_txt = Label(lframe_query_summary, text=var.last_query_elapsed_time).grid(column=2, row=0, padx=var.group_1_padx, pady=var.group_1_pady)

        self.lbl_shodan_elapsed_time_txt_value = StringVar()
        self.lbl_shodan_elapsed_time_txt_value.set(var.empty_value)
        self.lbl_shodan_elapsed_time_results = Label(lframe_query_summary, textvariable=self.lbl_shodan_elapsed_time_txt_value).grid(column= 3, row=0,padx=var.group_1_padx,pady=var.group_1_pady)

        lbl_shodan_query_txt = Label(lframe_query_summary, text=var.last_query_txt).grid(column=4, row=0, padx=var.group_1_padx, pady=var.group_1_pady)

        self.lbl_shodan_last_query_txt_value = StringVar()
        self.lbl_shodan_last_query_txt_value.set(var.empty_value)
        self.lbl_shodan_last_query_results = Label(lframe_query_summary, textvariable=self.lbl_shodan_last_query_txt_value).grid(column=5, row=0,padx=var.group_1_padx,pady=var.group_1_pady)

        self.lbl_shodan_total_results_txt_value = StringVar()
        self.lbl_shodan_total_results_txt_value.set(var.empty_value)
        self.lbl_shodan_total_results = Label(lframe_query_summary, textvariable=self.lbl_shodan_total_results_txt_value).grid(column=1, row=0,padx=var.group_1_padx,pady=var.group_1_pady)

        lbl_shodan_elapsed_txt = Label(lframe_query_summary, text=var.last_query_elapsed_time).grid(column=2, row=0, padx=var.group_1_padx, pady=var.group_1_pady)

        self.lbl_shodan_elapsed_time_txt_value = StringVar()
        self.lbl_shodan_elapsed_time_txt_value.set(var.empty_value)
        self.lbl_shodan_elapsed_time_results = Label(lframe_query_summary, textvariable=self.lbl_shodan_elapsed_time_txt_value).grid(column= 3, row=0,padx=var.group_1_padx,pady=var.group_1_pady)

        lbl_shodan_query_txt = Label(lframe_query_summary, text=var.last_query_txt).grid(column=4, row=0, padx=var.group_1_padx, pady=var.group_1_pady)

        self.lbl_shodan_last_query_txt_value = StringVar()
        self.lbl_shodan_last_query_txt_value.set(var.empty_value)
        self.lbl_shodan_last_query_results = Label(lframe_query_summary, textvariable=self.lbl_shodan_last_query_txt_value).grid(column=5, row=0,padx=var.group_1_padx,pady=var.group_1_pady)


        lbl_zoomeye_results_txt = Label(lframe_query_summary, text=var.zoomeye_txt + var.last_query_results).grid(column=0, row=1, padx=var.group_1_padx,pady=var.group_1_pady)

        self.lbl_zoomeye_total_results_txt_value = StringVar()
        self.lbl_zoomeye_total_results_txt_value.set(var.empty_value)
        self.lbl_zoomeye_total_results = Label(lframe_query_summary, textvariable=self.lbl_zoomeye_total_results_txt_value).grid(column=1, row=1,padx=var.group_1_padx,pady=var.group_1_pady)

        lbl_zoomeye_elapsed_txt = Label(lframe_query_summary, text=var.last_query_elapsed_time).grid(column=2, row=1, padx=var.group_1_padx, pady=var.group_1_pady)

        self.lbl_zoomeye_elapsed_time_txt_value = StringVar()
        self.lbl_zoomeye_elapsed_time_txt_value.set(var.empty_value)
        self.lbl_zoomeye_elapsed_time_results = Label(lframe_query_summary, textvariable=self.lbl_zoomeye_elapsed_time_txt_value).grid(column= 3, row=1,padx=var.group_1_padx,pady=var.group_1_pady)

        lbl_zoomeye_query_txt = Label(lframe_query_summary, text=var.last_query_txt).grid(column=4, row=1, padx=var.group_1_padx, pady=var.group_1_pady)

        self.lbl_zoomeye_last_query_txt_value = StringVar()
        self.lbl_zoomeye_last_query_txt_value.set(var.empty_value)
        self.lbl_zoomeye_last_query_results = Label(lframe_query_summary, textvariable=self.lbl_zoomeye_last_query_txt_value).grid(column=5, row=1,padx=var.group_1_padx,pady=var.group_1_pady)



        #self.shodan_top_1_value = StringVar()
        #self.shodan_top_1_value.set(var.tbd_stats)
        #label_shodantop1 = Label(frame_stats_compare, text=var.top1, width=10).grid(column=0, row=1, padx=var.group_1_padx, pady=var.group_1_pady)
        #label_shodantop1_value = Label(frame_stats_compare, textvariable=self.shodan_top_1_value, width=30).grid(column=1, row=1, padx=var.group_1_padx, pady=var.group_1_pady)


        """
        self.lbl_shodan_query_txt = Label(lframe_query_summary, text=var.last_query_txt + "-").grid(column=1, row=0,padx=var.group_1_padx,pady=var.group_1_pady)
        self.lbl_shodan_query_results = Label(lframe_query_summary, text=var.last_query_results + "-").grid(column=4, row=0,
                                                                                       padx=var.group_1_padx,
                                                                                       pady=var.group_1_pady)
        self.lbl_shodan_query_elapsed_time = Label(lframe_query_summary, text=var.last_query_elapsed_time + "-").grid(column=6, row=0,
                                                                                       padx=var.group_1_padx,
                                                                                       pady=var.group_1_pady)
        self.lbl_zoomeye_query = Label(lframe_query_summary, text=var.zoomeye_last_query + "-").grid(column=0, row=1,
                                                                                    padx=var.group_1_padx,
                                                                                    pady=var.group_1_pady)
        self.lbl_zoomeye_query_txt = Label(lframe_query_summary, text=var.last_query_txt + "-").grid(column=1, row=1,
                                                                                       padx=var.group_1_padx,
                                                                                       pady=var.group_1_pady)
        self.lbl_zoomeye_query_results = Label(lframe_query_summary, text=var.last_query_results + "-").grid(column=4, row=1,
                                                                                       padx=var.group_1_padx,
                                                                                       pady=var.group_1_pady)
        self.lbl_zoomeye_query_elapsed_time = Label(lframe_query_summary, text=var.last_query_elapsed_time + "-").grid(column=6, row=1,
                                                                                       padx=var.group_1_padx,
                                                                                       pady=var.group_1_pady)

        """


    # Method to create the query and display the results.
    def run_shodan_query(self):

        query = shodan_query_creator(self.txt_simpletext.get(), self.txt_ip.get(), self.txt_ip_net.get(), self.txt_port.get(), self.txt_protocol.get(), self.txt_os.get(), self.txt_server.get(), self.txt_city.get(), self.txt_country.get())
        self.lbl_shodan_total_results_txt_value.set(var.empty_value)
        self.lbl_shodan_elapsed_time_txt_value.set(var.empty_value)
        self.lbl_shodan_last_query_txt_value.set(query)
        if query != "":
           # self.lbl_shodan_query_txt.pack()
            start_time = time.time()
            self.display_shodan_results(self.shodan_query.run_shodan_query(query))
            end_time = time.time()
            time_elapsed = round(end_time - start_time, 3)
            self.lbl_shodan_elapsed_time_txt_value.set(str(time_elapsed) + ' sec')
        else:
            self.lbl_shodan_last_query_txt_value.set(var.empty_value)
            MessageBox.showinfo("Empty Search", "Please insert any search conditions")


    def run_zoomeye_query(self):
        query = zoomeye_query_creator(self.txt_simpletext.get(), self.txt_ip.get(), self.txt_ip_net.get(),
                                      self.txt_port.get(), self.txt_protocol.get(), self.txt_os.get(),
                                      self.txt_server.get(), self.txt_city.get(), self.txt_country.get())
        self.lbl_zoomeye_total_results_txt_value.set(var.empty_value)
        self.lbl_zoomeye_elapsed_time_txt_value.set(var.empty_value)
        self.lbl_zoomeye_last_query_txt_value.set(query)
        if query != "":
            self.lbl_zoomeye_last_query_txt_value.set(query)
            self.contador = '0'
            start_time = time.time()
            self.display_zoomeye_results(self.zoomeye_query.run_zoomeye_query(query,self.lbl_zoomeye_total_results_txt_value))
            end_time=time.time()
            time_elapsed = round(end_time - start_time, 3)
            self.lbl_zoomeye_elapsed_time_txt_value.set(str(time_elapsed) + ' sec')
        else:
            MessageBox.showinfo("Empty Search", "Please insert any search conditions")

    def run_both_queries(self):
        self.run_shodan_query()
        self.run_zoomeye_query()
        return None


    def clean_form(self):
        self.txt_simpletext.delete(0, "end")
        self.txt_ip.delete(0, "end")
        self.txt_ip_net.delete(0, "end")
        self.txt_port.delete(0, "end")
        self.txt_protocol.delete(0, "end")
        self.txt_os.delete(0, "end")
        self.txt_server.delete(0, "end")
        self.txt_city.delete(0, "end")
        self.txt_country.delete(0, "end")

    # Method to display the Shodan results
    def display_shodan_results(self, results):
        lframe_main_shodan_result = LabelFrame(self.frame_main_nbook, text="This is what Shodan found out:")
        lframe_main_shodan_result.grid(column=0, row=3, sticky="nsew")

        contador = utils.format_number(str(results['total']))

        self.lbl_shodan_total_results_txt_value.set(contador)

        columns = ("match", "ip_str", "port", "module", "os", "country", "city","nmap")

        # TreeView object to show the table of results.
        self.window_shodan_results = ttk.Treeview(lframe_main_shodan_result, columns=columns, show="headings", height=7, selectmode="browse")
        self.window_shodan_results.grid(column=0, row=0, rowspan=2)
        # Horizontal scroll (NOT CORRECT).
        scroll_horiz = ttk.Scrollbar(lframe_main_shodan_result, orient=HORIZONTAL, command=self.window_shodan_results.xview)
        self.window_shodan_results.configure(xscroll=scroll_horiz.set)
        scroll_horiz.grid(column=0, row=2, columnspan=2)
        # Vertical scroll.
        scroll_vert = ttk.Scrollbar(lframe_main_shodan_result, orient=VERTICAL, command=self.window_shodan_results.yview)
        self.window_shodan_results.configure(yscroll=scroll_vert.set)
        scroll_vert.grid(column=1, row=0, sticky="ns")
        # Headings of the table displaying the results.
        self.window_shodan_results.heading("match", text="#")
        self.window_shodan_results.heading("ip_str", text="IP")
        self.window_shodan_results.heading("port", text="Port")
        self.window_shodan_results.heading("module", text="Protocol")
        self.window_shodan_results.heading("os", text="OS")
        self.window_shodan_results.heading("country", text="Country")
        self.window_shodan_results.heading("city", text="City")
        self.window_shodan_results.heading("nmap", text="nmap")

        # Setting the width of the columns.
        self.window_shodan_results.column(var.col1, width=30)
        self.window_shodan_results.column(var.col2, width=100)
        self.window_shodan_results.column(var.col3, width=80)
        self.window_shodan_results.column(var.col4, width=100)
        self.window_shodan_results.column(var.col5, width=150)
        self.window_shodan_results.column(var.col6, width=150)
        self.window_shodan_results.column(var.col7, width=150)
        self.window_shodan_results.column(var.col8, width=120)
        # loop to display result by result the table (TreeView).
        i = 0
        #print(results)
        for result in results["matches"]:
            i = i + 1
            result_sample = (
                "{}".format(i),
                "{}".format(result["ip_str"]),
                "{}".format(result["port"]),
                "{}".format(result["_shodan"]["module"]),
                "{}".format(result["os"]),
                "{}".format(result["location"]["country_name"]),
                "{}".format(result["location"]["city"]),
                "{}".format("Not scanned"))
            self.window_shodan_results.insert('', END, iid=i, values=result_sample)
        self.results_shodan = results

        button_vulnerabily = Button(lframe_main_shodan_result, text="Show\nvulnerabilities\n associated", padx=var.group_1_padx, pady=var.group_1_pady, command=self.find_shodan_vulnerabilities)
        button_vulnerabily.grid(column=2, row=0)

        button_nmap = Button(lframe_main_shodan_result, text="Scan the finding \nwith Nmap", padx=var.group_1_padx, pady=var.group_1_pady, command=self.scan_shodan_with_nmap)
        button_nmap.grid(column=2, row=1)

        #csv
        #button_shodan_export_csv = Button(lframe_main_shodan_result, text="\nExport to csv \n", padx=var.group_1_padx,pady=var.group_1_pady, command=self.shodan_export_csv)
        #button_shodan_export_csv.grid(column=3, row=0)

    #csv
    def shodan_export_csv(self):
        self.shodandata = []
        print("len shodandata")
        print(len(self.shodandata))
        """"
        if len(shodandata) < -1:
            MessageBox.showinfo("No Data","No data available to export to csv")
            return False
        """
        shodan_export_file = Filedialog.asksaveasfile(mode='w',initialdir=os.getcwd(), title="shodan_export_csv", defaultextension=".csv", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")))
        if shodan_export_file is None:
            print ("None")
        exp_writer = csv.writer(shodan_export_file, delimiter=',')
        print("kk antes")
        for i in self.shodandata:
            print(i)
            exp_writer.writerow(i)
        #MessageBox.showinfo("Data exported", "Your data has been exported to " +  os.path.basename(shodan_export_file) + "successfully")
        return True



    def find_shodan_vulnerabilities(self):
        results = self.results_shodan
        if (self.window_shodan_results.focus() == ""):
            MessageBox.showinfo("Select some item!", "Please select one linea of the table \nto see its' possible exploitable vulnerabilies.")
        else:
            WindowVulnerabilities(results["matches"][int((self.window_shodan_results.focus()))-1])



    def display_zoomeye_results(self, results):
        lframe_main_zoomeye_result = LabelFrame(self.frame_main_nbook, text="This is what ZoomEye found out:")
        lframe_main_zoomeye_result.grid(column=0, row=4, sticky="nsew")

        #self.lbl_zoomeye_total_results_txt_value.set(self.api.show_count())

        columns = ("match", "ip_str", "port", "module", "os", "country", "city","nmap")
        #columns = ("match", "ip", "geoinfo.organization", "portinfo.os", "XXX", "portinfo.port")

        # TreeView object to show the table of results.
        self.window_zoomeye_results = ttk.Treeview(lframe_main_zoomeye_result, columns=columns, show="headings", height=7)
        self.window_zoomeye_results.grid(column=0, row=0)
        # Horizontal scroll (NOT CORRECT).
        scroll_horiz = ttk.Scrollbar(lframe_main_zoomeye_result, orient=HORIZONTAL, command=self.window_zoomeye_results.xview)
        self.window_zoomeye_results.configure(xscroll=scroll_horiz.set)
        scroll_horiz.grid(column=0, row=1, columnspan=2)
        # Vertical scroll.
        scroll_vert = ttk.Scrollbar(lframe_main_zoomeye_result, orient=VERTICAL, command=self.window_zoomeye_results.yview)
        self.window_zoomeye_results.configure(yscroll=scroll_vert.set)
        scroll_vert.grid(column=1, row=0, sticky="ns")

        # Headings of the table displaying the results.
        self.window_zoomeye_results.heading("match", text="#")
        self.window_zoomeye_results.heading("ip_str", text="IP")
        self.window_zoomeye_results.heading("port", text="Port")
        self.window_zoomeye_results.heading("module", text="Protocol")
        self.window_zoomeye_results.heading("os", text="OS")
        self.window_zoomeye_results.heading("country", text="Country")
        self.window_zoomeye_results.heading("city", text="Area")
        self.window_zoomeye_results.heading("nmap", text="nmap")

        # Setting the width of the columns.
        self.window_zoomeye_results.column(var.col1, width=30)
        self.window_zoomeye_results.column(var.col2, width=100)
        self.window_zoomeye_results.column(var.col3, width=80)
        self.window_zoomeye_results.column(var.col4, width=100)
        self.window_zoomeye_results.column(var.col5, width=150)
        self.window_zoomeye_results.column(var.col6, width=150)
        self.window_zoomeye_results.column(var.col7, width=150)
        self.window_zoomeye_results.column(var.col8, width=120)
        # loop to display result by result the table (TreeView).
        i = 0
        for result in results:
            i = i + 1
            result_sample = (
                "{}".format(i),
                "{}".format(result["ip"]),
                "{}".format(result["portinfo"]["port"]),
                "{}".format(result["portinfo"]["service"]),
                "{}".format(result["portinfo"]["os"]),
                "{}".format(result["geoinfo"]["country"]["names"]["en"]),
                "{}".format(result["geoinfo"]["subdivisions"]["names"]["en"]),
                "{}".format("Not scanned"))
            self.window_zoomeye_results.insert('', END, iid=i, values=result_sample)

            self.results_zoomeye = results
            button_nmap = Button(lframe_main_zoomeye_result, text="Scan the finding \nwith Nmap", padx=var.group_1_padx,
                                 pady=var.group_1_pady, command=self.scan_zoomeye_with_nmap)
            button_nmap.grid(column=2, row=0)

    def scan_shodan_with_nmap(self):
        results = self.results_shodan
        if (self.window_shodan_results.focus() == ""):
            MessageBox.showinfo("Select some item!", "Please select one linea of the table \nto scan with nmap the element found.")
        else:
            selected = self.window_shodan_results.focus()
            focused_ip=results["matches"][int((self.window_shodan_results.focus())) - 1]["ip_str"]
            focused_port=str(results["matches"][int((self.window_shodan_results.focus())) - 1]["port"])
            port = scan_ip_port(focused_ip, focused_port)
            values=self.window_shodan_results.item(selected, 'values')
            self.window_shodan_results.item(selected, text='', values=(values[0],values[1],values[2],values[3],values[4],values[5],values[6],port))

    def scan_zoomeye_with_nmap(self):
        results = self.results_zoomeye
        if (self.window_zoomeye_results.focus() == ""):
            MessageBox.showinfo("Select some item!", "Please select one linea of the table \nto scan with nmap the element found.")
        else:
            selected = self.window_zoomeye_results.focus()
            values = self.window_zoomeye_results.item(selected, 'values')
            focused_ip=values[1]
            focused_port=values[2]
            port = scan_ip_port(focused_ip, focused_port)
            values=self.window_zoomeye_results.item(selected, 'values')
            self.window_zoomeye_results.item(selected, text='', values=(values[0],values[1],values[2],values[3],values[4],values[5],values[6],port))


