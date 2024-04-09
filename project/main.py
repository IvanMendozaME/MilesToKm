from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20,pady=10)

def button_clicked():
    result.config(text=int(input.get())*1.609)
equal = Label(text="is equal to", font=("Arial","10", "bold"))
equal.grid(column=0,row=1)
miles = Label(text="Miles", font=("Arial","10", "bold"))
miles.grid(column=2,row=0)
km = Label(text="km", font=("Arial","10", "bold"))
km.grid(column=2,row=1)
result = Label(text="", font=("Arial","10", "bold"))
result.grid(column=1,row=1)


input = Entry(width=10)
input.grid(column=1,row=0)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1,row=3)

window.mainloop()