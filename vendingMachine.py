import tkinter as tk

window = tk.Tk()
window.title("Vending Machine")


def mySmarties():
    myLabel = tk.Label(text="You ordered smarties!!")
    myLabel.grid(row=3,column=0)

def myMoney():
    myLabel3 = tk.Label(text=e.get())
    myLabel3.grid(row=1,column=2)

hello = tk.Label(text="Make Your Selection!")
myLabel1 = tk.Label(text = "Enter cash: ")
e = tk.Entry(borderwidth=2)

hello.grid(row=0,column=0)
myLabel1.grid(row=1,column=0)
e.grid(row=1,column=1)

button1 = tk.Button(text="Smarties", command=mySmarties, bg="lightblue")
button2 = tk.Button(text="Cookies")
button3 = tk.Button(text="Enter Cash", command=myMoney, bg="lightgreen")
button1.grid(row=2,column=0)
button2.grid(row=2,column=1)
button3.grid(row=0,column=2)


tk.mainloop()
