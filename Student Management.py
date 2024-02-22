from tkinter import *
from tkinter import ttk
import sqlite3

class Student():

    def __init__(self,main):
        
        self.main=main
        self.T_Frame=Frame(self.main, height=40, width=1300, background="#CAE1FF" ).pack()
        self.Title=Label(self.T_Frame, text="Student Management System", font="arial 20 bold", width=1200, background="#CAE1FF" ).pack()


        self.Frame_1=Frame(self.main,height=570, width=550, background="#CAE1FF", border=2, relief=GROOVE )
        self.Frame_1.pack(side=LEFT)
        self.Frame_1.pack_propagate(0)

        Label(self.Frame_1, text="Student Details",background="#CAE1FF",font="arial 12 bold").place(x=20,y=20)
        
        self.Id=Label(self.Frame_1, text="Id",background="#CAE1FF",font="arial 11 bold")
        self.Id.place(x=40,y=60)
        
        self.Id_entry=Entry(self.Frame_1, width=40)
        self.Id_entry.place(x=120,y=60)

        self.Name=Label(self.Frame_1, text="Name",background="#CAE1FF",font="arial 11 bold")
        self.Name.place(x=40,y=100)

        self.Name_entry=Entry(self.Frame_1, width=40)
        self.Name_entry.place(x=120,y=100)
        
        self.Age=Label(self.Frame_1, text="Age",background="#CAE1FF",font="arial 11 bold")
        self.Age.place(x=40,y=140)

        self.Age_entry=Entry(self.Frame_1, width=40)
        self.Age_entry.place(x=120,y=140)

        self.Dob=Label(self.Frame_1, text="DOB",background="#CAE1FF",font="arial 11 bold")
        self.Dob.place(x=40,y=180)

        self.Dob_entry=Entry(self.Frame_1, width=40)
        self.Dob_entry.place(x=120,y=180)

        self.Gender=Label(self.Frame_1, text="Gender",background="#CAE1FF",font="arial 11 bold")
        self.Gender.place(x=40,y=220)

        self.Gender_entry=Entry(self.Frame_1, width=40)
        self.Gender_entry.place(x=120,y=220)

        self.City=Label(self.Frame_1, text="City",background="#CAE1FF",font="arial 11 bold")
        self.City.place(x=40,y=260)

        self.City_entry=Entry(self.Frame_1, width=40)
        self.City_entry.place(x=120,y=260)

  #--------------------------------BUTTON--------------------------------------#
        
        self.button_Frame=Frame(self.Frame_1, height=250, width=250, relief=GROOVE, bd=2, background="#BCD2EE")
        self.button_Frame.place(x=75, y=320)


        self.Add=Button(self.button_Frame,text="Add",width=35, font="arial 11 bold", command=self.add_entry)
        self.Add.pack()
        self.Delete=Button(self.button_Frame,text="Delete", width=35, font="arial 11 bold", command=self.Delete)
        self.Delete.pack()
        self.Update=Button(self.button_Frame,text="Update", width=35, font="arial 11 bold", command=self.Update)
        self.Update.pack()
        self.Clear=Button(self.button_Frame,text="Clear", width=35, font="arial 11 bold", command=self.Clear)
        self.Clear.pack()
        
        
        self.Frame_2=Frame(self.main,height=570, width=750, background="#CAE1FF",bd=2, relief=GROOVE )
        self.Frame_2.pack(side=RIGHT)

        self.tree=ttk.Treeview(self.Frame_2, columns=("c1", "c2", "c3", "c4", "c5", "c6"), show="headings", height=30)
    
        self.tree.column("#1", anchor="center", width=50)
        self.tree.heading("#1", text="ID")

        self.tree.column("#2", anchor="center")
        self.tree.heading("#2", text="Name")

        self.tree.column("#3", anchor="center", width=110)
        self.tree.heading("#3", text="Age")

        self.tree.column("#4", anchor="center", width=115)
        self.tree.heading("#4", text="DOB")

        self.tree.column("#5", anchor="center", width=110)
        self.tree.heading("#5", text="Gender")

        self.tree.column("#6", anchor="center")
        self.tree.heading("#6", text="City")
        self.tree.pack()

    def add_entry(self):
           id=self.Id_entry.get()
           name=self.Name_entry.get()
           age=self.Age_entry.get()
           dob=self.Dob_entry.get()
           gender=self.Gender_entry.get()
           city=self.City_entry.get()
           c=sqlite3.connect("Student.db")
           cursers=c.cursor()
           cursers.execute("INSERT INTO Student(ID, NAME, AGE, DOB, GENDER, CITY) values(?,?,?,?,?,?)", (id,name,age,dob,gender,city))
           c.commit()
           c.close()
           print("Values Added")
           self.tree.insert("", index=0, values=(id,name,age,dob,gender,city))

    def Delete(self):
           item= self.tree.selection()[0]
           selected_item=self.tree.item(item)["values"][0]
           c=sqlite3.connect("Student.db")
           cursers=c.cursor()
           cursers.execute("DELETE FROM Student WHERE ID={}".format(selected_item))
           c.commit()
           c.close()
           self.tree.delete(item)
           print("Vlaue Deleted")


    def Update(self):
           id=self.Id_entry.get()
           name=self.Name_entry.get()
           age=self.Age_entry.get()
           dob=self.Dob_entry.get()
           gender=self.Gender_entry.get()
           city=self.City_entry.get()
           item= self.tree.selection()[0]
           selected_item=self.tree.item(item)["values"][0]
           c=sqlite3.connect("student.db")
           cursers=c.cursor()
           cursers.execute("UPDATE Student SET ID=?, NAME=?, AGE=?, DOB=?, GENDER=?, CITY=? WHERE ID=?",(selected_item, name, age, dob, gender, city, selected_item))
           c.commit()
           c.close()
           print("values Updated")
           self.tree.item(item, values=(id,name,age,dob,gender,city))


    def Clear(self):
           self.Id_entry.delete(0,END)
           self.Name_entry.delete(0,END)
           self.Age_entry.delete(0,END)
           self.Dob_entry.delete(0,END)
           self.Gender_entry.delete(0,END)
           self.City_entry.delete(0,END)
           print("Values Cleared")
    

main=Tk()

main.title("Student Management System")

main.geometry("1300x600")


Student(main)

mainloop()
