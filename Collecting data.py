#Collecting data 

from tkinter import *


class Data_GUI:
    def __init__(self,parent): 
        main = Frame(parent)

        Processing.choice_list()
       
        Label(main,text=" Collecting Personal Data").grid(row=0,column=0,padx=10,pady=30,sticky=E)

        Button(main,text="Show All").grid(row=0,column=1,pady=30,padx=10)

        Label(main,text="First Name: ").grid(row=1,column=0)
        Entry(main).grid(row=1,column=1)
        Label(main,text="Age: ").grid(row=2,column=0)
        Entry(main).grid(row=2,column=1)
        Label(main,text="Do you have a mobile Phone?").grid(row=3,column=0,padx=5,pady=10)
        

        r = 4
        for i in(Processing.yeah_na):
            Radiobutton(main, text=i, value=i).grid(column=1, row=r, sticky=W,pady=5)
            r += 1

        main.grid()
        Button(parent,text="Enter Data",command=Processing.user_data).grid(padx=5,pady=15)
        
      

        
class Processing():
    def choice_list():
        Processing.yeah_na = ["Yes", "No"]
    
    def user_data():
        name =[]
        age=[]
        phone=[]


    

        




root = Tk()
root.title("Data Collector")
Data_GUI(root)
root.mainloop()
