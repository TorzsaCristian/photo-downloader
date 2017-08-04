import urllib.request
import os
from tkinter import *


class GUI:
    def __init__(self, master):
        self.master = master
        self.main_frame = Frame(self.master)

        self.website_label = Label(self.main_frame, text='Base url (with %d for number):')
        self.start_int_label = Label(self.main_frame, text='Start number (INT):')
        self.end_int_label = Label(self.main_frame, text='End number (INT):')
        self.status_label = Label(self.main_frame, text='Click start to download!')

        self.website_entry = Entry(self.main_frame, width=50)
        self.start_int_entry = Entry(self.main_frame)
        self.end_int_entry = Entry(self.main_frame)

        self.start_button = Button(self.main_frame, text='Start downloading',
                                   command=lambda: start_download(self.website_entry.get(), self.start_int_entry.get(),
                                                                  self.end_int_entry.get()))

    def initialize(self):
        self.main_frame.pack(side=LEFT)

        self.website_label.grid(row=0)
        self.website_entry.grid(row=0, column=1)

        self.start_int_label.grid(row=1)
        self.start_int_entry.grid(row=1, column=1)

        self.end_int_label.grid(row=2)
        self.end_int_entry.grid(row=2, column=1)

        self.start_button.grid(row=3, column=1)


def start_download(website, start, end):
    try:
        start = int(start)
        end = int(end)
    except:
        return

    for i in range(start, end):
        url = website % i
        try:
            print(url)
            urllib.request.urlretrieve(url, 'photo%d.jpg' % i)
        except:
            pass


def main():
    root = Tk()
    gui = GUI(root)
    gui.initialize()

    root.mainloop()


main()
