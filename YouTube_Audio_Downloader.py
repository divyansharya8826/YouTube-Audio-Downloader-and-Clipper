from tkinter import (Button, Canvas, PhotoImage, StringVar, Tk, ttk , filedialog)
from pytube import YouTube
from moviepy.editor import AudioFileClip
import os

root = Tk()
root.geometry("800x600")
root.resizable(width=1024,height=768)   # type: ignore
root.title("YouTube Audio Cliper")
bg = PhotoImage(file = "/Users/divyansharya/Projects/Divyansh/Python/i.ppm")
bg2 = PhotoImage(file = "/Users/divyansharya/Projects/Divyansh/Python/youtubevanced.png")
canvas1 = Canvas(root,width=1024,height=768)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image(0 , 0 , image = bg , anchor = "nw")
canvas1.create_image(0,-65,image = bg2 , anchor = "nw" )

l1 = canvas1.create_text((400,50),text = "Youtube Audio Cliper", font =('Helvetica',30,'bold','underline'),fill="red")
##enter link
link = StringVar()

l2 = canvas1.create_text((400,115), text = 'Paste Link Here:', font =('arial',20,'bold'),fill="black")
link_enter = ttk.Entry(root, width = 80,textvariable = link).place(x = 32, y = 125)

#set time duration for cliping
l3 = canvas1.create_text((100,215), text='Start', font=('arial',20,'bold'),fill='red')
Start = StringVar()
start_time = ttk.Entry(root, width=10,textvariable=Start).place(x=150 , y=200)
l4 = canvas1.create_text((550,215), text='End', font =('arial',20,'bold'),fill='red')
End = StringVar()
end_time = ttk.Entry(root, width=10 ,textvariable=End).place(x=600, y=200)

#path where to save the audio
folder=None
def get_save_path():
   global folder
   yt = YouTube(str(link.get()))
   folder = filedialog.asksaveasfilename(initialdir="/",initialfile=yt.title,title="save the file",defaultextension=".mp3")
progress = ttk.Progressbar(root, orient='horizontal', length=400, mode='determinate')
progress.place(x=200,y=360)

def clip_audio():
    import time
    for i in range(10,110,10): 
        progress['value'] = i
        root.update_idletasks()
        time.sleep(1)
    
    if (progress['value']==100):
        l5 = canvas1.create_text((400,400), text = 'DOWNLOADED', font = ('arial',15,'bold'), fill ='red')
    yt = YouTube(str(link.get()))
    audio = yt.streams.filter(only_audio=True,file_extension='mp4',abr='128kbps').first()
    clip = AudioFileClip(audio.url) # type:ignore
    clip = clip.subclip(Start.get(),End.get())
    out_file = clip.write_audiofile(filename = folder,codec='libmp3lame' , fps=44100) #type:ignore

clip = Button(root,text='CLIP AND\nDOWNLOAD',font=('arial',15,'bold'),background="red",padx = 10,command=lambda: [get_save_path(),clip_audio()],pady=3)
clip.place(x=340,y=240)

def audio():
    import time
    for i in range(10,110,10): 
        progress['value'] = i
        root.update_idletasks()
        time.sleep(1)

    if (progress['value']==100):
        l5 = canvas1.create_text((400,400), text = 'DOWNLOADED', font = ('arial',15,'bold'), fill ='red')
    yt = YouTube(str(link.get()))
    audio = yt.streams.filter(only_audio=True,file_extension='mp4',abr='128kbps').first()
    out_file = audio.download(filename=folder) # type:ignore

Download = Button(root,text = 'DOWNLOAD', font = ('arial',15,'bold') ,background = "blue", padx = 10, command =lambda: [get_save_path(),audio()],pady=5).place(x=340,y=300)
root.mainloop()