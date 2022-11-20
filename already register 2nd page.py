from tkinter import *

if __name__ =="__main__":
    gui=Tk()
    gui.title("ALREADY REGISTERED")
    gui.geometry("700x700")

    label = Label(gui, text="ALREADY REGISTRATED", font=30, bg="green")
    label.place(height=50, width=500, x=50, y=0)

    roll_no = Label(gui, text="ROLL NUMBER"). \
        place(height=50, width=100, x=50, y=100)
    roll_no_text = Entry(gui).place(height=30, width=200, x=200, y=100)

    student_name = Label(gui, text="STUDENT NAME"). \
        place(height=50, width=100, x=50, y=150)
    student_name_text = Entry(gui).place(height=30, width=200, x=200, y=150)

    book_issue = Button(gui, text="BOOK ISSUE", font=10). \
        place(height=50, width=250, x=100, y=200)

    book_return = Button(gui, text="BOOK RETURN", font=10). \
        place(height=50, width=250, x=400, y=200)

    label_2 = Label(gui, text="ALREADY ISSUED BOOKS", font=20, bg="green")
    label_2.place(height=50, width=500, x=60, y=270)


    penalty = Label(gui, text="PENALTY"). \
        place(height=50, width=100, x=50, y=500)
    penalty_text = Entry(gui).place(height=30, width=200, x=200, y=500)

    return_date = Label(gui, text="RETURN DATE"). \
        place(height=50, width=100, x=50, y=550)
    return_date_text = Entry(gui).place(height=30, width=200, x=200, y=550)

    submit_button = Button(gui, text="Submit"). \
        place(height=50, width=100, x=500, y=650)



    gui.mainloop()