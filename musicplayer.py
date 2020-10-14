from tkinter import *
from tkinter import filedialog
from pygame import mixer
root = Tk()
class MusicPlayer:
    root.configure(bg='#fcfcec')
    #root.geometry("470x150")
    def __init__(self, window ):
        def des():
            mixer.music.stop()
            Load.destroy()
            Play.destroy()
            Pause.destroy()
            Stop.destroy()
            Close.destroy()
            root.destroy()

        window.title('Universal Music Player'); window.resizable(0,0)
        Load = Button(window, text = 'Load',  width = 10, command = self.load,bg='#4b7fa4',fg="#fcfcec",font=("times", 20))
        Play = Button(window, text = 'Play',  width = 10, command = self.play,bg='#4b7fa4',fg="#fcfcec",font=("times", 20))
        Pause = Button(window,text = 'Pause',  width = 10, command = self.pause,bg='#4b7fa4',fg="#fcfcec",font=("times", 20))
        Stop = Button(window ,text = 'Stop',  width = 10, command = self.stop,bg='#cb464e',fg="#fcfcec",font=("times", 20))
        Close = Button(window ,text = 'Close',  width = 10, command = des,bg='#cb464e',fg="#fcfcec",font=("times", 20))
        Load.place(x=900,y=20);Play.place(x=1050,y=20);Pause.place(x=1200,y=20);Close.place(x=1050,y=75)
        self.music_file = False
        self.playing_state = False
    def load(self):
        self.music_file = filedialog.askopenfilename()
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state = False
    def stop(self):
        mixer.music.stop()
#app= MusicPlayer(root)        

#root.mainloop()

#app= MusicPlayer(root)        
