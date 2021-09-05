from tkinter import *
import tkinter.font as font

root = Tk()
root.title("Standard Calculator")
root.configure(bg="black")
def OnClick(number):  
    global operator         # declare operator globally
    symbol = ['+', '-', '*', "/"]       # list of operation    
    if len(operator) == 0 and number ==0:       #check the  operator has 0 length and the number you click is zero
        return
    if number in symbol and len(operator)==0:    # check if the number is in symbol but length is equal to zero   
        return
    if number in symbol and operator[-1] in symbol: # check the last element is in symbol and the current number is symbol
        return
    operator = operator +str(number)            #concatenate all the operator and number
    text_input.set(operator)        #set operator in the StringVar 

def ClearBtn():         # just clear the all value in the StringVar
    global operator     # operator will remove all the value
    operator=""
    text_input.set("") # back to zero input in the StringVar


def EqualBtn():         # this process will execute the operation
    global operator
    try :
        sumup = str(eval(operator)) # check if the operator can evaluate and change to string
        text_input.set(sumup)       # it will set the value in StringVar 
    except:
        text_input.set("Syntax Error") # if the try is error then the StringVar will set to Syntax error
    finally:            
        global holder
        holder = operator
        operator="" # it will clear the operator



operator = ""
text_input = StringVar()
myFont = font.Font(family="calibri",size=20,weight="bold")
e = Entry(root,width=20,borderwidth=10,justify='right',font = myFont,textvariable=text_input,bg="black",fg="white")
e.grid(row=0,column=0,columnspan=3,padx=20,pady=20)

button_1 = Button(root,text="1",padx=40,pady=20,fg="white",bg="black",command=lambda:OnClick(1),borderwidth = 10)
button_2 = Button(root,text="2",padx=40,pady=20,fg="white",bg="black",command=lambda:OnClick(2),borderwidth = 10)
button_3 = Button(root,text="3",padx=40,pady=20,fg="white",bg="black",command=lambda:OnClick(3),borderwidth = 10)
button_4 = Button(root,text="4",padx=40,pady=20,fg="white",bg="black",command=lambda:OnClick(4),borderwidth = 10)
button_5 = Button(root,text="5",padx=40,pady=20,fg="white",bg="black",command=lambda:OnClick(5),borderwidth = 10)
button_6 = Button(root,text="6",padx=40,pady=20,fg="white",bg="black",command=lambda:OnClick(6),borderwidth = 10)
button_7= Button(root,text="7",padx=40,pady=20,fg="white",bg="black",command=lambda:OnClick(7),borderwidth = 10)
button_8 = Button(root,text="8",padx=40,pady=20,fg="white",bg="black",command=lambda:OnClick(8),borderwidth = 10)
button_9 = Button(root,text="9",padx=40,pady=20,fg="white",bg="black",command=lambda:OnClick(9),borderwidth = 10)
button_0 = Button(root,text="0",padx=40,pady=20,fg="white",bg="black",command=lambda:OnClick(0),borderwidth = 10)
button_clear = Button(root,text="CLEAR",padx=81,pady=20,fg="white",bg="black",command=ClearBtn,borderwidth = 10)
button_add = Button(root,text="+",padx=39,pady=20,fg="white",bg="black",command=lambda:OnClick("+"),borderwidth = 10)
button_equal = Button(root,text="=",padx=95,pady=20,fg="white",bg="black",command=EqualBtn,borderwidth = 10)
button_subtract = Button(root,text="-",padx=40,pady=20,fg="white",bg="black",command=lambda:OnClick("-"),borderwidth = 10)
button_multiply = Button(root,text="x",padx=40,pady=20,fg="white",bg="black",command=lambda:OnClick("*"),borderwidth = 10)
button_division = Button(root,text="/",padx=40,pady=20,fg="white",bg="black",command=lambda:OnClick("/"),borderwidth = 10)

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
