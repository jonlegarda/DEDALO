from tkinter import *
from tkinter import ttk

import constants as var


class WindowVulnerabilities():

    def __init__(self, element):
        self.vuln_element = element
        self.vuln_window = Tk()
        self.vuln_window.geometry(var.vuln_window_size)
        self.vuln_window.title(var.vuln_window_title)

        try:
            print(self.vuln_element)
            if 'vulns' in dict(self.vuln_element).keys():
                label_yes_vulns = Label(self.vuln_window, text=var.label_yes_vulns_found).grid(column=0, row=0, padx=var.group_1_padx, pady=var.group_1_pady, sticky="w")
                self.display_vulnerability_list()
            else:
                label_no_vulns = Label(self.vuln_window, text=var.label_no_vulns_found).grid(column=0, row=0, padx=var.group_1_padx, pady=var.group_1_pady, sticky="w")
        except Exception as e:
            print(e)


    def display_vulnerability_list(self):
        columns = ("cve", "verified", "references", "cvss", "summary")

        vulns_tree_item = ttk.Treeview(self.vuln_window, columns=columns, show="headings", height=10, select="none")
        vulns_tree_item.grid(column=0, row=1, padx=var.group_1_padx, pady=var.group_1_pady)
        scroll_vert = ttk.Scrollbar(self.vuln_window, orient=VERTICAL, command=vulns_tree_item.yview)
        scroll_vert.grid(column=1, row=1, sticky="ns")
        vulns_tree_item.configure(yscroll=scroll_vert.set)

        vulns_tree_item.heading("cve", text="CVE")
        vulns_tree_item.heading("verified", text="Verified")
        vulns_tree_item.heading("references", text="References")
        vulns_tree_item.heading("cvss", text="CVSS")
        vulns_tree_item.heading("summary", text="Summary")

        vulns_tree_item.column(var.col1, width=100, stretch="NO")
        vulns_tree_item.column(var.col2, width=100, stretch="NO")
        vulns_tree_item.column(var.col3, width=200)
        vulns_tree_item.column(var.col4, width=70, stretch="NO")
        vulns_tree_item.column(var.col5, width=200)

        vulns = self.vuln_element["vulns"]
        i = 1
        for vuln in dict(vulns).items():
            row = (
                "{}".format(vuln[0]),
                "{}".format(vuln[1]["verified"]),
                "{}".format("Refs:"),
                "{}".format(vuln[1]["cvss"],
                "{}".format(vuln[1]["summary"])))
            tree_row = vulns_tree_item.insert('', END, iid=i, values=row)
            for ref in vuln[1]["references"]:
                i = i + 1
                vulns_tree_item.insert(tree_row, END, text="HEEEEEE", iid=i, open=False)
            i = i + 1