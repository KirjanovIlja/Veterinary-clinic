import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
from fontTools.ttLib import TTFont
from data_operator import *

# Fonts
light_font = TTFont("fonts\Jost-Light.ttf")
bold_font = TTFont("fonts\Jost-Bold.ttf")

# Data operator object
data_operator = DataOperator()


# The main method for running app

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Setting last ID's
        data_operator.get_last_id()

        # Setting minimal size of the window
        self.minheight = 500
        self.minwidth = 800

        self.minsize(self.minwidth, self.minheight)

        # Setting icon of the window
        tk.Tk.iconbitmap(self, default="images\Pet-Doctor.ico")
        tk.Tk.wm_title(self, "Veterinary Clinic by KirjanovIlja")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Container of pages
        self.frames = {}
        for f in (StartPage, Menu, DataBase, Dogs, Cats, Doctors, Owners):
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # By default app starts from the Start Page
        self.show_frame(StartPage)

    # Method to show the frame
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#EFFFFB")

        # Text greeting

        label = Label(self, text="Hello there", font=(bold_font, 20), bg="#EFFFFB", fg="#DF744A")
        label.place(x=400, y=100, anchor="n")
        label2 = Label(self, text="Veterinary Clinic by KirjanovIlja", font=(bold_font, 16), bg="#EFFFFB", fg="#DF744A")
        label2.place(x=400, y=150, anchor="n")

        # Images that for the buttons
        button_image_start = Image.open('images\_start.png')
        self.button_photo_start = ImageTk.PhotoImage(button_image_start)
        button_image_reset_database = Image.open("images\_reset_database.png")
        self.button_photo_database = ImageTk.PhotoImage(button_image_reset_database)

        # Navigation buttons
        button = Button(self, image=self.button_photo_start, bd=0, command=lambda: controller.show_frame(Menu))
        button.place(x=400, y=180, anchor="n")
        button_reset_data = Button(self, image=self.button_photo_database, bd=0, command=lambda: self.reset_data_base())
        button_reset_data.pack(anchor="s", expand=True)

    # Method references to DataOperator object and calls reset_data() method
    def reset_data_base(self):
        answer = messagebox.askyesno("Reset Database", message="Reset Database to default?")
        if answer == True:
            data_operator.restart_data()


class Menu(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.configure(bg="#EFFFFB")
        label = Label(self, text="Menu", font=(bold_font, 20), bg="#EFFFFB", fg="#DF744A")
        label.pack(pady=10, padx=10)

        # Images for the buttons
        button_image_back = Image.open("images\_back.png")
        self.button_photo_back = ImageTk.PhotoImage(button_image_back)
        button_image_exit = Image.open("images\_exit.png")
        self.button_photo_exit = ImageTk.PhotoImage(button_image_exit)
        button_image_database = Image.open("images\_database.png")
        self.button_photo_database = ImageTk.PhotoImage(button_image_database)


        # Navigation buttons
        button = tk.Button(self, image=self.button_photo_database,bd=0, command=lambda: controller.show_frame(DataBase))
        button.pack()
        button_back = tk.Button(self, image=self.button_photo_back, bd=0, command=lambda: controller.show_frame(StartPage))
        button_back.place(relx=1, rely=0.93, anchor="se")
        button_exit = tk.Button(self, image=self.button_photo_exit, bd=0, command=lambda: exit())
        button_exit.place(relx=1, rely=1, anchor="se")


class DataBase(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.configure(bg="#EFFFFB")

        label = Label(self, text="Database", font=(bold_font, 20),bg="#EFFFFB", fg="#DF744A")
        label.pack(pady=10, padx=10)

        # Images for the buttons

        button_image_back = Image.open("images\_back.png")
        self.button_photo_back = ImageTk.PhotoImage(button_image_back)
        button_image_exit = Image.open("images\_exit.png")
        self.button_photo_exit = ImageTk.PhotoImage(button_image_exit)
        button_image_dog = Image.open("images\_dog.png")
        self.button_photo_dog = ImageTk.PhotoImage(button_image_dog)
        button_image_cat = Image.open("images\_cat.png")
        self.button_photo_cat = ImageTk.PhotoImage(button_image_cat)
        button_image_owner= Image.open("images\_owner.png")
        self.button_photo_owner = ImageTk.PhotoImage(button_image_owner)
        button_image_doctor = Image.open("images\_doctor.png")
        self.button_photo_doctor = ImageTk.PhotoImage(button_image_doctor)

        # Navigation buttons
        button = Button(self, image=self.button_photo_dog, bd=0, command=lambda: controller.show_frame(Dogs))
        button.pack()
        button = Button(self, image=self.button_photo_cat, bd=0, command=lambda: controller.show_frame(Cats))
        button.pack()
        button2 = Button(self, image=self.button_photo_owner, bd=0, command=lambda: controller.show_frame(Owners))
        button2.pack()
        button3 = Button(self, image=self.button_photo_doctor, bd=0, command=lambda: controller.show_frame(Doctors))
        button3.pack()
        button_back = Button(self, image=self.button_photo_back, bd=0, command=lambda: controller.show_frame(Menu))
        button_back.place(relx=1, rely=0.93, anchor="se")
        button_exit = Button(self, image=self.button_photo_exit, bd=0, command=lambda: exit())
        button_exit.place(relx=1, rely=1, anchor="se")


class Dogs(tk.Frame):
    def __init__(self, parent, controller):


        # Headers
        tk.Frame.__init__(self, parent)
        self.configure(bg="#EFFFFB")
        label = Label(self, text="Dogs", font=(bold_font, 20),bg="#EFFFFB", fg="#DF744A")
        label.pack()
        label1 = Label(self, text="Adding",font=(bold_font, 16),bg="#EFFFFB", fg="#DF744A")
        label1.place(x=110, y=30)
        label2 = Label(self, text="Updating", font=(bold_font, 16),bg="#EFFFFB", fg="#DF744A")
        label2.place(x=615, y=30)
        label3 = Label(self, text="Deleting", font=(bold_font, 16),bg="#EFFFFB", fg="#DF744A")
        label3.place(x=370, y=70)

        # Adding dog
        name = Entry(self, bg="#FFF", font=(light_font, 10), fg="#F1C232", insertbackground="#DF744A")
        name.place(x=80, y=70, anchor="w")
        label_name = Label(self, text="Name", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
        label_name.place(x=80, y=70, anchor="e")

        age = Entry(self, bg="#FFF", font=(light_font, 10), fg="#F1C232", insertbackground="#DF744A")
        age.place(x=80, y=100, anchor="w")
        label_age = Label(self, text="Age", font=(bold_font, 10),bg="#EFFFFB", fg="#DF744A")
        label_age.place(x=80, y=100, anchor="e")

        breed = Entry(self, bg="#FFF", font=(light_font, 10), fg="#F1C232", insertbackground="#DF744A")
        breed.place(x=80, y=130, anchor="w")
        label_breed = Label(self, text="Breed", font=(bold_font, 10),bg="#EFFFFB", fg="#DF744A")
        label_breed.place(x=80, y=130, anchor="e")

        tail = Combobox(self, values=["Yes", "No"], width=17)
        tail.place(x=80, y=160, anchor="w")
        label_tail = Label(self, text="Is tail cut?", font=(bold_font, 10),bg="#EFFFFB", fg="#DF744A")
        label_tail.place(x=80, y=160, anchor="e")

        castrated = Combobox(self, values=["Yes", "No"], width=17)
        castrated.place(x=80, y=190, anchor="w")
        label_cast = Label(self, text="Castrated?", font=(bold_font, 10),bg="#EFFFFB", fg="#DF744A")
        label_cast.place(x=80, y=190, anchor="e")

        sound = Entry(self, bg="#FFF", font=(light_font, 10), fg="#F1C232", insertbackground="#DF744A")
        sound.place(x=80, y=220, anchor="w")
        label_sound = Label(self, text="Barking", font=(bold_font, 10),bg="#EFFFFB", fg="#DF744A")
        label_sound.place(x=80, y=220, anchor="e")

        sex = Combobox(self, values=["M", "F"], width=17)
        sex.place(x=80, y=250, anchor="w")
        label_sex = Label(self, text="Sex", font=(bold_font, 10),bg="#EFFFFB", fg="#DF744A")
        label_sex.place(x=80, y=250, anchor="e")

        doctor = Combobox(self, values=data_operator.get_data_base("doctors"), width=30)
        doctor.place(x=80, y=280, anchor="w")
        label_doctor = Label(self, text="Doctor", font=(bold_font, 10),bg="#EFFFFB", fg="#DF744A")
        label_doctor.place(x=80, y=280, anchor="e")

        owner = Combobox(self, values=data_operator.get_data_base("owners"), width=30)
        owner.place(x=80, y=310, anchor="w")
        label_owner = Label(self, text="Owner", font=(bold_font, 10),bg="#EFFFFB", fg="#DF744A")
        label_owner.place(x=80, y=310, anchor="e")

        button_add = Button(self, text="Add",
                            command=lambda: call_create_dog_and_reset_value(name, age, breed, tail, castrated, sound,
                                                                            sex, owner, doctor, list_of_dogs))
        button_add.place(x=80, y=340)

        # Scrolling option for the list of dogs
        scrollbar = Scrollbar(self, orient=VERTICAL)
        list_of_dogs = Listbox(self, yscrollcommand=scrollbar.set, width=50)
        scrollbar.config(command=list_of_dogs.yview)
        show_dog_data_base(list_of_dogs)
        list_of_dogs.place(relx=0.5, rely=1, anchor="s")

        # Deleting dog
        if len(data_operator.get_id_data_base("dogs")) < 1:
            label_empty = Label(self, text="List is empty", font=(bold_font, 16), bg="#EFFFFB", fg="#DF744A")
            label_empty.place(x=350, y=110)
        else:
            dog_id = Combobox(self, values=data_operator.get_id_data_base("dogs"), width=10)
            dog_id.place(x=370, y=110, anchor="w")
            label_id_delete = Label(self, text="Id to delete", font=(bold_font, 10),bg="#EFFFFB", fg="#DF744A")
            label_id_delete.place(x=370, y=110, anchor="e")
            button_delete = Button(self, text="Delete",
                                 command=lambda: delete_dog_and_reset_id_value(dog_id, list_of_dogs))
            button_delete.place(x=370, y=140)

        # Updating dog
        if len(data_operator.get_id_data_base("dogs")) < 1:
            label_empty = Label(self, text="List is empty", font=(bold_font, 16),bg="#EFFFFB", fg="#DF744A")
            label_empty.place(x=600, y=80)
        else:
            dog_id_upd = Combobox(self, values=data_operator.get_id_data_base("dogs"), width=10)
            dog_id_upd.place(x=620, y=70, anchor="w")
            label_id_delete = Label(self, text="Id to update", font=(bold_font, 10),bg="#EFFFFB", fg="#DF744A")
            label_id_delete.place(x=620, y=70, anchor="e")

            name_upd = Entry(self, bg="#FFF", font=(light_font, 10), fg="#F1C232", insertbackground="#DF744A")
            name_upd.place(x=620, y=100, anchor="w")
            label_name = Label(self, text="Name", font=(bold_font, 10),bg="#EFFFFB", fg="#DF744A")
            label_name.place(x=620, y=100, anchor="e")

            age_upd = Entry(self, bg="#FFF", font=(light_font, 10), fg="#F1C232", insertbackground="#DF744A")
            age_upd.place(x=620, y=130, anchor="w")
            label_age = Label(self, text="Age", font=(bold_font, 10),bg="#EFFFFB", fg="#DF744A")
            label_age.place(x=620, y=130, anchor="e")

            breed_upd = Entry(self, bg="#FFF", font=(light_font, 10), fg="#F1C232", insertbackground="#DF744A")
            breed_upd.place(x=620, y=160, anchor="w")
            label_breed = Label(self, text="Breed", font=(bold_font, 10),bg="#EFFFFB", fg="#DF744A")
            label_breed.place(x=620, y=160, anchor="e")

            tail_upd = Combobox(self, values=["Yes", "No"], width=17)
            tail_upd.place(x=620, y=190, anchor="w")
            label_tail = Label(self, text="Is tail cut?", font=(bold_font, 10),bg="#EFFFFB", fg="#DF744A")
            label_tail.place(x=620, y=190, anchor="e")

            castrated_upd = Combobox(self, values=["Yes", "No"], width=17)
            castrated_upd.place(x=620, y=220, anchor="w")
            label_cast = Label(self, text="Castrated?", font=(bold_font, 10),bg="#EFFFFB", fg="#DF744A")
            label_cast.place(x=620, y=220, anchor="e")

            sound_upd = Entry(self, bg="#FFF", font=(light_font, 10), fg="#F1C232", insertbackground="#DF744A")
            sound_upd.place(x=620, y=250, anchor="w")
            label_sound = Label(self, text="Barking", font=(bold_font, 10),bg="#EFFFFB", fg="#DF744A")
            label_sound.place(x=620, y=250, anchor="e")

            sex_upd = Combobox(self, values=["M", "F"], width=17)
            sex_upd.place(x=620, y=280, anchor="w")
            label_sex = Label(self, text="Sex", font=(bold_font, 10),bg="#EFFFFB", fg="#DF744A")
            label_sex.place(x=620, y=280, anchor="e")

            doctor_upd = Combobox(self, values=data_operator.get_data_base("doctors"), width=25)
            doctor_upd.place(x=620, y=310, anchor="w")
            label_doctor = Label(self, text="Doctor", font=(bold_font, 10),bg="#EFFFFB", fg="#DF744A")
            label_doctor.place(x=620, y=310, anchor="e")

            owner_upd = Combobox(self, values=data_operator.get_data_base("owners"), width=25)
            owner_upd.place(x=620, y=340, anchor="w")
            label_owner = Label(self, text="Owner", font=(bold_font, 10),bg="#EFFFFB", fg="#DF744A")
            label_owner.place(x=620, y=340, anchor="e")

            button_update = Button(self, text="Update",
                                       command=lambda: call_update_dog_and_reset_values(dog_id_upd, name_upd, age_upd,
                                                                                        breed_upd, tail_upd,
                                                                                        castrated_upd, sound_upd,
                                                                                        sex_upd, owner_upd, doctor_upd,
                                                                                        list_of_dogs))
            button_update.place(x=620, y=370)

        # Images for the buttons
        button_image_update = Image.open("images\_update.png")
        self.button_photo_update=ImageTk.PhotoImage(button_image_update)
        button_image_delete = Image.open("images\_delete.png")
        self.button_photo_delete = ImageTk.PhotoImage(button_image_delete)
        button_image_add = Image.open("images\_add.png")
        self.button_photo_add = ImageTk.PhotoImage(button_image_add)
        button_image_back = Image.open("images\_back.png")
        self.button_photo_back = ImageTk.PhotoImage(button_image_back)
        button_image_exit = Image.open("images\_exit.png")
        self.button_photo_exit = ImageTk.PhotoImage(button_image_exit)

        # Navigation
        try:
            button_update
            button_delete
            button_update.configure(bd=0, image=self.button_photo_update)
            button_delete.configure(bd=0, image=self.button_photo_delete)
        except NameError:
            pass
        button_add.configure(bd=0, image=self.button_photo_add)
        button_back = Button(self, image=self.button_photo_back, bd=0, command=lambda: controller.show_frame(DataBase))
        button_back.place(relx=1, rely=0.93, anchor="se")
        button_exit = Button(self, image=self.button_photo_exit,bd=0, command=lambda: exit())
        button_exit.place(relx=1, rely=1, anchor="se")

class Cats(tk.Frame):
    def __init__(self, parent, controller):

        # Headers
        tk.Frame.__init__(self, parent)
        self.configure(bg="#EFFFFB")
        label = Label(self, text="Cats", font=(bold_font, 20),bg="#EFFFFB", fg="#DF744A")
        label.pack()
        label1 = Label(self, text="Adding",font=(bold_font, 16),bg="#EFFFFB", fg="#DF744A")
        label1.place(x=110, y=30)
        label2 = Label(self, text="Updating", font=(bold_font, 16),bg="#EFFFFB", fg="#DF744A")
        label2.place(x=615, y=30)
        label3 = Label(self, text="Deleting", font=(bold_font, 16),bg="#EFFFFB", fg="#DF744A")
        label3.place(x=370, y=70)

        # Adding cat
        name = Entry(self, bg="#FFF", font=(light_font, 10), fg="#F1C232", insertbackground="#DF744A")
        name.place(x=80, y=70, anchor="w")
        label_name = Label(self, text="Name", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
        label_name.place(x=80, y=70, anchor="e")

        age = Entry(self, bg="#FFF", font=(light_font, 10), fg="#F1C232", insertbackground="#DF744A")
        age.place(x=80, y=100, anchor="w")
        label_age = Label(self, text="Age", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
        label_age.place(x=80, y=100, anchor="e")

        breed = Entry(self, bg="#FFF", font=(light_font, 10), fg="#F1C232", insertbackground="#DF744A")
        breed.place(x=80, y=130, anchor="w")
        label_breed = Label(self, text="Breed", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
        label_breed.place(x=80, y=130, anchor="e")

        castrated = Combobox(self, values=["Yes", "No"], width=17)
        castrated.place(x=80, y=160, anchor="w")
        label_cast = Label(self, text="Castrated?", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
        label_cast.place(x=80, y=160, anchor="e")

        sex = Combobox(self, values=["M", "F"], width=17)
        sex.place(x=80, y=190, anchor="w")
        label_sex = Label(self, text="Sex", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
        label_sex.place(x=80, y=190, anchor="e")

        doctor = Combobox(self, values=data_operator.get_data_base("doctors"), width=30)
        doctor.place(x=80, y=220, anchor="w")
        label_doctor = Label(self, text="Doctor", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
        label_doctor.place(x=80, y=220, anchor="e")

        owner = Combobox(self, values=data_operator.get_data_base("owners"), width=30)
        owner.place(x=80, y=250, anchor="w")
        label_owner = Label(self, text="Owner", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
        label_owner.place(x=80, y=250, anchor="e")

        scrollbar = Scrollbar(self, orient=VERTICAL)
        list_of_cats = Listbox(self, yscrollcommand=scrollbar.set, width=50)
        scrollbar.config(command=list_of_cats.yview)
        show_cat_data_base(list_of_cats)
        list_of_cats.place(relx=0.5, rely=1, anchor="s")

        button_add = Button(self, text="Submit",
                            command=lambda: call_create_cat_and_reset_value(name, age, breed, castrated, sex, owner,
                                                                            doctor, list_of_cats))
        button_add.place(x=80, y=280)

        # Deleting cat
        if len(data_operator.get_id_data_base("cats")) < 1:
            label_empty = Label(self, text="List is empty", font=(bold_font, 12), bg="#EFFFFB", fg="#DF744A")
            label_empty.place(x=350, y=110, anchor='w')
        else:
            cat_id = Combobox(self, values=data_operator.get_id_data_base("cats"), width=10)
            cat_id.place(x=370, y=110, anchor="w")
            label_id_delete = Label(self, text="Id to delete", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
            label_id_delete.place(x=370, y=110, anchor="e")
            button_delete = Button(self, text="Delete",
                                 command=lambda: delete_cat_and_reset_id_value(cat_id, list_of_cats))
            button_delete.place(x=370, y=140, anchor="w")

        # Updating cat
        if len(data_operator.get_id_data_base("cats")) < 1:
            label_empty = Label(self, text="List is empty", font=(bold_font, 12), bg="#EFFFFB", fg="#DF744A")
            label_empty.place(x=620, y=70)
        else:
            cat_id_upd = Combobox(self, values=data_operator.get_id_data_base("cats"), width=10)
            cat_id_upd.place(x=620, y=70, anchor="w")
            label_id_delete = Label(self, text="Id to update", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
            label_id_delete.place(x=620, y=70, anchor="e")

            name_upd = Entry(self, bg="#FFF", font=(light_font, 10), fg="#F1C232", insertbackground="#DF744A")
            name_upd.place(x=620, y=100, anchor="w")
            label_name = Label(self, text="Name", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
            label_name.place(x=620, y=100, anchor="e")

            age_upd = Entry(self, bg="#FFF", font=(light_font, 10), fg="#F1C232", insertbackground="#DF744A")
            age_upd.place(x=620, y=130, anchor="w")
            label_age = Label(self, text="Age", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
            label_age.place(x=620, y=130, anchor="e")

            breed_upd = Entry(self, bg="#FFF", font=(light_font, 10), fg="#F1C232", insertbackground="#DF744A")
            breed_upd.place(x=620, y=160, anchor="w")
            label_breed = Label(self, text="Breed", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
            label_breed.place(x=620, y=160, anchor="e")

            castrated_upd = Combobox(self, values=["Yes", "No"], width=17)
            castrated_upd.place(x=620, y=190, anchor="w")
            label_cast = Label(self, text="Castrated?", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
            label_cast.place(x=620, y=190, anchor="e")

            sex_upd = Combobox(self, values=["M", "F"], width=17)
            sex_upd.place(x=620, y=220, anchor="w")
            label_sex = Label(self, text="Sex", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
            label_sex.place(x=620, y=220, anchor="e")

            doctor_upd = Combobox(self, values=data_operator.get_data_base("doctors"), width=25)
            doctor_upd.place(x=620, y=250, anchor="w")
            label_doctor = Label(self, text="Doctor", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
            label_doctor.place(x=620, y=250, anchor="e")

            owner_upd = Combobox(self, values=data_operator.get_data_base("owners"), width=25)
            owner_upd.place(x=620, y=280, anchor="w")
            label_owner = Label(self, text="Owner", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
            label_owner.place(x=620, y=280, anchor="e")

            button_update = Button(self, text="Update",
                                       command=lambda: call_update_cat_and_reset_values(cat_id_upd, name_upd,
                                                                                        age_upd,
                                                                                        breed_upd,
                                                                                        castrated_upd,
                                                                                        sex_upd, owner_upd,
                                                                                        doctor_upd,
                                                                                        list_of_cats))
            button_update.place(x=620, y=310)
        # Images for the buttons
        button_image_update = Image.open("images\_update.png")
        self.button_photo_update=ImageTk.PhotoImage(button_image_update)
        button_image_delete = Image.open("images\_delete.png")
        self.button_photo_delete = ImageTk.PhotoImage(button_image_delete)
        button_image_add = Image.open("images\_add.png")
        self.button_photo_add = ImageTk.PhotoImage(button_image_add)
        button_image_back = Image.open("images\_back.png")
        self.button_photo_back = ImageTk.PhotoImage(button_image_back)
        button_image_exit = Image.open("images\_exit.png")
        self.button_photo_exit = ImageTk.PhotoImage(button_image_exit)

        # Navigation
        try:
            button_update
            button_delete
            button_update.configure(bd=0, image=self.button_photo_update)
            button_delete.configure(bd=0, image=self.button_photo_delete)
        except NameError:
            pass
        button_add.configure(bd=0, image=self.button_photo_add)
        button_back = Button(self, image=self.button_photo_back, bd=0, command=lambda: controller.show_frame(DataBase))
        button_back.place(relx=1, rely=0.93, anchor="se")
        button_exit = Button(self, image=self.button_photo_exit,bd=0, command=lambda: exit())
        button_exit.place(relx=1, rely=1, anchor="se")


class Owners(tk.Frame):
    def __init__(self, parent, controller):

        # Headers
        tk.Frame.__init__(self, parent)
        self.configure(bg="#EFFFFB")

        label = Label(self, text="Owners", font=(bold_font, 20),bg="#EFFFFB", fg="#DF744A")
        label.pack()
        label1 = Label(self, text="Adding",font=(bold_font, 16),bg="#EFFFFB", fg="#DF744A")
        label1.place(x=110, y=30)
        label2 = Label(self, text="Updating", font=(bold_font, 16),bg="#EFFFFB", fg="#DF744A")
        label2.place(x=615, y=30)
        label3 = Label(self, text="Deleting", font=(bold_font, 16),bg="#EFFFFB", fg="#DF744A")
        label3.place(x=370, y=70)

        # Adding owner
        name = Entry(self, bg="#FFF", font=(light_font, 10), fg="#F1C232", insertbackground="#DF744A")
        name.place(x=80, y=70, anchor="w")
        label_name = Label(self, text="Name", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
        label_name.place(x=80, y=70, anchor="e")

        surname = Entry(self, bg="#FFF", font=(light_font, 10), fg="#F1C232", insertbackground="#DF744A")
        surname.place(x=80, y=100, anchor="w")
        label_surname = Label(self, text="Surname", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
        label_surname.place(x=80, y=100, anchor="e")

        contact = Entry(self, bg="#FFF", font=(light_font, 10), fg="#F1C232", insertbackground="#DF744A")
        contact.place(x=80, y=130, anchor="w")
        label_contact = Label(self, text="Contact", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
        label_contact.place(x=80, y=130, anchor="e")

        scrollbar = Scrollbar(self, orient=VERTICAL)
        list_of_owners = Listbox(self, yscrollcommand=scrollbar.set, width=50)
        scrollbar.config(command=list_of_owners.yview)
        show_owner_data_base(list_of_owners)
        list_of_owners.place(relx=0.5, rely=1, anchor="s")

        button_add = Button(self, text="Add",
                            command=lambda: call_create_owner_and_reset_value(name, surname, contact, list_of_owners))
        button_add.place(x=80, y=160)

        # Deleting owner
        if len(data_operator.get_id_data_base("owners")) < 1:
            label_empty = Label(self, text="List is empty", font=(bold_font, 12), bg="#EFFFFB", fg="#DF744A")
            label_empty.place(x=350, y=110)
        else:
            owner_id = Combobox(self, values=data_operator.get_id_data_base("owners"), width=10)
            owner_id.place(x=370, y=110, anchor="w")
            label_id_delete = Label(self, text="Id to delete", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
            label_id_delete.place(x=370, y=110, anchor="e")
            button_delete = Button(self, text="Delete",
                                 command=lambda: delete_owner_and_reset_id_value(owner_id, list_of_owners))
            button_delete.place(x=370, y=140, anchor="w")

        # Updating owner
        if len(data_operator.get_id_data_base("owners")) < 1:
            label_empty = Label(self, text="List is empty", font=(bold_font, 12), bg="#EFFFFB", fg="#DF744A")
            label_empty.place(x=620, y=70)
        else:
            owner_id_upd = Combobox(self, values=data_operator.get_id_data_base("owners"), width=10)
            owner_id_upd.place(x=620, y=70, anchor="w")
            label_id_delete = Label(self, text="Id to update", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
            label_id_delete.place(x=620, y=70, anchor="e")

            name_upd = Entry(self, bg="#FFF", font=(light_font, 10), fg="#F1C232", insertbackground="#DF744A")
            name_upd.place(x=620, y=100, anchor="w")
            label_name = Label(self, text="Name", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
            label_name.place(x=620, y=100, anchor="e")

            surname_upd = Entry(self, bg="#FFF", font=(light_font, 10), fg="#F1C232", insertbackground="#DF744A")
            surname_upd.place(x=620, y=130, anchor="w")
            label_surname = Label(self, text="Surname", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
            label_surname.place(x=620, y=130, anchor="e")

            contact_upd = Entry(self, bg="#FFF", font=(light_font, 10), fg="#F1C232", insertbackground="#DF744A")
            contact_upd.place(x=620, y=160, anchor="w")
            label_contact = Label(self, text="Contact", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
            label_contact.place(x=620, y=160, anchor="e")

            button_update = Button(self, text="Update",
                                       command=lambda: call_update_owner_and_reset_values(owner_id_upd, name_upd,
                                                                                          surname_upd,
                                                                                          contact_upd,
                                                                                          list_of_owners))
            button_update.place(x=620, y=190)

        # Images for the buttons
        button_image_update = Image.open("images\_update.png")
        self.button_photo_update=ImageTk.PhotoImage(button_image_update)
        button_image_delete = Image.open("images\_delete.png")
        self.button_photo_delete = ImageTk.PhotoImage(button_image_delete)
        button_image_add = Image.open("images\_add.png")
        self.button_photo_add = ImageTk.PhotoImage(button_image_add)
        button_image_back = Image.open("images\_back.png")
        self.button_photo_back = ImageTk.PhotoImage(button_image_back)
        button_image_exit = Image.open("images\_exit.png")
        self.button_photo_exit = ImageTk.PhotoImage(button_image_exit)

        # Navigation
        try:
            button_update
            button_delete
            button_update.configure(bd=0, image=self.button_photo_update)
            button_delete.configure(bd=0, image=self.button_photo_delete)
        except NameError:
            pass
        button_add.configure(bd=0, image=self.button_photo_add)
        button_back = Button(self, image=self.button_photo_back, bd=0, command=lambda: controller.show_frame(DataBase))
        button_back.place(relx=1, rely=0.93, anchor="se")
        button_exit = Button(self, image=self.button_photo_exit,bd=0, command=lambda: exit())
        button_exit.place(relx=1, rely=1, anchor="se")

class Doctors(tk.Frame):
    def __init__(self, parent, controller):

        # Headers
        tk.Frame.__init__(self, parent)
        self.configure(bg="#EFFFFB")

        label = Label(self, text="Doctors", font=(bold_font, 20),bg="#EFFFFB", fg="#DF744A")
        label.pack()
        label1 = Label(self, text="Adding",font=(bold_font, 16),bg="#EFFFFB", fg="#DF744A")
        label1.place(x=110, y=30)
        label2 = Label(self, text="Updating", font=(bold_font, 16),bg="#EFFFFB", fg="#DF744A")
        label2.place(x=615, y=30)
        label3 = Label(self, text="Deleting", font=(bold_font, 16),bg="#EFFFFB", fg="#DF744A")
        label3.place(x=370, y=70)

        # Adding doctor
        name = Entry(self, bg="#FFF", font=(light_font, 10), fg="#F1C232", insertbackground="#DF744A")
        name.place(x=80, y=70, anchor="w")
        label_name = Label(self, text="Name", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
        label_name.place(x=80, y=70, anchor="e")

        surname = Entry(self, bg="#FFF", font=(light_font, 10), fg="#F1C232", insertbackground="#DF744A")
        surname.place(x=80, y=100, anchor="w")
        label_surname = Label(self, text="Surname", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
        label_surname.place(x=80, y=100, anchor="e")

        contact = Entry(self, bg="#FFF", font=(light_font, 10), fg="#F1C232", insertbackground="#DF744A")
        contact.place(x=80, y=130, anchor="w")
        label_contact = Label(self, text="Contact", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
        label_contact.place(x=80, y=130, anchor="e")

        salary = Entry(self, bg="#FFF", font=(light_font, 10), fg="#F1C232", insertbackground="#DF744A")
        salary.place(x=80, y=160, anchor="w")
        label_salary = Label(self, text="Salary", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
        label_salary.place(x=80, y=160, anchor="e")

        position = Combobox(self, values=["Doctor", "Nurse"], width=17)
        position.place(x=80, y=190, anchor="w")
        label_position = Label(self, text="Position", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
        label_position.place(x=80, y=190, anchor="e")

        scrollbar = Scrollbar(self, orient=VERTICAL)
        list_of_doctors = Listbox(self, yscrollcommand=scrollbar.set, width=50)
        scrollbar.config(command=list_of_doctors.yview)
        show_doctor_data_base(list_of_doctors)
        list_of_doctors.place(relx=0.5, rely=1, anchor="s")

        button_add = Button(self, text="Add",
                            command=lambda: call_create_doctor_and_reset_value(name, surname, contact, salary,
                                                                               position, list_of_doctors))
        button_add.place(x=80, y=220)

        # Deleting doctor
        if len(data_operator.get_id_data_base("doctors")) < 1:
            label_empty = Label(self, text="List is empty", font=(bold_font, 12), bg="#EFFFFB", fg="#DF744A")
            label_empty.place(x=350, y=110)
        else:
            doc_id = Combobox(self, values=data_operator.get_id_data_base("doctors"), width=10)
            doc_id.place(x=370, y=110, anchor="w")
            label_id_delete = Label(self, text="Id to delete", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
            label_id_delete.place(x=370, y=110, anchor="e")
            button_delete = Button(self, text="Delete",
                                 command=lambda: delete_doc_and_reset_id_value(doc_id, list_of_doctors))
            button_delete.place(x=370, y=140, anchor="w")

        # Updating doctor
        if len(data_operator.get_id_data_base("doctors")) < 1:
            label_empty = Label(self, text="List is empty", font=(bold_font, 12), bg="#EFFFFB", fg="#DF744A")
            label_empty.place(x=620, y=70)
        else:
            doc_id_upd = Combobox(self, values=data_operator.get_id_data_base("doctors"), width=10)
            doc_id_upd.place(x=620, y=70, anchor="w")
            label_id_delete = Label(self, text="Id to update", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
            label_id_delete.place(x=620, y=70, anchor="e")

            name_upd = Entry(self, bg="#FFF", font=(light_font, 10), fg="#F1C232", insertbackground="#DF744A")
            name_upd.place(x=620, y=100, anchor="w")
            label_name = Label(self, text="Name", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
            label_name.place(x=620, y=100, anchor="e")

            surname_upd = Entry(self, bg="#FFF", font=(light_font, 10), fg="#F1C232", insertbackground="#DF744A")
            surname_upd.place(x=620, y=130, anchor="w")
            label_surname = Label(self, text="Surname", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
            label_surname.place(x=620, y=130, anchor="e")

            contact_upd = Entry(self, bg="#FFF", font=(light_font, 10), fg="#F1C232", insertbackground="#DF744A")
            contact_upd.place(x=620, y=160, anchor="w")
            label_contact = Label(self, text="Contact", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
            label_contact.place(x=620, y=160, anchor="e")

            salary_upd = Entry(self, bg="#FFF", font=(light_font, 10), fg="#F1C232", insertbackground="#DF744A")
            salary_upd.place(x=620, y=190, anchor="w")
            label_salary = Label(self, text="Salary", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
            label_salary.place(x=620, y=190, anchor="e")

            position_upd = Combobox(self, values=["Doctor", "Nurse"], width=17)
            position_upd.place(x=620, y=220, anchor="w")
            label_position = Label(self, text="Position", font=(bold_font, 10), bg="#EFFFFB", fg="#DF744A")
            label_position.place(x=620, y=220, anchor="e")

            button_update = Button(self, text="Update",
                                       command=lambda: call_update_doctor_and_reset_values(doc_id_upd, name_upd,
                                                                                           surname_upd,
                                                                                           contact_upd,
                                                                                           salary_upd,
                                                                                           position_upd,
                                                                                           list_of_doctors))
            button_update.place(x=620, y=250)

        # Images for the buttons
        button_image_update = Image.open("images\_update.png")
        self.button_photo_update=ImageTk.PhotoImage(button_image_update)
        button_image_delete = Image.open("images\_delete.png")
        self.button_photo_delete = ImageTk.PhotoImage(button_image_delete)
        button_image_add = Image.open("images\_add.png")
        self.button_photo_add = ImageTk.PhotoImage(button_image_add)
        button_image_back = Image.open("images\_back.png")
        self.button_photo_back = ImageTk.PhotoImage(button_image_back)
        button_image_exit = Image.open("images\_exit.png")
        self.button_photo_exit = ImageTk.PhotoImage(button_image_exit)

        # Navigation
        try:
            button_update
            button_delete
            button_update.configure(bd=0, image=self.button_photo_update)
            button_delete.configure(bd=0, image=self.button_photo_delete)
        except NameError:
            pass
        button_add.configure(bd=0, image=self.button_photo_add)
        button_back = Button(self, image=self.button_photo_back, bd=0, command=lambda: controller.show_frame(DataBase))
        button_back.place(relx=1, rely=0.93, anchor="se")
        button_exit = Button(self, image=self.button_photo_exit,bd=0, command=lambda: exit())
        button_exit.place(relx=1, rely=1, anchor="se")

# ------------------------------------------------- FUNCTION -------------------------------------------


# Owner


# function that resets values for owner fields
def reset_values_owner(name, surname, contact):
    name.delete(0, END)
    surname.delete(0, END)
    contact.delete(0, END)
    name.insert(0, "")
    surname.insert(0, "")
    contact.insert(0, "")


def call_create_owner_and_reset_value(name, surname, contact, list_of_owners):
    create_owner(name.get(), surname.get(), contact.get())
    reset_values_owner(name, surname, contact)
    list_of_owners.delete(0, "end")
    show_owner_data_base(list_of_owners)


# function that creates Owner object and adds it to the database
def create_owner(name, surname, contact):
    owner = Owner()
    owner.set_name(name)
    owner.set_surname(surname)
    owner.set_contact(contact)
    data_operator.insert_data(owner)


# function that shows Owner table
def show_owner_data_base(l):
    rows = data_operator.get_data_base("owners")
    for row in rows:
        insert_data = str(row[0]) + "  " + row[1] + "  " + row[2] + "  " + row[3]
        l.insert(l.size() + 1, insert_data)


# function that deletes Owner object with given ID from the database
def delete_owner_and_reset_id_value(owner_id, list_of_owners):
    data_operator.drop_data("Owners", int(owner_id.get()))
    list_of_owners.delete(0, "end")
    show_owner_data_base(list_of_owners)


def call_update_owner_and_reset_values(id, name_upd, surname_upd, contact_upd, list_of_owners):
    updates = {}
    if name_upd.get() != "": updates["name"] = name_upd.get()
    if surname_upd.get() != "": updates["surname"] = surname_upd.get()
    if contact_upd.get() != "": updates["contact"] = contact_upd.get()

    data_operator.update("owners", int(id.get()), updates)
    reset_values_owner(name_upd, surname_upd, contact_upd)
    list_of_owners.delete(0, "end")
    show_owner_data_base(list_of_owners)


# For Doctor, Dog and Cat classes similar methods were created below

# Doctor


def reset_values_doctor(name, surname, contact, salary, position):
    name.delete(0, END)
    surname.delete(0, END)
    contact.delete(0, END)
    salary.delete(0, END)
    position.delete(0, END)
    name.insert(0, "")
    surname.insert(0, "")
    contact.insert(0, "")
    salary.insert(0, "")
    position.insert(0, "")


def check_salary(salary):
    sal = salary.get()
    try:
        int(sal)
        return 1
    except ValueError:
        messagebox.showerror("Error", "Salary is an integer value")


def call_create_doctor_and_reset_value(name, surname, contact, salary, position, list):
    if check_salary(salary) == 1:
        create_doctor(name.get(), surname.get(), contact.get(), salary.get(), position.get())
        reset_values_doctor(name, surname, contact, salary, position)
        list.delete(0, "end")
        show_doctor_data_base(list)
    else:
        reset_values_doctor(name, surname, contact, salary, position)


def create_doctor(name, surname, contact, salary, position):
    doctor = Doctor()
    doctor.set_name(name)
    doctor.set_surname(surname)
    doctor.set_contact(contact)
    doctor.set_salary(salary)
    doctor.set_position(position)
    data_operator.insert_data(doctor)


def show_doctor_data_base(l):
    rows = data_operator.get_data_base("doctors")
    for row in rows:
        insert_data = str(row[0]) + "  " + row[1] + "  " + str(row[2]) + "  " + str(row[3]) + "  " + row[4] + "  " + \
                      row[5]
        l.insert(l.size() + 1, insert_data)


def delete_doc_and_reset_id_value(doc_id, list_of_doctors):
    data_operator.drop_data("Doctors", int(doc_id.get()))
    list_of_doctors.delete(0, "end")
    show_doctor_data_base(list_of_doctors)


def call_update_doctor_and_reset_values(id, name_upd, surname_upd, contact_upd, salary_upd, position_upd,
                                        list_of_doctors):
    updates = {}
    if name_upd.get() != "": updates["name"] = name_upd.get()
    if surname_upd.get() != "": updates["surname"] = surname_upd.get()
    if contact_upd.get() != "": updates["contact"] = contact_upd.get()
    if salary_upd.get() != "": updates["salary"] = salary_upd.get()
    if position_upd.get() != "": updates["position"] = position_upd.get()

    data_operator.update("doctors", int(id.get()), updates)
    reset_values_doctor(name_upd, surname_upd, contact_upd, salary_upd, position_upd)
    list_of_doctors.delete(0, "end")
    show_doctor_data_base(list_of_doctors)


# Dog

def call_create_dog_and_reset_value(name, age, breed, tail, castrated, sound, sex, owner, doctor, list_of_dogs):
    create_dog(name.get(), age.get(), breed.get(), tail.get(), castrated.get(), sound.get(), sex.get(),
               tuple(owner.get().split(' '))[0], tuple(doctor.get().split(' '))[0])
    reset_values_dog(name, age, breed, tail, castrated, sound, sex, owner, doctor)
    list_of_dogs.delete(0, "end")
    show_dog_data_base(list_of_dogs)


def delete_dog_and_reset_id_value(dog_id, list_of_dogs):
    data_operator.drop_data("Dogs", int(dog_id.get()))
    list_of_dogs.delete(0, "end")
    show_dog_data_base(list_of_dogs)


def call_update_dog_and_reset_values(id, name_upd, age_upd, breed_upd, tail_upd, castrated_upd, sound_upd, sex_upd,
                                     owner_upd, doctor_upd, list_of_dogs):
    updates = {}
    if name_upd.get() != "": updates["name"] = name_upd.get()
    if age_upd.get() != "" and type(age_upd.get) == int: updates["age"] = age_upd.get()
    if breed_upd.get() != "": updates["breed"] = breed_upd.get()
    if tail_upd.get() != "": updates["is_tail_cut"] = tail_upd.get()
    if castrated_upd.get() != "": updates["is_castrated"] = castrated_upd.get()
    if sound_upd.get() != "": updates["sound"] = sound_upd.get()
    if sex_upd.get() != "": updates["sex"] = sex_upd.get()
    if owner_upd.get() != "": updates["owner_id"] = tuple(owner_upd.get().split(' '))[0]
    if doctor_upd.get() != "": updates["doctor_id"] = tuple(doctor_upd.get().split(' '))[0]

    data_operator.update("dogs", int(id.get()), updates)
    reset_values_dog(name_upd, age_upd, breed_upd, tail_upd, castrated_upd, sound_upd, sex_upd, owner_upd, doctor_upd)
    list_of_dogs.delete(0, "end")
    show_dog_data_base(list_of_dogs)


def reset_values_dog(name, age, breed, tail, castrated, sound, sex, owner, doctor):
    name.delete(0, END)
    age.delete(0, END)
    breed.delete(0, END)
    tail.set("")
    castrated.set("")
    sound.delete(0, END)
    sex.set("")
    owner.set("")
    doctor.set("")
    name.insert(0, "")
    age.insert(0, "")
    breed.insert(0, "")
    sound.insert(0, "")


def create_dog(name, age, breed, tail, castrated, sound, sex, owner, doctor):
    dog = Dog()
    dog.set_name(name)
    dog.set_age(int(age))
    dog.set_breed(breed)
    dog.set_sound(sound)
    dog.set_sex(sex)
    dog.set_is_tail_cut(tail)
    dog.set_castrated(castrated)
    dog.set_owner_id(int(owner))
    dog.set_doctor_id(int(doctor))
    data_operator.insert_data(dog)


def show_dog_data_base(l):
    rows = data_operator.get_data_base("dogs")

    for row in rows:
        insert_data = str(row[0]) + "  " + row[1] + "  " + str(row[2]) + "  " + row[3] + "  " + row[4] + "  " + \
                      row[5] + "  " + row[6] + "  " + row[7] + "  " + str(row[8]) + "  " + str(row[9])
        l.insert(l.size() + 1, insert_data)


# Cat
def delete_cat_and_reset_id_value(cat_id, list_of_cats):
    data_operator.drop_data("Cats", int(cat_id.get()))
    list_of_cats.delete(0, "end")
    show_cat_data_base(list_of_cats)


def create_cat(name, age, breed, castrated, sex, owner, doctor):
    cat = Cat()
    cat.set_owner_id(int(owner))
    cat.set_doctor_id(int(doctor))
    cat.set_name(name)
    cat.set_age(age)
    cat.set_breed(breed)
    cat.set_castrated(castrated)
    cat.set_sex(sex)
    data_operator.insert_data(cat)

padding_size = 10

def show_cat_data_base(l):
    rows = data_operator.get_data_base("cats")

    for row in rows:
        insert_data=""
        for a in row:
            a = str(a) + " "*(padding_size-len(str(a)))
            insert_data += a
        l.insert(l.size() + 1, insert_data)


def reset_values_cat(name, age, breed, castrated, sex, owner, doctor):
    name.delete(0, END)
    age.delete(0, END)
    breed.delete(0, END)
    castrated.set("")
    sex.set("")
    owner.set("")
    doctor.set("")
    name.insert(0, "")
    age.insert(0, "")
    breed.insert(0, "")


def call_create_cat_and_reset_value(name, age, breed, castrated, sex, owner, doctor, list_of_cats):
    create_cat(name.get(), age.get(), breed.get(), castrated.get(), sex.get(),
               tuple(owner.get().split(' '))[0], tuple(doctor.get().split(' '))[0])
    reset_values_cat(name, age, breed, castrated, sex, owner, doctor)
    list_of_cats.delete(0, "end")
    show_cat_data_base(list_of_cats)


def call_update_cat_and_reset_values(id, name_upd, age_upd, breed_upd, castrated_upd, sex_upd,
                                     owner_upd, doctor_upd, list_of_cats):
    updates = {}
    if name_upd.get() != "": updates["name"] = name_upd.get()
    if age_upd.get() != "" and type(age_upd.get) == int: updates["age"] = age_upd.get()
    if breed_upd.get() != "": updates["breed"] = breed_upd.get()
    if castrated_upd.get() != "": updates["is_castrated"] = castrated_upd.get()
    if sex_upd.get() != "": updates["sex"] = sex_upd.get()
    if owner_upd.get() != "": updates["owner_id"] = tuple(owner_upd.get().split(' '))[0]
    if doctor_upd.get() != "": updates["doctor_id"] = tuple(doctor_upd.get().split(' '))[0]

    data_operator.update("cats", int(id.get()), updates)
    reset_values_cat(name_upd, age_upd, breed_upd, castrated_upd, sex_upd, owner_upd, doctor_upd)
    list_of_cats.delete(0, "end")
    show_cat_data_base(list_of_cats)


app = App()
app.mainloop()
