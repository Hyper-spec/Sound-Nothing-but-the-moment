from pygame import mixer
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import filedialog

current_volume = float(0.5)

#Functions
def play_song():
    filename = filedialog.askopenfilename(initialdir="C:/", title="Please select a music file")
    current_song = filename
    song_title = filename.split("/")
    song_title = song_title[-1]
    print(song_title)
    try:
        mixer.init()
        mixer.music.load(current_song)
        mixer.music.set_volume(current_volume)
        mixer.music.play()
        song_title_label.config(fg="green", text=f"Now playing: {song_title}")
        volume_label.config(fg="green", text=f"Volume: {current_volume}")

    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="Error playing track")


def reduce_volume():
    try:
        global current_volume
        if current_volume <= 0:
            volume_label.config(fg="red", text="Volume: Muted")
            return
        current_volume = current_volume - float(0.1)
        current_volume = round(current_volume, 1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="green", text=f"Volume: {current_volume}")
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="Track hasn´t been selected yet")


def increase_volume():
    try:
        global current_volume
        if current_volume >= 1:
            volume_label.config(fg="green", text="Volume: Max")
            return
        current_volume = current_volume + float(0.1)
        current_volume = round(current_volume, 1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="green", text=f"Volume: {str(current_volume)} ")
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="Track hasn´t been selected yet")


def pause():
    try:
        mixer.music.pause()
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="Track hasn´t been selected yet")


def resume():
    try:
        mixer.music.unpause()
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="Track hasn´t been selected yet")


def rewind():
    try:
        mixer.music.rewind()
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="Track hasn´t been selected yet")




#Main Screen
master = Tk()
master.title('Sound+')

#Labels
Label(master, text="Sound+ / Nothing but the moment", font=("Bahnschrift", 22), fg="dodgerblue",).grid(sticky="N", row=0, padx=130, pady=10)
Label(master, text="Select the song you would like to play", font=("Bahnschrift", 14), fg="dodgerblue").grid(sticky="N", row=1, pady=6)
song_title_label = Label(master, font=('Bahnschrift', 14))
song_title_label.grid(sticky="N", row=6, pady=14)


volume_label = Label(master, font=("Bahnschrift", 14))
volume_label.grid(sticky="N", row=9)


#Buttons
Button(master, text="Select Song", font=('Bahnschrift', 12), fg="black", bg="lightgray", command=play_song) .grid(row=4, sticky="N", pady=14)
Button(master, text="Pause", font=("Bahnschrift", 12),  bg="lightgray", width=9, command=pause).grid(sticky="E", row=8)
Button(master, text="Resume", font=("Bahnschrift", 12), bg="lightgray", width=9, command=resume).grid(sticky="W", row=8)
Button(master, text="Rewind", font=("Bahnschrift", 12), bg="lightgray", width=9, command=rewind).grid(sticky="N", row=8, pady=12)
Button(master, text="-", font=("Bahnschrift", 12), width=9, bg="dodgerblue", command=reduce_volume).grid(sticky="W", row=9)
Button(master, text="+", font=("Bahnschrift", 12), width=9, bg="dodgerblue", command=increase_volume).grid(sticky="E", row=9)


master.mainloop()
#To show the menu

