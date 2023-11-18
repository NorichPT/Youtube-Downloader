import tkinter
import customtkinter
from pytube import YouTube

def Download():
    try:
        yturl = link.get()
        ytobj = YouTube(yturl, on_progress_callback=on_progress)
        video = ytobj.streams.get_highest_resolution()
        title.configure(text=ytobj.title, text_color="white")
        video.download()
        finishlabel.configure(text="Download completo!", text_color="green")
    except:
        finishlabel.configure(text="O link do youtube é inválido", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloader = total_size - bytes_remaining
    percentage_of_completion = bytes_downloader / total_size * 100
    per = str(int(percentage_of_completion))
    percentage.configure(text=per + "%")
    percentage.update()

    progressbar.set(float(percentage_of_completion) / 100)

# DEFINIÇÕES SISTEMA
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Primeiro programa")

# ui elements
title = customtkinter.CTkLabel(app, text="Escreve o link do youtube")
title.pack(padx=10, pady=10)

# link input
url = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url)
link.pack()

#finish download
finishlabel = customtkinter.CTkLabel(app, text="")
finishlabel.pack()

#progress download
percentage = customtkinter.CTkLabel(app, text="0%")
percentage.pack()

progressbar = customtkinter.CTkProgressBar(app, width=400)
progressbar.set(0)
progressbar.pack(padx=10, pady=10)


# download button
download = customtkinter.CTkButton(app, text="Download", command=Download)
download.pack(padx=10, pady=10)

# run app
app.mainloop()
