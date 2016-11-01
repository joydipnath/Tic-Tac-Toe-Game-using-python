from tkinter import *
import tkinter.messagebox

tk= Tk()
tk.title("Tic Tac Toe by JOYDIP")
frame = Frame(tk)
frame2= Frame(tk)
frame3= Frame(tk)

click = TRUE

def check(button):
    global click
    if button["text"] == "  " and click == TRUE:
        button["text"] = "X"
        click= FALSE
    elif button["text"] == " " and click == FALSE:
        button["text"] = "O"
        click= TRUE
    elif (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
        button4["text"] == "X" and button4["text"] == "X" and button4["text"] == "X" or
        button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
        button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
        button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
        button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" or
        button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" or
        button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X"):
        tkinter.messagebox.showerror("Winner X", "Congrats")
    elif (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
        button4["text"] == "O" and button4["text"] == "O" and button4["text"] == "O" or
        button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
        button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
        button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
        button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O" or
        button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O" or
        button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O"):
        tkinter.messagebox.showerror("Winner O", "Congrats")

button = StringVar()

button1= Button(frame, text="  ", height = 4 , width = 4,command=lambda:check(button1))
button2= Button(frame, text="  ", height = 4 , width = 4,command=lambda:check(button2))
button3= Button(frame, text="  ", height = 4 , width = 4,command=lambda:check(button3))

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)

button4= Button(frame2, text="  ", height = 4 , width = 4,command=lambda:check(button4))
button5= Button(frame2, text="  ", height = 4 , width = 4,command=lambda:check(button5))
button6= Button(frame2, text="  ", height = 4 , width = 4,command=lambda:check(button6))
button4.pack(side=LEFT)
button5.pack(side=LEFT)
button6.pack(side=LEFT)

button7= Button(frame3, text=" ", height = 4 , width = 4,command=lambda:check(button7))
button8= Button(frame3, text=" ", height = 4 , width = 4,command=lambda:check(button8))
button9= Button(frame3, text=" ", height = 4 , width = 4,command=lambda:check(button9))
button7.pack(side=LEFT)
button8.pack(side=LEFT)
button9.pack(side=LEFT)


frame.pack()
frame2.pack()
frame3.pack()

tk.mainloop()
