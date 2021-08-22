from tkinter import *
import tkinter.font as font

root = Tk()
root.title("Simple Calculator")
myFont = font.Font(family="calibri",size=20,weight="bold")
e = Entry(root,width=25,borderwidth=5,font=myFont,justify="right")

e.grid(row=0,column=0,columnspan=3,padx=10,pady=10,)
global identifier
identifier = ""
def type_checker(data):
    if type(data) is not int:
        return float(data)
def AddNum(number):
        current = e.get()# 10
        e.delete(0,END)
        e.insert(0,str(current)+str(number))

def Num_Clear():
    e.delete(0,END)

def Button_Add(first_number):
    if len(e.get())==0:
        return
    try:
        first_number = int(first_number)
    except:
        first_number = type_checker(first_number)

    e.delete(0,END)
    global f_num
    f_num = first_number
    global identifier
    identifier="+"

def Num_Sub(first_number):
    if len(e.get())==0:
        return
    try:
        first_number = int(first_number)
    except:
        first_number = type_checker(first_number)

    e.delete(0,END)
    global f_num
    f_num = first_number
    global identifier
    identifier = "-"
def Num_Mul(first_number):
    if len(e.get())==0:
        return
    try:
        first_number = int(first_number)
    except:
        first_number = type_checker(first_number)

    e.delete(0,END)
    global f_num
    f_num = first_number
    global identifier
    identifier = "*"

def Num_Div(first_number):
    if len(e.get()) == 0:
        return
    try:
        first_number = int(first_number)
    except:
        first_number = type_checker(first_number)

    e.delete(0,END)
    global f_num
    f_num = first_number
    global identifier
    identifier="/"

def Num_Equal():
    print(identifier)
    if identifier =="+":
        try:
            second_number = int(e.get())
        except:
            second_number = type_checker(e.get())
        e.delete(0,END)
        e.insert(0,f_num+second_number)
    elif identifier =="-":
        try:
            second_number = int(e.get())
        except:
            second_number = type_checker(e.get())
        e.delete(0,END)
        e.insert(0,f_num-second_number)
    elif identifier == "*":
        try:
            second_number = int(e.get())
        except:
            second_number = type_checker(e.get())
        e.delete(0,END)
        e.insert(0,f_num * second_number)
    elif identifier =="/":
        try:
            second_number = int(e.get())
        except:
            second_number = type_checker(e.get())
        e.delete(0,END)
        if second_number == 0:
            e.insert(0,"Cannot divide by zero")
        else:
            div = f_num / second_number
            e.insert(0, div)
    else:
        pass


# creating a button
button_1 = Button(root,text="1",padx=40,pady=20,command=lambda:AddNum(1),fg="white",bg="black")
button_2 = Button(root,text="2",padx=40,pady=20,command=lambda:AddNum(2),fg="white",bg="black")
button_3 = Button(root,text="3",padx=40,pady=20,command=lambda:AddNum(3),fg="white",bg="black")
button_4 = Button(root,text="4",padx=40,pady=20,command=lambda:AddNum(4),fg="white",bg="black")
button_5 = Button(root,text="5",padx=40,pady=20,command=lambda:AddNum(5),fg="white",bg="black")
button_6 = Button(root,text="6",padx=40,pady=20,command=lambda:AddNum(6),fg="white",bg="black")
button_7= Button(root,text="7",padx=40,pady=20,command=lambda:AddNum(7),fg="white",bg="black")
button_8 = Button(root,text="8",padx=40,pady=20,command=lambda:AddNum(8),fg="white",bg="black")
button_9 = Button(root,text="9",padx=40,pady=20,command=lambda:AddNum(9),fg="white",bg="black")
button_0 = Button(root,text="0",padx=40,pady=20,command=lambda:AddNum(0),fg="white",bg="black")
button_clear = Button(root,text="CLEAR",padx=81,pady=20,command=Num_Clear,fg="white",bg="black")
button_add = Button(root,text="+",padx=39,pady=20,command=lambda:Button_Add(e.get()),fg="white",bg="black")
button_equal = Button(root,text="=",padx=95,pady=20,command=Num_Equal,fg="white",bg="black")
button_subtract = Button(root,text="-",padx=40,pady=20,command=lambda : Num_Sub(e.get()),fg="white",bg="black")
button_multiply = Button(root,text="x",padx=40,pady=20,command=lambda : Num_Mul(e.get()),fg="white",bg="black")
button_division = Button(root,text="/",padx=40,pady=20,command=lambda : Num_Div(e.get()),fg="white",bg="black")

# use a grid
button_1.grid(row=3,column=0,pady=3)
button_2.grid(row=3,column=1,pady=3)
button_3.grid(row=3,column=2,pady=3)

button_4.grid(row=2,column=0,pady=3)
button_5.grid(row=2,column=1,pady=3)
button_6.grid(row=2,column=2,pady=3)

button_7.grid(row=1,column=0,pady=3)
button_8.grid(row=1,column=1,pady=3)
button_9.grid(row=1,column=2,pady=3)

button_0.grid(row=4,column=0,pady=3)
button_clear.grid(row=5,column=1,columnspan=2,pady=3)
button_add.grid(row=5,column=0,pady=3)
button_equal.grid(row=6,column=1,columnspan=2,pady=3)
button_subtract.grid(row=6,column=0,pady=3)
button_multiply.grid(row=4,column=1,pady=3)
button_division.grid(row=4,column=2,pady=3)



root.mainloop()