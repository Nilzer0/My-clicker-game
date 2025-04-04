from tkinter import *

window = Tk()
window.geometry("400x260")
window.title("my fist click game")
window.config(bg= "#222533")

point = 0
def click():
    global point
    point += 1
    label.config(text = point)

label = Label(window, text = "0", bg = "#222533", fg = "#fafafa", font = ("families", 40, "bold"), relief = RAISED, bd = 10)
label.place(x = 10, y = 10)

button = Button(window, text = "click me!")
button.config(command = click)
button.config(bg = "#222533")
button.config(fg = "#ff4d5d")
button.place(x = 10, y = 102)
button.config(font = ("families", 19, "bold"))
button.config(relief = RAISED, bd = 7)
button.config(padx = 40)
window.mainloop()