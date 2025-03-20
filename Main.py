from tkinter import *
from tkinter import ttk
import os
import tkinter as tk

def delete2():
    screen3.destroy()

def delete3():
    screen4.destroy()

def delete4():
    screen5.destroy()

def save():
    print("save")

def create_notes():
    global raw_filename
    raw_filename = StringVar()
    global raw_notes
    raw_notes = StringVar()

    screen9 = Toplevel(screen)
    screen9.title("Info")
    screen9.geometry("300x250")
    Label(screen9 , text= "Please enter a filename for the note be :").pack()
    Entry(screen9, textvariable= raw_filename).pack()
    Label(screen9 , text= "Please enter the notes for the file below :").pack()
    Entry(screen9, textvariable= raw_notes).pack()
    Button(text= "Save", command= save).pack()

    
def session():
    screen8 = Toplevel(screen)
    screen8.title("Dashboard")
    screen8.geometry("400x400")
    Label(screen8, text = "Welcome to Dashboard!").pack()
    Button(screen8, text = "Create note", command= create_notes).pack()
    Button(screen8, text = "View note").pack()
    Button(screen8, text = "Delete note").pack()



def login_sucess():
    session()
    






  
def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Password Error")
    screen4.geometry("150x100")
    Label(screen4, text="Password Error").pack()
    Button(screen4, text= "OK", command=delete3).pack()



def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("User Not Found")
    screen5.geometry("150x100")
    Label(screen5, text="User Not Found").pack()
    Button(screen5, text= "OK", command=delete4).pack()



def register_user():
    print("working")

    #files and storing user data
    username_info = username.get()
    password_info = password.get()

    file=open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

#Registration successs message
    Label(screen1, text="Registration Success", fg="green", font = ("calibri", 11)).pack()


#function which verifies if youve logged in or not 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0,END)
    password_entry1.delete(0, END)

# if statements to verify the username and password
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
           login_sucess()
        else:
           password_not_recognised()
    
    else:
        user_not_found()



def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")


    global username
    global password
    global username_entry
    global password_entry

    username = StringVar()
    password = StringVar()

#Registration Page (where you register if you haven't made an acocunt yet)
    Label(screen1, text = "Please enter details below *  \n (make sure not to put a different password as it \n will not be stored securely) ").pack() 
    Label(screen1, text = "Username * ").pack() 
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "Password * ").pack() 
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    password_entry.pack()
    Label(screen1, text = "").pack() 
    Button(screen1, text= "Register", width= 10, height= 1, command= register_user).pack()





#login function which runs the login box
def login():
    global screen2 
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text="Please enter details below to login").pack()
    Label(screen2, text= "").pack()
    
    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    
    global username_entry1
    global password_entry1

    Label(screen2, text= "Username").pack()
    username_entry1 = Entry(screen2,textvariable= username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password").pack()
    password_entry1 = Entry(screen2, textvariable = password_verify)
    password_entry1.pack()
    Label(screen2, text= "").pack()
    Button(screen2, text="Login", width= 10, height= 1, command = login_verify).pack()
    

#Main screen Page (the login page)
def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Rosmini Homework Planner 2025")




    Label(text="Rosmini Homework Planner", bg="blue", fg="red", width="300", height="2", font=("Calibri", 15), padx=10, pady=10).pack()
    Label(text = "").pack()
    Button(text = "Login", height="2", width="30", command=login).pack()
    Label(text = "").pack() 
    Label(text = "If you dont have an account register here!", width="300", height="2", font = ("Calibri", 9)).pack()
    Button(text = "Register", height = "2", width = "30", command=register).pack()

    screen.mainloop()

main_screen()















    