import tkinter as tk
def on_click(key):
    current_text = entry.get()
    if key == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif key == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, key)
root=tk.Tk()
root.title("Calculator")
root.geometry("500x500")
head_frame=tk.Label(root,text="Calculator",font=('Brush Script MT', 40))
head_frame.pack(pady=20)
entry = tk.Entry(root, width=25, font=("Helvetica", 20), bd=5, justify=tk.RIGHT)
entry.pack(padx=10, pady=10)
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+")
]
for row in buttons:
    button_row = tk.Frame(root)
    button_row.pack(side=tk.TOP)

    for label in row:
        button = tk.Button(button_row, text=label, width=5, height=2, font=("Helvetica", 15), command=lambda key=label: on_click(key))
        button.pack(side=tk.LEFT, padx=5, pady=5)
root.mainloop()
