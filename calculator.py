import tkinter as tk
from math import *

convert_constant = 1
inverse_convert_constant = 1
def fsin(arg):
    return sin(arg * convert_constant)
def fcos(arg):
    return cos(arg * convert_constant)
def ftan(arg):
    return tan(arg * convert_constant)
def arcsin(arg):
    return (inverse_convert_constant * (asin(arg)))
def arccos(arg):
    return (inverse_convert_constant * (acos(arg)))
def arctan(arg):
    return (inverse_convert_constant * (atan(arg)))

class Calculator:
    def __init__(self, master):

        self.expression = ""

        self.recall = ""

        self.sum_up = ""

        self.text_Input = tk.StringVar()

        self.master = master

        top_frame = tk.Frame(master, width=650, height=20, bd=4, relief='flat', bg='#666666')
        top_frame.pack(side=tk.TOP)

        bottom_frame = tk.Frame(master, width=650, height=470, bd=4, relief='flat', bg='#666666')
        bottom_frame.pack(side=tk.BOTTOM)

        my_item = tk.Label(top_frame, text="SCIENTIFIC CALCULATOR", font=('calibri', 14), fg='white', width=26,bg='#666666')
        my_item.pack()

        txtDisplay = tk.Entry(top_frame, font=('arial', 36), relief='flat', bg='#666666', fg='white',textvariable=self.text_Input, width=60, bd=4, justify='right')
        txtDisplay.pack()

        self.btn_left_brack = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#666666',font=('arial', 18), width=2, height=2,text="(", relief='flat', activebackground="#666666",command=lambda: self.btnClick('('))
        self.btn_left_brack.grid(row=0, column=0)

        self.btn_right_brack = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#666666',font=('arial', 18),width=2, height=2, relief='flat', text=")", activebackground="#666666",command=lambda: self.btnClick(')'))
        self.btn_right_brack.grid(row=0, column=1)

        self.btn_exp = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#666666', font=('arial', 18),width=2,height=2, relief='flat', text="exp", activebackground="#666666",command=lambda: self.btnClick('exp('))
        self.btn_exp.grid(row=0, column=2)

        self.btn_pi = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#666666', font=('arial', 18),width=2, height=2, relief='flat', activebackground="#666666", text="π",command=lambda: self.btnClick('pi'))
        self.btn_pi.grid(row=0, column=3)

        self.btn_clear = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#666666', font=('arial', 18),width=2,height=2, text="C", relief='flat', activebackground="#666666",command=self.btnClearAll)
        self.btn_clear.grid(row=0, column=4)

        self.btn_del = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#666666', font=('arial', 18),width=2,height=2, text="del", relief='flat', activebackground="#666666",command=self.btnClear1)
        self.btn_del.grid(row=0, column=5)

        self.btn_change_sign = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#666666',font=('arial', 18),width=2, height=2, relief='flat', text="+/-", activebackground="#666666",command=self.change_signs)
        self.btn_change_sign.grid(row=0, column=6)

        self.btn_div = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#666666', font=('arial', 18),width=2,height=2, text="/", relief='flat', activebackground="#666666",command=lambda: self.btnClick('/'))
        self.btn_div.grid(row=0, column=7)

        self.btn_sqrt = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#666666', font=('arial', 18),width=2,height=2, relief='flat', text="√", activebackground="#666666",command=lambda: self.btnClick('sqrt('))
        self.btn_sqrt.grid(row=0, column=8)
        # row 1
        self.btn_Deg = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#666666', font=('arial', 18),width=2, height=2,text="Deg", relief='flat', activebackground="#666666", foreground='white',activeforeground='orange', command=self.convert_deg)
        self.btn_Deg.grid(row=1, column=0)

        self.btn_Rad = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#666666', font=('arial', 18),width=2,height=2, text="Rad", relief='flat', foreground='orange', activeforeground='orange',activebackground="#666666", command=self.convert_rad)
        self.btn_Rad.grid(row=1, column=1)

        self.btn_root_of = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#666666', font=('arial', 18),width=2, height=2,text="x√  ", relief='flat', activebackground="#666666",command=lambda: self.btnClick('**(1/'))
        self.btn_root_of.grid(row=1, column=2)

        self.btn_abs = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#666666', font=('arial', 18),width=2,height=2, relief='flat', text="abs", activebackground="#666666",command=lambda: self.btnClick('abs' + '('))
        self.btn_abs.grid(row=1, column=3)

        self.btn_7 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#4d4d4d', font=('arial', 18),width=2, height=2,text="7", relief='flat', activebackground="#4d4d4d", command=lambda: self.btnClick(7))
        self.btn_7.grid(row=1, column=4)

        self.btn_8 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#4d4d4d', font=('arial', 18),width=2, height=2,text="8", relief='flat', activebackground="#4d4d4d", command=lambda: self.btnClick(8))
        self.btn_8.grid(row=1, column=5)

        self.btn_9 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#4d4d4d', font=('arial', 18),width=2, height=2,text="9", relief='flat', activebackground="#4d4d4d", command=lambda: self.btnClick(9))
        self.btn_9.grid(row=1, column=6)

        self.btn_mult = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#666666', font=('arial', 18),width=2,height=2, relief='flat', text="x", activebackground="#666666",command=lambda: self.btnClick('*'))
        self.btn_mult.grid(row=1, column=7)

        self.btn_MC = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#666666', font=('arial', 18),width=2, height=2,text="MC", relief='flat', activebackground="#666666",command=self.memory_clear)
        self.btn_MC.grid(row=1, column=8)

        # row 2
        self.btn_sin = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#666666', font=('arial', 18),width=2, height=2,text="sin", relief='flat', activebackground="#666666",command=lambda: self.btnClick('fsin('))
        self.btn_sin.grid(row=2, column=0)

        self.btn_cos = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#666666', font=('arial', 18),width=2, height=2,text="cos", relief='flat', activebackground="#666666",command=lambda: self.btnClick('fcos('))
        self.btn_cos.grid(row=2, column=1)

        self.btn_tan = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#666666', font=('arial', 18),width=2,height=2, relief='flat', activebackground="#666666", text="tan",command=lambda: self.btnClick('ftan('))
        self.btn_tan.grid(row=2, column=2)

        self.btn_log = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#666666', font=('arial', 18),width=2, height=2,text="log", relief='flat', activebackground="#666666",command=lambda: self.btnClick('log('))
        self.btn_log.grid(row=2, column=3)

        self.btn4 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#4d4d4d', font=('arial', 18),width=2, height=2,text="4", relief='flat', activebackground="#4d4d4d", command=lambda: self.btnClick(4))
        self.btn4.grid(row=2, column=4)

        self.btn5 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#4d4d4d', font=('arial', 18),width=2, height=2,text="5", relief='flat', activebackground="#4d4d4d", command=lambda: self.btnClick(5))
        self.btn5.grid(row=2, column=5)

        self.btn6 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#4d4d4d', font=('arial', 18),width=2, height=2,text="6", relief='flat', activebackground="#4d4d4d", command=lambda: self.btnClick(6))
        self.btn6.grid(row=2, column=6)

        self.btnSub = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#666666', font=('arial', 18),width=2, height=2,text="-", relief='flat', activebackground="#4d4d4d", command=lambda: self.btnClick('-'))
        self.btnSub.grid(row=2, column=7)
 
        self.btn_MR = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#666666', font=('arial', 18),width=2, height=2,text="MR", relief='flat', activebackground="#666666",command=self.memory_recall)
        self.btn_MR.grid(row=2, column=8)

        # row 3
        self.btn_sin_inverse = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#666666',font=('arial', 18), width=2, height=2,text="sin⁻¹", relief='flat', activebackground="#666666",command=lambda: self.btnClick('arcsin('))
        self.btn_sin_inverse.grid(row=3, column=0)

        self.btn_cos_inverse = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#666666',font=('arial', 18), width=2, height=2,text="cos⁻¹", relief='flat', activebackground="#666666",command=lambda: self.btnClick('arccos('))
        self.btn_cos_inverse.grid(row=3, column=1)

        self.btn_tan_inverse = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#666666',font=('arial', 18), width=2, height=2,text="tan⁻¹", relief='flat', activebackground="#666666",command=lambda: self.btnClick('arctan('))
        self.btn_tan_inverse.grid(row=3, column=2)

        self.btn_ln = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#666666', font=('arial', 18),width=2, height=2,text="ln", relief='flat', activebackground="#666666",command=lambda: self.btnClick('log1p('))
        self.btn_ln.grid(row=3, column=3)

        self.btn1 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#4d4d4d', font=('arial', 18),width=2, height=2,text="1", relief='flat', activebackground="#4d4d4d", command=lambda: self.btnClick(1))
        self.btn1.grid(row=3, column=4)

        self.btn2 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#4d4d4d', font=('arial', 18),width=2, height=2,text="2", relief='flat', activebackground="#4d4d4d", command=lambda: self.btnClick(2))
        self.btn2.grid(row=3, column=5)

        self.btn3 = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#4d4d4d', font=('arial', 18),width=2, height=2,text="3", relief='flat', activebackground="#4d4d4d", command=lambda: self.btnClick(3))
        self.btn3.grid(row=3, column=6)

        self.btn_add = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#666666', font=('arial', 18),width=2, height=2,text="+", relief='flat', activebackground="#666666",command=lambda: self.btnClick('+'))
        self.btn_add.grid(row=3, column=7)

        self.btn_M_plus = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#666666', font=('arial', 18),width=2, height=2,text="M+", relief='flat', activebackground="#666666",command=self.memory_add)
        self.btn_M_plus.grid(row=3, column=8)

        # row 4
        self.btn_fact = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#666666', font=('arial', 18),width=2, height=2,text="n!", relief='flat', activebackground="#666666",command=lambda: self.btnClick('factorial('))
        self.btn_fact.grid(row=4, column=0)

        self.btn_sqr = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#666666', font=('arial', 18),width=2, height=2,text=u"x\u00B2", relief='flat', activebackground="#666666",command=lambda: self.btnClick('**2'))
        self.btn_sqr.grid(row=4, column=1)

        self.btn_power = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#666666', font=('arial', 18),width=2, height=2,text="xʸ", relief='flat', activebackground="#666666",command=lambda: self.btnClick('**'))
        self.btn_power.grid(row=4, column=2)

        self.btn_ans = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#666666', font=('arial', 18),width=2, height=2,text="ans", relief='flat', activebackground="#666666", command=self.answer)
        self.btn_ans.grid(row=4, column=3)

        self.btn_0 = tk.Button(bottom_frame, padx=16, pady=1, bd=5, fg='white', bg='#4d4d4d', font=('arial', 18),width=7, height=2,text="0", relief='flat', activebackground="#4d4d4d", command=lambda: self.btnClick(0))
        self.btn_0.grid(row=4, column=4, columnspan=2)

        self.btn_eq = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='orange', font=('arial', 18),width=2, height=2,text="=", relief='flat', activebackground="#666666", command=self.btnEqual)
        self.btn_eq.grid(row=4, column=6)

        self.btn_dec = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#666666', font=('arial', 18),width=2, height=2,text=".", relief='flat', activebackground="#666666",command=lambda: self.btnClick('.'))
        self.btn_dec.grid(row=4, column=7)

        self.btn_comma = tk.Button(bottom_frame, padx=16, pady=1, bd=4, fg='white', bg='#666666', font=('arial', 18),width=2, height=2,text=",", relief='flat', activebackground="#666666",command=lambda: self.btnClick(','))
        self.btn_comma.grid(row=4, column=8)

    def btnClick(self, expression_val):
        self.expression = self.expression + str(expression_val)
        self.text_Input.set(self.expression)

    def btnClear1(self):
        self.expression = self.expression[:-1]
        self.text_Input.set(self.expression)

    def change_signs(self):
        self.expression = self.expression + '-'
        self.text_Input.set(self.expression)

    def memory_clear(self):
        self.recall = ""

    def memory_add(self):
        self.recall = self.recall + '+' + self.expression

    def answer(self):
        self.answer = self.sum_up
        self.text_Input.set(self.expression + self.answer)

    def memory_recall(self):
        if self.expression == "":
            self.text_Input.set('0' + self.expression + self.recall)
        else:
            self.text_Input.set(self.expression + self.recall)

    def convert_deg(self):
        global convert_constant
        global inverse_convert_constant
        convert_constant = pi / 180
        inverse_convert_constant = 180 / pi
        self.btn_Rad["foreground"] = 'white'
        self.btn_Deg["foreground"] = 'orange'
    def convert_rad(self):
        global convert_constant
        global inverse_convert_constant
        convert_constant = 1
        inverse_convert_constant = 1
        self.btn_Rad["foreground"] = 'orange'
        self.btn_Deg["foreground"] = 'white'

    def btnClearAll(self):
        self.expression = ""
        self.text_Input.set("")

    def btnEqual(self):
        self.sum_up = str(eval(self.expression))
        self.text_Input.set(self.sum_up)
        self.expression = ""

root = tk.Tk()
b = Calculator(root)
root.title("Simple Scientific Calculator")
root.geometry("650x490+50+50")
root.resizable(False, False)
root.mainloop()