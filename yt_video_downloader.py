from pytube import YouTube
import tkinter as tk

root = tk.Tk()

root.geometry('1024x700')
root.title('BG_VIDEO_DOWNLOADER')

label = tk.Label(root, text="WELCOME TO BG VIDEO DOWNLOADER!", font=('Arial', 30))
label.pack(padx=20, pady=20)

e = tk.Entry(root, width=100, borderwidth=7)
e.pack()
e.insert(0, 'Please enter video link: ')

clicked = tk.StringVar()
clicked.set("low quality")

drop = tk.OptionMenu(root, clicked, "low quality", "high quality", "audio only")
drop.place(x=465, y=150)

def Myclick():
    quality = clicked.get()
    mylabel = tk.Label(root, text='Video link submitted successfully!', font=('Arial', 25))
    mylabel.place(x=300, y=400)
    if quality == "low quality":
            vid = e.get()
            vid_link = vid.replace('Please enter video link: ', '')
            yt = YouTube(vid_link)
            video = yt.streams.get_lowest_resolution()
            video.download('bg video download')
    if quality == "high quality":
        vid = e.get()
        vid_link = vid.replace('Please enter video link: ', '')
        yt = YouTube(vid_link)
        video = yt.streams.get_highest_resolution()
        video.download('bg video download')
    if quality == "audio only":
        vid = e.get()
        vid_link = vid.replace('Please enter video link: ', '')
        yt = YouTube(vid_link)
        video = yt.streams.get_audio_only()
        video.download('bg video download')

    completed_label = tk.Label(root, text='Video downloaded successfully!', font=('Arial', 25))
    completed_label.place(x=320, y=500)


button = tk.Button(root, text='SUBMIT', font=('Arial', 20), command=Myclick)
button.place(x=455, y=300)

def exit():
    root.destroy()

exit_button = tk.Button(root, text='EXIT', font=('Arial', 20), command=exit)
exit_button.place(x=475, y=600)

root.mainloop()
