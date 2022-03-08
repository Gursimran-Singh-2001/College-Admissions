from tkinter import *
import mysql.connector as mysql
root = Tk()
import tkinter.messagebox as tmsg
root.title("College Admission Records")
# Label
root.geometry("740x580")
root.minsize(450, 300)
root.maxsize(740,580)
root.configure(borderwidth=6, bg="white")
def disp_selected(choice):
    choice = tc.get()
# f1 Frame
f1 = Frame(root, borderwidth=8, relief=SUNKEN, bg="green")
f1.pack(side="top", fill="x")
heading = Label(f1, text="College Admission records",
                font="normal 25 bold underline", fg="yellow", bg="green")
heading.pack()
# f2 Frame
f2 = Frame(root, borderwidth=5, relief=RAISED , border=10)
f2.pack(pady=10, padx=10, fill=BOTH)
f2.configure(bg="white")


# Labels
ID = Label(f2, text="ID", font="normal 12 italic")
ID.grid(row=1, column=0)
ID.configure(bg="white", fg="black")
Name = Label(f2, text="Student name", font="normal 12 italic")
Name.grid(row=2, column=0)
Name.configure(bg="white", fg="black")

age = Label(f2, text="Age", font="normal 12 italic")
age.grid(row=3, column=0)
age.configure(bg="white", fg="black")

gender = Label(f2, text="Gender", font="normal 12 italic")
gender.grid(row=4, column=0)
gender.configure(bg="white", fg="black")

PCMaggregate = Label(f2, text="PCM Aggregate", font="normal 12 italic")
PCMaggregate.grid(row=5, column=0)
PCMaggregate.configure(bg="white", fg="black")

category = Label(f2, text="Category", font="normal 12 italic")
category.grid(row=6, column=0)
category.configure(bg="white", fg="black")

Jee = Label(f2, text="JEE MAINS SCORE", font="normal 12 italic")
Jee.grid(row=7, column=0)
Jee.configure(bg="white", fg="black")

Check = Checkbutton(f2, variable=IntVar(),
                    text="I accept all terms and conditions",font="normal 12 italic")
Check.grid(row=8, column=0)
# Entries
IDval = Entry(f2, relief=RAISED, borderwidth=6,
              textvariable=IntVar(), font="normal 12 italic", width=40)
IDval.delete(0, 'end')
IDval.grid(row=1, column=1, pady=10, padx=10)
IDval.configure(bg="white", fg="black")
Nameval = Entry(f2, relief=RAISED, borderwidth=6,
                textvariable=StringVar(), font="normal 12 italic", width=40)
Nameval.grid(row=2, column=1, pady=10, padx=10)


ageval = Entry(f2, relief=RAISED, borderwidth=3, textvariable=IntVar(),
               font="normal 12 italic", width=40)
ageval.delete(0, "end")
ageval.grid(row=3, column=1, pady=10, padx=10)

stvar = StringVar()
genderval = ["Male", "Female"]
genders = OptionMenu(f2, stvar, *genderval)
genders.grid(row=4, column=1, pady=10, padx=10)
genders.config(width=35, font="normal 12 italic", relief=RAISED, borderwidth=5)
genders.configure(bg="white", fg="black")

PCMaggregateval = Entry(f2, relief=RAISED, borderwidth=3,
                        textvariable=IntVar(), font="normal 12 italic", width=40)
PCMaggregateval.delete(0, "end")
PCMaggregateval.grid(row=5, column=1, pady=10, padx=10)

tc = StringVar()
categoryv = ["General", "OBC", "SC", "ST"]
categoryval = OptionMenu(f2, tc, *categoryv, command=disp_selected)
categoryval.config(width=35, font="normal 12 italic",
                   relief=RAISED, borderwidth=5)
categoryval.grid(row=6, column=1, pady=10, padx=10)

Jeeval = Entry(f2, relief=RAISED, borderwidth=3,
               textvariable=IntVar(), font="normal 12 italic", width=40)
Jeeval.delete(0, "end")
Jeeval.grid(row=7, column=1, pady=10, padx=10)


def updater():
    if(IDval.get() == ""):
        tmsg.showerror("Error", "Please Fill ID for which you want to Update")
    else:
        con = mysql.connect(host="localhost", user="root",
                            password="", database="admission_records")
        cursor = con.cursor()
        cursor.execute("update student set Name='"+Nameval.get()+"',Age='"+ageval.get()+"',Gender='"+stvar.get()+"',Category='" +
                       tc.get()+"',Jee_Score='"+Jeeval.get()+"',PCM_Aggregate='"+PCMaggregateval.get() + "' where ID='"+IDval.get()+"'")
        cursor.execute("commit")
        tmsg.showinfo("Updated", "Data Successfully updated")

# Light Mode


def LightMode(event):
    root.configure(borderwidth=6, bg="white")
    f2.configure(bg="white")
    Name.configure(bg="white", fg="black")
    age.configure(bg="white", fg="black")
    gender.configure(bg="white", fg="black")
    PCMaggregate.configure(bg="white", fg="black")
    Jee.configure(bg="white", fg="black")
    gender.config(bg="white", fg="black")
    category.config(bg="white", fg="black")
    ID.configure(bg="white", fg="black")
    # Entries
    Nameval.configure(bg="white", fg="black", border=5)
    ageval.configure(bg="white", fg="black", border=5)
    genders.configure(bg="white", fg="black", border=5)
    categoryval.config(bg="white", fg="black", border=5)
    PCMaggregateval.configure(bg="white", fg="black", border=5)
    Jeeval.configure(bg="white", fg="black", border=5)
    Dark.configure(text="Dark Mode", bg="black", fg="white")
    Dark.bind('<Button-1>', DarkMode)
    IDval.configure(bg="white", fg="black")
    f3.configure(bg="white")


def DarkMode(event):
    clr = ["white", "black"]
    root.configure(borderwidth=6, bg="black")
    f2.configure(bg="black")
    Name.configure(bg="black", fg="white")
    age.configure(bg="black", fg="white")
    gender.configure(bg="black", fg="white")
    PCMaggregate.configure(bg="black", fg="white")
    Jee.configure(bg="black", fg="white")
    gender.config(bg="black", fg="white")
    category.config(bg="black", fg="white")
    ID.configure(fg="white", bg="black")
    f3.configure(bg="black")
    # Entries
    Nameval.configure(bg="black", fg="white", border=5)
    ageval.configure(bg="black", fg="white", border=5)
    genders.configure(bg="black", fg="white", border=5)
    categoryval.config(bg="black", fg="white", border=5)
    PCMaggregateval.configure(bg="black", fg="white", border=5)
    Jeeval.configure(bg="black", fg="white", border=5)
    Dark.configure(text="Light Mode", bg="white", fg="black")
    IDval.configure(bg="black", fg="white")
    Dark.bind('<Button-1>', LightMode)


def deleter():
    if(IDval.get() == ""):
        tmsg.showerror("Error", "Please Fill ID for which you want to delete")
    else:
        con = mysql.connect(user="root", password="",
                            database="admission_records")
        cursor = con.cursor()
        cursor.execute("delete from student where ID=('"+IDval.get()+"')")
        cursor.execute("commit")
        tmsg.showinfo("Deleted", "Successfully Deleted!!!")


def submission():
    Check.select()
    if(Nameval.get() == ""):
        tmsg.showerror("Name Error", "Please Enter your name")
    elif(stvar.get() == ""):
        tmsg.showerror("Gender Error", "Please Enter your gender")
    elif(tc.get() == ""):
        tmsg.showerror("Category Error", "Please Enter your Category")
    elif(ageval.get() == "0" or ageval.get() == ""):
        tmsg.showerror("Age Error", "Please Enter your age correctly")
    elif(Jeeval.get() == "0" or Jeeval.get() == ""):
        tmsg.showerror("JEE Mains Score Error",
                       "Please Enter Your Valid Jee Mains Score")
    elif(PCMaggregateval.get() == "0" or PCMaggregateval.get() == ""):
        tmsg.showerror("PCM Aggregate Error",
                       "Please Enter your PCM aggregate")
    else:
        con = mysql.connect(host="localhost", user="root",
                            password="", database="admission_records")
        cursor = con.cursor()
        cursor.execute("insert into student values('"+IDval.get()+"','"+Nameval.get()+"','"+ageval.get() +
                       "','"+stvar.get()+"','"+tc.get()+"','"+Jeeval.get()+"','"+PCMaggregateval.get()+"')")

        cursor.execute("commit")

        tmsg.showinfo("Registered", "Registered Successfully")
        
f3 = Frame(root)
f3.pack(side=LEFT, anchor="w")
submit = Button(f3, text="Submit", command=submission,
                relief=RAISED, borderwidth=6, width=10, font="NORMAL 15 bold", bg="green", fg="white", pady=5)
submit.pack(padx=10, side=LEFT)

Delete = Button(f3, text="Delete", relief=RAISED, borderwidth=6, width=10, font="NORMAL 15 bold", bg="green", fg="white",
                pady=5, command=deleter)
Delete.pack(side=LEFT, padx=10)

Update = Button(f3, text="Update", bg="green", fg="white", relief=RAISED, font="NORMAL 15 bold", borderwidth=6, width=10,
                pady=5, command=updater)
Update.pack(side=LEFT, padx=10)
Dark = Button(f3, text="Dark Mode", relief=RAISED,borderwidth=6, width=10,
              bg="black", fg="white", font="normal 15 bold")
Dark.pack(side=LEFT, padx=10)
Dark.bind('<Button-1>', DarkMode)


root.mainloop()
