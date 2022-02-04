from tkinter import Label
from tkinter import ttk
import constants as var
from tkinter import *
import configparser
from tkinter.ttk import Separator
from tkinter import messagebox as MessageBox
from IPy import IP

from shodan_handler import shodan_query_creator
from zoomeye_handler import zoomeye_query_creator

class WindowHistory():
    config_file_name = '../config/config.cfg'

    def __init__(self, main_frame, shodan_object, zoomeye_object):
        config_file = configparser.ConfigParser()
        config_file.read(self.config_file_name)
        self.max_no_records = config_file['HISTORICAL']['MAX_NO_RECODS']
        print(type(self.max_no_records))
        self.shodan_his_query = shodan_object
        self.zoomeye_his_query = zoomeye_object

        self.root = main_frame
        self.lframe_history_query = LabelFrame(self.root, text=var.history_window_search_title)
        self.lframe_history_query.grid(column=0, row=0)
        #self.shodan_query = shodan_object
        #self.zoomeye_query = zoomeye_object
        self.display_nbook_history_query()


    def display_nbook_history_query(self):
        history_network_label = Label(self.lframe_history_query, text=var.label_ip_net).grid(column=0, row=0,
                                                                                              padx=var.group_1_padx,
                                                                                              pady=var.group_1_pady)
        self.history_network_entry = Entry(self.lframe_history_query, width=var.text_entry_size)
        self.history_network_entry.grid(column=1, row=0, padx=var.group_1_padx, pady=var.group_1_pady)

        history_max_no_records_label = Label(self.lframe_history_query, text=var.text_max_no_records + " " + self.max_no_records).grid(column=2, row=0,
                                                                                              padx=var.group_1_padx,
                                                                                              pady=var.group_1_pady)
        sep_1 = ttk.Separator(self.lframe_history_query, orient="vertical").grid(column=3, row=0, rowspan=3, sticky="ns")

        btn_shodan_his = Button(self.lframe_history_query, text=var.button_run_shodan_query, width=12, height=5, command=self.run_shodan_his_query)
        btn_shodan_his.grid(column=4, row=0, rowspan=3, padx=5, pady=5)

        btn_zoomeye_his = Button(self.lframe_history_query, text=var.button_run_zoomeye_query, width=12, height=5,command=self.run_zoomeye_his_query)
        btn_zoomeye_his.grid(column=5, row=0, rowspan=3, padx=5, pady=5)

        button_both_his_queries = Button(self.lframe_history_query, text=var.button_both_queries, width=20,command=self.run_both_his_queries)
        button_both_his_queries.grid(column=6, row=0, rowspan=2, padx=5)


        button_clean_form = Button(self.lframe_history_query, text=var.button_clean_form, width=20, command=self.clean_form)
        button_clean_form.grid(column=6, row=2, padx=3)

    def clean_form(self):
        self.history_network_entry.delete(0, "end")

    def run_shodan_his_query(self):
        query = self.history_network_entry.get()
        results = []
        if query != "":
            try:
                ip = IP(query)
                for contador in ip:
                    try:
                        currentip = str(contador)
                        #host = api.host(currentip, history=True)
                        host=self.shodan_his_query.run_shodan_his_query(currentip)
                        if host != []:
                            results.append(host[0])
                    except Exception as e:
                        pass
            except Exception:
                results = []
            self.display_shodan_his_results(results)
        else:
            MessageBox.showinfo("Empty Search", "Please insert any search conditions.")

    def run_zoomeye_his_query(self):
        query = self.history_network_entry.get()
        if query != "":
            try:
                results = self.shodan_his_query.run_zoomeye_his_query(query)
            except Exception:
                results = []
            self.display_zoomeye_his_results(results)
        else:
            MessageBox.showinfo("Empty Search", "Please insert any search conditions.")


    def run_both_his_queries(self):
        self.run_shodan_his_query()
        self.run_zoomeye_his_query()


    def display_shodan_his_results(self, results):
        self.lframe_main_shodan_hist_result = LabelFrame(self.root, text="This is what Shodan found out:")
        self.lframe_main_shodan_hist_result.grid(column=0, row=1, sticky="nsew")

        print('display_shodan_his_results')

        columns = ("#", "IP", "Port", "Timestamp")

        # TreeView object to show the table of results.
        self.window_shodan_his_results = ttk.Treeview(self.lframe_main_shodan_hist_result, columns=columns, show="headings", height=10, selectmode="browse")
        self.window_shodan_his_results.grid(column=0, row=0)
        # Horizontal scroll (NOT CORRECT).
        scroll_horiz = ttk.Scrollbar(self.lframe_main_shodan_hist_result, orient=HORIZONTAL, command=self.window_shodan_his_results.xview)
        self.window_shodan_his_results.configure(xscroll=scroll_horiz.set)
        scroll_horiz.grid(column=0, row=1, columnspan=2)
        # Vertical scroll.
        scroll_vert = ttk.Scrollbar(self.lframe_main_shodan_hist_result, orient=VERTICAL, command=self.window_shodan_his_results.yview)
        self.window_shodan_his_results.configure(yscroll=scroll_vert.set)
        scroll_vert.grid(column=1, row=0, sticky="ns")
        # Headings of the table displaying the results.
        self.window_shodan_his_results.heading("#", text="#")
        self.window_shodan_his_results.heading("IP", text="IP")
        self.window_shodan_his_results.heading("Port", text="Port")
        self.window_shodan_his_results.heading("Timestamp", text="Timestamp")

        # Setting the width of the columns.
        self.window_shodan_his_results.column(var.col1, width=30)
        self.window_shodan_his_results.column(var.col2, width=120)
        self.window_shodan_his_results.column(var.col3, width=80)
        self.window_shodan_his_results.column(var.col4, width=300)

        int_max_no_records = int(self.max_no_records)
        i = 0
        for x in results:
            if i > int_max_no_records:
                break
            ip = x[0]
            timestamp = x[1]
            puertos = x[2]
            for puerto in puertos:
                i = i + 1
                if i > int_max_no_records:
                    break
                result_sample = (
                    "{}".format(i),
                    "{}".format(ip),
                    "{}".format(puerto),
                    "{}".format(timestamp))
                self.window_shodan_his_results.insert('', END, iid=i, values=result_sample)

    def display_zoomeye_his_results(self, results):
        self.lframe_main_zoomeye_hist_result = LabelFrame(self.root, text="This is what Zoomeye found out:")
        self.lframe_main_zoomeye_hist_result.grid(column=0, row=2, sticky="nsew")

        print('hola')

        columns = ("#", "IP", "Port", "Timestamp")

        # TreeView object to show the table of results.
        self.window_zoomeye_his_results = ttk.Treeview(self.lframe_main_zoomeye_hist_result, columns=columns, show="headings", height=10, selectmode="browse")
        self.window_zoomeye_his_results.grid(column=0, row=0)
        # Horizontal scroll (NOT CORRECT).
        scroll_horiz = ttk.Scrollbar(self.lframe_main_zoomeye_hist_result, orient=HORIZONTAL, command=self.window_zoomeye_his_results.xview)
        self.window_zoomeye_his_results.configure(xscroll=scroll_horiz.set)
        scroll_horiz.grid(column=0, row=1, columnspan=2)
        # Vertical scroll.
        scroll_vert = ttk.Scrollbar(self.lframe_main_zoomeye_hist_result, orient=VERTICAL, command=self.window_zoomeye_his_results.yview)
        self.window_zoomeye_his_results.configure(yscroll=scroll_vert.set)
        scroll_vert.grid(column=1, row=0, sticky="ns")
        # Headings of the table displaying the results.
        self.window_zoomeye_his_results.heading("#", text="#")
        self.window_zoomeye_his_results.heading("IP", text="IP")
        self.window_zoomeye_his_results.heading("Port", text="Port")
        self.window_zoomeye_his_results.heading("Timestamp", text="Timestamp")

        # Setting the width of the columns.
        self.window_zoomeye_his_results.column(var.col1, width=30)
        self.window_zoomeye_his_results.column(var.col2, width=120)
        self.window_zoomeye_his_results.column(var.col3, width=80)
        self.window_zoomeye_his_results.column(var.col4, width=300)

        int_max_no_records = int(self.max_no_records)
        i = 0
        for x in results:
            if i > int_max_no_records:
                break
            ip = x[0]
            timestamp = x[1]
            puertos = x[2]
            for puerto in puertos:
                i = i + 1
                if i > int_max_no_records:
                    break
                print(i)
                print(ip)
                print(puerto)
                print(timestamp)
                result_sample = (
                    "{}".format(i),
                    "{}".format(ip),
                    "{}".format(puerto),
                    "{}".format(timestamp))
                self.window_zoomeye_his_results.insert('', END, iid=i, values=result_sample)



