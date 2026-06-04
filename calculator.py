from tkinter import Tk
from tkinter import Button,Label
root = Tk()
root.geometry('300x300')
root.title('calculator')
n1=""
n2=0
def undade(val,val2):
    global n1,n2
    n2+=val2
    on=True
    if val2==0 or n2==3:
        n2=0
    elif n2==2:
        on=False
    if on:
        n1=n1+val
        lb1.configure(text=n1)
def cal():
    try:
        global n1
        n1=str(eval(n1))
        lb1.configure(text=n1)
    except ValueError:
        return
bt1=Button(root,text='1',command=lambda:undade(val="1",val2=0))
bt1.place(x=0, y=0, width=50, height=50)
bt2=Button(root,text='2',command=lambda:undade(val="2",val2=0))
bt2.place(x=50, y=0, width=50, height=50)
bt3=Button(root,text='3',command=lambda:undade(val="3",val2=0))
bt3.place(x=100, y=0, width=50, height=50)
bt4=Button(root,text='4',command=lambda:undade(val="4",val2=0))
bt4.place(x=0, y=50, width=50, height=50)
bt5=Button(root,text='5',command=lambda:undade(val="5",val2=0))
bt5.place(x=50, y=50, width=50, height=50)
bt6=Button(root,text='6',command=lambda:undade(val="6",val2=0))
bt6.place(x=100, y=50, width=50, height=50)
bt7=Button(root,text='7',command=lambda:undade(val="7",val2=0))
bt7.place(x=0, y=100, width=50, height=50)
bt8=Button(root,text='8',command=lambda:undade(val="8",val2=0))
bt8.place(x=50, y=100, width=50, height=50)
bt9=Button(root,text='9',command=lambda:undade(val="9",val2=0))
bt9.place(x=100, y=100, width=50, height=50)
bt10=Button(root,text='+',command=lambda:undade(val="+",val2=1))
bt10.place(x=150, y=0, width=50, height=50)
bt11=Button(root,text='-',command=lambda:undade(val="-",val2=1))
bt11.place(x=150, y=50, width=50, height=50)
bt12=Button(root,text='x',command=lambda:undade(val="*",val2=1))
bt12.place(x=150, y=100, width=50, height=50)
bt13=Button(root,text='÷',command=lambda:undade(val="/",val2=1))
bt13.place(x=150, y=150, width=50, height=50)
bt14=Button(root,text='=',command=lambda:cal())
bt14.place(x=100, y=150, width=50, height=50)
bt15=Button(root,text='0',command=lambda:undade(val="0",val2=0))
bt15.place(x=50, y=150, width=50, height=50)
bt16=Button(root,text=',',command=lambda:undade(val=".",val2=1))
bt16.place(x=0, y=150, width=50, height=50)
lb1=Label(root,text='')
lb1.place(x=50, y=200, width=50, height=50)
root.mainloop()