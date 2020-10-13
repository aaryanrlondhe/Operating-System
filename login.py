from tkinter import *
from PIL import ImageTk,Image
def log():
  root=Tk()
  root.configure(bg='#fcfcec')
  root.iconbitmap('image.ico')
  #r'images/melody.ico'
  def pin():
    if e.get()=="123":
      mylabel2.destroy()
      myLabel.destroy()
      e.destroy()
      mybutton.destroy()
      root.destroy()
      from home import homi
      homi()
    else :
      print('Not Allowed')

  my_img=ImageTk.PhotoImage(Image.open("image.ico"))
  mylabel2=Label(image=my_img)
  mylabel2.grid(row=0,column=4,padx=650,pady=60)    
  myLabel= Label(root,text="Enter Pin",bg='#fcfcec',fg="#4b7fa4",font=("times", 20))
  myLabel.grid(row=1,column=4,padx=400,pady=20)
  e =Entry(root,width=50,bg="white",fg="black",border=10)
  e.grid(row=2,column=4,pady=20)
  mybutton=Button(root,text="Login",bg='#cb464e',fg="#fcfcec",command=pin,font=("times",20))
  mybutton.grid(row=3,column=4,pady=20)
  root.attributes('-fullscreen', True)
  root.title('Login')
  root.mainloop()

