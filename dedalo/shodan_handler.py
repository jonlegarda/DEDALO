import json
from shodan import Shodan
from tkinter import messagebox as MessageBox
from api_config_default_handler import ApiKeyShodanDefaultConfig, ApiKeyZoomeyeDefaultConfig
#from IPy import IP

# Method to create the shodan query taking into account all the elements and adding to the query string if not empty.
def shodan_query_creator(simple_query, ip, ip_net, port, protocol, os, server, city, country):
    query_string = ""
    if (simple_query != ""):
        query_string += " {}".format(simple_query)
    if (ip != ""):
        query_string += " " + "ip:{}".format(ip)
    if (ip_net != ""):
        query_string += " " + "net:{}".format(ip_net)
    if (port != ""):
        query_string += " " + "port:{}".format(port)
    if (protocol != ""):
        query_string += " " + "protocol:{}".format(protocol)
    if (os != ""):
        query_string += " " + "os:{}".format(os)
    if (server != ""):
        query_string += " " + "server:{}".format(server)
    if (city != ""):
        query_string += " " + "city:{}".format(city)
    if (country != ""):
        query_string += " " + "country:{}".format(country)
    print("Shodan query created -> {}".format(query_string))
    return query_string


class ShodanQuery:

    FACETS_SHODAN = [
        'product',
        'device',
        'os',
        'port',
        'city',
        'country',
    ]

    # ShodanQuery initializer:
    #   initializes the api key string taking into account the config file and creates the api object.
    def __init__(self):
        self.result_num = 1
        self.api_key_config = ApiKeyShodanDefaultConfig()
        self.shodan_api_key = self.api_key_config.get_api_key()
        self.api = Shodan(self.shodan_api_key)
        print("Class initializer: ShodanQuery | Api-Key = {}".format(self.shodan_api_key))

    # method that runs the runs the query, saves a JSON file with the result and returns the result (in a dict structure).
    def run_shodan_query(self, search_text):
        try:
            results = self.api.search(search_text)
            file = open("../results_json/shodan_query/result_" + str(self.result_num) + ".json", "w")
            json.dump(results, file)
            file.close()
            self.result_num = self.result_num + 1
            print("Method: ShodanQuery().run_shodan_query | Api-Key = {} ".format(self.shodan_api_key))
            return results
        except Exception as e:
            MessageBox.showerror("Shodan query error", str(e))
            print('Error: {}'.format(e))

    def run_shodan_his_query(self, search_text):
        #ip = IP(search_text)
        results = []
        #for contador in ip:
        try:
            #currentip = str(contador)
            host = self.api.host(search_text, history=True)
            #print(host)
            results.append([host['ip_str'], host['last_update'], host['ports']])
        except Exception as e:
            print('pass')
            pass
        return results


    # method that runs the runs the query with Facets, saves a JSON file with the result and returns the result (in a dict structure).
    def run_shodan_query_facets(self, search_text):
        try:
            results = self.api.count(search_text, facets=self.FACETS_SHODAN)
            file = open("../results_json/shodan_facets/shodan_facets" + str(self.result_num) + ".json", "w")
            json.dump(results, file)
            file.close()
            self.result_num = self.result_num + 1
            print("Method: ShodanQuery().run_shodan_query_facets | Api-Key = {} ".format(self.shodan_api_key))
            return results
        except Exception as e:
            print('Error: {}'.format(e))


    # method that checks if a possible api key is correct, creating a Shodan object and geting the info of it.
    #   In case the possible api key is correct, returns True.
    #   In case the possible api key is not correct, an exception is triggered and returns False.
    def check_api_key(possible_api_key):
        try:
            possible_api = Shodan(possible_api_key)
            info = possible_api.info()
            return True
        except Exception:
            return False


    # Method that modifies the local parameters shodan_api_key and api using a new_api_key.
    # Before using this method, use "check_api_key".
    def set_new_api_key (self, new_api_key):
        self.shodan_api_key = new_api_key
        self.api = Shodan(self.shodan_api_key)
        print("Method: ShodanQuery().set_new_api_key | Api-Key = {} ".format(self.shodan_api_key))


    # Method that returns a dict with the api information.
    def get_api_info(self):
        print("Class: ShodanQuery(). Method: get_api_info() | Api-Key = {}".format(self.shodan_api_key))
        return self.api.info()