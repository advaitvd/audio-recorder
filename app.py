from tkinter import *
from tkinter import filedialog
import play
import record
import os

open_file_path = {'path': None}

def browseFiles():
    filename = filedialog.askopenfilename(
        initialdir='.',
        title = 'Select a File'
    )
    label_file_explorer.configure(
        text=f"File Opened: {filename}"
    )
    open_file_path["path"] = filename

def play_audio():
    if open_file_path["path"] is not None:
        play.play_audio(open_file_path["path"])

def record_audio():
    filename = input_file_name.get()
    record_time = record_duration.get()
    record.record_audio(filename)

def delete_file():
    file_name = open_file_path["path"]
    print(file_name)
    if os.path.exists(file_name) and (input("Are you sure?[y/yes]\n").lower() in ("y", "yes", "")):
        os.system(f'rm {file_name}')


root = Tk()
root.title("Audio Player")

root.geometry("700x300")
root.config(background="white")

input_label = Label(
    root,
    text="Enter File Name:"
)
input_file_name = Entry(root)

record_duration_label = Label(
    root,
    text="Time in seconds:"
)
record_duration = Entry(root)

button_record = Button(
    root,
    text="Record",
    command=record_audio
)

label_file_explorer = Label(
    root,
    text="Explore files",
    width=100, height=4,
)

button_explore = Button(root,
    text="Browse Files",
    command=browseFiles
)

button_play = Button(
    root,
    text="Play",
    command=play_audio
)

button_delete = Button(
    root,
    text="Delete File",
    command=delete_file
)


input_label.pack()
input_file_name.pack()
record_duration_label.pack()
record_duration.pack()
button_record.pack()
label_file_explorer.pack()
button_explore.pack()
button_play.pack()
button_delete.pack()

root.mainloop()