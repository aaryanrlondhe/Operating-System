from tkinter import *
from PIL import ImageTk,Image
def homi():
	root=Tk()
	root.configure(bg='#fcfcec')

	def cal():
		from calend import cale
		cale()
	
	def calsi():
		from calulator import love
		love()	
	def alar():
		from alarm import alr 
		alr()

	def web():
		from browser import bro
		bro()

	def toe():
		import tic 	
		execfile('tic.py')
	def sound():
		from musicplayer import MusicPlayer
		app= MusicPlayer(root)


	myimg=ImageTk.PhotoImage(Image.open("calender2.png"))
	myLabel= Label(root,text="Calender",fg="#4b7fa4",bg='#fcfcec',font=("times",12,"bold"))
	mybutton=Button(root,image=myimg,bg='#fcfcec',command=cal)
	mybutton.grid(row=0,column=0,padx=25,pady=8)
	myLabel.grid(row=1,column=0,pady=2)
	myimg1=ImageTk.PhotoImage(Image.open("calculator2.png"))
	myLabel1= Label(root,text="Calculator",fg="#4b7fa4",bg='#fcfcec',font=("times",12,"bold"))
	mybutton1=Button(root,image=myimg1,bg='#fcfcec',command=calsi)
	mybutton1.grid(row=2,column=0,padx=25,pady=8)
	myLabel1.grid(row=3,column=0,pady=2)
	myimg2=ImageTk.PhotoImage(Image.open("browser2.png"))
	myLabel2= Label(root,text="Browser",fg="#4b7fa4",bg='#fcfcec',font=("times",12,"bold"))
	mybutton2=Button(root,image=myimg2,bg='#fcfcec',command=web)
	mybutton2.grid(row=4,column=0,padx=25,pady=8)
	myLabel2.grid(row=5,column=0,pady=2)
	myimg3=ImageTk.PhotoImage(Image.open("alarm2.png"))
	myLabel3= Label(root,text="Alarm",fg="#4b7fa4",bg='#fcfcec',font=("times",12,"bold"))
	mybutton3=Button(root,image=myimg3,bg='#fcfcec',command=alar)
	mybutton3.grid(row=6,column=0,padx=25,pady=8)
	myLabel3.grid(row=7,column=0,pady=2)
	myimg4=ImageTk.PhotoImage(Image.open("tic2.png"))
	myLabel4= Label(root,text="Tic-Tac-Toe",fg="#4b7fa4",bg='#fcfcec',font=("times",12,"bold"))
	mybutton4=Button(root,image=myimg4,bg='#fcfcec',command=toe)
	mybutton4.grid(row=8,column=0,padx=25,pady=8)
	myLabel4.grid(row=9,column=0,pady=2)
	myimg5=ImageTk.PhotoImage(Image.open("music2.png"))
	myLabel5= Label(root,text="Music Player",fg="#4b7fa4",bg='#fcfcec',font=("times",12,"bold"))
	mybutton5=Button(root,image=myimg5,bg='#fcfcec',command=sound)
	mybutton5.grid(row=10,column=0,padx=25,pady=8)
	myLabel5.grid(row=11,column=0,pady=2)
	root.attributes('-fullscreen', True)
	root.title('Login')
	root.mainloop()

homi()	
