from tkinter import *
import datetime
import time
import winsound
def alr():

    def alarm(set_alarm_timer):
        while True:
            time.sleep(1)
            current_time = datetime.datetime.now()
            now = current_time.strftime("%H:%M:%S")
            date = current_time.strftime("%d/%m/%Y")
            if now == set_alarm_timer:
                print("Time to Wake up")
                winsound.PlaySound("sound.mp3",winsound.SND_ASYNC)
                break
     
    def actual_time():
        set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
        alarm(set_alarm_timer)
     
    clock = Tk()
    clock.configure(bg='#fcfcec')
    clock.title("Alarm Clock")
    clock.geometry("400x150")
    time_format=Label(clock, text= "Enter Time in 24 hour Format!", fg="#4b7fa4",bg="#fcfcec",font=("Arial Bold",13)).place(x=90,y=120)
    addTime = Label(clock,text = "Hour  Min   Sec",font=60, fg="#cb464e",bg="#fcfcec").place(x = 201)
    setYourAlarm = Label(clock,text = "Time to Wake Up",fg="#4b7fa4",bg="#fcfcec",font=("Arial Bold",13,"bold")).place(x=0, y=29)
     
    # The Variables we require to set the alarm(initialization):
    hour = StringVar()
    min = StringVar()
    sec = StringVar()
     
    #Time required to set the alarm clock:
    hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 20).place(x=180,y=30)
    minTime= Entry(clock,textvariable = min,bg = "pink",width = 20).place(x=250,y=30)
    secTime = Entry(clock,textvariable = sec,bg = "pink",width = 20).place(x=290,y=30)
     
    #To take the time input by user:
    submit = Button(clock,text = "Set Alarm",fg="#fcfcec",bg="#cb464e",width = 10,command = actual_time,font=("times",12,"bold")).place(x =150,y=70)
     
    clock.mainloop()
    #Execution of the window.
     

    
