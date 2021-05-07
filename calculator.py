from tkinter import*

def btnClick(numbers) :
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay() :
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput() : 
    global operator
    sumOp=str(eval(operator))
    text_Input.set(sumOp)
    operator=""

cal = Tk()
cal.title("Calculator")
operator=""
text_Input =StringVar()

txtDisplay = Entry(cal, fg='#969696', font=('calibri', 20, 'bold'), textvariable=text_Input, bd=10, insertwidth=4, bg='#282828', justify='right').grid(columnspan=4)

btn7=Button(cal, padx=16, pady=16, bd=8, fg='#969696', font=('calibri', 20, 'bold'), text="7", command=lambda:btnClick(7), bg='#282828').grid(row=1,column=0)
btn8=Button(cal, padx=16, pady=16, bd=8, fg='#969696', font=('calibri', 20, 'bold'), text="8", command=lambda:btnClick(8), bg='#282828').grid(row=1,column=1)
btn9=Button(cal, padx=16, pady=16, bd=8, fg='#969696', font=('calibri', 20, 'bold'), text="9", command=lambda:btnClick(9), bg='#282828').grid(row=1,column=2)
btnAdd=Button(cal, padx=16, pady=16, bd=8, fg='yellow', font=('calibri', 20, 'bold'), text="+", command=lambda:btnClick("+"), bg='#282828').grid(row=1,column=3)
#=======================
btn4=Button(cal, padx=16, pady=16, bd=8, fg='#969696', font=('calibri', 20, 'bold'), text="4", command=lambda:btnClick(4), bg='#282828').grid(row=2,column=0)
btn5=Button(cal, padx=16, pady=16, bd=8, fg='#969696', font=('calibri', 20, 'bold'), text="5", command=lambda:btnClick(5), bg='#282828').grid(row=2,column=1)
btn6=Button(cal, padx=16, pady=16, bd=8, fg='#969696', font=('calibri', 20, 'bold'), text="6", command=lambda:btnClick(6), bg='#282828').grid(row=2,column=2)
btnSub=Button(cal, padx=16, pady=16, bd=8, fg='yellow', font=('calibri', 20, 'bold'), text="-", command=lambda:btnClick("-"), bg='#282828').grid(row=2,column=3)
#=======================
btn1=Button(cal, padx=16, pady=16, bd=8, fg='#969696', font=('calibri', 20, 'bold'), text="1", command=lambda:btnClick(1), bg='#282828').grid(row=3,column=0)
btn2=Button(cal, padx=16, pady=16, bd=8, fg='#969696', font=('calibri', 20, 'bold'), text="2", command=lambda:btnClick(2), bg='#282828').grid(row=3,column=1)
btn3=Button(cal, padx=16, pady=16, bd=8, fg='#969696', font=('calibri', 20, 'bold'), text="3", command=lambda:btnClick(3), bg='#282828').grid(row=3,column=2)
btnMul=Button(cal, padx=16, pady=16, bd=8, fg='yellow', font=('calibri', 20, 'bold'), text="*", command=lambda:btnClick("*"), bg='#282828').grid(row=3,column=3)
#=======================
btn0=Button(cal, padx=16, pady=16, bd=8, fg='#969696', font=('calibri', 20, 'bold'), text="0", command=lambda:btnClick(0), bg='#282828').grid(row=4,column=0)
btnClear=Button(cal, padx=16, pady=16, bd=8, fg='yellow', font=('calibri', 20, 'bold'), text="C", command=btnClearDisplay, bg='#282828').grid(row=4,column=1)
btnEqual=Button(cal, padx=16, pady=16, bd=8, fg='yellow', font=('calibri', 20, 'bold'), text="=", command=btnEqualsInput, bg='#282828').grid(row=4,column=2)
btnDiv=Button(cal, padx=16, pady=16, bd=8, fg='yellow', font=('calibri', 20, 'bold'), text="/", command=lambda:btnClick("/"), bg='#282828').grid(row=4,column=3)

cal.mainloop()