from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
#import getpass
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window | IPEC Cafeteria")
        self.root.geometry("1000x480+290+150")
        self.root.resizable(0,0)

        #====Background Image======
        self.bg=ImageTk.PhotoImage(file="C:/Users/visha/Desktop/Mini_Pro/Bills/images/blue.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #====Image========
        self.left=ImageTk.PhotoImage(file="C:/Users/visha/Desktop/Mini_Pro/Bills/images/reg.png")
        left=Label(self.root,image=self.left).place(x=0,y=0,width=365,relheight=1)


        #====Registeration Frame=====
        frame1=Frame(self.root,bg="#1c939c")
        frame1.place(x=385,y=10,width=590,height=465)

        title=Label(frame1,text="REGISTER HERE",font=("comic sans ms",20,"bold"),bg="#1c939c",fg="white").place(x=20,y=15)

        f_name=Label(frame1,text="First Name",font=("comic sans ms",15,"bold"),bg="#1c939c",fg="white").place(x=25,y=85)
        txt_fname=Entry(frame1,font=("comic sans ms",15)).place(x=25,y=120,width=195)

        l_name=Label(frame1,text="Last Name",font=("comic sans ms",15,"bold"),bg="#1c939c",fg="white").place(x=340,y=85)
        txt_lname=Entry(frame1,font=("comic sans ms",15)).place(x=340,y=120,width=195)

        contact=Label(frame1,text="Contact No.",font=("comic sans ms",15,"bold"),bg="#1c939c",fg="white").place(x=25,y=160)
        txt_contact=Entry(frame1,font=("comic sans ms",15)).place(x=25,y=195,width=195)

        email=Label(frame1,text="Email",font=("comic sans ms",15,"bold"),bg="#1c939c",fg="white").place(x=340,y=160)
        txt_email=Entry(frame1,font=("comic sans ms",15)).place(x=340,y=195,width=195)

        security=Label(frame1,text="Security Ques.",font=("comic sans ms",15,"bold"),bg="#1c939c",fg="white").place(x=25,y=235)
        
        cmb_security=ttk.Combobox(frame1,font=("comic sans ms",15),state='readonly')
        cmb_security['values']=("Select","Your Birth Place","Your Best Friend","Your First Pet Name")
        cmb_security.place(x=25,y=270,width=195)
        cmb_security.current(0)

        answer=Label(frame1,text="Answer",font=("comic sans ms",15,"bold"),bg="#1c939c",fg="white").place(x=340,y=235)
        txt_answer=Entry(frame1,font=("comic sans ms",15)).place(x=340,y=270,width=195)

        password=Label(frame1,text="Password",font=("comic sans ms",15,"bold"),bg="#1c939c",fg="white").place(x=25,y=310)
        txt_password=Entry(frame1,font=("comic sans ms",15),show="*").place(x=25,y=345,width=195)

        c_password=Label(frame1,text="Confirm Password",font=("comic sans ms",15,"bold"),bg="#1c939c",fg="white").place(x=340,y=310)
        txt_c_password=Entry(frame1,font=("comic sans ms",15),show="*").place(x=340,y=345,width=195)

        #=======Register Button=========
        self.btn_img=ImageTk.PhotoImage(file="C:/Users/visha/Desktop/Mini_Pro/Bills/images/LOGO.png")
        btn=Button(frame1,image=self.btn_img,bg="#1c939c",bd=0,cursor="hand2").place(x=26,y=385,width=193,height=73)

        #=======Sign In Button==========
        self.btn_img_1=ImageTk.PhotoImage(file="C:/Users/visha/Desktop/Mini_Pro/Bills/images/LOGO-2.png")
        btn=Button(frame1,image=self.btn_img_1,bg="#1c939c",bd=0,cursor="hand2").place(x=341,y=385,width=193,height=73)








root=Tk()
obj=Register(root)
root.mainloop()