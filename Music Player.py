from pydoc import plain
from struct import pack
from tkinter import *
import pygame
import os
from tkinter.filedialog import askdirectory #khandan file mp3 az dakhele system




#WINDOW
player = Tk()
player.title('Music Player')
player.geometry('600x600')

#pygame init
pygame.init()   #ba estefade az in method mitunim az emkanate pygame estefade konim
pygame.mixer.init()  #baraye ghesmate  pakhshe  Media az in dastur estefade mikonim 





playlist = Listbox()
playlist.pack()

def Play():
    pygame.mixer.music.load(playlist.get(ACTIVE))
    var.set(playlist.get(ACTIVE))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(volume.get())

def Stop():
    pygame.mixer.music.stop()

def Pause():
    pygame.mixer.music.pause()

def UnPause():
    pygame.mixer.music.unpause()

def ChangeVolume(a):
    a = volume.get()
    pygame.mixer.music.set_volume(a)

def Load():
    directory = askdirectory()
    os.chdir(directory)  #dadane masir
    music_list = os.listdir(directory)  #listi az musichaye entekhabie karbar 
    
    for item in music_list:
        if item.endswith('.mp3'):
            i = 0
            playlist.insert(i,item)
            i +=1




#btn

btn_play = Button(player, width=5, height=3,text='Play', command=Play)
btn_play.pack(fill = 'x')
btn_stop = Button(player, width=5, height=3, text='Stop', command=Stop)
btn_stop.pack(fill = 'x')
btn_pause = Button(player, width=5, height=3,text='Pause',command=Pause )
btn_pause.pack(fill = 'x')
btn_unpause = Button(player, width=5, height=3,text='unPause',command=UnPause )
btn_unpause.pack(fill = 'x')
btn_load = Button(player,  width=5, height=3,text='Load Music',command=Load )
btn_load.pack(fill = 'x')

#Volume
volume = Scale(player,from_=0, to_= 1, resolution=0.1, orient=HORIZONTAL, command= ChangeVolume)
volume.pack()

#music name
var = StringVar()
musictitle = Label(player, textvariable=var)
musictitle.pack()

#place

player.mainloop()