import json
import tkinter
from tkinter import *
from tkinter.messagebox import showinfo
import requests

class login_view(Frame):
    def __init__(self, root, title, geometry, URL):
        super().__init__(root)
        # root window
        self.frame = root
        self.frame.title(title)
        self.frame.geometry(geometry)

        self.frame.update()
        self.w, self.h = root.winfo_width(), root.winfo_height()

        self.entryWidth = 500

        # store email address and password
        self.email = tkinter.StringVar()
        self.password = tkinter.StringVar()

        self.placement = 50

        # GUI opsætning
        self.email_label = tkinter.Label(self.frame, text="Email Address:", font=("Helvetica", 14))
        self.email_label.place(x = self.w/2 - self.entryWidth/2, y = self.placement+20)

        self.email_entry = Entry(self.frame, textvariable=self.email, font=("Helvetica", 20))
        self.email_entry.place(x = self.w/2 - self.entryWidth/2, y = self.placement+50, height=50, width = self.entryWidth)

        # password
        self.password_label = Label(self.frame, text="Password:", font=("Helvetica", 14))
        self.password_label.place(x = self.w/2 - self.entryWidth/2, y = self.placement+110)

        self.password_entry = Entry(self.frame, textvariable=self.password, show="*", font=("Helvetica", 20))
        self.password_entry.place(x = self.w/2 - self.entryWidth/2, y = self.placement+140, height=50, width = self.entryWidth)

        # login button
        self.login_button = Button(self.frame, text="Login", font=("Helvetica", 30), command=self.login_clicked)
        self.login_button.place(x = self.w / 2 - 75, y = self.placement+210, height=100, width = 150)

        self.exit_button = Button(self.frame, text="Exit", font=("Helvetica", 30), command=self.exitProgram)
        self.exit_button.place(x=self.w / 2 - 75, y=self.placement+350, height=100, width = 150)

        self.exit = False
        self.LoggedIn = False
        self.turbineDict = None
        self.token = None

        self.URL = URL
        self.frame.mainloop()
        self.turbineData = {}



    def retrieve_list(self, data):
        if data:
            headers = {
                'Authorization': f'Token {data[0]}'
            }

            x = requests.get(self.URL + '/api/v1/campaign/' + data[1] + '/turbines/', headers=headers)
            turbineDict = json.loads(x.text)

            return turbineDict

    def login_clicked(self):
        """ callback when the login button clicked
        """
        self.email = self.email_entry.get()
        self.password = self.password_entry.get()

        if self.email == "" or self.password == "":
            print('error')
        else:
            data ={
                "email": self.email,
                "password": self.password
            }
            try:
                response = requests.post(self.URL + '/api/v1/auth/signin/', data=data)
                response_dict = json.loads(response.text)

                data = []
                data.append(response_dict['token'])
                data.append(response_dict['profile']['current_campaign']['id'])
                self.token = response_dict['token']
                self.turbineDict = self.retrieve_list(data)
                self.LoggedIn = True
                self.frame.destroy()

            except Exception as e:
                print(e)

    def exitProgram(self):
        self.exit = True
        self.frame.destroy()
