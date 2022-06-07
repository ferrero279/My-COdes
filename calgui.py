import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN
window =tk.Tk()
window.title('Calculator GUI')
frame=tk.Frame(master=window,bg="cyan",padx=12)
frame.pack()
entry=tk.Entry(master=frame,relief=SUNKEN,borderwidth=3,width=32)
entry.grid(row=0,column=0,columnspan=3,ipady=2,pady=2)
def myclick(num):
    entry.insert(tk.END,num)
def equal():
    try:
        y=str(eval(entry.get()))
        entry.delete(0,tk.END)
        entry.insert(0,y)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error: ")

def clear():
    entry.delete(0,tk.END)

but1=tk.Button(master=frame,text='1',padx=15,pady=5,width=3,command=lambda:myclick(1))
but1.grid(row=1,column=0,pady=2)
but2=tk.Button(master=frame,text='2',padx=15,pady=5,width=3,command=lambda:myclick(2))
but2.grid(row=1,column=1,pady=2)
but3=tk.Button(master=frame,text='3',padx=15,pady=5,width=3,command=lambda:myclick(3))
but3.grid(row=1,column=2,pady=2)
but4=tk.Button(master=frame,text='4',padx=15,pady=5,width=3,command=lambda:myclick(4))
but4.grid(row=2,column=0,pady=2)
but5=tk.Button(master=frame,text='5',padx=15,pady=5,width=3,command=lambda:myclick(5))
but5.grid(row=2,column=1,pady=2)
but6=tk.Button(master=frame,text='6',padx=15,pady=5,width=3,command=lambda:myclick(6))
but6.grid(row=2,column=2,pady=2)
but7=tk.Button(master=frame,text='7',padx=15,pady=5,width=3,command=lambda:myclick(7))
but7.grid(row=3,column=0,pady=2)
but8=tk.Button(master=frame,text='8',padx=15,pady=5,width=3,command=lambda:myclick(8))
but8.grid(row=3,column=1,pady=2)
but9=tk.Button(master=frame,text='9',padx=15,pady=5,width=3,command=lambda:myclick(9))
but9.grid(row=3,column=2,pady=2)
but0=tk.Button(master=frame,text='0',padx=15,pady=5,width=3,command=lambda:myclick(0))
but0.grid(row=4,column=1,pady=2)

but_add=tk.Button(master=frame,text="+",padx=15,pady=5,width=3,command=lambda:myclick('+'))
but_add.grid(row=5,column=0,pady=2)
but_sub=tk.Button(master=frame,text="-",padx=15,pady=5,width=3,command=lambda:myclick('-'))
but_sub.grid(row=5,column=1,pady=2)
but_mul=tk.Button(master=frame,text="*",padx=15,pady=5,width=3,command=lambda:myclick('*'))
but_mul.grid(row=5,column=2,pady=2)
but_div=tk.Button(master=frame,text="/",padx=15,pady=5,width=3,command=lambda:myclick('/'))
but_div.grid(row=6,column=0,pady=2)

but_clear=tk.Button(master=frame,text="clear",padx=15,pady=5,width=12,command=clear)
but_clear.grid(row=6,column=1,columnspan=2,pady=2)
but_equal=tk.Button(master=frame,text="Equals",padx=15,pady=5,width=15,command=equal)
but_equal.grid(row=7,column=0,columnspan=3,pady=2)
window.mainloop()
