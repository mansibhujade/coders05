from tkinter import *

if __name__=="__main__":

    gui=Tk()
    gui.title("REGISTRATION PAGE")
    gui.geometry("700x600")

    label=Label(gui,text="NEW REGISTRATION",font=30,bg="green")
    label.place(height=50,width=500,x=50,y=0)

    roll_no=Label(gui,text="ROLL NUMBER").\
        place(height=50,width=100,x=50,y=100)
    roll_no_text=Entry(gui).place(height=30, width=200, x=200, y=100)



    student_name=Label(gui,text="STUDENT NAME").\
        place(height=50,width=100,x=50,y=150)
    student_name_text = Entry(gui).place(height=30, width=200, x=200, y=150)

    branch=Label(gui,text="BRANCH").\
        place(height=50,width=100,x=50,y=200)
    branch_text = Entry(gui).place(height=30, width=200, x=200, y=200)

    submit_button = Button(gui, text="Submit").\
        place(height=50, width=100, x=500, y=450)



    gui.mainloop()