#Collecting data 


from tkinter import *


class Data_GUI:
    def __init__(self,parent): 
        main = Frame(parent)

       

        
        Processing.Lists()
       
        Label(main,text=" Collecting Personal Data").grid(row=0,column=0,padx=10,pady=30,sticky=E)
        Button(main,text="Show All").grid(row=0,column=1,pady=30,padx=10)
        Label(main,text="First Name: ").grid(row=1,column=0)
        Data_GUI.name = Entry(main)
        Data_GUI.name.grid(row=1,column=1)
        Label(main,text="Age: ").grid(row=2,column=0)
        
        Data_GUI.age = Entry(main)
        Data_GUI.age.grid(row=2,column=1)
        Label(main,text="Do you have a mobile Phone?").grid(row=3,column=0,padx=5,pady=10)
        

        r = 3
        for i in(Processing.yeah_na):
            Radiobutton(main, text=i, value=i, variable=Processing.selected_option).grid(column=1, row=r, sticky=W,pady=5)
            r += 1

        main.grid()
        Button(parent,text="Enter Data",command=Processing.user_data).grid(padx=5,pady=15)
        
      

        
class Processing():
    def Lists():
        Processing.name =[]
        Processing.age = []
        Processing.phone = [] 
        Processing.selected_option = StringVar()
        Processing.yeah_na = ["Yes", "No"]

    
    def user_data():
        print("****")


        Processing.name.append(Data_GUI.name.get())
        print(Processing.name)


        Processing.age.append(Data_GUI.age.get())
        print(Processing.age)

        Processing.phone.append(Processing.selected_option.get())
        print(Processing.phone)


        
        

    
        




    

        




root = Tk()
root.title("Data Collector")
Data_GUI(root)
root.mainloop()
