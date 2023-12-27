from tkinter import Tk,Label,Entry,PhotoImage,StringVar,Button,messagebox
from random import randint


def love():
    lov = None
    for i in range(max(len(partner1.get()),len(partner2.get()))):
        lov = str(randint(0,9))+str(randint(0,9))
    else:
        messagebox.showinfo("LOVE",f"LOVE PERCENTAGE IS:- {lov}%")


if __name__ =="__main__":
    #SETTING TITLE AND GEOMETRY
    root = Tk()
    root.geometry("360x200")
    root.minsize(430,170)
    root.maxsize(430,170)
    root.title("Love Calculator")

    #SETTING ICONS
    icon = PhotoImage(file="OIP.png")
    root.iconphoto(True,icon)

    #TAKING INPUT'S OF NAME
    partner1 = StringVar()
    partner2 = StringVar()
    Label(root,text = "Enter the Partner 1:- ",font="Aerial 16 bold").grid(row=30,column=1)
    Label(root,text = "Enter the Partner 2:- ",font="Aerial 16 bold").grid(row=50,column=1)
    Entry(root,textvariable=partner1,width=20).grid(row=30,column=8)
    Entry(root,textvariable=partner2,width=20).grid(row=50,column=8)

    #MAKING CALCULATE AND EXIT BUTTON 
    Button(root,text="Calculate",font="Aerial 16 bold",command=love).grid(row=70,column=1)
    Button(root,text="Exit",font="Aerial 16 bold",command=exit).grid(row=90,column=1)

    #START GUI
    root.mainloop()
