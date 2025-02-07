from tkinter.filedialog import *
import tkinter as tk

def openFile (): 
    file = askopenfile(mode='r', filetypes=[('text files', '*.txt')])
    if file is not None:
        content = file.read()
        entry.insert(tk.END, content)
        file.close()

def saveFile ():
    new_file = asksaveasfile(mode='w', filetype=[('text files', '*.txt')])
    if new_file:
        text = entry.get('1.0', tk.END)
        new_file.write(text)
        new_file.close()

canvas = tk.Tk()
canvas.geometry("400x600")
canvas.title("Notepad")
canvas.config(bg="#2e2e2e")
top = tk.Frame(canvas)
top.pack(padx=10, pady=5, anchor="nw")

b1 = tk.Button(canvas, text="Open", bg = "white", command = openFile)
b1.pack(in_=top, side="left")

b2 = tk.Button(canvas, text="Save", bg = "white", command=saveFile)
b2.pack(in_=top, side="left")

b3 = tk.Button(canvas, text="Clear", bg = "white", command=lambda: entry.delete(1.0, tk.END))
b3.pack(in_=top, side="left")

b4 = tk.Button(canvas, text="Exit", bg = "white", command=exit)
b4.pack(in_=top, side="left")

entry = tk.Text(canvas, wrap="word", bg="#F9DDA4", font=("poppins", 12))
entry.pack(padx=10, pady=5, expand=True, fill="both")

canvas.mainloop()