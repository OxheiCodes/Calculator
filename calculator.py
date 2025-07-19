import tkinter as tk

# Colors matching logo
BG_COLOR = "#f5f0df"
BUTTON_BG = "#124c87"
BUTTON_FG = "#fce7a5"
DISPLAY_BG = "#fce7a5"
DISPLAY_FG = "#124c87"
FONT = ("Arial Rounded MT Bold", 20)

def on_button_click(char):
    if char == '=':
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif char == 'C':
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, char)

root = tk.Tk()
root.title("OxheiCodes Calculator")
root.geometry("320x420")
root.configure(bg=BG_COLOR)

entry = tk.Entry(
    root, font=FONT, bg=DISPLAY_BG, fg=DISPLAY_FG, borderwidth=4,
    relief="ridge", justify='right'
)
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', 'C', '=', '+')
]

frame = tk.Frame(root, bg=BG_COLOR)
frame.pack()

for row in buttons:
    button_row = tk.Frame(frame, bg=BG_COLOR)
    button_row.pack(expand=True, fill='both')
    for char in row:
        button = tk.Button(
            button_row, text=char, font=FONT, bg=BUTTON_BG, fg=BUTTON_FG,
            activebackground="#103b6c", activeforeground="white",
            command=lambda c=char: on_button_click(c)
        )
        button.pack(side='left', expand=True, fill='both', padx=4, pady=4)

root.mainloop()
