from tkinter import*
import random
window=Tk()
window.title("Choice.exe")
window.geometry("600x700")
window.config(background="yellow")
label=Label(window,text="\nAre You a Angry?")
label.config(font=('none',50,'bold'),fg="purple")
label.config(background="yellow")
label.pack()

def click1():
    for widget in window.winfo_children():
        widget.destroy()
        window.config(background="green")
    label=Label(window,text="\n\n\n\n\n\nYeeeee :)")
    label.config(font=('none',35,'bold'),background="green",fg="yellow")
    label.pack()
def click2():
    p=random.randint(100,500)
    q=random.randint(200,600)
    button2.place(x=p,y=q)

button1=Button(window,text='No')
button1.place(x=60,y=350)
button1.config(font=('none',35,'bold'))
button1.config(command=click1)
button1.config(bg="orange")
button1.config(fg="blue")
button1.config(activebackground="red")
button1.config(activeforeground="blue")

button2=Button(window,text='YES')
button2.place(x=30,y=350)
button2.config(font=('none',35,'bold'))
button2.config(command=click2)
button2.config(bg="orange")
button2.config(fg="blue")
button2.config(activebackground="red")
button2.config(activeforeground="blue")

window.mainloop()
