from tkinter import *

if __name__ == "__main__":
    gui=Tk()
    gui.title("intro page")
    gui.geometry('700x600')

    l1=Label(gui,text="welcome to  library",bg="green" ,width=30,font=100).\
        place(height=100,width=550,x=75,y=00)


    new_registration=Button(gui,text="NEW REGISTRATION",font=10).\
        place(height=50,width=250,x=100,y=100)

    already_registration = Button(gui, text="ALREADY REGISTRATED",font=10). \
        place(height=50, width=250, x=400, y=100)

    add_books = Button(gui, text="ADD BOOKS",font=10). \
        place(height=50, width=200, x=100, y=200)

    view_books = Button(gui, text="VIEW BOOKS",font=10). \
        place(height=50, width=200, x=400, y=200)

    issued_books = Button(gui, text="ISSUED BOOKS", font=10). \
        place(height=50, width=200, x=270, y=300)

    gui.mainloop()
