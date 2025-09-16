import tkinter as tk

root = tk.Tk()
root.title("game")
root.geometry("500x500")

frame = tk.Frame(root)
frame.pack(pady=20)

def rock() :
    import random

    global p1
    global p2

    b = "rock"

    list1 = ["rock","paper","scissors"]

    a = random.choice(list1)

    label2.config(text=f"computer move : {a}")

    if  p1 == 3 :
        label5.config(text="GOOD BYE")    
    elif p2 == 3 :
        label5.config(text="GOOD BYE")
        

    if b == "rock" and a == "rock" :
        label3.config(text="draw",fg="black")
    elif b == "rock" and a == "paper" :
        label3.config(text="computer win",fg="red")
        p2 += 1
        label4.config(text=f"your point : {p1} | computer point : {p2}" , font=("Arial",20))
    elif b == "rock" and a == "scissors" :
        label3.config(text="you win",fg="green")
        p1 += 1
        label4.config(text=f"your point : {p1} | computer point : {p2}" , font=("Arial",20))
    # if  p1 == 3 :
    #         root.destroy
    # elif p2 == 3 :
    #         root.destroy
    

def paper() :
    import random

    global p1
    global p2

    b = "paper"

    list1 = ["rock","paper","scissors"]

    a = random.choice(list1)

    label2.config(text=f"computer move : {a}")


    if  p1 == 2 :
        label5.config(text="GOOD BYE")
        label4 = tk.Label(frame , text=f"your point : {p1} | computer point : {p2}" , font=("Arial",20))   
    elif p2 == 2 :
        label5.config(text="GOOD BYE")


            


    if b == "paper" and a == "paper" :
        label3.config(text="draw",fg="black")
    elif b == "paper" and a == "scissors" :
        label3.config(text="computer win",fg="red")
        p2 += 1
        label4.config(text=f"your point : {p1} | computer point : {p2}" , font=("Arial",20))
    elif b == "paper" and a == "rock" :
        label3.config(text="you win",fg="green")
        p1 += 1
        label4.config(text=f"your point : {p1} | computer point : {p2}" , font=("Arial",20))

def scissors() :
    import random

    global p1
    global p2

    b = "scissors"

    list1 = ["rock","paper","scissors"]

    a = random.choice(list1)

    label2.config(text=f"computer move : {a}")

    if p1 == 2 :
        label5.config(text="GOOD BYE")
        label4.config
    elif p2 == 2 :
        label5.config(text="GOOD BYE")
        label4.config
            


    if b == "scissors" and a == "scissors" :
        label3.config(text="draw",fg="black")
    elif b == "scissors" and a == "rock" :
        label3.config(text="computer win",fg="red")
        p2 += 1
        label4.config(text=f"your point : {p1} | computer point : {p2}" , font=("Arial",20))
    elif b == "scissors" and a == "paper" :
        label3.config(text="you win",fg="green")
        p1 += 1
        label4.config(text=f"your point : {p1} | computer point : {p2}" , font=("Arial",20))
    
    
p1 = 0

p2 = 0

label1 = tk.Label(frame , text="-- ROCK - PAPER - SCISSORS --", font=("Arial",20) , fg="green")
label1.grid(row=0 , columnspan=3 , pady=30)

label4 = tk.Label(frame , text=f"your point : {p1} | computer point : {p2}" , font=("Arial",20))
label4.grid(row=1 , columnspan=3)

button1 = tk.Button(frame , text="👊",width=17 , height=5 , bg="gray" , command= rock)
button1.grid(row=2 , column=0)

button2 = tk.Button(frame , text="✋",width=17 , height=5 , bg="gray" , command= paper)
button2.grid(row=2 , column=1)

button3 = tk.Button(frame , text="✌",width=17 , height=5 , bg="gray" , command=scissors)
button3.grid(row=2 , column=2 , pady=30)

label2 = tk.Label(frame , text="",font=("Arial",17))        #for cpu
label2.grid(row=3,columnspan=3)

label3 = tk.Label(frame , text="",font=("Arial",17))        #for result
label3.grid(row=4,columnspan=3,pady=30)

label5 = tk.Label(frame, text="",font=("Arial",20))
label5.grid(row=5,columnspan=3)


root.mainloop()