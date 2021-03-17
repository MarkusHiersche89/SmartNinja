from tkinter import *

main_window = Tk()
main_window.geometry("500x500")
"""
w1 = Label(main_window, text="Rot", bg="red")
w1.pack(fill=X)
w2 = Label(main_window, text="Grün", bg="green")
w2.pack(fill=X)
w3 = Label(main_window, text="Blau", bg="blue", fg="white")
w3.pack(fill=X, padx=10, pady=10)

w1 = Label(main_window, text="Rot", bg="red")
w1.pack(fill=X, side=LEFT)
w2 = Label(main_window, text="Grün", bg="green")
w2.pack(fill=X, side=LEFT)
w3 = Label(main_window, text="Blau", bg="blue", fg="white")
w3.pack(fill=X, padx=10, pady=10, side=LEFT)
"""

wg0 = Label(main_window, text="Blau", bg="blue").grid(row=0, column=0)
wg1 = Label(main_window, text="Rot", bg="red").grid(row=1, column=1)
wg2 = Label(main_window, text="Grün", bg="green").grid(row=3, column=2)

mainloop()