
import tkinter
from tkinter import *
from tkinter.ttk import Combobox
import random
import string
from tkinter import messagebox
import pyperclip 

code = Tk()
code.title("Password Generator")
code.geometry("500x500")
code.config(bg="#ffffff")
code.resizable(False,False)

def password_generate():
   try:
       length_password = int(solidboss.get())
       small_letters = string.ascii_lowercase
       capital_letters = string.ascii_uppercase                                                      
       digits = string.digits
       special_character = string.punctuation
       all_list = []
       all_list.extend(list(small_letters))
       all_list.extend(list(capital_letters))
       all_list.extend(list(digits))
       all_list.extend(list(special_character))                
       random.shuffle(all_list)
       password.set("".join(all_list[0:length_password]))
       
   except:
       messagebox.askretrycancel("Something Went Wrong!", "Please Try Again")


def copy():
     random_password=password_final.get()
     pyperclip.copy(random_password)


       
all_num = {"0" : "0" , "1" : "1" , "2" : "2" , "3" : "3" , "4" : "4" ,"5" : "5",
                 "6" : "6" , "7" : "7" , "8" : "8" , "9" : "9" ,"10" : "10",
                "11" : "11" , "12" : "12" , "13" : "13" , "14" : "14" ,"15" : "15",
                "16" : "16" , "17" : "17" , "18" : "18" , "19" : "19" ,"20" : "20",
                "21" : "21" , "22" : "22" , "23" : "23" , "24" : "24" ,"25" : "25",
                "26" : "26" , "27" : "27" , "28" : "28" , "29" : "29" ,"30" : "30",}

Title = Label(code, text="Password Generator", bg="#ffffff", fg="#000000", font=("futura", 19, "bold"))
Title.pack(anchor="center", pady="20px")

length = Label(code,text="Select Password Length:", fg="#000000", bg="#ffffff", font=("ubuntu", 15))
length.place(x="20px", y="70px")



def on_enter(e):
    Generate_button['bg'] = "#808080" 
    Generate_button['fg'] = "#ffffff"

def on_leave(e):
    Generate_button['bg'] = "#add8e6"
    Generate_button['fg'] = "#000000"


solidboss = IntVar()
Selector = Combobox(code, textvariable=solidboss, state="readonly")
Selector['values'] = [l for l in all_num.keys()]
Selector.current(7)
Selector.place(x="270", y="72px")
Generate_button = Button(code, text ="Generate Password", bg="#add8e6", fg="#000000", font=("ubuntu", 15), cursor="hand2",
                  command=password_generate)
Generate_button.bind("<Enter>", on_enter)
Generate_button.bind("<Leave>", on_leave)
Generate_button.pack(anchor="center", pady="50px")
                    
result_label = Label(code, text="Generated Password:", bg="#ffffff", fg="#000000", font=("ubuntu",15))
result_label.place(x="20px", y="177px")

password = StringVar()
password_final = Entry(code, textvariable = password, state ="readonly", fg="#000000",
                 font =("ubuntu",15))
password_final.place(x="190px", y="180px")

Copy_Button = Button(code,text="Copy", bg="#90ee90", fg="#000000", font=("ubuntu",15),
              command=copy)
Copy_Button.pack(anchor="center", pady="34px")
code.mainloop()

 
