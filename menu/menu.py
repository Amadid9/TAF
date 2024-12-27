import tkinter as tk

def renitialiser():
    q.delete(0, tk.END)
    total.config(text="00 dhs")
def calc(x):
        qte = int(q.get())
        tot = menu[x] * qte
        total.config(text=f"Total: {tot} dhs")
menu= {
    "pizza": 40,
    "tacos": 49,
    "sandwich": 30,
    "burger": 32,
    "frites": 15,
    "nuggets": 35,
    "soda": 15,
    "limonad": 18
}
a = tk.Tk()
a.geometry("800x500")
a.title("TAF_MENU_PYTHON")
b = tk.Label(a, text="Bien venu dans le menu de notre restaurant", font=("arial", 18))
b.pack(padx=20, pady=10)
f = tk.Label(a, text="entrer le quantité dans ce champs", font=("arial", 8))
f.pack(padx=20, pady=10)
q = tk.Entry(a, width=70)
q.pack(padx=20, pady=10)
e = tk.Frame(a)
e.columnconfigure(0, weight=1)
e.columnconfigure(1, weight=1)
e.columnconfigure(2, weight=1)
e.pack(fill='x')
btn1 = tk.Button(e, text="🍕 pizza", font=("arial", 16), command=lambda: calc("pizza"))
btn1.grid(row=0, column=0, sticky=tk.W + tk.E)
btn2 = tk.Button(e, text="🌮 tacos", font=("arial", 16), command=lambda: calc("tacos"))
btn2.grid(row=0, column=1, sticky=tk.W + tk.E)
btn3 = tk.Button(e, text="🥪 sandwich", font=("arial", 16), command=lambda: calc("sandwich"))
btn3.grid(row=0, column=2, sticky=tk.W + tk.E)
btn4 = tk.Button(e, text="🍔 burger", font=("arial", 16), command=lambda: calc("burger"))
btn4.grid(row=1, column=0, sticky=tk.W + tk.E)
btn5 = tk.Button(e, text="🍟 frites", font=("arial", 16), command=lambda: calc("frites"))
btn5.grid(row=1, column=1, sticky=tk.W + tk.E)
btn6 = tk.Button(e, text="🥔 nuggets", font=("arial", 16), command=lambda: calc("nuggets"))
btn6.grid(row=1, column=2, sticky=tk.W + tk.E)
btn7 = tk.Button(e, text="🥤 soda", font=("arial", 16), command=lambda: calc("soda"))
btn7.grid(row=2, column=0, sticky=tk.W + tk.E)
btn8 = tk.Button(e, text="🍶 limonad", font=("arial", 16), command=lambda: calc("limonad"))
btn8.grid(row=2, column=1, sticky=tk.W + tk.E)
reset_btn = tk.Button(a, text="Reset", font=("arial", 16), command=renitialiser)
reset_btn.pack(pady=20)
total = tk.Label(a, font=("arial", 18))
total.pack(pady=20)
a.mainloop()