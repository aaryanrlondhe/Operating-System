from tkinter import *
from PIL import ImageTk,Image
import calendar 
def cale():
	root=Tk()
	def calen():
		root.configure(bg='#fcfcec')
		firstnum=e.get()
		fnum=int(firstnum)
		mylabel1=Label(root,text=calendar.calendar(fnum),font=("Consolas 10 bold"),bg="#fcfcec",fg="#cb464e")
		mylabel1.grid(row=1,column=0, padx = 20)

	myLabel= Label(root,text="Enter Year :- ",bg='#fcfcec',fg="#4b7fa4",font=("times", 20))
	myLabel.grid(row=0,column=1)
	e =Entry(root,width=50,bg="white",fg="black",border=10)
	e.grid(row=0,column=2)
	mybutton=Button(root,text="Go",bg='#cb464e',fg="#fcfcec",command=calen,font=("times",15))
	mybutton.grid(row=0,column=3)
	root.title('Calender')
	root.mainloop()
