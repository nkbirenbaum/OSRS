import tkinter as tk

gui = tk.Tk()

gui.geometry("500x500")
gui.resizable(0, 0)
gui.geometry('+0+0')

label = tk.Label(
    text="Hello, Tkinter",
    fg='#FFFFFF',
    bg="#000000",
    width=16,
    height=3
)

button = tk.Button(
    text="Click me!",
    width=16,
    height=3,
    bg="blue",
    fg="yellow",
)

entry = tk.Entry()

label.pack()
button.pack()

gui.mainloop()
