import tkinter as tk
import tkinter.font as font
from tkinter import *
import requests
from datetime import datetime
import yttmp3

def pingWebsite(url):
    try:
        response = requests.get(url)
        session = requests.Session()
        session.verify = False

        if response.status_code == 200:
            return True
        else:
            print(f"Website is unreachable (Status code: {response.status_code}).")
            return False
    except (requests.ConnectionError, requests.exceptions.MissingSchema):
        print(f"Website is unreachable.")
        return False

def flash_label(label):
    if label.cget("foreground") == "red":
        label.config(foreground="black")
    else:
        label.config(foreground="red")
    label.after(500, flash_label, label)

def main_gui():
    # Create the main application window
    root = tk.Tk()
    root.title("YouTube to MP3/MP4 Converter")  # Set the title of the window
    root.size()
    root.geometry("600x400")
    root.resizable(False, False)

    title = font.Font(size=25)
    body = font.Font(size=12)
    trackFont = font.Font(size=9)
    errorFont = font.Font(size=9, weight='bold')

    # Create a label widget
    label = tk.Label(root, text="YouTube to MP3/MP4 Converter", font=title)
    label.pack(anchor='center')  # Use pack() method to add the label to the window

    label = tk.Label(root, text = "Input URL to a YouTube Video", font=body)
    label.place(relx=0.5, rely=0.18, anchor=CENTER)


    error = tk.Label(root, font=errorFont, fg="red")
    error.place(relx=0.5, rely=0.125, anchor=CENTER)

    url = Entry(root, width = 90)
    url.place(relx=0.5, rely=0.25, anchor=CENTER)

    labelframe = LabelFrame(root, text="Price Tracker")

    timeLabel = Label(root)
    timeLabel.place(relx=0.5, rely = 0.975, anchor=CENTER)

    def clock():
        t = datetime.now().strftime("Current Time: %H:%M:%S")
        timeLabel['text'] = t
        root.after(1000, clock) # run itself again after 1000 ms
    clock()

    # Create a function to handle button click event
    def button_click():
        yttmp3.yttmp3(url.get())
        completed.place(relx = 0.5, rely = 0.5, anchor=CENTER)  # Add the button to the window


    # Create a button widget
    button = tk.Button(root, text="Begin Tracking", command=button_click)
    button.place(relx = 0.5, rely = 0.35, anchor=CENTER)  # Add the button to the window

    completed = tk.Label(root, text="Download Completed")

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main_gui()