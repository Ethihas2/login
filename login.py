from tkinter import *

root = Tk()
root.title("Login")
root.geometry("500x600")

label_name = Label(root,text="Name: ")
label_name.place(relx=0.35,rely=0.2,anchor=CENTER)
entry_name = Entry(root)
entry_name.place(relx=0.55,rely=0.2,anchor=CENTER)

label_pass = Label(root,text="Password: ")
label_pass.place(relx=0.35,rely=0.3,anchor=CENTER)
entry_pass = Entry(root)
entry_pass.place(relx=0.55,rely=0.3,anchor=CENTER)

label_cap = Label(root,text="Captcha: ")
label_cap.place(relx=0.35,rely=0.4,anchor=CENTER)
entry_cap = Entry(root)
entry_cap.place(relx=0.55,rely=0.4,anchor=CENTER)


label_storedName = Label(root)
label_storedName.place(relx=0.5,rely=0.7,anchor=CENTER)
label_storedPass = Label(root)
label_storedPass.place(relx=0.5,rely=0.8,anchor=CENTER)
label_storedCap = Label(root)
label_storedCap.place(relx=0.5,rely=0.9,anchor=CENTER)

class userDB():
    def __init__(self):
        self.__password = "PaSSWORD!@"
        self.__name = "Ethihas"
        self.__cap = "5tag"
    def showUser(self):
        label_storedName["text"]="Name: ",self.__name
        label_storedPass["text"]="Password: ",self.__password
        print(self.__password)
        label_storedCap["text"]="Captcha: ",self.__cap


obj = userDB()

def add_user():
    global obj
    obj.password = entry_pass.get()
    obj.name = entry_name.get()
    obj.cao = entry_cap.get()
    
btn1 = Button(root,text="Add User",command=add_user)
btn1.place(relx=0.3,rely=0.55,anchor=CENTER)

btn2 = Button(root,text="Show Profile",command=obj.showUser)
btn2.place(relx=0.6,rely=0.55,anchor=CENTER)
    
root.mainloop()