import webbrowser
from tkinter import *
from functools import partial
import time
import csv
import sys

def validateLogin(username, password):
    InputedName = username.get()
    InputedPassword = password.get()
    csv_file = csv.reader(open('TestInputsNames.csv', "r"), delimiter=",")
    for row in csv_file:
        if InputedName == row[0]:
            print ("Exists")
        else:
            print ("doesn't exist")
    csv_file = csv.reader(open('TestInputsPasswords.csv', "r"), delimiter=",")
    for row in csv_file:
        if InputedPassword == row[0]:
            print ("Exists")
        else:
            print ("doesn't exist")
    return


#window
tkWindow = Tk()  
#tkWindow.geometry('400x150')  
tkWindow.title('RonicCommunication - Ronic')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)  

tkWindow.mainloop()



chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
url1 = "https://www.facebook.com/"
url2 = "https://www.instagram.com/"
url3 = "https://discord.com/channels/@me"
url = [url2, url1, url3]

#webbrowser.get(chrome_path).open("https://www.google.com/")
print ("am here0")

for i in url:
    webbrowser.get(chrome_path).open_new(i)
    print ("am here1")
    time.sleep(1)