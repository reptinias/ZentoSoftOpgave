import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image

window_width = 1500
window_height = 1080

root = tk.Tk()
root.title('Tkinter Window Demo')

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)
root.attributes('-alpha', 0.9)

ttk.Label(
    root,
    text='A Label with the Helvetica font',
    font=("Helvetica", 14)).pack(ipadx=10,ipady=10)

label = ttk.Label(root)
label['text'] = "hi, there"
label.pack()


def button_clicked():
    print('Button clicked')

button = ttk.Button(root, text="click me", command=button_clicked).pack()


def select(option):
    print(option)

ttk.Button(root, text='Rock', command=lambda: select('Rock')).pack()
ttk.Button(root, text='Paper',command=lambda: select('Paper')).pack()
ttk.Button(root, text='Scissors', command=lambda: select('Scissors')).pack()


def return_pressed(event):
    print('Return key pressed.')

def log(event):
    print(event)

btn = ttk.Button(root, text='Save')
btn.bind('<Return>', return_pressed)


btn.focus()
btn.pack(expand=True)

photo = ImageTk.PhotoImage(Image.open('download.png'))
image_label = ttk.Label(
    root,
    image=photo,
    text="python",
    padding=5
)
image_label.pack()

ttk.Button(
    root,
    text='Exit',
    command=lambda: root.quit()
).pack()

def download_clicked():
    showinfo(
        title='Information',
        message='Download button clicked!'
    )

ttk.Button(
    root,
    image=photo,
    text="download",
    command=download_clicked,
    compound=tk.LEFT,
).pack()


root.mainloop()
