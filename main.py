from tkinter import *
import math,random,os
from tkinter import messagebox
import datetime

class Bill_App:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("IPEC CAFETERIA")
        self.root.resizable(0,0)
        self.root["bg"]="#9a204a"
        bg_color = "#9a204a"
        title = Label(self.root, text = "🍔 T2 FAST FOOD CORNER 🍟" , bd = 12 , relief= GROOVE ,bg =  bg_color, fg = "orange",font =("times new roman" , 30 , "bold"), pady = 2 ).pack(fill=X)

        #================variables==================
        #==============Snacks===================
        self.bread = IntVar()
        self.sandwich = IntVar()
        self.burger = IntVar()
        self.chilly = IntVar()
        self.spring = IntVar()
        self.momos = IntVar()

        #=======================Mini Meals===============
        self.bhature = IntVar()
        self.puri = IntVar()
        self.rajma = IntVar()
        self.kadhi = IntVar()
        self.chole = IntVar()
        self.thali = IntVar()

        #============Beverages======================
        self.tea = IntVar()
        self.drink = IntVar()
        self.coffee = IntVar()
        self.cold= IntVar()
        self.ice = IntVar()
        self.mineral = IntVar()

        #==============Total Product Price & Tax variable=======
        self.snacks_price = StringVar()
        self.meals_price = StringVar()
        self.beverages_price = StringVar()

        self.service_tax = StringVar()
        self.packing_tax = StringVar()
        self.welfare_tax = StringVar()

        #=========Customer==============
        self.c_name = StringVar()
        self.c_phone= StringVar()
        self.bill_no= StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))

        self.search_bill = StringVar()

        #===================Customer Detail Frame
        F1 = LabelFrame(self.root ,bd = 10 , relief = RIDGE, text = "Customer Details 🙂", font= ("times new roman", 15 , "bold"),fg = "gold", bg= bg_color)
        F1.place(x = 0 , y = 79 , relwidth=1,height=99)

        cname_lbl = Label(F1 , text="Customer Name",bg = bg_color , fg = "lightgreen", font= ("times new roman",18,"bold")).grid(row = 0 , column = 0 , padx= 20 , pady = 5)
        cname_txt = Entry(F1 , width = 15 ,textvariable= self.c_name, font= "arial 15", bd = 7 , relief = SUNKEN).grid(row = 0 , column = 1 , pady = 5 , padx = 10)

        cphn_lbl = Label(F1, text="Phone No. 📞", bg=bg_color, fg="lightgreen", font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15,textvariable= self.c_phone, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number", bg=bg_color, fg="lightgreen", font=("times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15,textvariable= self.search_bill, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        bill_btn = Button(F1 , text = "Search",command=self.find_bill,bg="orange",fg="black", width = 10 , bd = 6 , font = "arial 12 bold").grid(row = 0 , column = 6 ,padx = 10,pady = 10)


        #=================Snacks Frame ================
        F2 = LabelFrame(self.root , bd = 10 , relief = GROOVE, text = "Snacks 🍕", font= ("times new roman", 15 , "bold"),fg = "gold", bg= bg_color)
        F2.place(x = 2, y = 180 ,width=325 , height = 380)

        bread_lbl = Label(F2 , text="Bread Pakoda", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 0 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        bread_tst= Entry(F2 , width=10, textvariable= self.bread, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 0 , column = 1 , padx = 10 , pady = 10)

        sandwich_lbl = Label(F2 , text="Veg Sandwich", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 1 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        sandwich_tst= Entry(F2 , width=10, textvariable= self.sandwich, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 1 , column = 1 , padx = 10 , pady = 10)

        burger_w_lbl = Label(F2 , text="Burger", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 2 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        burger_w_tst= Entry(F2 , width=10 , textvariable= self.burger,font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 2 , column = 1 , padx = 10 , pady = 10)

        chilly_s_lbl = Label(F2 , text="Chilly Potato", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 3 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        chilly_s_tst= Entry(F2 , width=10, textvariable= self.chilly,font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 3 , column = 1 , padx = 10 , pady = 10)

        spring_g_lbl = Label(F2 , text="Spring Roll", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 4 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        spring_g_tst= Entry(F2 , width=10, textvariable= self.spring,font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 4 , column = 1 , padx = 10 , pady = 10)

        momos_lbl = Label(F2 , text="Momos", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 5 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        momos_tst= Entry(F2 , width=10, textvariable= self.momos, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 5 , column = 1 , padx = 10 , pady = 10)

        #=================Mini Meals Frame ================
        F3 = LabelFrame(self.root , bd = 10 , relief = GROOVE, text = "Mini Meals 🍜", font= ("times new roman", 15 , "bold"),fg = "gold", bg= bg_color)
        F3.place(x = 327 , y = 180 ,width=330 , height = 380)

        g1_lbl = Label(F3 , text="Chole Bhature", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 0 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        g1_tst= Entry(F3 , width=10,textvariable= self.bhature, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 0 , column = 1 , padx = 10 , pady = 10)

        g2_lbl = Label(F3 , text="Puri Aloo", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 1 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        g2_tst= Entry(F3 , width=10,textvariable= self.puri, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 1 , column = 1 , padx = 10 , pady = 10)

        g3_lbl = Label(F3 , text="Rajma Rice", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 2 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        g3_tst= Entry(F3 , width=10, textvariable= self.rajma,font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 2 , column = 1 , padx = 10 , pady = 10)

        g4_lbl = Label(F3 , text="Kadhi Chawal", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 3 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        g4_tst= Entry(F3 , width=10, textvariable= self.kadhi,font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 3 , column = 1 , padx = 10 , pady = 10)

        g5_lbl = Label(F3 , text="Chole Rice", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 4 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        g5_tst= Entry(F3 , width=10, textvariable= self.chole,font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 4 , column = 1 , padx = 10 , pady = 10)

        g6_lbl = Label(F3 , text="Veg Thali", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 5 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        g6_tst= Entry(F3 , width=10, textvariable= self.thali,font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 5 , column = 1 , padx = 10 , pady = 10)

        #=================Beverages Frame ================

        F4 = LabelFrame(self.root , bd = 10 , relief = GROOVE, text = "Beverages ☕", font= ("times new roman", 15 , "bold"),fg = "gold", bg= bg_color)
        F4.place(x = 657 , y = 180 ,width=325 , height = 380)

        c1_lbl = Label(F4 , text="Tea", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 0 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        c1_tst= Entry(F4 , width=10,textvariable= self.tea, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 0 , column = 1 , padx = 10 , pady = 10)

        c2_lbl = Label(F4 , text="Coffee", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 1 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        c2_tst= Entry(F4 , width=10,textvariable= self.coffee, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 1 , column = 1 , padx = 10 , pady = 10)

        c3_lbl = Label(F4 , text="Cold Drink", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 2 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        c3_tst= Entry(F4 , width=10, textvariable= self.drink, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 2 , column = 1 , padx = 10 , pady = 10)

        c4_lbl = Label(F4 , text="Cold Coffee", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 3 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        c4_tst= Entry(F4 , width=10, textvariable= self.cold,font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 3 , column = 1 , padx = 10 , pady = 10)

        c5_lbl = Label(F4 , text="Ice Tea", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 4 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        c5_tst= Entry(F4 , width=10,textvariable= self.ice, font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 4 , column = 1 , padx = 10 , pady = 10)

        c6_lbl = Label(F4 , text="Mineral Water", font = ("times new roman" , 16 , "bold") , bg = bg_color , fg = "lightgreen" ).grid(row = 5 , column = 0 , padx = 10 , pady = 10 , sticky = "w")
        c6_tst= Entry(F4 , width=10, textvariable= self.mineral,font = ("times new roman" , 16 , "bold"), bd = 5 , relief = SUNKEN).grid(row = 5 , column = 1 , padx = 10 , pady = 10)

        #========Bill Area========
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=990, y=180, width=360, height=380)
        bill_title=Label(F5,text="Customer Bill",font="arial 15 bold",bd=7,bg="orange",relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack()

        #========ButtonFrame========
        F6=LabelFrame(self.root , bd = 10 , relief = GROOVE, text = "Bill Menu 🛒", font= ("times new roman", 15 , "bold"),fg = "gold", bg= bg_color)
        F6.place(x = 0 , y = 560 ,relwidth=1 , height = 140)
        m1_lbl=Label(F6,text="Total Snacks Price",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable= self.snacks_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl = Label(F6, text="Total Meals Price", bg=bg_color, fg="lightgreen",font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
        m2_txt = Entry(F6, width=18,textvariable= self.meals_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        m3_lbl = Label(F6, text="Total Beverages Price", bg=bg_color, fg="lightgreen",font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        m3_txt = Entry(F6, width=18,textvariable= self.beverages_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        c1_lbl = Label(F6, text="Service Tax", bg=bg_color, fg="lightgreen",
                       font=("times new roman", 14, "bold")).grid(row=0, column=2, padx=20, pady=1, sticky="w")
        c1_txt = Entry(F6, width=18,textvariable= self.service_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        c2_lbl = Label(F6, text="Packing Charges", bg=bg_color, fg="lightgreen",
                       font=("times new roman", 14, "bold")).grid(row=1, column=2, padx=20, pady=1, sticky="w")
        c2_txt = Entry(F6, width=18,textvariable= self.packing_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        c3_lbl = Label(F6, text="Welfare Tax", bg=bg_color, fg="lightgreen",
                       font=("times new roman", 14, "bold")).grid(row=2, column=2, padx=20, pady=1, sticky="w")
        c3_txt = Entry(F6, width=18, textvariable= self.welfare_tax,font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

        btn_F=Frame(F6,bg="#9a204a")
        btn_F.place(x=750,width=580,height=105)

        total_btn=Button(btn_F,command = self.total,text="Total",bg="orange",fg="black",bd=3,pady=15,width=10,height=2,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        GBill_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bg="orange",fg="black",bd=3,pady=15,width=12,height=2,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="orange",fg="black",bd=3,pady=15,width=10,height=2,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_F,text="Exit",command=self.Exit_app,bg="orange",fg="black",bd=3,pady=15,width=10,height=2,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()
    def total(self):
        self.c_s_p= self.bread.get()*15
        self.c_fc_p= self.sandwich.get()*25
        self.c_fw_p = self.burger.get()*25
        self.c_hs_p = self.chilly.get()*40
        self.c_hg_p = self.spring.get()*40
        self.c_bl_p = self.momos.get()*35

        self.total_snacks_price= float(
            self.c_s_p+
            self.c_fc_p+
            self.c_fw_p+
            self.c_hs_p+
            self.c_hg_p+
            self.c_bl_p
        )

        self.snacks_price.set("Rs. "+str(self.total_snacks_price))
        self.c_tax=round((self.total_snacks_price*0.03),2)
        self.service_tax.set("Rs. "+str(self.c_tax))

        self.g_r_p=self.bhature.get() * 40
        self.g_f_p=self.puri.get() * 40
        self.g_d_p=self.rajma.get() * 45
        self.g_w_p=self.kadhi.get() * 40
        self.g_s_p=self.chole.get() * 45
        self.g_t_p=self.thali.get() * 60

        self.total_meals_price = float(
                    self.g_r_p+
                    self.g_f_p+
                    self.g_d_p+
                    self.g_w_p+
                    self.g_s_p+
                    self.g_t_p
        )
        self.meals_price.set("Rs. "+str(self.total_meals_price))
        self.g_tax=round((self.total_meals_price * 0.02), 2)
        self.packing_tax.set("Rs. " + str(self.g_tax))

        self.d_m_p=self.tea.get()  *10
        self.d_c_p=self.coffee.get() * 15
        self.d_f_p=self.drink.get() * 22
        self.d_t_p=self.cold.get() * 30
        self.d_l_p=self.ice.get() * 25
        self.d_s_p=self.mineral.get() * 21

        self.total_beverages_price = float(
             self.d_m_p+
             self.d_c_p+
             self.d_f_p+
             self.d_t_p+
             self.d_l_p+
             self.d_s_p
        )
        self.beverages_price.set("Rs. "+str(self.total_beverages_price))
        self.d_tax=round((self.total_beverages_price * 0.04), 2)
        self.welfare_tax.set("Rs. " +str(self.d_tax))

        self.Total_bill=float(
                            self.total_snacks_price+
                            self.total_meals_price+
                            self.total_beverages_price+
                            self.c_tax+
                            self.g_tax+
                            self.d_tax
        )
        self.final_cost = round((self.Total_bill), 2)

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END, "        Welcome To IPEC Cafeteria\n")
        self.txtarea.insert(END, "            Ghaziabad,201010\n")
        self.txtarea.insert(END, '\n Time: {:%H:%M:%S       Date: %d-%m-%Y}'.format(datetime.datetime.now()))
        self.txtarea.insert(END, f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone Number : {self.c_phone.get()}")
        self.txtarea.insert(END, f"\n ======================================")
        self.txtarea.insert(END, f"\n Products   |\t\tQTY    |  \tPrice")
        self.txtarea.insert(END, f"\n ======================================")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error Cafeteria","Please Enter Customer Details First!")
        elif len(self.c_phone.get())!=10:
            messagebox.showerror("Error Cafeteria", "Please Enter 10 Digit Phone Number!")
        elif self.snacks_price.get() == "Rs. 0.0" and self.beverages_price.get() == "Rs. 0.0" and self.meals_price.get() == "Rs. 0.0":
            messagebox.showerror("Error Cafeteria","No Product Selected!")
        else:
            self.welcome_bill()
            #========Snacks=====
            if self.bread.get()!=0:
                self.txtarea.insert(END,f"\n Bread Pakoda\t\t {self.bread.get()}\t    {self.c_s_p}")
            if self.sandwich.get()!=0:
                self.txtarea.insert(END,f"\n Veg Sandwich\t\t {self.sandwich.get()}\t    {self.c_fc_p}")
            if self.burger.get()!=0:
                self.txtarea.insert(END,f"\n Burger\t\t {self.burger.get()}\t    {self.c_fw_p}")
            if self.chilly.get()!=0:
                self.txtarea.insert(END,f"\n Chilly Potato\t\t {self.chilly.get()}\t    {self.c_hs_p}")
            if self.spring.get()!=0:
                self.txtarea.insert(END,f"\n Spring Roll\t\t {self.spring.get()}\t    {self.c_hg_p}")
            if self.momos.get()!=0:
                self.txtarea.insert(END,f"\n Momos\t\t {self.momos.get()}\t    {self.c_bl_p}")

            # ========Mini Meals=====
            if self.bhature.get() != 0:
                self.txtarea.insert(END, f"\n Chole Bhature\t\t {self.bhature.get()}\t    {self.g_r_p}")
            if self.puri.get() != 0:
                self.txtarea.insert(END, f"\n Puri Aloo\t\t {self.puri.get()}\t    {self.g_f_p}")
            if self.rajma.get() != 0:
                self.txtarea.insert(END, f"\n Rajma Rice\t\t {self.rajma.get()}\t    {self.g_d_p}")
            if self.kadhi.get() != 0:
                self.txtarea.insert(END, f"\n Khadi Chawal\t\t {self.kadhi.get()}\t    {self.g_w_p}")
            if self.chole.get() != 0:
                self.txtarea.insert(END, f"\n Chole Rice\t\t {self.chole.get()}\t    {self.g_s_p}")
            if self.thali.get() != 0:
                self.txtarea.insert(END, f"\n Veg Thali\t\t {self.thali.get()}\t    {self.g_t_p}")

            #========Beverages=====
            if self.tea.get() != 0:
                self.txtarea.insert(END, f"\n Tea\t\t {self.tea.get()}\t    {self.d_m_p}")
            if self.coffee.get() != 0:
                self.txtarea.insert(END, f"\n Coffee\t\t {self.coffee.get()}\t    {self.d_c_p}")
            if self.drink.get() != 0:
                self.txtarea.insert(END, f"\n Cold Drink\t\t {self.drink.get()}\t    {self.d_f_p}")
            if self.cold.get() != 0:
                self.txtarea.insert(END, f"\n Cold Coffee\t\t {self.cold.get()}\t    {self.d_t_p}")
            if self.ice.get() != 0:
                self.txtarea.insert(END, f"\n Ice Tea\t\t {self.ice.get()}\t    {self.d_l_p}")
            if self.mineral.get() != 0:
                self.txtarea.insert(END, f"\n Mineral Water\t\t {self.mineral.get()}\t    {self.d_s_p}")

            self.txtarea.insert(END, f"\n\n **************************************")
            if self.service_tax.get()!= "0.0":
                self.txtarea.insert(END, f"\n Service Tax\t\t\t  {self.service_tax.get()}")
            if self.packing_tax.get()!= "0.0":
                self.txtarea.insert(END, f"\n Packing Charges\t\t\t  {self.packing_tax.get()}")
            if self.welfare_tax.get()!= "0.0":
                self.txtarea.insert(END, f"\n Welfare Tax\t\t\t  {self.welfare_tax.get()}")

            self.txtarea.insert(END, f"\n **************************************")
            self.txtarea.insert(END, f"\n --------------------------------------")
            self.txtarea.insert(END, f"\n Total Bill\t\t\t  Rs. {self.final_cost}")
            self.txtarea.insert(END, f"\n --------------------------------------")
            self.txtarea.insert(END, f"\n    *ThankYou For Shopping With Us*")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("Bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved Bill",f"Bill No.:{self.bill_no.get()} saved Successfully")
        else:
            return

    def find_bill(self):
        present="no"
        for i in os.listdir("Bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"Bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")

    def clear_data(self):

        op = messagebox.askyesno("Clear Details", "Do you really want to Clear Data?")
        if op > 0:

            # ==============Snacks===================
            self.bread.set(0)
            self.sandwich.set(0)
            self.burger.set(0)
            self.chilly.set(0)
            self.spring.set(0)
            self.momos.set(0)

            # =======================Mini Meals===============
            self.bhature.set(0)
            self.puri.set(0)
            self.rajma.set(0)
            self.kadhi.set(0)
            self.chole.set(0)
            self.thali.set(0)

            # ============Beverages======================
            self.tea.set(0)
            self.drink.set(0)
            self.coffee.set(0)
            self.cold.set(0)
            self.ice.set(0)
            self.mineral.set(0)

            # ==============Total Product Price & Tax variable=======
            self.snacks_price.set("")
            self.meals_price.set("")
            self.beverages_price.set("")

            self.service_tax.set("")
            self.packing_tax.set("")
            self.welfare_tax.set("")

            # =========Customer==============
            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to Exit?")
        if op>0:
            self.root.destroy()


root = Tk()
obj = Bill_App(root)
root.mainloop()

