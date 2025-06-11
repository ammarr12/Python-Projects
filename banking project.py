from tkinter import *
from tkinter import messagebox

class Banking:
    accounts_list=[]
    def __init__(self,name,pin,value):
        self.__name=name
        self.__pin=pin
        self.value=value
        Banking.accounts_list.append(self)

    @property
    def get_name(self):
        return self.__name
    
    @get_name.setter
    def set_name(self,var):
        self.__name=var
    
    @property
    def get_pin(self):
        return self.__pin
    
    @get_pin.setter
    def set_pin(self,var):
        self.__pin=var
    
    @classmethod
    def transaction(S,name,value):
        for i in S.accounts_list:
            if name==i.get_name:
                i.value+=value
                print("hello")
    
    
    @classmethod
    def write_data(Banking):
        with open("test_file.txt","w") as f1:
            for i in Banking.accounts_list:
                f1.write(i.get_name)
                f1.write(",")
                f1.write(str(i.get_pin))
                f1.write(",")
                f1.write(str(i.value))
                f1.write("\n")
    
    
    @classmethod
    def read_data(B):
        with open("test_file.txt","r") as f1:
            x=f1.readlines()
            print(x)
            for i in range(len(x)):
                x[i]=x[i][:-1]                
                x[i]=x[i].split(",")
                Banking(x[i][0],int(x[i][1]),int(x[i][2]))
            
    
    def account_details(self):
        return f"Name\tPin\tBalace\n{self.get_name}\t{self.get_pin}\t{self.value}"
                                                                                                                        
                                                                                                                               
Banking.read_data()

class Authentication:
    def __init__(self):
        self.window=Tk()
        self.window.geometry("400x300")
        self.name=Entry(self.window,width=20)
        self.b=Label(self.window,text="Name")
        self.value=Entry(self.window,width=20)
        self.c=Label(self.window,text="Pin")
        self.select=Button(self.window,text="Enter",padx=20,pady=2,command=lambda:self.func(self.name.get(),self.value.get()))
        self.window.protocol("WM_DELET_WINDOW")
        self.b.place(x=90,y=90)
        self.name.place(x=140,y=90)
        self.c.place(x=90,y=140)
        self.value.place(x=140,y=140)
        self.select.place(x=150,y=240)
        self.window.mainloop()

    def func(self,name,pin):
        for i in range(len(Banking.accounts_list)):
            if (name==Banking.accounts_list[i].get_name) and (int(pin)==Banking.accounts_list[i].get_pin):
                self.window.destroy()
                Mainmenu.user=i
                Mainmenu()
                break
        else:
            messagebox.showwarning(self.window,message="Invalid acount details!")



class Mainmenu:
    user=-1
    
    def __init__(self):
        self.window=Tk()
        self.window.title("main menu")
        self.window.geometry("400x200")
        
        Label(self.window,text="Banking System",font=("helveltica",14)).pack()
        self.v=IntVar()
        self.options={"Withdraw":1,
                     "Deposit":2,
                     "transaction":3,
                     "Account details":4}

        for (text,value) in self.options.items():
            Radiobutton(self.window,text=text,value=value,variable=self.v).pack(anchor=W)
    
        Button(self.window,text="select",padx=20,pady=2,command=lambda:self.on_selecting()).place(x=150,y=150)
        print(Mainmenu.user)
        self.window.protocol("WM_DELETE_WINDOW",self.onclosing)
        self.window.mainloop()

    def on_selecting(self):
        if self.v.get()==1:
            self.window.destroy()
            Withdraw()
        
        if self.v.get()==2:
            self.window.destroy()
            Deposit()
        
        if self.v.get()==3:
            self.window.destroy()
            Transaction()    
        
        if self.v.get()==4:
            self.window.destroy()
            Acount_Details()

    def onclosing(self):
        Banking.write_data()
        self.window.destroy()
       

class Withdraw:
    def __init__(self):
        self.window=Tk()
        self.window.title("Withdraw")
        self.window.geometry("400x300")
        Label(self.window,text=" Enter the Withdraw Value",font=("Times New Roman",17)).pack()
        self.withdraw_value=Entry(self.window,width=20)
        self.select=Button(self.window,text="Enter",padx=20,pady=2,command=lambda:self.withdraw(self.withdraw_value.get()))
        self.window.protocol("WM_DELETE_WINDOW",self.onclosing)
        self.withdraw_value.place(x=130,y=90)
        self.select.place(x=150,y=200)
        self.window.mainloop()
    
    def onclosing(self):
        self.window.destroy()
        Mainmenu()

    def withdraw(self,value):
        if int(value) < Banking.accounts_list[Mainmenu.user].value:
            Banking.accounts_list[Mainmenu.user].value-=int(value)
            messagebox.showinfo(self.window,message=f"Wthdraw successful! {Banking.accounts_list[Mainmenu.user].value}")
        else:
            messagebox.showwarning(self.window,message="Invalid Value")


class Deposit:
    def __init__(self):
        self.window=Tk()
        self.window.geometry("400x300")
        self.window.title("deposit")
        Label(self.window,text="Enter the Deposit value",font=("Times new roman",15)).pack()
        self.deposit_value=Entry(self.window,width=20)
        self.select=Button(self.window,text="Enter",padx=20,pady=2,command=lambda:self.deposit(self.deposit_value.get()))
        self.deposit_value.place(x=130,y=90)
        self.select.place(x=150,y=200)
        self.window.protocol("WM_DELETE_WINDOW",self.onclosing)
        self.window.mainloop()
    
    def onclosing(self):
        self.window.destroy()
        Mainmenu()

    def deposit(self,value):
        Banking.accounts_list[Mainmenu.user].value+=int(value)
        messagebox.showinfo(self.window,message=f"Wthdraw successful! {Banking.accounts_list[Mainmenu.user].value}")
        



class Transaction:
    def __init__(self):
        self.window=Tk()
        self.window.geometry("400x300")
        self.window.title("deposit")
        self.a=Label(self.window,text="Transaction",font=("helveltica",15)).pack()
        self.recieptant_name=Entry(self.window,width=20)
        self.b=Label(self.window,text="Name")
        self.value=Entry(self.window,width=20)
        self.c=Label(self.window,text="Value")
        self.select=Button(self.window,text="Enter",padx=20,pady=2,command=lambda:self.transaction(self.recieptant_name.get(),int(self.value.get())))
        self.b.place(x=90,y=90)
        self.recieptant_name.place(x=140,y=90)
        self.c.place(x=90,y=140)
        self.value.place(x=140,y=140)
        self.select.place(x=150,y=240)
        self.window.protocol("WM_DELETE_WINDOW",self.onclosing)
        self.window.mainloop()
    
    def onclosing(self):
        self.window.destroy()
        Mainmenu()


    def transaction(self,name,value):
        Banking.transaction(name,value)
        messagebox.showinfo(self.window,message="Transaction successful")






class Acount_Details:
    def __init__(self):
        self.window=Tk()
        self.x=Banking.accounts_list[Mainmenu.user].account_details()
        self.T=Text(self.window,height=5,width=40,font=("helveltica",14),pady=10,padx=50)
        self.T.insert(END,self.x)
        self.window.protocol("WM_DELETE_WINDOW",self.onclosing)
        self.T.pack()
        self.window.mainloop()
        
    
    def onclosing(self):
        self.window.destroy()
        Mainmenu()


Authentication()
