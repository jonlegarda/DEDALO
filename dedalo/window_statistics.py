from tkinter import *
from tkinter.ttk import Separator
from tkinter import messagebox as MessageBox

from shodan_handler import shodan_query_creator
from zoomeye_handler import zoomeye_query_creator
import constants as var
import utils as util


class WindowStatistics():


    def __init__(self, main_frame, shodan_object, zoomeye_object):
        self.shodan_statistics_results = None
        self.zoomeye_statistics_results = None
        self.root = main_frame
        self.lframe_search = LabelFrame(self.root, text=var.main_window_search_title)
        self.lframe_search.grid(column=0, row=0)
        self.shodan_query = shodan_object
        self.zoomeye_query = zoomeye_object
        self.display_nbook_statistics()


    def display_nbook_statistics(self):
        simple_query_label = Label(self.lframe_search, text=var.label_simpletext_1).grid(column=0, row=0,
                                                                                              padx=var.group_1_padx,
                                                                                              pady=var.group_1_pady)
        self.simple_query_txt_entry = Entry(self.lframe_search, width=var.text_entry_size)
        self.simple_query_txt_entry.grid(column=1, row=0, padx=var.group_1_padx, pady=var.group_1_pady)

        ip_label = Label(self.lframe_search, text=var.label_ip_1).grid(column=0, row=1, padx=var.group_1_padx, pady=var.group_1_pady)
        self.ip_txt_entry = Entry(self.lframe_search, width=var.text_entry_size)
        self.ip_txt_entry.grid(column=1, row=1, padx=var.group_1_padx, pady=var.group_1_pady)

        ip_net_label = Label(self.lframe_search, text=var.label_ip_net).grid(column=0, row=2, padx=var.group_1_padx,
                                                                             pady=var.group_1_pady)
        self.ip_net_txt_entry = Entry(self.lframe_search, width=var.text_entry_size)
        self.ip_net_txt_entry.grid(column=1, row=2, padx=var.group_1_padx, pady=var.group_1_pady)

        sep_1 = Separator(self.lframe_search, orient="vertical").grid(column=3, row=0, rowspan=3, sticky="ns")

        port_label = Label(self.lframe_search, text=var.label_port_1).grid(column=4, row=0, padx=var.group_1_padx,
                                                                           pady=var.group_1_pady)
        self.port_txt_entry = Entry(self.lframe_search, width=var.text_entry_size)
        self.port_txt_entry.grid(column=5, row=0, padx=var.group_1_padx, pady=var.group_1_pady)

        protocol_label = Label(self.lframe_search, text=var.label_protocol_1).grid(column=4, row=1,
                                                                                   padx=var.group_1_padx,
                                                                                   pady=var.group_1_pady)
        self.protocol_txt_entry = Entry(self.lframe_search, width=var.text_entry_size)
        self.protocol_txt_entry.grid(column=5, row=1, padx=var.group_1_padx, pady=var.group_1_pady)

        os_label = Label(self.lframe_search, text=var.label_os_1).grid(column=4, row=2, padx=var.group_1_padx,
                                                                       pady=var.group_1_pady)
        self.os_txt_entry = Entry(self.lframe_search, width=var.text_entry_size)
        self.os_txt_entry.grid(column=5, row=2, padx=var.group_1_padx, pady=var.group_1_pady)

        sep_2 = Separator(self.lframe_search, orient="vertical").grid(column=6, row=0, rowspan=3, sticky="ns")

        server_label = Label(self.lframe_search, text=var.label_server_1).grid(column=7, row=0, padx=var.group_1_padx,
                                                                               pady=var.group_1_pady)
        self.server_txt_entry = Entry(self.lframe_search, width=var.text_entry_size)
        self.server_txt_entry.grid(column=8, row=0, padx=var.group_1_padx, pady=var.group_1_pady)

        city_label = Label(self.lframe_search, text=var.label_city_1).grid(column=7, row=1, padx=var.group_1_padx,
                                                                           pady=var.group_1_pady)
        self.city_txt_entry = Entry(self.lframe_search, width=var.text_entry_size)
        self.city_txt_entry.grid(column=8, row=1, padx=var.group_1_padx, pady=var.group_1_pady)

        country_label = Label(self.lframe_search, text=var.label_country_1).grid(column=7, row=2, padx=var.group_1_padx,
                                                                                 pady=var.group_1_pady)
        self.country_txt_entry = Entry(self.lframe_search, width=var.text_entry_size)
        self.country_txt_entry.grid(column=8, row=2, padx=var.group_1_padx, pady=var.group_1_pady)

        sep_3 = Separator(self.lframe_search, orient="vertical").grid(column=9, row=0, rowspan=3, sticky="ns")

        button_shodan_statistics = Button(self.lframe_search, text=var.button_shodan_statistics, width=12, height=5,
                                          command=self.run_shodan_statistics)
        button_shodan_statistics.grid(column=10, row=0, rowspan=3, padx=5, pady=5)

        button_zoomeye_statistics = Button(self.lframe_search, text=var.button_zoomeye_statistics, width=12, height=5,
                                           command=self.run_zoomeye_statistics)
        button_zoomeye_statistics.grid(column=11, row=0, rowspan=3, padx=5, pady=5)

        button_both_statistics = Button(self.lframe_search, text=var.button_both_statistics, width=20,
                                        command=self.run_both_statistics)
        button_both_statistics.grid(column=12, row=0, rowspan=2, padx=5)

        button_clean_form = Button(self.lframe_search, text=var.button_clean_form, width=20, command=self.clean_form)
        button_clean_form.grid(column=12, row=2, padx=5)

        lframe_statistics = LabelFrame(self.root, text=var.window_statistics_results)
        lframe_statistics.grid(column=0, row=1, sticky="w")

        lframe_radiobuttons = LabelFrame(lframe_statistics, text=var.window_statistics_radiobuttons)
        lframe_radiobuttons.grid(column=0, row=0)
        self.sel_radiobutton = StringVar()
        self.radiobtn_product = Radiobutton(lframe_radiobuttons, text=var.radiobtn_product, variable=self.sel_radiobutton, value=var.radiobtn_product_value,
                                            command=self.update_statistics)
        self.radiobtn_product.grid(column=0, row=0, sticky="w")
        self.radiobtn_device = Radiobutton(lframe_radiobuttons, text=var.radiobtn_device, variable=self.sel_radiobutton, value=var.radiobtn_device_value,
                                           command=self.update_statistics)
        self.radiobtn_device.grid(column=0, row=1, sticky="w")
        # Se comenta el Radiobutton de "Service", ya que en Shodan no se consigue el dato.
        #self.radiobtn_service = Radiobutton(lframe_radiobuttons, text=var.radiobtn_service, variable=self.sel_radiobutton, value=var.radiobtn_service_value, command=self.update_statistics)
        #self.radiobtn_service.grid(column=0, row=2, sticky="w")
        self.radiobtn_os = Radiobutton(lframe_radiobuttons, text=var.radiobtn_os, variable=self.sel_radiobutton, value=var.radiobtn_os_value,
                                       command=self.update_statistics)
        self.radiobtn_os.grid(column=0, row=3, sticky="w")
        self.radiobtn_port = Radiobutton(lframe_radiobuttons, text=var.radiobtn_port, variable=self.sel_radiobutton, value=var.radiobtn_port_value,
                                         command=self.update_statistics)
        self.radiobtn_port.grid(column=0, row=4, sticky="w")
        self.radiobtn_city = Radiobutton(lframe_radiobuttons, text=var.radiobtn_city, variable=self.sel_radiobutton, value=var.radiobtn_city_value,
                                         command=self.update_statistics)
        self.radiobtn_city.grid(column=0, row=5, sticky="w")
        self.radiobtn_country = Radiobutton(lframe_radiobuttons, text=var.radiobtn_country, variable=self.sel_radiobutton, value=var.radiobtn_country_value,
                                            command=self.update_statistics)
        self.radiobtn_country.grid(column=0, row=6, sticky="w")

        frame_stats_compare = Frame(lframe_statistics)
        frame_stats_compare.grid(column=1, row=0)
        label_shodan_top5 = Label(frame_stats_compare, text=var.shodan_top5, font=var.shodan_top5_font)
        label_shodan_top5.grid(column=0, row=0, columnspan=4, padx=var.group_1_padx, pady=var.group_1_pady)
        self.shodan_top_1_value = StringVar()
        self.shodan_top_1_value.set(var.tbd_stats)
        self.shodan_top_1_count = StringVar()
        self.shodan_top_1_count.set(var.tbd_stats)
        self.shodan_top_2_value = StringVar()
        self.shodan_top_2_value.set(var.tbd_stats)
        self.shodan_top_2_count = StringVar()
        self.shodan_top_2_count.set(var.tbd_stats)
        self.shodan_top_3_value = StringVar()
        self.shodan_top_3_value.set(var.tbd_stats)
        self.shodan_top_3_count = StringVar()
        self.shodan_top_3_count.set(var.tbd_stats)
        self.shodan_top_4_value = StringVar()
        self.shodan_top_4_value.set(var.tbd_stats)
        self.shodan_top_4_count = StringVar()
        self.shodan_top_4_count.set(var.tbd_stats)
        self.shodan_top_5_value = StringVar()
        self.shodan_top_5_value.set(var.tbd_stats)
        self.shodan_top_5_count = StringVar()
        self.shodan_top_5_count.set(var.tbd_stats)

        label_shodantop1 = Label(frame_stats_compare, text=var.top1, width=10).grid(column=0, row=1, padx=var.group_1_padx, pady=var.group_1_pady)
        label_shodantop1_value = Label(frame_stats_compare, textvariable=self.shodan_top_1_value, width=var.top_value_width).grid(column=1, row=1, padx=var.group_1_padx, pady=var.group_1_pady)
        label_shodantop1_count = Label(frame_stats_compare, textvariable=self.shodan_top_1_count, width=10).grid(column=2, row=1, padx=var.group_1_padx, pady=var.group_1_pady)
        label_shodantop2 = Label(frame_stats_compare, text=var.top2).grid(column=0, row=3, padx=var.group_1_padx, pady=var.group_1_pady)
        label_shodantop2_value = Label(frame_stats_compare, textvariable=self.shodan_top_2_value).grid(column=1, row=3, padx=var.group_1_padx, pady=var.group_1_pady)
        label_shodantop2_count = Label(frame_stats_compare, textvariable=self.shodan_top_2_count).grid(column=2, row=3, padx=var.group_1_padx, pady=var.group_1_pady)
        label_shodantop3 = Label(frame_stats_compare, text=var.top3).grid(column=0, row=5, padx=var.group_1_padx, pady=var.group_1_pady)
        label_shodantop3_value = Label(frame_stats_compare, textvariable=self.shodan_top_3_value).grid(column=1, row=5, padx=var.group_1_padx, pady=var.group_1_pady)
        label_shodantop3_count = Label(frame_stats_compare, textvariable=self.shodan_top_3_count).grid(column=2, row=5, padx=var.group_1_padx, pady=var.group_1_pady)
        label_shodantop4 = Label(frame_stats_compare, text=var.top4).grid(column=0, row=7, padx=var.group_1_padx, pady=var.group_1_pady)
        label_shodantop4_value = Label(frame_stats_compare, textvariable=self.shodan_top_4_value).grid(column=1, row=7, padx=var.group_1_padx, pady=var.group_1_pady)
        label_shodantop4_count = Label(frame_stats_compare, textvariable=self.shodan_top_4_count).grid(column=2, row=7, padx=var.group_1_padx, pady=var.group_1_pady)
        label_shodantop5 = Label(frame_stats_compare, text=var.top5).grid(column=0, row=9, padx=var.group_1_padx, pady=var.group_1_pady)
        label_shodantop5_value = Label(frame_stats_compare, textvariable=self.shodan_top_5_value).grid(column=1, row=9, padx=var.group_1_padx, pady=var.group_1_pady)
        label_shodantop5_count = Label(frame_stats_compare, textvariable=self.shodan_top_5_count).grid(column=2, row=9, padx=var.group_1_padx, pady=var.group_1_pady)

        sep1_2 = Separator(frame_stats_compare, orient="horizontal").grid(row=2, columnspan=7, sticky="ew")
        sep2_3 = Separator(frame_stats_compare, orient="horizontal").grid(row=4, columnspan=7, sticky="ew")
        sep3_4 = Separator(frame_stats_compare, orient="horizontal").grid(row=6, columnspan=7, sticky="ew")
        sep4_5 = Separator(frame_stats_compare, orient="horizontal").grid(row=8, columnspan=7, sticky="ew")
        sep_vs = Separator(frame_stats_compare, orient="vertical").grid(column=3, row=1, rowspan=9, sticky="ns")

        label_zoomeye_top5 = Label(frame_stats_compare, text=var.zoomeye_top5, font=var.zoomeye_top5_font)
        label_zoomeye_top5.grid(column=4, row=0, columnspan=4, padx=var.group_1_padx, pady=var.group_1_pady)
        self.zoomeye_top_1_value = StringVar()
        self.zoomeye_top_1_value.set(var.tbd_stats)
        self.zoomeye_top_1_count = StringVar()
        self.zoomeye_top_1_count.set(var.tbd_stats)
        self.zoomeye_top_2_value = StringVar()
        self.zoomeye_top_2_value.set(var.tbd_stats)
        self.zoomeye_top_2_count = StringVar()
        self.zoomeye_top_2_count.set(var.tbd_stats)
        self.zoomeye_top_3_value = StringVar()
        self.zoomeye_top_3_value.set(var.tbd_stats)
        self.zoomeye_top_3_count = StringVar()
        self.zoomeye_top_3_count.set(var.tbd_stats)
        self.zoomeye_top_4_value = StringVar()
        self.zoomeye_top_4_value.set(var.tbd_stats)
        self.zoomeye_top_4_count = StringVar()
        self.zoomeye_top_4_count.set(var.tbd_stats)
        self.zoomeye_top_5_value = StringVar()
        self.zoomeye_top_5_value.set(var.tbd_stats)
        self.zoomeye_top_5_count = StringVar()
        self.zoomeye_top_5_count.set(var.tbd_stats)

        label_zoomeyetop1 = Label(frame_stats_compare, text=var.top1, width=10).grid(column=4, row=1, padx=var.group_1_padx, pady=var.group_1_pady)
        label_zoomeyetop1_value = Label(frame_stats_compare, textvariable=self.zoomeye_top_1_value, width=var.top_value_width).grid(column=5, row=1, padx=var.group_1_padx, pady=var.group_1_pady)
        label_zoomeyetop1_count = Label(frame_stats_compare, textvariable=self.zoomeye_top_1_count, width=10).grid(column=6, row=1, padx=var.group_1_padx, pady=var.group_1_pady)
        label_zoomeyetop2 = Label(frame_stats_compare, text=var.top2).grid(column=4, row=3, padx=var.group_1_padx, pady=var.group_1_pady)
        label_zoomeyetop2_value = Label(frame_stats_compare, textvariable=self.zoomeye_top_2_value).grid(column=5, row=3, padx=var.group_1_padx, pady=var.group_1_pady)
        label_zoomeyetop2_count = Label(frame_stats_compare, textvariable=self.zoomeye_top_2_count).grid(column=6, row=3, padx=var.group_1_padx, pady=var.group_1_pady)
        label_zoomeyetop3 = Label(frame_stats_compare, text=var.top3).grid(column=4, row=5, padx=var.group_1_padx, pady=var.group_1_pady)
        label_zoomeyetop3_value = Label(frame_stats_compare, textvariable=self.zoomeye_top_3_value).grid(column=5, row=5, padx=var.group_1_padx, pady=var.group_1_pady)
        label_zoomeyetop3_count = Label(frame_stats_compare, textvariable=self.zoomeye_top_3_count).grid(column=6, row=5, padx=var.group_1_padx, pady=var.group_1_pady)
        label_zoomeyetop4 = Label(frame_stats_compare, text=var.top4).grid(column=4, row=7, padx=var.group_1_padx, pady=var.group_1_pady)
        label_zoomeyetop4_value = Label(frame_stats_compare, textvariable=self.zoomeye_top_4_value).grid(column=5, row=7, padx=var.group_1_padx, pady=var.group_1_pady)
        label_zoomeyetop4_count = Label(frame_stats_compare, textvariable=self.zoomeye_top_4_count).grid(column=6, row=7, padx=var.group_1_padx, pady=var.group_1_pady)
        label_zoomeyetop5 = Label(frame_stats_compare, text=var.top5).grid(column=4, row=9, padx=var.group_1_padx, pady=var.group_1_pady)
        label_zoomeyetop5_value = Label(frame_stats_compare, textvariable=self.zoomeye_top_5_value).grid(column=5, row=9, padx=var.group_1_padx, pady=var.group_1_pady)
        label_zoomeyetop5_count = Label(frame_stats_compare, textvariable=self.zoomeye_top_5_count).grid(column=6, row=9, padx=var.group_1_padx, pady=var.group_1_pady)


    def run_shodan_statistics(self):
        query = shodan_query_creator(self.simple_query_txt_entry.get(), self.ip_txt_entry.get(), self.ip_net_txt_entry.get(), self.port_txt_entry.get(), self.protocol_txt_entry.get(), self.os_txt_entry.get(), self.server_txt_entry.get(), self.city_txt_entry.get(), self.country_txt_entry.get())
        if query != "":
            self.shodan_statistics_results = self.shodan_query.run_shodan_query_facets(query)
            self.update_statistics()
        else:
            MessageBox.showinfo("Empty Search", "Please insert any search conditions.")


    def run_zoomeye_statistics(self):
        query = zoomeye_query_creator(self.simple_query_txt_entry.get(), self.ip_txt_entry.get(), self.ip_net_txt_entry.get(),
                                        self.port_txt_entry.get(), self.protocol_txt_entry.get(), self.os_txt_entry.get(),
                                     self.server_txt_entry.get(), self.city_txt_entry.get(), self.country_txt_entry.get())
        if query != "":
            self.zoomeye_statistics_results = self.zoomeye_query.run_zoomeye_query_facets(query)
            self.update_statistics()
        else:
            MessageBox.showinfo("Empty Search", "Please insert any search conditions.")


    def run_both_statistics(self):
        self.run_shodan_statistics()
        self.run_zoomeye_statistics()
        return None


    def clean_form(self):
        self.simple_query_txt_entry.delete(0, "end")
        self.ip_txt_entry.delete(0, "end")
        self.ip_net_txt_entry.delete(0, "end")
        self.port_txt_entry.delete(0, "end")
        self.protocol_txt_entry.delete(0, "end")
        self.os_txt_entry.delete(0, "end")
        self.server_txt_entry.delete(0, "end")
        self.city_txt_entry.delete(0, "end")
        self.country_txt_entry.delete(0, "end")


    def update_statistics(self):
        facet = self.sel_radiobutton.get()
        try:
            self.clean_shodan_stats()
            self.shodan_top_1_value.set(self.shodan_statistics_results["facets"][facet][0]["value"])
            self.shodan_top_1_count.set(util.format_number(str(self.shodan_statistics_results["facets"][facet][0]["count"])))
            self.shodan_top_2_value.set(self.shodan_statistics_results["facets"][facet][1]["value"])
            self.shodan_top_2_count.set(util.format_number(str(self.shodan_statistics_results["facets"][facet][1]["count"])))
            self.shodan_top_3_value.set(self.shodan_statistics_results["facets"][facet][2]["value"])
            self.shodan_top_3_count.set(util.format_number(str(self.shodan_statistics_results["facets"][facet][2]["count"])))
            self.shodan_top_4_value.set(self.shodan_statistics_results["facets"][facet][3]["value"])
            self.shodan_top_4_count.set(util.format_number(str(self.shodan_statistics_results["facets"][facet][3]["count"])))
            self.shodan_top_5_value.set(self.shodan_statistics_results["facets"][facet][4]["value"])
            self.shodan_top_5_count.set(util.format_number(str(self.shodan_statistics_results["facets"][facet][4]["count"])))
        except Exception as e:
            print("Method: update_statistics_both() | Error: No more Shodan data found.")
        try:
            self.clean_zoomeye_stats()
            self.zoomeye_top_1_value.set(self.zoomeye_statistics_results[facet][0]["name"])
            self.zoomeye_top_1_count.set(util.format_number(str(self.zoomeye_statistics_results[facet][0]["count"])))
            self.zoomeye_top_2_value.set(self.zoomeye_statistics_results[facet][1]["name"])
            self.zoomeye_top_2_count.set(util.format_number(str(self.zoomeye_statistics_results[facet][1]["count"])))
            self.zoomeye_top_3_value.set(self.zoomeye_statistics_results[facet][2]["name"])
            self.zoomeye_top_3_count.set(util.format_number(str(self.zoomeye_statistics_results[facet][2]["count"])))
            self.zoomeye_top_4_value.set(self.zoomeye_statistics_results[facet][3]["name"])
            self.zoomeye_top_4_count.set(util.format_number(str(self.zoomeye_statistics_results[facet][3]["count"])))
            self.zoomeye_top_5_value.set(self.zoomeye_statistics_results[facet][4]["name"])
            self.zoomeye_top_5_count.set(util.format_number(str(self.zoomeye_statistics_results[facet][4]["count"])))
        except Exception as e:
            print("Method: update_statistics_both() | Error: No more ZoomEye data found.")


    def clean_shodan_stats(self):
        self.shodan_top_1_value.set("")
        self.shodan_top_1_count.set("")
        self.shodan_top_2_value.set("")
        self.shodan_top_2_count.set("")
        self.shodan_top_3_value.set("")
        self.shodan_top_3_count.set("")
        self.shodan_top_4_value.set("")
        self.shodan_top_4_count.set("")
        self.shodan_top_5_value.set("")
        self.shodan_top_5_count.set("")


    def clean_zoomeye_stats(self):
        self.zoomeye_top_1_value.set("")
        self.zoomeye_top_1_count.set("")
        self.zoomeye_top_2_value.set("")
        self.zoomeye_top_2_count.set("")
        self.zoomeye_top_3_value.set("")
        self.zoomeye_top_3_count.set("")
        self.zoomeye_top_4_value.set("")
        self.zoomeye_top_4_count.set("")
        self.zoomeye_top_5_value.set("")
        self.zoomeye_top_5_count.set("")