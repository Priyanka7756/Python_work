from tkinter import Label,Tk
import time

app_window=Tk()
app_window.title("DIGITAL CLOCK")
app_window.geometry("450x150")
app_window.resizable(1,1)

text_font=("Boulder", 68, "bold")
background= "light green"
foreground="blue"
bordr_width=25

label=Label(app_window,font=text_font,bg=background,fg=foreground,bd=bordr_width)
label.grid(row=0,column=1)

def digitalclock():
    live_time=time.strftime("%H:%M:%S")
    label.config(text=live_time)
    label.after(100,digitalclock)

digitalclock()

app_window.mainloop()


