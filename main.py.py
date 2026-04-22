from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random
import os
import tempfile


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1540x880+0+0")
        self.root.title("BILLING SOFTWARE")

        # ===== Variables =====
        self.c_name = StringVar()
        self.c_phon = StringVar()
        self.billno = StringVar()
        z = random.randint(1000, 9999)
        self.billno.set(z)
        self.c_email = StringVar()
        self.search_bill = StringVar()
        self.product = StringVar()
        self.prices = IntVar()
        self.qty = IntVar(value=1)
        self.sub_total = StringVar()
        self.tax_input = StringVar()
        self.total = StringVar()
        self.tax_rate = 5  # 5% GST

        self.l = []  # item list

        # ===== Category Data =====
        self.Category = ("Select Option", "Clothing", "LifeStyle", "Electronics")
        self.SubCatClothing = ["Pant", "T-Shirt", "Shirt"]
        self.pant = {"Levis": 1500, "D2S": 1200, "HM": 7800}
        self.tshirt = {"Polo": 3200, "Peter England": 2500}
        self.shirt = {"Addidas": 800, "Park Avanue": 700}

        self.SubCatLifestyle = ["Bath Soap", "Face cream", "Hair Oil"]
        self.bathsoap = {"LUX": 500, "NO1": 800, "Lifebuoy": 700}
        self.facecream = {"AYUR": 50, "PONDS": 80, "Olay": 70}
        self.hairoil = {"Dabur": 350, "Parachute": 150, "Amla": 200}

        self.SubCatElectronics = ["Iphone", "Samsung", "realme"]
        self.iphone = {"16": 180000, "16pro": 150000, "17": 200000}
        self.samsung = {"G2": 35000, "S23": 150000, "S24": 200000}
        self.realme = {"Narzo40": 25000, "Narzo50": 18500, "12": 36000}

        # ====== Header Images ======
        # Image 1
        img = Image.open("image/good.jpg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        lbl_img = Label(self.root, image=self.photoimg)
        lbl_img.place(x=0, y=0, width=500, height=130)

        # Image 2
        img_2 = Image.open("image/aa3.jpg")
        img_2 = img_2.resize((520, 130), Image.LANCZOS)
        self.photoimg_2 = ImageTk.PhotoImage(img_2)
        lbl_img_2 = Label(self.root, image=self.photoimg_2)
        lbl_img_2.place(x=500, y=0, width=520, height=130)

        # Image 3
        img_3 = Image.open("image/aa6.webp")
        img_3 = img_3.resize((520, 130), Image.LANCZOS)
        self.photoimg_3 = ImageTk.PhotoImage(img_3)
        lbl_img_3 = Label(self.root, image=self.photoimg_3)
        lbl_img_3.place(x=1020, y=0, width=520, height=130)

        # ====== Title Label below header images ======
        lbl_title = Label(self.root, text="BILLING MANAGEMENT SYSTEM",
                          font=("times new roman", 35, "bold"),
                          bg="white", fg="blue")
        lbl_title.place(x=0, y=130, width=1540, height=60)

        # ===== Main Frame =====
        Main_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="white")
        Main_Frame.place(x=0, y=190, width=1530, height=690)

        # ===== Customer Frame =====
        Cust_Frame = LabelFrame(Main_Frame, text="Customer", font=("times new roman", 12, "bold"), bg="white", fg="blue")
        Cust_Frame.place(x=10, y=5, width=350, height=140)

        Label(Cust_Frame, text="Mobile No:", font=("times new roman", 12, "bold"), bg="white").grid(row=0, column=0, padx=5)
        ttk.Entry(Cust_Frame, textvariable=self.c_phon, width=24).grid(row=0, column=1, padx=5)

        Label(Cust_Frame, text="Customer Name:", font=("times new roman", 12, "bold"), bg="white").grid(row=1, column=0, padx=5)
        ttk.Entry(Cust_Frame, textvariable=self.c_name, width=24).grid(row=1, column=1, padx=5)

        Label(Cust_Frame, text="Email:", font=("times new roman", 12, "bold"), bg="white").grid(row=2, column=0, padx=5)
        ttk.Entry(Cust_Frame, textvariable=self.c_email, width=24).grid(row=2, column=1, padx=5)

        # ===== Product Frame =====
        Product_Frame = LabelFrame(Main_Frame, text="Products", font=("times new roman", 12, "bold"), bg="white", fg="blue")
        Product_Frame.place(x=370, y=5, width=620, height=140)

        Label(Product_Frame, text="Select Category", font=("arial", 12, "bold"), bg="white").grid(row=0, column=0, padx=5)
        self.Combo_Category = ttk.Combobox(Product_Frame, values=self.Category, state="readonly", width=20)
        self.Combo_Category.grid(row=0, column=1, padx=5)
        self.Combo_Category.bind("<<ComboboxSelected>>", self.Categories)

        Label(Product_Frame, text="Sub Category", font=("arial", 12, "bold"), bg="white").grid(row=1, column=0, padx=5)
        self.ComboSubCategory = ttk.Combobox(Product_Frame, state="readonly", width=20)
        self.ComboSubCategory.grid(row=1, column=1, padx=5)
        self.ComboSubCategory.bind("<<ComboboxSelected>>", self.Product_add)

        Label(Product_Frame, text="Product Name", font=("arial", 12, "bold"), bg="white").grid(row=2, column=0, padx=5)
        self.ComboProduct = ttk.Combobox(Product_Frame, textvariable=self.product, state="readonly", width=20)
        self.ComboProduct.grid(row=2, column=1, padx=5)
        self.ComboProduct.bind("<<ComboboxSelected>>", self.price)

        Label(Product_Frame, text="Price", font=("arial", 12, "bold"), bg="white").grid(row=0, column=2, padx=5)
        ttk.Entry(Product_Frame, textvariable=self.prices, width=20, state="readonly").grid(row=0, column=3, padx=5)

        Label(Product_Frame, text="Qty", font=("arial", 12, "bold"), bg="white").grid(row=1, column=2, padx=5)
        ttk.Entry(Product_Frame, textvariable=self.qty, width=20).grid(row=1, column=3, padx=5)
        # middle frame (image)
        MiddleFrame=Frame(Main_Frame, bd=10)
        MiddleFrame.place(x=10, y=150, width=980, height=340)

        #Image 1
        img12 = Image.open("image/good.jpg")
        img12 = img12.resize((490,340), Image.LANCZOS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        lbl_img12 = Label(MiddleFrame,image=self.photoimg)
        lbl_img12.place(x=0, y=0, width=490, height=340)    

#Image 2
        img_13 = Image.open("image/aa3.jpg")
        img_13 = img_13.resize((490,340), Image.LANCZOS)
        self.photoimg_13=ImageTk.PhotoImage(img_13)

        lbl_img_13 = Label(MiddleFrame,image=self.photoimg_13)
        lbl_img_13.place(x=490, y=0, width=500, height=340)  

# search
        Search_Frame=Frame(Main_Frame, bd=2, bg="White")
        Search_Frame.place(x=1020, y=10, width=500, height=40)


        self.lblBill=Label(Search_Frame, font=("arial", 12, "bold"),fg="white", bg="blue", text="Bill Number")
        self.lblBill.grid(row=0, column=0,sticky=W,padx=5)

        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=("arial",10, "bold"), width=26)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=2)


        self.BtnSearch=Button(Search_Frame,command=self.find_bill, text="Search", font=("arial", 10, "bold"), bg="Blue",fg="white", width=15, cursor="hand2")
        self.BtnSearch.grid(row=0, column=2)  

        # ====== Bill Area ======
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman ", 12, "bold"), bg="white", fg="blue")
        RightLabelFrame.place(x=1000, y=45, width=480, height=440)

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set, bg="white",fg="blue",font=("times new roman ", 12, "bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)
        self.welcome()

        # ====== Bottom Frame ======
        Bottom_Frame = LabelFrame(Main_Frame, text="Bill Counter", font=("times new roman", 12, "bold"), bg="white", fg="blue")
        Bottom_Frame.place(x=0, y=470, width=1520, height=200)

        Label(Bottom_Frame, text="SubTotal", font=("arial", 15, "bold"), bg="white").grid(row=0, column=0, padx=5)
        ttk.Entry(Bottom_Frame, textvariable=self.sub_total, width=20, state="readonly").grid(row=0, column=1, padx=5)

        Label(Bottom_Frame, text="Tax", font=("arial", 15, "bold"), bg="white").grid(row=1, column=0, padx=5)
        ttk.Entry(Bottom_Frame, textvariable=self.tax_input, width=20, state="readonly").grid(row=1, column=1, padx=5)

        Label(Bottom_Frame, text="Total", font=("arial", 15, "bold"), bg="white").grid(row=2, column=0, padx=5)
        ttk.Entry(Bottom_Frame, textvariable=self.total, width=20, state="readonly").grid(row=2, column=1, padx=5)

        # ====== Buttons ======
        # Button Frame
        Btn_Frame=Frame(Bottom_Frame, bd=2, bg="White")
        Btn_Frame.place(x=320, y=0)
# for add to cart button
        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,height=3, text="Add to Cart", font=("arial", 15, "bold"), bg="Blue",fg="white", width=15, cursor="hand2")
        self.BtnAddToCart.grid(row=0, column=0)        
# for generate bill button
        self.BtngenerateBill=Button(Btn_Frame, command=self.generate_bill, height=3, text="Generate Bill", font=("arial", 15, "bold"), bg="BLue",fg="white", width=15, cursor="hand2")
        self.BtngenerateBill.grid(row=0, column=1)   
# for save bill button
        self.BtnSaveBill=Button(Btn_Frame, height=3,command=self.save_bill ,text="Save Bill", font=("arial", 15, "bold"), bg="Blue",fg="white", width=15, cursor="hand2")
        self.BtnSaveBill.grid(row=0, column=2)   
 # for Print button
        self.BtnPrintBill=Button(Btn_Frame, command=self.iprint, height=3, text="Print Bill", font=("arial", 15, "bold"), bg="Blue",fg="white", width=15, cursor="hand2")
        self.BtnPrintBill.grid(row=0, column=3)   
 # for clear button
        self.BtnClearBill=Button(Btn_Frame, height=3, command=self.clear ,text="Clear", font=("arial", 15, "bold"), bg="BLue",fg="white", width=15, cursor="hand2")
        self.BtnClearBill.grid(row=0, column=4)   
  # for Exit button
        self.BtnExitBill=Button(Btn_Frame, height=3, command=self.ExitApp,text="Exit", font=("arial", 15, "bold"), bg="Blue",fg="white", width=15, cursor="hand2")
        self.BtnExitBill.grid(row=0, column=5)  
    # ====== Functions ======
    def welcome(self):
        self.textarea.delete(1.0, END)
        self.textarea.insert(END, "\t\tWELCOME TO VISHAL MEGA MART")
        self.textarea.insert(END, f"\nBill No: {self.billno.get()}")
        self.textarea.insert(END, f"\nCustomer Name: {self.c_name.get()}")
        self.textarea.insert(END, f"\nPhone No: {self.c_phon.get()}")
        self.textarea.insert(END, "\n=================================================")
        self.textarea.insert(END, "\nProduct\t\tQty\tPrice")
        self.textarea.insert(END, "\n=================================================")

    def AddItem(self):
        if self.product.get() == "":
            messagebox.showerror("Error", "Please select product")
            return
        price = self.prices.get()
        qty = self.qty.get()
        total = price * qty
        self.l.append(total)
        self.textarea.insert(END, f"\n{self.product.get()}\t\t{qty}\t{total}")
        self.sub_total.set(str(sum(self.l)))
        tax = (sum(self.l) * self.tax_rate) / 100
        self.tax_input.set(str(round(tax, 2)))
        self.total.set(str(round(sum(self.l) + tax, 2)))


    def generate_bill(self):
        if self.c_name.get() == "" or self.c_phon.get() == "":
            messagebox.showerror("Error", "Customer details required")
            return
        if len(self.l) == 0:
            messagebox.showerror("Error", "No products added")
            return
        self.textarea.delete(1.0, END)

    # ===== Bill Header =====
        self.textarea.insert(END, "\t\tVISHAL MEGA MART\n")
        self.textarea.insert(END, "=================================================\n")
        self.textarea.insert(END, f"Bill No: {self.billno.get()}\n")
        self.textarea.insert(END, f"Customer Name: {self.c_name.get()}\n")
        self.textarea.insert(END, f"Phone No: {self.c_phon.get()}\n")
        self.textarea.insert(END, "=================================================\n")
        self.textarea.insert(END, "Product\t\tQty\tPrice\n")
        self.textarea.insert(END, "=================================================\n")
        for idx in range(len(self.l)):
            pass  
        self.textarea.insert(END, "\n-------------------------------------------------")
        self.textarea.insert(END, f"\nSub Total:\t\t\tRs {self.sub_total.get()}")
        self.textarea.insert(END, f"\nTax (5%):\t\t\tRs {self.tax_input.get()}")
        self.textarea.insert(END, f"\nTotal Amount:\t\t\tRs {self.total.get()}")
        self.textarea.insert(END, "\n-------------------------------------------------")



    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the Bill?")
        if op > 0:
            bill_data = self.textarea.get(1.0, END)
            if not os.path.exists("bills"):
                os.mkdir("bills")
            with open(f"bills/{self.billno.get()}.txt", "w") as f:
                f.write(bill_data)
            messagebox.showinfo("Saved", f"Bill No: {self.billno.get()} saved successfully")
    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")

    def find_bill(self):
        found = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                with open(f"bills/{i}", "r") as f1:
                    self.textarea.delete(1.0, END)
                    self.textarea.insert(END, f1.read())
                    found = "yes"
                    break
            if found == "no":
                    messagebox.showerror("Error", "Invalid Bill No")

    def ExitApp(self):
        self.root.destroy()
        exit_btn = Button(self.root, text="Exit", font=("Arial", 12, "bold"),
                          bg="red", fg="white", command=self.ExitApp)
        exit_btn.place(x=1300, y=700)   # coordinates adjust kar lena








    def clear(self):
        self.textarea.delete(1.0, END)
        self.l.clear()
        self.c_name.set("")
        self.c_phon.set("")
        self.c_email.set("")
        self.sub_total.set("")
        self.tax_input.set("")
        self.total.set("")
        self.welcome()

    def Categories(self, event=""):
        if self.Combo_Category.get() == "Clothing":
            self.ComboSubCategory.config(value=self.SubCatClothing)
        elif self.Combo_Category.get() == "LifeStyle":
            self.ComboSubCategory.config(value=self.SubCatLifestyle)
        elif self.Combo_Category.get() == "Electronics":
            self.ComboSubCategory.config(value=self.SubCatElectronics)

    def Product_add(self, event=""):
        subcat = self.ComboSubCategory.get()
        mapping = {
            "Pant": self.pant, "T-Shirt": self.tshirt, "Shirt": self.shirt,
            "Bath Soap": self.bathsoap, "Face cream": self.facecream, "Hair Oil": self.hairoil,
            "Iphone": self.iphone, "Samsung": self.samsung, "realme": self.realme
        }
        if subcat in mapping:
            self.ComboProduct.config(value=list(mapping[subcat].keys()))

    def price(self, event=""):
        subcat = self.ComboSubCategory.get()
        mapping = {
            "Pant": self.pant, "T-Shirt": self.tshirt, "Shirt": self.shirt,
            "Bath Soap": self.bathsoap, "Face cream": self.facecream, "Hair Oil": self.hairoil,
            "Iphone": self.iphone, "Samsung": self.samsung, "realme": self.realme
        }
        product_name = self.ComboProduct.get()
        if subcat in mapping and product_name in mapping[subcat]:
            self.prices.set(mapping[subcat][product_name])

            # required imports (agar pehle se nahi hain)

if __name__ == "__main__":
    if not os.path.exists("bills"):
        os.mkdir("bills")
    root = Tk()
    obj = Bill_App(root)
    root.mainloop()
