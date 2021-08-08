import datetime
from tkinter import *
##Configing tkinter window 
root=Tk()
root.config(bg="white")
root.geometry("425x700")
##Done of configing the root window
def entered(event):
    birthdayyear.delete(0,'end')
    birthdayyear.config(fg="black")

def entered1(event):

    birthdaymonth.config(fg="black")
    birthdaymonth.delete(0,'end')
def entered2(event): 
    birthday.delete(0,'end')
    birthday.config(fg="black")
def result(event):

    m = birthdaymonth.get() 
    d = birthday.get()

    birth = datetime.date(2000, int(m), int(d))

    today = datetime.date.today()

    if(
        today.month == birth.month
        and today.day >= birth.day
        or today.month > birth.month
    ):
        nextBirthdayYear = today.year + 1
    else:
        nextBirthdayYear = today.year

    nextBirthday = datetime.date(
        nextBirthdayYear, birth.month, birth.day
    )

    diff = nextBirthday - today
    result1.config(text=diff.days)
def limitSizeDay(*args):
    values = value.get()
    try:
        fr=values[0]
    except:
        pass
    try:
        sc=values[1]
    except:
        pass
    try:
        th=values[2]
    except:
        pass
    try:
        fo=values[3]
    except:
        pass
    if len(values) > 4: value.set(f'{fr}{sc}{th}{fo}')
def limitmonth(*args):
    print("x")
    values = value1.get()
    try:
        fr=values[0]
    except:
        pass
    try:
        sc=values[1]
    except:
        pass
    if len(values)>2:value1.set(f'{fr}{sc}')
def limitday(*args):
    print("x")
    values = value2.get()
    try:
        fr=values[0]
    except:
        pass
    try:
        sc=values[1]
    except:
        pass
    if len(values)>2:value2.set(f'{fr}{sc}')
def main():
###upperFrame
    upper=Frame(root,bg="orange")
    upper.pack(side="top",fill=BOTH)
    bu1=Button(upper,text="1",bg="gray17",bd=0,width=2,fg="white",height=1)
    bu1.place(x=1,y=1)
    label=Label(upper,text="still ... for your birthday",fg="white",font=("system",20),bg="orange")
    label.pack()
###
###Middle done 
    global birthdaymonth
    birthdaymonth=Entry(root,textvariable=value1,bg="white",fg="#bdbdbd",font=("arial",50),width=3,bd=0)
    birthdaymonth.pack(side="left",pady=(10,300),padx=50)
    birthdaymonth.insert(0,"mm")
    birthdaymonth.bind("<Button-1>",entered1)

###Done of birthdaymonth
    L=Label(root,text=":",fg="black",font=("arial",50))
    L.pack(side="left",pady=(10,300))
##Middle done
    global birthday
    birthday=Entry(root,textvariable=value2,bg="white",fg="#bdbdbd",font=("arial",50),width=2,bd=0)
    birthday.pack(side="left",pady=(10,300),padx=50)
    birthday.insert(0,"dd")
    birthday.bind("<Button-1>",entered2)
##label for shsma
    global result1
    result1=Button(root,bd=0,text="RESULT",bg="black",fg="WHITE",font=("arial",20))
    result1.place(x=150,y=500)
    result1.bind("<Button-1>",result)
value=StringVar()
value.trace('w',limitSizeDay)
value1=StringVar()
value1.trace('w',limitmonth)
value2=StringVar()
value2.trace('w',limitday)
main()
root.title("still .... for your birthday")
root.mainloop()
