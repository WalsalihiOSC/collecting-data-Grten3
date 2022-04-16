#Collecting data 



from tkinter import *


class Data_GUI:
    def __init__(self,parent): 
        Data_GUI.main_1 = Frame(parent)
        Data_GUI.main_1.grid()
       

        
        Processing.setup(self)
       
        Label(Data_GUI.main_1,text=" Collecting Personal Data").grid(row=0,column=0,padx=10,pady=30,sticky=E)
        Button(Data_GUI.main_1,text="Show All",command=Processing.show).grid(row=0,column=1,pady=30,padx=10)
        Label(Data_GUI.main_1,text="First Name: ").grid(row=1,column=0,sticky=E)
        Data_GUI.name = Entry(Data_GUI.main_1)
        Data_GUI.name.grid(row=1,column=1)
        Label(Data_GUI.main_1,text="Age: ").grid(row=2,column=0,sticky=E)
        
        Data_GUI.age = Entry(Data_GUI.main_1)
        Data_GUI.age.grid(row=2,column=1)
        Label(Data_GUI.main_1,text="Do you have a mobile Phone?").grid(row=3,column=0,padx=5,pady=10)

       

        r = 3
        for i in(Processing.yeah_na):
            Radiobutton(Data_GUI.main_1, text=i, value=i, variable=Processing.selected_option).grid(column=1, row=r, sticky=W,pady=5)
            r += 1

    
        Data_GUI.Enter_data = Button(Data_GUI.main_1,text="Enter Data",command=Processing.user_data)
        Data_GUI.Enter_data.grid(padx=5,pady=15,columnspan=2)
        Data_GUI.Error_message = Label(Data_GUI.main_1,fg="red")
        Data_GUI.Error_message.grid(padx=5,pady=5,columnspan=2)

#Show DATA Frame ********

        Data_GUI.main_2 = Frame(parent)
        Data_GUI.main_2.grid()
        Data_GUI.main_2.grid_forget()

        Label(Data_GUI.main_2,text="Displaying Personal Data").grid(row=0,column=0,padx=10,pady=30,sticky=E)
        Button(Data_GUI.main_2,text="Add new Person",command=Processing.enter).grid(row=0,column=1,pady=30,padx=10)

        Label(Data_GUI.main_2,text="First Name: ").grid(row=1,column=0,sticky=E)
        Data_GUI.show_name = Label(Data_GUI.main_2, text="")
        Data_GUI.show_name.grid(row=1,column=1)

        Label(Data_GUI.main_2,text="Age: ").grid(row=2,column=0,sticky=E)
        Data_GUI.show_age = Label(Data_GUI.main_2, text= "")
        Data_GUI.show_age.grid(row=2,column=1)

        Label(Data_GUI.main_2,text="Do you have a mobile Phone?").grid(row=3,column=0,padx=5,pady=10,columnspan=2)

        Button(Data_GUI.main_2,text="Previous",command=Processing.previous).grid(row=4,column=0,sticky=W,padx=10)
        Button(Data_GUI.main_2,text="Next",command=Processing.next).grid(row=4,column=1,sticky=E,padx=10)

        
        
        
      

        
class Processing:
    def setup(self):
        Processing.i = 0 
        Processing.data =[]
        Processing.selected_option = StringVar()
        Processing.yeah_na = ["Yes", "No"]

    
    def user_data():
        if len(Data_GUI.name.get()) == 0 or len(Data_GUI.age.get()) == 0 or len(Processing.selected_option.get()) == 0: 
            Data_GUI.Error_message.configure(text = "*Please fill in all the info")

        else:
            Data_GUI.Error_message.configure(text = "                              ")

            Processing.data.append(Data_GUI.name.get())
            Processing.data.append(Data_GUI.age.get())  
            Processing.data.append(Processing.selected_option.get())
            print(Processing.data)

            Data_GUI.name.delete(0,END)
            Data_GUI.age.delete(0,END)
            Processing.selected_option.set(0)



    def show():
        Data_GUI.main_1.grid_forget()
        Data_GUI.main_2.grid()
        Data_GUI.show_name.configure(text=Processing.data[Processing.i])
        Data_GUI.show_age.configure(text=Processing.data[Processing.i + 1])

    def enter():
        Data_GUI.main_2.grid_forget()
        Data_GUI.main_1.grid()

    def next():
        Processing.i += 3
        Data_GUI.show_name.configure(text=Processing.data[Processing.i])
        Data_GUI.show_age.configure(text=Processing.data[Processing.i + 1])

    def previous():
        Processing.i -= 3
        Data_GUI.show_name.configure(text=Processing.data[Processing.i])
        Data_GUI.show_age.configure(text=Processing.data[Processing.i + 1])


        

        


        
        







root = Tk()
root.title("Data Collector")
root.geometry('395x310')
Data_GUI(root)
root.mainloop()
