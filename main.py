import os
import time
import tkinter
from tkinter import *
from tkinter import simpledialog, messagebox
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image, ImageFont, ImageDraw, ImageShow
import textwrap


#set selection for yes to continue to main gui or no to quit
#store selected picture as variable
#output selected picture and gui
#store all entries to variable to on click event
#store and output saved file


def load_button_click():
    text = textwrap.wrap(text=text_box.get('1.0', 'end-1c'), width=50)
    text2 = ""
    for i in text:
        text2 = text2 + i + '\n'
    msg = f"Pet's Name:{animal_name_var.get()}\n\n" \
          f"Animals breed:{dog_breed.get()}\n\n" \
          f"Age:{dog_age_var.get()}\n\n" \
          f"Date:{Date_var.get()}\n\n" \
          f"Description:{text2}"
    messagebox.showinfo(title="Test1", message=msg)
    global craft_img
    craft_img = Image.new("RGB", (480, 480), (240, 240, 240))
    img_w, img_h = ask_file_into_tk_image.size
    x, y = craft_img.size
    offset = ((x - img_w) // 2, (y - img_h) // int(1.4))
    craft_img.paste(im=ask_file_into_tk_image, box=offset)
    craft_img_1 = ImageDraw.Draw(craft_img)

    font = ImageFont.truetype("C:/Windows/Fonts/BELL.TTF", 18)

    pos = (0, 0)
    color = (0, 0, 0)

    craft_img_1.text(pos, f"{msg}", fill=color, font=font)

    ImageShow.show(craft_img)

#saves file to the computer and opens it so the user
def save_button_click():
    file_name = tkinter.simpledialog.askstring(title="File name", prompt="What would you like to name your file? :")
    file_name = file_name + ".pdf"
    Image.Image.save(craft_img, file_name)
    time.sleep(6)
    os.startfile(f"{file_name}")

def help_button_click():
    help_root = tkinter.Tk()
    help_root.title("Help")
    help_label = tkinter.Label(help_root,text="Users should fill out each entry with the appropriate data for its category.\n\n"
                                              "*The load to file button* :temporary store all text entries to prepare to save file\n"
                                 "\n *The save button* :saves the image and text document to a pdf file then opens it so\n "
                                 "the user can preview the file before saving it to their preferred destination\n\n")
    help_label.grid(column=0,row=0)

def create_folder():
    #path = "C:/Program Files/"
    #path += tkinter.simpledialog.askstring(title="Folder Creator",prompt="What would you like for the file name?")
    #path = tkinter.filedialog.askdirectory()

    #print("Directory '% s' created" % path)
    pass

checkin = tkinter.Tk()
checkin.title("Animal Data Verification")
tkinter.Label(checkin, text="Do you want to create an entry of data for your pet?").pack()

# A button that destroys the checkin root
tkinter.Button(checkin, text="YES", command=checkin.destroy, width=50, borderwidth=2, relief="solid").pack(
    pady=10, padx=10)

# A button that stops current program
tkinter.Button(checkin, text="NO", command=quit, width=50, borderwidth=2, relief="solid").pack(pady=10, padx=10)

checkin.mainloop()

# Places a loop to pause the program until a button is pressed
while checkin is True:
    pass

# Grabs picture before the creation of root
ask_file = askopenfilename(title="Find picture of your animal",filetypes=(
        ('JPEG', ('*.jpg', '*.jpeg', '*.jpe')), ('PNG', '*.png'),("all files", "*.*")))

# Setup and configuration of root
root = tkinter.Tk()
root.title("Pet Meta-Data")
root.geometry("500x500")
root.configure(relief="sunken", borderwidth=10, background="#ADD8E6")
root.minsize(1100, 500)
root.maxsize(1100, 500)
root.columnconfigure(0, weight=3)
root.columnconfigure(1, weight=3)
root.columnconfigure(2, weight=3)
root.columnconfigure(3, weight=2)
root.columnconfigure(4, weight=2)
root.columnconfigure(5, weight=2)
root.rowconfigure("all", weight=2)

# Displays photo
ask_file_into_tk_image = Image.open(ask_file).resize((200, 200))
ask_file_into_tk_image1 = ImageTk.PhotoImage(ask_file_into_tk_image, height=200, width=200)
tkinter.Label(root, image=ask_file_into_tk_image1, borderwidth=2, relief="solid", anchor="e", justify="right").grid(
    column=5, row=1, rowspan=2)

# Title of app
label = tkinter.Label(root, text="Pet Pic data", font=20, justify="center", anchor="center", background="#ADD8E6")
label.grid(column=4, row=0, sticky='')

# Animal name
animal_name_var = tkinter.StringVar()
animal_name_label = tkinter.Label(root, text="Animal name:", justify="center", background="#ADD8E6")
animal_name_label.grid(column=1, row=1, rowspan=3, sticky="e")
animal_name_entry = tkinter.Entry(root, textvariable=animal_name_var, borderwidth=3, relief="solid")
animal_name_entry.grid(column=2, row=1, rowspan=3, sticky="w")

# Animal Gender
animal_gender_var = tkinter.StringVar()
animal_gender_label = tkinter.Label(root, text="Gender of the pet:", background="#ADD8E6")
animal_gender_label.grid(column=1, row=2, rowspan=2, sticky="e")
animal_gender_entry = tkinter.Entry(root, textvariable=animal_gender_var, borderwidth=3, relief="solid")
animal_gender_entry.grid(column=2, row=2, rowspan=2, sticky="w")

# Dog breed label and entry
dog_breed = tkinter.StringVar()
tkinter.Label(root, text="Pet species and breed:", anchor="e", background="#ADD8E6", justify="right").grid(column=1, row=3, pady=20,
                                                                                               sticky="e")
entry1 = tkinter.Entry(root, borderwidth=3, relief="solid", textvariable=dog_breed)
entry1.place(height=400, width=20)
entry1.grid(column=2, row=3, sticky="w")

# Label and Entry for dog age
dog_age_var = tkinter.StringVar()
dog_age_label = tkinter.Label(root, text="Age of Pet:", anchor="e", justify="right", background="#ADD8E6")
dog_age_label.grid(column=1, row=4, sticky="e")
dog_age_entry = tkinter.Entry(root, borderwidth=3, relief="solid", textvariable=dog_age_var)
dog_age_entry.grid(column=2, row=4, sticky="w")

# Date of photo label and entry
Date_var = tkinter.StringVar()
Date_of_photo_label = tkinter.Label(root, text="Date of Photo:", anchor="e", justify="right", background="#ADD8E6")
Date_of_photo_label.grid(column=1, row=5, sticky="e")
Date_of_photo_entry = tkinter.Entry(root, borderwidth=3, relief="solid", textvariable=Date_var)
Date_of_photo_entry.grid(column=2, row=5, sticky="w")

# pet description
pet_desc_var = tkinter.StringVar()
tkinter.Label(root, text="Describe your pet!", width=50, background="#ADD8E6").grid(column=5, columnspan=5, row=3)
text_box = tkinter.Text(root, width=50, height=10, borderwidth=3, relief="solid", )
text_box.grid(column=5, columnspan=5, rowspan=4, row=4)

# Button to save file
save_button = tkinter.Button(root, text="Save contents", command=save_button_click)
save_button.grid(column=1, row=7, columnspan=2, sticky="")

# Button to load items to an image variable
load_button = tkinter.Button(root, text="Load contents to file", command=load_button_click)
load_button.grid(column=1, row=6, columnspan=2, sticky="")

#Button for instructions
help_button = tkinter.Button(root,text="Help",command=help_button_click)
help_button.grid(column=2,row=6,columnspan=2,padx=20,sticky="")

#Button for creating a folder
folder_button = tkinter.Button(root,text="Create a folder",command=create_folder)
folder_button.grid(column=2,row=7,columnspan=2,padx=20,sticky="")

root.mainloop()

