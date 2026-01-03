import tkinter as tk

root = tk.Tk()
root.title("My Calculator")
root.geometry("350x400")   
root.resizable(False, False)

display = tk.Entry(
    root,
    font=("Arial", 24),    
    borderwidth=3,
    relief="ridge",
    justify="right"
)
display.pack(fill="x", padx=10, pady=15, ipady=10)  

def press(key):
    display.insert(tk.END, key)

def clear():
    display.delete(0, tk.END)
def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Undefined")

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

buttons = [
    ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
    ('0', 3, 0), ('.', 3, 1), ('+', 3, 2), ('=', 3, 3)
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(
            btn_frame, text=text, font=("Arial", 14),
            width=5, height=2, command=calculate, bg="#4CAF50", fg="black"
        )
    else:
        btn = tk.Button(
            btn_frame, text=text, font=("Arial", 14),
            width=5, height=2, command=lambda t=text: press(t)
        )
    btn.grid(row=row, column=col, padx=5, pady=5)

clear_btn = tk.Button(
    root, text="C", font=("Arial", 14),
    command=clear, bg="red", fg="white"
)
clear_btn.pack(fill="x", padx=10, pady=10)

root.mainloop()
