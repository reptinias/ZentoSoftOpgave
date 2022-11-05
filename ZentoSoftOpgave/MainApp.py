from Login import login_view
from Turbines import turbines_view

import tkinter as tk

data = None
token = None
loggedIn = False
exitProgram = False
URL = 'https://raven-api-eu.clobotics.com'


if __name__ == "__main__" :
    while True:
        root = tk.Tk()
        w, h = root.winfo_screenwidth() - 50, root.winfo_screenheight() - 50
        geometry = "%dx%d+0+0" % (w, h)
        root.resizable(False, False)

        if loggedIn:
            title = "Your Turbines"
            displayTurbines = turbines_view(root, title, geometry, URL, data, token)

            loggedIn = displayTurbines.LoggedIn
            data = None
            token = None

        else:
            title = "login"
            loginWindow = login_view(root, title, geometry, URL)

            data = loginWindow.turbineDict
            loggedIn = loginWindow.LoggedIn
            token = loginWindow.token
            exitProgram = loginWindow.exit


        if exitProgram:
            break