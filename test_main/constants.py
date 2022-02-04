# Variables used in the application

window_title = "Shodan TFM - Gonzalo & Jon. 2021."
window_size = "1300x800"

window_main = "   Queries & Findings   "
window_statistics = "   Statistics   "
window_history = "    Historical Queries    "
window_api = "   API Configuration   "
window_about_us = "   About Us   "

# Size of the text entry
text_entry_size = 25
text_entry_api_key_size = 50

# padx & pady
group_1_padx = 10
group_1_pady = 3
group_2_padx = 5
group_2_pady = 5
group_3_padx = 5
group_3_pady = 5

# column situation.
col1 = 0
col2 = 1
col3 = 2
col4 = 3
col5 = 4
col6 = 5
col7 = 6
col8 = 7
main_window_search_title = "Insert the information you want to find about below:"
history_window_search_title = "Find historical data of a network:"
# text's of the Main window' labels.
label_simpletext_1 = "Simple Text: "
text_label_simpletext_2 = "For general searches"
label_ip_1 = "IP: "
text_label_ip_2 = "format: X.X.X.X. Example: 8.8.8.8"
label_ip_net = "IP/Net "
label_country_1 = "Country: "
text_label_country_2 = "format: XX. Example: ES"
label_city_1 = "City: "
text_label_city_2 = "format: xxxxx. Example: Madrid"
label_port_1 = "Port: "
text_label_port_2 = "format: xxx. Example: 443"
label_protocol_1 = "Protocol: "
text_label_protocol_2 = "format: xxx. Example: tcp"
label_os_1 = "Operating system: "
text_label_os_2 = "format: xxxxx. Example: Ubuntu"
label_server_1 = "Server name: "
text_label_server_2 = "format: xxxxx. Example: Cisco"
text_label_country_list_1 = "Country: "

text_max_no_records = "Maximum number of records:"

button_run_shodan_query = "Run \n Shodan \n Query"
button_run_zoomeye_query = "Run \n ZoomEye \n Query"
button_both_queries = "Run \n Shodan & ZoomEye \n Query"


button_shodan_statistics = "Launch \n Shodan \n Statistics"
button_zoomeye_statistics = "Launch \n ZoomEye \n Statistics"
button_both_statistics = "Launch \n Shodan & ZoomEye \n Statistics"
button_clean_form = "Clear Form"

# text's of the query summary window
window_query_summary = "Last query Information: "
shodan_txt = "Shodan "
zoomeye_txt = "Zoomeye "
last_query_txt = "Last query: "
last_query_results = "Total Results: "
last_query_elapsed_time = "Elapsed Time: "
empty_value =  "             "

# text's of the Shodan API window' labels.
text_label_api_explain = "Configure your Shodan & Zoomeye API-Key. In case this is not done, a predefined API-Key will be used."
text_label_shodan_api_insert = "Insert your Shodan API-Key: "
text_label_zoomeye_api_insert = "Insert your Zoomeye API-Key: "

window_statistics_results = "Compare the statistics obtained from the applications: "
window_statistics_radiobuttons = "Select the item to compare: "

radiobtn_product = "Product"
radiobtn_product_value = "product"
radiobtn_device = "Device"
radiobtn_device_value = "device"
radiobtn_service = "Service"
radiobtn_service_value = "service"
radiobtn_os = "Operating System"
radiobtn_os_value = "os"
radiobtn_port= "Port"
radiobtn_port_value = "port"
radiobtn_city = "City"
radiobtn_city_value = "city"
radiobtn_country = "Country"
radiobtn_country_value = "country"

shodan_top5 = "SHODAN - TOP 5"
zoomeye_top5 = "ZOOMEYE - TOP 5"
shodan_top5_font = "lucida 10 bold"
zoomeye_top5_font = "lucida 10 bold"

top1 = "1.- "
top2 = "2.- "
top3 = "3.- "
top4 = "4.- "
top5 = "5.- "

top_value_width = 40

tbd_stats = "TBD."

# text's of the new API-Key status response.
text_api_state_ok = "The new API-Key has been correctly configured.                "
text_api_state_ko = "Error: the API-Key is not correct. Try another.               "

vuln_window_title = "Vulnerabilities associated..."
vuln_window_size = "800x300"
label_yes_vulns_found = "Be careful! These are the vulnerabilities associated to the element you selected..."
label_no_vulns_found = "Lucky you! No vulnerabilities associated to the item you selected."

country_list = [
    "",
    "Afghanistan",
    "Albania",
    "Algeria",
    "AmericanSamoa",
    "Andorra",
    "Angola"
]

about_us = "The application goal is making the comparation between two of the most important\n" \
           "libraries about Internet of Things elements: Shodan & ZoomEye.\n\n" \
           "Cybersecurity Master's Degree - Universidad de la Rioja (UNIR)\n\n" \
           "Gonzalo Ochoa de Eguileor López de Maturana & Jon Legarda Gonzalez\n\n" \
           "2021 December."