from tkinter import *
import math,random
class Bill_App:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("IPEC CAFETERIA")
        bg_color = "#072763"
        title = Label(self.root, text = "FAST FOOD CORNER" , bd = 12 , relief= GROOVE ,bg =  bg_color, fg = "white",font =("times new roman" , 30 , "bold"), pady = 2 ).pack(fill=X)
        #================variables==================
        #==============Cosmetics===================
        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.spray = IntVar()
        self.gell = IntVar()
        self.loshan = IntVar()

        #=======================Grocery===============
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()

        #============Cold Drink ======================
        self.maza = IntVar()
        self.frooty = IntVar()
        self.pepsi = IntVar()
        self.thumbsup= IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()

        #==============Total Product Price & Tax variable=======
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()

        #=========Customer==============
        self.c_name = StringVar()
        self.c_phone= StringVar()
        self.bill_no= StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))

        self.search_bill = StringVar()

        #===================Customer Detail Frame
        F1 = LabelFrame(self.root ,bd = 10 , relief = GROOVE, text = "Customer Details", font= ("times new roman", 15 , "bold"),fg = "gold", bg= bg_color)
        F1.place(x = 0 , y = 80 , relwidth=1)

        cname_lbl = Label(F1 , text="Customer Name",bg = bg_color , fg = "white", font= ("times new roman",18,"bold")).grid(row = 0 , column = 0 , padx= 20 , pady = 5)
        cname_txt = Entry(F1 , width = 15 ,textvariable= self.c_name, font= "arial 15", bd = 7 , relief = SUNKEN).grid(row = 0 , column = 1 , pady = 5 , padx = 10)

        cphn_lbl = Label(F1, text="Phone No.", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15,textvariable= self.c_phone, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15,textvariable= self.search_bill, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        bill_btn = Button(F1 , text = "Search", width = 10 , bd = 7 , font = "arial 12 bold").grid(row = 0 , column = 6 ,padx = 10,pady = 10)


        #=================Cosmetics Frame ================
        F2 = LabelFrame(self.root , bd = 10 , relief = GROOVE, text = "Cosmetics", font= ("times new roman", 15 , "bold"),fg = "gold", bg= bg_color)
        F2.place(x = 5 , y = 180 ,width=325 , height = 380)

        bath_lbl = Label(F2 , text="Bath Soap", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 0 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        bath_tst= Entry(F2 , width=10, textvariable= self.soap, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 0 , column = 1 , padx = 10 , pady = 10)

        Face_cream_lbl = Label(F2 , text="Face Cream", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 1 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        Face_cream_tst= Entry(F2 , width=10, textvariable= self.face_cream, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 1 , column = 1 , padx = 10 , pady = 10)

        face_w_lbl = Label(F2 , text="Face Wash", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 2 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        face_w_tst= Entry(F2 , width=10 , textvariable= self.face_wash,font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 2 , column = 1 , padx = 10 , pady = 10)

        hair_s_lbl = Label(F2 , text="Hair Spray", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 3 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        hair_s_tst= Entry(F2 , width=10, textvariable= self.spray,font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 3 , column = 1 , padx = 10 , pady = 10)

        hair_g_lbl = Label(F2 , text="Hair Gel", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 4 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        hair_g_tst= Entry(F2 , width=10, textvariable= self.gell,font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 4 , column = 1 , padx = 10 , pady = 10)

        body_lbl = Label(F2 , text="Body Loshan", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 5 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        body_tst= Entry(F2 , width=10, textvariable= self.loshan, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 5 , column = 1 , padx = 10 , pady = 10)

        #=================Grocery Frame ================
        F3 = LabelFrame(self.root , bd = 10 , relief = GROOVE, text = "Grocery", font= ("times new roman", 15 , "bold"),fg = "gold", bg= bg_color)
        F3.place(x = 340 , y = 180 ,width=325 , height = 380)

        g1_lbl = Label(F3 , text="Rice", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 0 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        g1_tst= Entry(F3 , width=10,textvariable= self.rice, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 0 , column = 1 , padx = 10 , pady = 10)

        g2_lbl = Label(F3 , text="Food Oil", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 1 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        g2_tst= Entry(F3 , width=10,textvariable= self.food_oil, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 1 , column = 1 , padx = 10 , pady = 10)

        g3_lbl = Label(F3 , text="Dall", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 2 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        g3_tst= Entry(F3 , width=10, textvariable= self.daal,font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 2 , column = 1 , padx = 10 , pady = 10)

        g4_lbl = Label(F3 , text="Wheat", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 3 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        g4_tst= Entry(F3 , width=10, textvariable= self.wheat,font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 3 , column = 1 , padx = 10 , pady = 10)

        g5_lbl = Label(F3 , text="Sugar", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 4 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        g5_tst= Entry(F3 , width=10, textvariable= self.sugar,font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 4 , column = 1 , padx = 10 , pady = 10)

        g6_lbl = Label(F3 , text="Tea", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 5 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        g6_tst= Entry(F3 , width=10, textvariable= self.tea,font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 5 , column = 1 , padx = 10 , pady = 10)

        #=================Cold Drink Frame ================

        F4 = LabelFrame(self.root , bd = 10 , relief = GROOVE, text = "Cold Drinks", font= ("times new roman", 15 , "bold"),fg = "gold", bg= bg_color)
        F4.place(x = 670 , y = 180 ,width=325 , height = 380)

        c1_lbl = Label(F4 , text="Maza", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 0 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        c1_tst= Entry(F4 , width=10,textvariable= self.maza, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 0 , column = 1 , padx = 10 , pady = 10)

        c2_lbl = Label(F4 , text="Pepsi", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 1 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        c2_tst= Entry(F4 , width=10,textvariable= self.pepsi, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 1 , column = 1 , padx = 10 , pady = 10)

        c3_lbl = Label(F4 , text="Frooti", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 2 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        c3_tst= Entry(F4 , width=10, textvariable= self.frooty, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 2 , column = 1 , padx = 10 , pady = 10)

        c4_lbl = Label(F4 , text="Thumbs Up", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 3 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        c4_tst= Entry(F4 , width=10, textvariable= self.thumbsup,font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 3 , column = 1 , padx = 10 , pady = 10)

        c5_lbl = Label(F4 , text="Limca", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 4 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        c5_tst= Entry(F4 , width=10,textvariable= self.limca, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 4 , column = 1 , padx = 10 , pady = 10)

        c6_lbl = Label(F4 , text="Sprite", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 5 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        c6_tst= Entry(F4 , width=10, textvariable= self.sprite,font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 5 , column = 1 , padx = 10 , pady = 10)

        #========Bill Area========
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=330, height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack()

        #========ButtonFrame========
        F6=LabelFrame(self.root , bd = 10 , relief = GROOVE, text = "Bill Menu", font= ("times new roman", 15 , "bold"),fg = "gold", bg= bg_color)
        F6.place(x = 0 , y = 560 ,relwidth=1 , height = 140)
        m1_lbl=Label(F6,text="Total Cosmetic Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable= self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl = Label(F6, text="Total Grocery Price", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
        m2_txt = Entry(F6, width=18,textvariable= self.grocery_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        m3_lbl = Label(F6, text="Total Cold Drinks Price", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        m3_txt = Entry(F6, width=18,textvariable= self.cold_drink_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        c1_lbl = Label(F6, text="Cosmetic Tax", bg=bg_color, fg="white",
                       font=("times new roman", 14, "bold")).grid(row=0, column=2, padx=20, pady=1, sticky="w")
        c1_txt = Entry(F6, width=18,textvariable= self.cosmetic_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        c2_lbl = Label(F6, text="Grocery Tax", bg=bg_color, fg="white",
                       font=("times new roman", 14, "bold")).grid(row=1, column=2, padx=20, pady=1, sticky="w")
        c2_txt = Entry(F6, width=18,textvariable= self.grocery_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        c3_lbl = Label(F6, text="Cold Drinks Tax", bg=bg_color, fg="white",
                       font=("times new roman", 14, "bold")).grid(row=2, column=2, padx=20, pady=1, sticky="w")
        c3_txt = Entry(F6, width=18, textvariable= self.cold_drink_tax,font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

        btn_F=Frame(F6,bg="#072363")
        btn_F.place(x=750,width=580,height=105)

        total_btn=Button(btn_F,command = self.total,text="Total",bg="cadetblue",fg="black",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        GBill_btn=Button(btn_F,text="Generate Bill",command=self.welcome_bill,bg="cadetblue",fg="black",bd=2,pady=15,width=12,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn_F,text="Clear",bg="cadetblue",fg="black",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_F,text="Exit",bg="cadetblue",fg="black",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()
    def total(self):
        self.total_cosmetic_price= float(
                                        (self.soap.get()*40)+
                                        (self.face_cream.get()*120)+
                                        (self.face_wash.get()*60)+
                                        (self.spray.get()*180)+
                                        (self.gell.get()*140)+
                                        (self.loshan.get()*180)
                                        )
        self.cosmetic_price.set("Rs."+str(self.total_cosmetic_price)
        )
        self.cosmetic_tax.set("Rs."+str(round((self.total_cosmetic_price*0.05),2)))

        self.total_grocery_price = float(
            (self.rice.get() * 80) +
            (self.food_oil.get() * 180) +
            (self.daal.get() * 60) +
            (self.wheat.get() * 240) +
            (self.sugar.get() * 45) +
            (self.tea.get() * 150)
        )
        self.grocery_price.set("Rs."+str(self.total_grocery_price)
                                )
        self.grocery_tax.set("Rs." + str(round((self.total_grocery_price * 0.1), 2)))

        self.total_drinks_price = float(
            (self.maza.get() * 60) +
            (self.pepsi.get() * 60) +
            (self.frooty.get() * 50) +
            (self.thumbsup.get() * 45) +
            (self.limca.get() * 40) +
            (self.sprite.get() * 60)
        )
        self.cold_drink_price.set("Rs."+str(self.total_drinks_price)
                                )
        self.cold_drink_tax.set("Rs." + str(round((self.total_drinks_price * 0.05), 2)))

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END, "\tWelcome Webcode Retail\n")
        self.txtarea.insert(END, f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone Number : {self.c_phone.get()}")
        self.txtarea.insert(END, f"\n ===================================")
        self.txtarea.insert(END, f"\n Products\t\tQTY\tPrice")
        self.txtarea.insert(END, f"\n ===================================")
    def bill_area(self):
        pass

root = Tk()
obj = Bill_App(root)
root.mainloop()

