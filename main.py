from tkinter import*
class Bill_App:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#074463"
        title = Label(self.root, text = "Billing Software" , bd = 12 , relief= GROOVE ,bg =  bg_color, fg = "white",font =("times new roman" , 30 , "bold"), pady = 2 ).pack(fill=X)

        #===================Customer Detail Frame
        F1 = LabelFrame(self.root ,bd = 10 , relief = GROOVE, text = "Customer Details", font= ("times new roman", 15 , "bold"),fg = "gold", bg= bg_color)
        F1.place(x = 0 , y = 80 , relwidth=1)

        cname_lbl = Label(F1 , text="Customer Name",bg = bg_color , fg = "white", font= ("times new roman",18,"bold")).grid(row = 0 , column = 0 , padx= 20 , pady = 5)
        cname_txt = Entry(F1 , width = 15 , font= "arial 15", bd = 7 , relief = SUNKEN).grid(row = 0 , column = 1 , pady = 5 , padx = 10)

        cphn_lbl = Label(F1, text="Phone No.", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        bill_btn = Button(F1 , text = "Search", width = 10 , bd = 7 , font = "arial 12 bold").grid(row = 0 , column = 6 ,padx = 10,pady = 10)


        #=================Cosmetics Frame ================
        F2 = LabelFrame(self.root , bd = 10 , relief = GROOVE, text = "Cusmetics", font= ("times new roman", 15 , "bold"),fg = "gold", bg= bg_color)
        F2.place(x = 5 , y = 180 ,width=325 , height = 380)

        bath_lbl = Label(F2 , text="Bath Soap", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 0 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        bath_tst= Entry(F2 , width=10, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 0 , column = 1 , padx = 10 , pady = 10)

        Face_cream_lbl = Label(F2 , text="Face Cream", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 1 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        Face_cream_tst= Entry(F2 , width=10, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 1 , column = 1 , padx = 10 , pady = 10)

        face_w_lbl = Label(F2 , text="Face Wash", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 2 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        face_w_tst= Entry(F2 , width=10, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 2 , column = 1 , padx = 10 , pady = 10)

        hair_s_lbl = Label(F2 , text="Hair Spray", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 3 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        hair_s_tst= Entry(F2 , width=10, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 3 , column = 1 , padx = 10 , pady = 10)

        hair_g_lbl = Label(F2 , text="Hair Gel", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 4 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        hair_g_tst= Entry(F2 , width=10, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 4 , column = 1 , padx = 10 , pady = 10)

        body_lbl = Label(F2 , text="Body Loshan", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 5 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        body_tst= Entry(F2 , width=10, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 5 , column = 1 , padx = 10 , pady = 10)

        #=================Grocery Frame ================
        F3 = LabelFrame(self.root , bd = 10 , relief = GROOVE, text = "Cusmetics", font= ("times new roman", 15 , "bold"),fg = "gold", bg= bg_color)
        F3.place(x = 340 , y = 180 ,width=325 , height = 380)

        g1_lbl = Label(F3 , text="Rice", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 0 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        g1_tst= Entry(F3 , width=10, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 0 , column = 1 , padx = 10 , pady = 10)

        g2_lbl = Label(F3 , text="Food Oil", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 1 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        g2_tst= Entry(F3 , width=10, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 1 , column = 1 , padx = 10 , pady = 10)

        g3_lbl = Label(F3 , text="Dall", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 2 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        g3_tst= Entry(F3 , width=10, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 2 , column = 1 , padx = 10 , pady = 10)

        g4_lbl = Label(F3 , text="Wheat", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 3 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        g4_tst= Entry(F3 , width=10, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 3 , column = 1 , padx = 10 , pady = 10)

        g5_lbl = Label(F3 , text="Sugar", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 4 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        g5_tst= Entry(F3 , width=10, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 4 , column = 1 , padx = 10 , pady = 10)

        g6_lbl = Label(F3 , text="Tea", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 5 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        g6_tst= Entry(F3 , width=10, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 5 , column = 1 , padx = 10 , pady = 10)

        #=================Cold Drink Frame ================

        F4 = LabelFrame(self.root , bd = 10 , relief = GROOVE, text = "Cusmetics", font= ("times new roman", 15 , "bold"),fg = "gold", bg= bg_color)
        F4.place(x = 670 , y = 180 ,width=325 , height = 380)

        c1_lbl = Label(F4 , text="Maza", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 0 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        c1_tst= Entry(F4 , width=10, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 0 , column = 1 , padx = 10 , pady = 10)

        c2_lbl = Label(F4 , text="Coke", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 1 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        c2_tst= Entry(F4 , width=10, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 1 , column = 1 , padx = 10 , pady = 10)

        c3_lbl = Label(F4 , text="Frooti", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 2 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        c3_tst= Entry(F4 , width=10, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 2 , column = 1 , padx = 10 , pady = 10)

        c4_lbl = Label(F4 , text="Thumbs Up", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 3 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        c4_tst= Entry(F4 , width=10, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 3 , column = 1 , padx = 10 , pady = 10)

        c5_lbl = Label(F4 , text="Limca", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 4 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        c5_tst= Entry(F4 , width=10, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 4 , column = 1 , padx = 10 , pady = 10)

        c6_lbl = Label(F4 , text="Sprite", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 5 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        c6_tst= Entry(F4 , width=10, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 5 , column = 1 , padx = 10 , pady = 10)


root = Tk()
obj = Bill_App(root)
root.mainloop()
