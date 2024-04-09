from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50,pady=50)

my_label = Label(text="I am a label", font=("Arial","24", "bold"))
my_label.grid(column=0,row=0)

my_label["text"] = "New Text"
my_label.config(text="New Text")

def button_clicked():
    
    my_label.config(text=input.get())
    

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1,row=1)

button = Button(text="Click Me New", command=button_clicked)
button.grid(column=3,row=0)

input = Entry(width=10)
input.grid(column=4,row=3)




window.mainloop()