import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import requests
import json
import webbrowser

class windmillObj(tkinter.Tk):
    def __init__(self, item, frame, token, URL, xPos, yPos):
        super().__init__()
        self.item = item
        self.frame = frame
        self.token = token
        self.URL = URL
        self.frame.update()
        gridXSize = self.frame.winfo_width()/4
        gridYSize = self.frame.winfo_width()/4 + 100
        padding = 20

        self.photo = ImageTk.PhotoImage(Image.open('png-transparent-wind-farm-wind-turbine-wind-power-windmill-energy-angle-renewable-energy-wind-turbine-thumbnail.png'))
        imageHeight = self.photo.height()

        button = Button(self.frame, image=self.photo, command=lambda: self.openTurbineDetails(item))
        button.place(x=xPos*gridXSize, y=yPos*gridYSize+padding)

        Label(
            self.frame,
            text="Windmill name: " + self.item['name'],
            font=("Helvetica", 14)).place(x=xPos*gridXSize, y=yPos*gridYSize + padding + imageHeight + 10)

        Label(
            self.frame,
            text= "lat: " + str(item['gps']['lat']) + " lon: " + str(item['gps']['lon']),
            font=("Helvetica", 14)).place(x=xPos*gridXSize, y=yPos*gridYSize + padding + imageHeight + 40)


    def openTurbineDetails(self, dict):
        turbineView = Tk()
        turbineView.title(self.item['name'])
        headers = {
            'Authorization': f'Token {self.token}'
        }
        x = requests.get(self.URL + '/api/v1/turbine/' + dict['id'] + '/defects/detailed/', headers=headers)
        turbineDetail = json.loads(x.text)

        Label(
            turbineView,
            text=dict['name'],
            font=("Helvetica", 14)).pack(ipadx=10, ipady=10)

        Label(
            turbineView,
            text="defect amount: " + str(turbineDetail['data']['total_count']),
            font=("Helvetica", 14)).pack(ipadx=10, ipady=10)

        for key in turbineDetail['data']['defects']:
            Label(
                turbineView,
                text="Defect type: " + key['defect_type'],
                font=("Helvetica", 14)).pack(ipadx=10, ipady=10)

        link1 = Label(turbineView, text="Open report online", fg="blue", cursor="hand2")
        link1.pack()
        link1.bind("<Button-1>", lambda e: self.openOnline(dict['pdfs'][0]['blob']))

        link2 = Label(turbineView, text="Download Report", fg="blue", cursor="hand2")
        link2.pack()
        link2.bind("<Button-1>", lambda e: self.downloadPDF(str(dict['pdfs'][0]['blob']), dict['pdfs'][0]['filename']))

        print(turbineDetail)


    def openOnline(self, url):
        webbrowser.open_new(url)


    def downloadPDF(self, url, filename):
        r = requests.get(url)

        with open(filename, 'wb') as f:
            f.write(r.content)