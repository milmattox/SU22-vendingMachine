import tkinter as tk
import random
#set up window
window = tk.Tk()
window.title("Vending Machine")
window.geometry("300x300")
#initialize global variables
smarties,cookies,snickers,cheetos,reeses =0,0,0,0,0

itemName = ['smarties','snickers','cheetos','cookies','musketeers']
itemQuantity = [0,0,0,0,0]
itemQuantityLabel = [0,0,0,0,0]
itemButton =[0,0,0,0,0]
def setQuantities():  #set the starting inventory
    for i in range(len(itemName)):
        itemQuantity[i] =random.randint(1,10)
        
def myOrder(itemnum): #if they want a smarties
    itemQuantity[itemnum]-=1
    itemQuantityLabel[itemnum].config(text=itemQuantity[itemnum])
    
def myMoney(): #enter money
    myLabel3 = tk.Label(text=e.get())
    myLabel3.grid(row=1,column=2)

#place acks on window
ack1 = tk.Label(text="Make Your Selection!")
e = tk.Entry(borderwidth=2, width=15) #enter money
#e.insert(0,"Enter amount")
cashButton = tk.Button(text="Enter Cash", command=myMoney, bg="lightgreen")
#place instructions on grid
ack1.grid(row=0,column=0)
#place entry box on grid
e.grid(row=1,column=1)
cashButton.grid(row=1,column=0)
#buttons
itemButton[0] = tk.Button(text=itemName[0], command=lambda:myOrder(0), bg="lightblue")
itemButton[1] = tk.Button(text=itemName[1], command=lambda:myOrder(1), bg="lightpink")
itemButton[2] = tk.Button(text=itemName[2], command=lambda:myOrder(2), bg="lightyellow")
#place buttons
itemButton[0].grid(row=2,column=0)
itemButton[1].grid(row=2,column=1)
itemButton[2].grid(row=2, column=2)
setQuantities()
#quantity labels
itemQuantityLabel[0] = tk.Label(text = itemQuantity[0])
itemQuantityLabel[1] = tk.Label(text = itemQuantity[1])
itemQuantityLabel[2] = tk.Label(text = itemQuantity[2])
#place quantity labels
itemQuantityLabel[0].grid(row=3,column=0)
itemQuantityLabel[1].grid(row=3,column=1)
itemQuantityLabel[2].grid(row=3,column=2)

tk.mainloop()
