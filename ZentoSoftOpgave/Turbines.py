import requests
import json
import webbrowser
from tkinter import *
from tkinter import ttk
from windmillObj import windmillObj

class turbines_view(Frame):
    def __init__(self, main, title, geometry, URL, dict, token):
        super().__init__(main)
        self.frame = main
        self.frame.title(title)
        self.frame.geometry(geometry)
        self.turbineData = dict
        self.token = token
        self.URL = URL
        self.LoggedIn = True
        self.frame.update()

        ttk.Button(self.frame, text="Log Out", command=self.logout).place(x=self.frame.winfo_width() / 8 - 75, y=self.frame.winfo_width() / 8 - 50, height=100, width = 150)

        xPos = 1
        yPos = 0

        for item in self.turbineData['turbines']:
            windmillObj(item, self.frame, self.token, self.URL, xPos, yPos)
            xPos += 1
            if xPos == 3:
                xPos = 1
                yPos += 1

        self.frame.mainloop()

    def logout(self):
        self.LoggedIn = False
        self.frame.destroy()
