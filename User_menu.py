import sqlite3
from tkinter import ttk
from tkinter import *
from Addtional_features import mycombobox
import os
import datetime
from tkinter import Tk, messagebox
from reportlab.platypus import Table, TableStyle
from reportlab.pdfgen import canvas
from reportlab.lib import colors

# USER MENU
class User:
    def __init__(self, mainw, cur, base):
        self.mainw = mainw
        self.cur = cur
        self.base = base

    def user_mainmenu(self,a,b):
        self.mainframe = LabelFrame(self.mainw, width=800, height=140, bg="#12171c")
        self.mainframe.place(x=330, y=120)
        mi = PhotoImage(file="images/items.png")
        mi = mi.subsample(a, b)
        self.aitems = Button(self.mainframe, text="Items",bd=5,font="Montserrat 11 bold",bg="white",width=90,height=90, image=mi, compound=TOP,command=self.builditemtable)
        self.aitems.image = mi
        self.aitems.place(x=80, y=17)
        mi = PhotoImage(file="images/invoice2.png")
        mi = mi.subsample(a,b)
        self.aitems = Button(self.mainframe, text="Invoice",bd=5,bg="white",font="Montserrat 11 bold",width=90,height=90, image=mi, compound=TOP,command=self.make_invoice)
        self.aitems.image = mi
        self.aitems.place(x=260, y=17)
        mi = PhotoImage(file="images/change1.png")
        mi = mi.subsample(a, b)
        self.changeuser = Button(self.mainframe, text="Sign out",bd=5,bg="white",font="Montserrat 11 bold",width=90,height=90, image=mi, compound=TOP)
        self.changeuser.image = mi
        self.changeuser.place(x=440, y=17)
        mi = PhotoImage(file="images/Door_Out-512.png")
        mi = mi.subsample(a, b)
        self.logout = Button(self.mainframe, text="Quit",bd=5,bg="white",font="Montserrat 11 bold",width=90,height=90, image=mi, compound=TOP)
        self.logout.image = mi
        self.logout.place(x=620, y=17)
        self.tableframe1 =Frame(self.mainw, width=150, height=400,bg="#12171c")
        self.tableframe1.place(x=1230, y=270, anchor=NE)
        self.tableframe1info=self.tableframe1.place_info()
        self.tableframe =Frame(self.mainw, width=350, height=700,bg="#12171c")
        self.tableframe.place(x=1110, y=300, anchor=NE)
        self.tableframeinfo = self.tableframe.place_info()
        self.entryframe = Frame(self.mainw, width=800, height=350, bg="#12171c")
        self.entryframe.place(x=780, y=460+20)
        self.entryframeinfo = self.entryframe.place_info()
        self.entryframe1 = Frame(self.mainw, width=500, height=350, bg="#12171c")
        self.entryframe1.place(x=230, y=470+20)
        self.entryframe1info=self.entryframe1.place_info()

    def builditemtable(self):
         self.entryframe.place_forget()
         self.entryframe1.place_forget()
         self.tableframe.place(self.tableframeinfo)
         self.tableframe1.place_forget()
         scrollbarx = Scrollbar(self.tableframe, orient=HORIZONTAL)
         scrollbary = Scrollbar(self.tableframe, orient=VERTICAL)
         self.tree = ttk.Treeview(self.tableframe, columns=("Product ID", "Product Name", "Description", "Category",
                                                            'Price', 'Stocks'), selectmode="extended", height=18,
                                  yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
         self.tree.column('#0', stretch=NO, minwidth=0, width=0)
         self.tree.column('#1', stretch=NO, minwidth=0, width=100)
         self.tree.column('#2', stretch=NO, minwidth=0, width=150)
         self.tree.column('#3', stretch=NO, minwidth=0, width=150)
         self.tree.column('#4', stretch=NO, minwidth=0, width=100)
         self.tree.column('#5', stretch=NO, minwidth=0, width=100)
         self.tree.column('#6', stretch=NO, minwidth=0, width=100)
         self.tree.heading('Product ID', text="Product ID", anchor=W)
         self.tree.heading('Product Name', text="Product Name", anchor=W)
         self.tree.heading('Description', text="Description", anchor=W)
         self.tree.heading('Category', text="Category", anchor=W)
         self.tree.heading('Price', text="Price", anchor=W)
         self.tree.heading('Stocks', text="Stocks", anchor=W)
         self.tree.grid(row=1, column=0, sticky="W")
         scrollbary.config(command=self.tree.yview)
         scrollbarx.grid(row=2, column=0, sticky="we")
         scrollbarx.config(command=self.tree.xview)
         scrollbary.grid(row=1, column=1, sticky="ns", pady=30)
         self.getproducts()


    def getproducts(self):
         self.cur.execute("select * from products")
         productlist = self.cur.fetchall()
         for i in productlist:
              self.tree.insert('', 'end', values=(i))
    def make_invoice(self):

        self.tableframe.place_forget()
        self.entryframe.place(self.entryframeinfo)
        self.entryframe1.place(self.entryframe1info)
        self.tableframe1.place(self.tableframe1info)
        scrollbarx = Scrollbar(self.tableframe1, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.tableframe1, orient=VERTICAL)
        self.tree = ttk.Treeview(self.tableframe1, columns=("Transaction ID", "Product ID", "Product Name",
        'Quantity', 'Price','Date','Time'), selectmode="browse", height=6,yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=140)
        self.tree.column('#2', stretch=NO, minwidth=0, width=150)
        self.tree.column('#3', stretch=NO, minwidth=0, width=170)
        self.tree.column('#4', stretch=NO, minwidth=0, width=130)
        self.tree.column('#5', stretch=NO, minwidth=0, width=130)
        self.tree.column('#6', stretch=NO, minwidth=0, width=130)
        self.tree.column('#7', stretch=NO, minwidth=0, width=130)
        self.tree.heading('Transaction ID', text="Transaction ID", anchor=W)
        self.tree.heading('Product ID', text="Product ID", anchor=W)
        self.tree.heading('Product Name', text="Product Name", anchor=W)
        self.tree.heading('Quantity', text="Quantity", anchor=W)
        self.tree.heading('Price', text="Price", anchor=W)
        self.tree.heading('Date', text="Date", anchor=W)
        self.tree.heading('Time', text="Time", anchor=W)
        self.tree.grid(row=1, column=0, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=2, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=1, column=1, sticky="ns", pady=30)
        self.tree.bind("<<TreeviewSelect>>", self.clicktranstable)
        self.user_input()

    def user_input(self):
       self.cur.execute('select max(trans_id) from sales')
       li = self.cur.fetchall()
       if(li[0][0]!=None):
        self.transid = li[0][0] + 1
       else:
           self.transid = 100
       self.qty = StringVar(value=1)
       self.additem=StringVar()
       self.total=IntVar(value=0)
       Button(self.entryframe, text="Proceed", command=self.transtableadd, bd=8, width=7, height=6, bg="#32373d", fg="white",font="Montserrat 11 bold").place(x=0, y=30)
       Button(self.entryframe, text="Add to cart", command=self.addtotrans, bd=8, width=12, height=1, bg="#32373d", fg="white", font="Montserrat 11 bold").place(x=130, y=110)
       Button(self.entryframe, text="Remove", command=self.removecart, bd=8, width=12, height=1, bg="#32373d", fg="white", font="Montserrat 11 bold").place(x=310, y=110)
       entercart=mycombobox(self.entryframe,width=20,textvariable=self.additem,font="Montserrat 12")
       entercart.place(x=130,y=30,height=30)
       cartqty = Entry(self.entryframe,textvariable=self.qty,width=9,bg="#ffffff",font="Montserrat 12")
       cartqty.place(x=390,y=30,height=30)
       carttotal = Entry(self.entryframe, textvariable=self.total, width=20, state='readonly', bg="#ffffff", font="Montserrat 12")
       carttotal.place(x=130, y=205, height=30)
       Label(self.entryframe, text="Quantity", font="Montserrat 12 bold", bg="#12171c",fg="white").place(x=390,y=0)
       Label(self.entryframe, text="Search", font="Montserrat 12 bold", bg="#12171c",fg="white").place(x=130, y=0)
       Label(self.entryframe, text="Amount Due", font="Montserrat 12 bold", bg="#12171c",fg="white").place(x=0, y=205)
       self.cur.execute("select max(invoice) from sales")
       self.invoice = self.cur.fetchall()
       self.invoice = self.invoice[0][0] + 1
       Label(self.tableframe1, text="Invoice No. "+str(self.invoice), font="Montserrat 12 bold", bg="#12171c",fg="white").grid(row=0, column=0)
       self.cur.execute("select product_desc,product_price from products")
       li=self.cur.fetchall()
       self.inventory = []
       self.desc_price=dict()
       for i in range(0, len(li)):
           if (self.inventory.count(li[i][0]) == 0):
               self.inventory.append(li[i][0])
           self.desc_price[li[i][0]]=li[i][1]
       entercart.set_completion_list(self.inventory)
       li=['Product Id','Product Name','Price','Left Stock']
       va=0
       for i in range(0,4):
           Label(self.entryframe1, text=li[i], font="Montserrat 12 bold", bg="#12171c",fg="white").place(x=0, y=va)
           va += 65
       self.cartitemid = StringVar()
       self.cartitem = StringVar()
       self.cartitemprice = StringVar()
       self.cartitemstock = StringVar()
       Entry(self.entryframe1, textvariable=self.cartitemid, font="roboto 14", bg="#FFFFFF", width=25, state='readonly').place(x=162, y=0,height = 40)
       Entry(self.entryframe1, textvariable=self.cartitem, font="roboto 14", bg="#FFFFFF", width=25, state='readonly').place(x=162, y=65,height=40)
       Entry(self.entryframe1, textvariable=self.cartitemprice, font="roboto 14", bg="#FFFFFF", width=25, state='readonly').place(x=162,y=65*2,height=40)
       Entry(self.entryframe1, textvariable=self.cartitemstock, font="roboto 14", bg="#FFFFFF", width=25, state='readonly').place(x=162,y=65*3,height=40)
       self.id_qty=dict()
       self.cur.execute("select product_id from products")
       l=self.cur.fetchall()
       for i in range(0,len(l)):
           self.id_qty[l[i][0]]=0

    def addtotrans(self):
        if(len(self.additem.get()) == 0 or self.inventory.count(self.additem.get())==0):
            messagebox.showerror("Error", "Product Not Found!")
            return
        else:
            if(not self.qty.get().isdigit()):
                messagebox.showerror('Error','Invalid quantity!')
                return
            if(int(self.qty.get()) <= 0):
                messagebox.showerror('Error', 'Invalid quantity!')
                return
            self.cur.execute("select product_id,product_desc from products where product_desc = ? ",(self.additem.get(),))
            row = self.cur.fetchall()
            row = [list(row[0])]
            row[0].insert(0,self.transid)
            self.transid+=1
            row[0].append(int(self.qty.get()))
            row[0].append((int(self.qty.get())*self.desc_price[self.additem.get()]))
            x=str(datetime.datetime.now().strftime("%d-%m-%y"))
            row[0].append(x)
            x=datetime.datetime.now()
            x=str(x.hour)+' : '+str(x.minute)+' : '+str(x.second)
            row[0].append(x)
            row = [tuple(row[0])]
            self.cartitemid.set(row[0][1])
            self.cartitemprice.set(self.desc_price[self.additem.get()])
            self.cartitem.set(row[0][2])
            self.cur.execute("select stocks from products where product_id=?", (row[0][1],))
            li = self.cur.fetchall()
            if((li[0][0]-self.id_qty[row[0][1]])-int(self.qty.get())<0):
                if(li[0][0]!=0):
                    messagebox.showerror('Error','Product with this quantity not available!')
                else:
                    messagebox.showerror('Error', 'Product out of stock!')
                return
            self.id_qty[row[0][1]] += int(self.qty.get())
            self.cartitemstock.set(li[0][0]-self.id_qty[row[0][1]])
            for data in row:
                self.tree.insert('', 'end', values=(data))
            self.total.set(self.total.get() + (int(self.qty.get()) * self.desc_price[self.additem.get()]))
            self.qty.set('1')
            self.additem.set('')

    def transtableadd(self):
        x=self.tree.get_children()
        if(len(x) == 0):
            messagebox.showerror('Error','Empty cart!')
            return
        if (messagebox.askyesno('Alert!','Do you want to proceed?') == False):
            return
        a=[]
        self.cur.execute("select max(invoice) from sales")
        self.invoice=self.cur.fetchall()
        self.invoice=self.invoice[0][0]+1
        for i in x:
            l=self.tree.item(i)
            a.append(l['values'])
        for i in a:
            s = (str(i[5])).split('-')
            i[5] = s[2] + "-" + s[1] + "-" + s[0]
            self.cur.execute("insert into sales values (?,?,?,?,?,?)",(int(i[0]),int(self.invoice),int(i[1]),int(i[3]),i[5],i[6]))
            self.cur.execute("select stocks from products where product_id=?",(int(i[1]),))
            l=self.cur.fetchall()
            self.cur.execute("update products set stocks=? where product_id=?",(l[0][0]-self.id_qty[str(i[1])],int(i[1])))
            self.base.commit()
        messagebox.showinfo('Success','Transaction Successful!')
        self.makeprint()
        self.tree.delete(*self.tree.get_children())
        self.cartitemstock.set('')
        self.cartitem.set('')
        self.cartitemid.set('')
        self.cartitemprice.set('')
        self.total.set(0)
        self.additem.set('')
        self.qty.set('1')
        self.cur.execute("select product_id from products")
        l = self.cur.fetchall()
        for i in range(0, len(l)):
            self.id_qty[l[i][0]] = 0
        self.make_invoice()

    def removecart(self):
        re = self.tree.selection()
        if(len(re)==0):
            messagebox.showerror('Error','No cart selected')
            return
        if (messagebox.askyesno('Alert!','Remove cart?') == True):
            x = self.tree.get_children()
            re=re[0]
            l=[]
            fi=[]
            for i in x:
                if(i!=re):
                    l.append(tuple((self.tree.item(i))['values']))
                else:
                    fi=((self.tree.item(i))['values'])
            self.tree.delete(*self.tree.get_children())
            for i in l:
                self.tree.insert('', 'end', values=(i))
            self.cartitemstock.set('')
            self.cartitem.set('')
            self.cartitemid.set('')
            self.cartitemprice.set('')
            self.additem.set('')
            self.qty.set('1')
            self.id_qty[str(fi[1])]-=fi[3]
            self.total.set(self.total.get()-fi[4])
            return

    def makeprint(self):
        if messagebox.askyesno("Alert!", "Print this transaction?"):
            x = datetime.datetime.now()
            dir_path = "./Invoice"
            if not os.path.exists(dir_path):
                os.makedirs("./Invoice")

            file_name = os.path.join(dir_path, f"Invoice_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.pdf")

            c = canvas.Canvas(file_name)
            c.setStrokeColorRGB(0, 0, 0) 
            c.rect(20, 20, 560, 780)  

            heading = "Invoice Heading"
            c.setFont("Helvetica-Bold", 24)
            c.drawCentredString(300, 750, heading)

            heading_y = 720
            table_y = heading_y - 100  

            bill_number = f"Bill Number: {self.invoice} | Date/Time: {x.strftime('%d %b, %Y | %I:%M %p')}"
            c.setFont("Helvetica-Bold", 16)
            c.drawCentredString(300, heading_y, bill_number)

            data = [["Item Name", "Quantity", "Price", "Total"]]
            x = self.tree.get_children()
            total_amount = 0
            for i in range(len(x)):
                item_name = self.tree.item(x[i])['values'][2]
                quantity = int(self.tree.item(x[i])['values'][3])
                price = float(self.tree.item(x[i])['values'][4])
                total = quantity * price  
                total_amount += total
                data.append([item_name, quantity, price, total])

            table_width = sum([200, 80, 80, 80])  
            table_x = (c._pagesize[0] - table_width) / 2  

            table = Table(data, colWidths=[200, 80, 80, 80])
            table.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                    ('BACKGROUND', (0, 0), (-1, 0), '#32373d'),
                                    ('TEXTCOLOR', (0, 0), (-1, 0), (1, 1, 1),'white'),
                                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                    ('BACKGROUND', (0, 1), (-1, -1), '#12171c'),
                                    ('GRID', (0, 0), (-1, -1), 1, 'white'),
                                    ('TEXTCOLOR', (0, 1), (-1, -1), colors.white)
                                    ]))

            table.wrapOn(c, 0, 0)
            table.drawOn(c, table_x, table_y)

            total_text = f"Total Amount: {total_amount:.2f}"
            c.setFont("Helvetica-Bold", 14)
            c.drawCentredString(300, table_y - 50, total_text)

            # Save the PDF and open it
            c.save()
            os.startfile(file_name)


        
    def clicktranstable(self,event):
        cur = self.tree.selection()
        cur = self.tree.item(cur)
        li = cur['values']
        if (len(li) == 7):
            self.cartitemid.set((li[1]))
            self.cartitem.set((li[2]))
            self.cur.execute("select product_price,stocks from products where product_id=?",(li[1],))
            li = self.cur.fetchall()
            self.cartitemprice.set(li[0][0])
            self.cartitemstock.set(li[0][1]-self.id_qty[self.cartitemid.get()])