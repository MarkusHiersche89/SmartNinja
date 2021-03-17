from tkinter import messagebox
import tkinter

secret = 10

def pruefen():
    if int(eingabe.get()) == secret:
        text = "Korrekt"
    elif int(eingabe.get()) > secret:
        text = "zu groß"
    else:
        text = "zu klein"
    #print(eingabe.get())
    messagebox.showinfo("Ergebnis= ", text)

main_window = tkinter.Tk()
main_window.geometry("500x500") # breite x höhe
main_window.title("Wetterstation")

willkommenstext = tkinter.Label(main_window, text="Eigene Wetterstation")
willkommenstext.pack()

eingabe = tkinter.Entry(main_window)
eingabe.pack()
#print(eingabe)

ok = tkinter.Button(main_window, text="Übertragen", command=pruefen, fg="red")
ok.pack()

main_window.mainloop()