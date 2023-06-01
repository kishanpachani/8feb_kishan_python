
import tkinter 
from tkinter import DoubleVar,ttk,messagebox 


screen=tkinter.Tk()
screen.geometry('500x400')
screen.title('Registration Form')
screen.config(bg='#ddd')

tkinter.Label(text='Name *',font='bold',bg='#ddd',fg='black').grid(row=0,column=2,sticky='W') 
tkinter.Label(text='Contact *',font='bold',bg='#ddd',fg='black').grid(row=3,column=2,sticky='W') 
tkinter.Label(text='Email *',font='bold',bg='#ddd',fg='black').grid(row=5,column=2,sticky='W') 

tkinter.Entry().grid(row=0,column=4,sticky='W') 
tkinter.Entry().grid(row=3,column=4,sticky='W') 
tkinter.Entry().grid(row=5,column=4,sticky='W') 

tkinter.Label(text='Gender *',font='bold',bg='#ddd',fg='black').grid(row=7,column=2,sticky='W') 
tkinter.Radiobutton(value=0, text='Male',font=' bold',bg='#ddd',fg='black').grid(row=7,column=3,sticky='W') 
tkinter.Radiobutton(value=1, text='Female',font=' bold',bg='#ddd',fg='black').grid(row=7,column=4,sticky='W')  

city=['Ahmedabad','Surat','Baroda','Rajkot','Jamnagar'] 
tkinter.Button(command=2,text='Submit',font='bold').place(x=200,y=200) 
tkinter.Label(text='City *',font='bold',bg='#ddd',fg='black').grid(row=9,column=2,sticky='W')
city=['Ahmedabad','Surat','Baroda','Rajkot','Jamnagar'] 
ttk.Combobox(values=city).grid(row=9,column=4) 

State=['gujrat','rajasthan','bihar','punjab',] 
tkinter.Button(command=2,text='Register',font='bold').place(x=200,y=200) 
tkinter.Label(text='State *',font='bold',bg='#ddd',fg='black').grid(row=10,column=2,sticky='W')
State=['gujrat','rajasthan','bihar','punjab'] 
ttk.Combobox(values=State).grid(row=10,column=4) 
  
  
def btnclick():
 
           messagebox.askyesnocancel("Download","Do you want to continue?") 
  
l2=tkinter.Label().grid(row=10,column=0) 
  
def show2(): 
  sel = "VerticalScaleValue="+str(nis.get())
  l2.config(text=sel, font=("Courier",14)) 
N=DoubleVar()


screen.mainloop()

