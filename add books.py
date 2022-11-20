from tkinter import *

if __name__ =="__main__":
    gui=Tk()
    gui.title("ADD BOOKS")
    gui.geometry("700x600")


    label = Label(gui, text="ADD BOOKS", font=30, bg="green")
    label.place(height=50, width=500, x=50, y=0)


    book_id=Label(gui,text="BOOK ID").\
        place(height=50,width=100,x=50,y=100)
    book_id_text=Entry(gui).place(height=30, width=200, x=200, y=100)

    book_name=Label(gui,text="BOOK NAME").\
        place(height=50,width=100,x=50,y=150)
    book_name_text = Entry(gui).place(height=30, width=200, x=200, y=150)

    title_name=Label(gui,text="TITLE").\
        place(height=50,width=100,x=50,y=200)
    title_name_text = Entry(gui).place(height=30, width=200, x=200, y=200)

    author_name=Label(gui,text="AUTHOR NAME").\
        place(height=50,width=100,x=50,y=250)
    book_name_text = Entry(gui).place(height=30, width=200, x=200, y=250)
    
    copies=Label(gui,text="COPIES").\
        place(height=50,width=100,x=50,y=300)
    copies_text = Entry(gui).place(height=30, width=200, x=200, y=300)

    submit_button = Button(gui, text="Submit").\
        place(height=50, width=100, x=500, y=450)

    gui.mainloop()
