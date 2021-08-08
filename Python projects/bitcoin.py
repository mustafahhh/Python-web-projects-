import requests as r
from tkinter import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from PIL import ImageTk, Image
import concurrent.futures

from datetime import datetime 

root = Tk()
style.use('fivethirtyeight')
fig=plt.figure()
ax1=fig.add_subplot(1,1,1)
bitcoinprice=[]

def foo(bar):
    print('hello {}'.format(bar))
    return r.get(f'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms={bar}').json()[bar]


def ex():
    print(x)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        res = executor.submit(foo, x)
        res = res.result()
        print(res)
    e=Label(root,text="^^Bitcoin price^^",fg="white",bg="#272727",font=("Courier",20))
    e.place(x=120,y=200)

    s=Label(root,text=res,fg="white",bg="#272727",font=("Courier",15))
    s.place(x=200,y=175)
    root.after(1000,ex)
def limitSizeDay(*args):
    values = value.get()
    fr=values[0]
    sc=values[1]
    th=values[2]
    if len(values) > 3: value.set(f'{fr}{sc}{th}')
def xx(*args):
    values = value.get()
    value.set(values.upper())
def trans(*args):
    global x
    x=currency.get().upper()
    label.destroy()
    currency.destroy()
    button.destroy()
    root.after(0,ex)
    global now
    now = datetime.now()
    
value = StringVar()
value.trace('w', limitSizeDay)
value.trace('w',xx)
label = Label(root,text="Enter currency shortcut(like USD)",fg="white",bg="#272727",font=("Courier",20))
currency=Entry(root,bg="white",textvariable=value,fg="#272727",font=("Courier", 19))
currency.place(x=100,y=100,height=50,width=200)
label.place(x=50,y=50)
button= Button(root,text="enter",fg="#272727",bg="orange",bd=0,font=("Courier",13))
button.place(x=300,y=100,width=50,height=50)
button.bind('<Button-1>',trans)
root.configure(bg="#272727")
root.geometry("579x400")
root.mainloop()

