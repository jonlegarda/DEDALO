from tkinter import *
from tkinter import ttk

from zoomeye.sdk import ZoomEye

from api_config_default_handler import ApiKeyShodanDefaultConfig, ApiKeyZoomeyeDefaultConfig
from shodan_handler import ShodanQuery, shodan_query_creator
from zoomeye_handler import ZoomEyeQuery, zoomeye_query_creator
import constants as var


class WindowApiConfiguration():

    def __init__(self, main_frame, shodan_object, zoomeye_object):
        self.root = main_frame
        self.lframe_search = LabelFrame(self.root, text=var.window_api)
        self.lframe_search.grid(column=0, row=0)
        self.shodan_query = shodan_object
        self.zoomeye_query = zoomeye_object
        self.display_nbook_api(self.root)


    def display_nbook_api(self, frame):
        self.lframe_api_config = LabelFrame(frame, text="Configure the Shodan API-Key:")
        self.lframe_api_config.grid(column=0, row=0)
        lbl_api_explain = Label(self.lframe_api_config, text=var.text_label_api_explain).grid(column=0, row=0, columnspan=6, padx=var.group_1_padx, pady=25)
        lbl_api_insert = Label(self.lframe_api_config, text=var.text_label_shodan_api_insert).grid(column=0, row=1, padx=var.group_1_padx, pady=var.group_1_pady)
        lbl_api_insert = Label(self.lframe_api_config, text=var.text_label_zoomeye_api_insert).grid(column=3, row=1, padx=var.group_1_padx, pady=var.group_1_pady)

        sep_1 = ttk.Separator(self.lframe_api_config, orient="vertical").grid(column=2, row=1, rowspan=3, padx=30, sticky="ns")

        # Cargamos la entry de Shodan con la API_KEY guardada en la configuración
        shodan_api_temp = ApiKeyShodanDefaultConfig()
        self.txt_shodan_api_key = Entry(self.lframe_api_config, width=var.text_entry_api_key_size)
        self.txt_shodan_api_key.insert(0, shodan_api_temp.api_key)
        self.txt_shodan_api_key.grid(column=1, row=1)
        btn_execute = Button(self.lframe_api_config, text="Check Shodan", width=25, height=2, command=self.check_shodan_api_key)
        btn_execute.grid(column=0, row=2, columnspan=2, padx=20, pady=20)
        lframe_nbook_api_info = LabelFrame(self.lframe_api_config, text="Shodan API Information:")
        lframe_nbook_api_info.grid(column=0, row=2, padx=10)

        # Entry de Zoomeye
        zoomeye_api_temp = ApiKeyZoomeyeDefaultConfig()
        self.txt_zoomeye_api_key = Entry(self.lframe_api_config, width=var.text_entry_api_key_size)
        self.txt_zoomeye_api_key.insert(0, zoomeye_api_temp.api_key)
        self.txt_zoomeye_api_key.grid(column=4, row=1)
        btn_execute = Button(self.lframe_api_config, text="Check Zoomeye", width=25, height=2, command=self.check_zoomeye_api_key)
        btn_execute.grid(column=3, row=2, columnspan=2, padx=20, pady=20)


    # Method to update the API-Key
    def check_shodan_api_key(self):
        try:
            self.lframe_shodan_api_info.grid_remove()
        except:
            nada = None
        try:
            self.lbl_api_shodan_state.grid_remove()
        except:
            nada = None
        self.lbl_api_shodan_state = Label(self.lframe_api_config, text="Checking API-KEY")
        self.lbl_api_shodan_state.grid(column=0, row=3, columnspan=2, padx=10, pady=10)
        print("check_shodan_api_key")
        if (self.txt_shodan_api_key.get() != ""):
            new_api_key = self.txt_shodan_api_key.get()
            if (ShodanQuery.check_api_key(new_api_key)):
                self.shodan_query.set_new_api_key(new_api_key)
                self.lbl_api_shodan_state.config(text=var.text_api_state_ok)
                self.display_shodan_api_info()
            else:
                self.lbl_api_shodan_state.config(text=var.text_api_state_ko)


    # Method to update the API-Key
    def check_zoomeye_api_key(self):
        try:
            self.lframe_zoomeye_api_info.grid_remove()
        except:
            nada = None
        try:
            self.lbl_api_zoomeye_state.grid_remove()
        except:
            nada = None
        self.lbl_api_zoomeye_state = Label(self.lframe_api_config, text="Checking API-KEY")
        self.lbl_api_zoomeye_state.grid(column=3, row=3, columnspan=2, padx=10, pady=10)

        if (self.txt_zoomeye_api_key.get() != ""):
            new_api_key = self.txt_zoomeye_api_key.get()
            print(new_api_key)
            print("check_zoomeye_api_key")
            try:
                zm = ZoomEye(api_key=new_api_key)
                login_result = zm.resources_info()
                print(login_result)
                self.lbl_api_zoomeye_state.config(text=var.text_api_state_ok)
                self.display_zoomeye_api_info(login_info=login_result)
            except:
                self.lbl_api_zoomeye_state.config(text=var.text_api_state_ko)


    # Method to display the API Info.
    def display_shodan_api_info(self):
        api_info = self.shodan_query.get_api_info()
        self.lframe_shodan_api_info = LabelFrame(self.lframe_api_config, text="Shodan Account info:")
        self.lframe_shodan_api_info.grid(column=0, row=4, columnspan=2)
        lbl_api_info1 = Label(self.lframe_shodan_api_info, text="Scan Credits: {}".format(api_info["scan_credits"])).grid(column=0, row=0, padx=10, pady=10)
        lbl_api_info2 = Label(self.lframe_shodan_api_info, text="Query Credits: {}".format(api_info["query_credits"])).grid(column=0, row=1, padx=10, pady=10)
        lbl_api_info3 = Label(self.lframe_shodan_api_info, text="Unlocked: {}".format(api_info["unlocked"])).grid(column=0, row=2, padx=10, pady=10)
        lbl_api_info4 = Label(self.lframe_shodan_api_info, text="Unlocked Left: {}".format(api_info["unlocked_left"])).grid(column=1, row=0, padx=10, pady=10)
        lbl_api_info5 = Label(self.lframe_shodan_api_info, text="Plan: {}".format(api_info["plan"])).grid(column=1, row=1, padx=10, pady=10)


    # Method to display the API Info.
    def display_zoomeye_api_info(self, login_info):
        print(login_info)
        user = login_info['user_info']['name']
        quota = str(login_info['quota_info']['remain_total_quota'])
        plan = login_info['plan']
        api_info = self.shodan_query.get_api_info()
        self.lframe_zoomeye_api_info = LabelFrame(self.lframe_api_config, text="Zoomeye Account info:")
        self.lframe_zoomeye_api_info.grid(column=3, row=4, columnspan=2)
        lbl_api_info1 = Label(self.lframe_zoomeye_api_info, text="User: " + user).grid(column=0, row=0, padx=10, pady=10)
        lbl_api_info2 = Label(self.lframe_zoomeye_api_info, text="Plan: " + plan).grid(column=0, row=1, padx=10, pady=10)
        lbl_api_info3 = Label(self.lframe_zoomeye_api_info, text="Quota Left: " + quota).grid(column=0, row=2, padx=10, pady=10)
        lbl_api_info4 = Label(self.lframe_zoomeye_api_info, text=" ").grid(column=1, row=0, padx=10, pady=10)
        lbl_api_info5 = Label(self.lframe_zoomeye_api_info, text=" ").grid(column=1, row=1, padx=10, pady=10)