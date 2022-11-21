from tkinter import *
from tkinter import messagebox
if __name__=="__main__":

    gui=Tk()
    gui.title("REGISTRATION PAGE")
    gui.geometry("1000x500")

    label=Label(gui,text="NEW REGISTRATION",font=("Papyrus 22 bold"),fg="red",bg="black")
    label.place(height=50,width=1000,x=0,y=0)

    roll_no=Label(gui,text=" ROLL NUMBER :- ",font=40). \
    place(height=30, width=150, x=250, y=100)
    book_id_text = Entry(gui).place(height=30, width=200, x=400, y=100)


    student_name=Label(gui,text="STUDENT NAME :-",font=40).\
    place(height=30,width=200,x=220,y=150)
    student_name_text = Entry(gui).place(height=30, width=200, x=400, y=150)

    branch=Label(gui,text="BRANCH:-",font=40).\
    place(height=30,width=250,x=220,y=200)
    branch_text = Entry(gui).place(height=30, width=200, x=400, y=200)

    date_of_brith = Label(gui, text="DATE OF BRITH :-", font=40). \
    place(height=30, width=300, x=180, y=250)
    date_of_brith_text = Entry(gui).place(height=30, width=200, x=400, y=250)

    number= Label(gui, text="NUMBER :-", font=40). \
    place(height=30, width=350, x=180, y=300)
    NUMBER_text = Entry(gui).place(height=30, width=200, x=400, y=300)

    email = Label(gui, text="EMAIL :-", font=40). \
    place(height=30, width=400, x=150, y=350)
    date_of_brith_text = Entry(gui).place(height=30, width=200, x=400, y=350)


    def showMsg():
        messagebox.showinfo('Message', 'You clicked the Submit button!')


    button = Button(gui,
                    text='Submit', bg='black', fg='red', font="Papyrus 22 bold",
                    command=showMsg). \
        place(height=60, width=200, x=400, y=400)



    gui.mainloop()
