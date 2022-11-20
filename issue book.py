from tkinter import *

if __name__ =="__main__":
    gui=Tk()
    gui.title("ISSUE BOOK")
    gui.geometry("500x500")

    label = Label(gui, text="ISSUE BOOK", font=30, bg="green")
    label.place(height=50, width=500, x=0, y=0)

    student_id = Label(gui, text="STUDENT ID"). \
        place(height=50, width=100, x=50, y=100)
    student_id_text = Entry(gui).place(height=30, width=200, x=200, y=100)

    book_id = Label(gui, text="BOOK ID"). \
        place(height=50, width=100, x=50, y=150)
    book_id_text = Entry(gui).place(height=30, width=200, x=200, y=150)

    back_button = Button(gui, text="BACK"). \
        place(height=50, width=100, x=50, y=400)

    issue_button = Button(gui, text="ISSUE"). \
        place(height=50, width=100, x=300, y=400)

    gui.mainloop()