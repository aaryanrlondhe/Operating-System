import youtube_dl
import urllib
import shutil
import webbrowser
import tkinter
from tkinter import filedialog
from tkinter import *
import webbrowser
#rom googlesearch import search 
def bro():
	root=Tk()
	root.geometry("630x150")
	root.title('Browser')
	root.configure(bg='#fcfcec')	
	amazoni=PhotoImage(file="b.png")
	youtubei=PhotoImage(file="c.png")
	L1=Label(root,text="Enter What To Search :- ",bg='#fcfcec',fg="#4b7fa4",font=("times", 20))		
	e =Entry(root,width=100,bg="white",fg="#cb464e",border=10)
	def pas():
		for j in search(e.get(),tld="co.in", num=6, stop=6, pause=2): 
			webbrowser.open(j)
	
	mybutton=Button(root,text="Search",bg='#cb464e',fg="#fcfcec",command=pas,font=("times",20))
	L1.grid(row=0,column=0)
	e.grid(row=1,column=0)
	mybutton.grid(row=2,column=0)
	root.mainloop()
bro()	