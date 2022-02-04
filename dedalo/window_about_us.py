from tkinter import Label
import constants as var


class WindowAboutUs():

    def __init__(self, main_frame):
        label_about_us = Label(main_frame, text=var.about_us)
        label_about_us.grid(column=0, row=0, padx=50, pady=25)