import tkinter as tk
root= tk. Tk()
root.title("Lijan")
root.geometry("350x400")

entry= tk.Entry(root)
entry.pack()

def greed_me():
    name= entry.get()
    
    label.config(text=(f"Hello {name}"))
    
button= tk.Button(root,text="submit", command=greed_me())
button.pack()

label=tk.Label(root,text="")
label.pack()


root.mainloop()



