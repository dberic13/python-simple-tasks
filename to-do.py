import tkinter as tk

def on_click():
    task = entry.get()
    if task:
        listaZadataka.insert(tk.END, f"• {task}")
        entry.delete(0, tk.END)

def on_delete():
    selection = listaZadataka.curselection()
    if selection:
        listaZadataka.delete(selection[0])

def on_done():
    selection = listaZadataka.curselection()
    if selection:
        listaZadataka.itemconfig(selection[0], fg="red")

def on_edit():
    selection = listaZadataka.curselection()
    if selection:
        task = listaZadataka.get(selection[0])
        entry.delete(0, tk.END)
        entry.insert(tk.END, task[2:])
        listaZadataka.delete(selection[0])

root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="left")
entry.grid(row=0, column=0, columnspan=4)
entry.bind("<Return>", lambda event: on_click())

listaZadataka = tk.Listbox(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="left")
listaZadataka.grid(row=1, column=0, columnspan=4)

gumbDodaj = tk.Button(root, text="Dodaj", width=5, height=2, font=("Arial", 18), command=on_click)
gumbDodaj.grid(row=2, column=0, columnspan=2)

gumbObrisi = tk.Button(root, text="Obrisi", width=5, height=2, font=("Arial", 18), command=on_delete)
gumbObrisi.grid(row=2, column=2, columnspan=2)

listaZadataka.bind("<Double-1>", lambda event: on_done())
listaZadataka.bind("<Delete>", lambda event: on_delete())
listaZadataka.bind("<F2>", lambda event: on_edit())

root.mainloop()

