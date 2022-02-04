import json
import zoomeye.sdk as ZoomEye
import utils
from tkinter import messagebox as MessageBox
from api_config_default_handler import ApiKeyZoomeyeDefaultConfig


def zoomeye_query_creator(simple_query, ip, ip_net, port, protocol, os, server, city, country):
    query_string = ""
    if (simple_query != ""):
        query_string += " {}".format(simple_query)
    if (ip != ""):
        if (query_string != ""):
            query_string += " +"
        query_string += " " + "ip:{}".format(ip)
    if (ip_net != ""):
        if (query_string != ""):
            query_string += " +"
        query_string += " " + "cidr:{}".format(ip_net)
    if (port != ""):
        if (query_string != ""):
            query_string += " +"
        query_string += " " + "port:{}".format(port)
    if (protocol != ""):
        if (query_string != ""):
            query_string += " +"
        query_string += " " + "protocol:{}".format(protocol)
    if (os != ""):
        if (query_string != ""):
            query_string += " +"
        query_string += " " + "os:{}".format(os)
    if (server != ""):
        if (query_string != ""):
            query_string += " +"
        query_string += " " + "server:{}".format(server)
    if (city != ""):
        if (query_string != ""):
            query_string += " +"
        query_string += " " + "city:{}".format(city)
    if (country != ""):
        if (query_string != ""):
            query_string += " +"
        query_string += " " + "country:{}".format(country)
    print("ZoomEye query created -> {}".format(query_string))
    return query_string


class ZoomEyeQuery:

    FACETS_ZOOMEYE = ['product', 'device', 'webapp', 'service', 'os', 'port', 'country', 'city']

    #   ZoomeyeQuery initializer:
    #   initializes the api key string taking into account the config file and creates the api object.
    def __init__(self):
        self.result_num = 1
        self.api_key_config = ApiKeyZoomeyeDefaultConfig()
        self.zoomeye_api_key = self.api_key_config.get_api_key()
        self.api = ZoomEye.ZoomEye(api_key=self.zoomeye_api_key)
        print("Class initializer: ZoomEyeQuery | Api-Key = {}".format(self.zoomeye_api_key))

    # method that runs the runs the query, saves a JSON file with the result and returns the result (in a dict structure).
    def run_zoomeye_query(self, search_text, contador):
        try:
            results = self.api.multi_page_search(search_text, page=5)
            print(self.api.show_count())
            contador.set(utils.format_number(str(self.api.show_count())))
            file = open("../results_zoomeye/result_" + str(self.result_num) + ".json", "w")
            json.dump(results, file)
            file.close()
            self.result_num = self.result_num + 1
            print("Method: ZoomeyeQuery().run_zoomeye_query | Api-Key = {} ".format(self.zoomeye_api_key))
            return results
        except Exception as e:
            contador.set('0')
            MessageBox.showerror("Zoomeye query error",str(e))
            print('Error: {}'.format(e))

    # method that runs the runs the query, saves a JSON file with the result and returns the result (in a dict structure).
    def run_zoomeye_his_query(self, search_text):
        results = []
        try:
            host = self.api.history_ip(search_text)
            print("Method: ZoomeyeQuery().run_zoomeye_query | Api-Key = {} ".format(self.zoomeye_api_key))
            for linea in host:
                results.append(search_text,linea['timestamp'],linea['portinfo']['port'])
        except Exception as e:
            print('Error: {}'.format(e))

    # method that runs the runs the query, saves a JSON file with the result and returns the result (in a dict structure).
    def run_zoomeye_query_facets(self, search_text):
        try:
            self.api.dork_search(search_text, facets=self.FACETS_ZOOMEYE)
            results = self.api.facet_data
            file = open("../results_json/zoomeye_facets/result_" + str(self.result_num) + ".json", "w")
            json.dump(results, file)
            file.close()
            self.result_num = self.result_num + 1
            print("Method: ZoomeyeQuery().run_zoomeye_query_facets | Api-Key = {} ".format(self.zoomeye_api_key))
            return results
        except Exception as e:
            print('Error: {}'.format(e))


    # method that checks if a possible api key is correct, creating a Zoomeye object and geting the info of it.
    #   In case the possible api key is correct, returns True.
    #   In case the possible api key is not correct, an exception is triggered and returns False.
    def check_api_key(possible_api_key):
        try:
            possible_api = ZoomEye.ZoomEye(possible_api_key)
            info = possible_api.info()
            return True
        except Exception:
            return False


    # Method that modifies the local parameters zoomeye_api_key and api using a new_api_key.
    # Before using this method, use "check_api_key".
    def set_new_api_key (self, new_api_key):
        self.zoomeye_api_key = new_api_key
        self.api = ZoomEye(self.zoomeye_api_key)
        print("Method: ZoomeyeQuery().set_new_api_key | Api-Key = {} ".format(self.zoomeye_api_key))


    # Method that returns a dict with the api information.
    def get_api_info(self):
        print("Class: ZoomEyeQuery(). Method: get_api_info() | Api-Key = {}".format(self.zoomeye_api_key))
        return self.api.info()
