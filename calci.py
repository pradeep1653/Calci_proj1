import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.config(bg="#1E1E2E")  # Dark-themed background color

# Entry field
entry = tk.Entry(root, width=18, font=("Arial", 20), justify="right", bg="#FFFFFF", fg="#000000")
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Function to update entry field
def on_click(button_text):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + button_text)

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear entry
def clear():
    entry.delete(0, tk.END)

# Buttons Layout
buttons = [
    ("7", "#a88c7f"), ("8", "#a88c7f"), ("9", "#a88c7f"), ("/", "#f44336"),
    ("4", "#a88c7f"), ("5", "#a88c7f"), ("6", "#a88c7f"), ("*", "#f44336"),
    ("1", "#a88c7f"), ("2", "#a88c7f"), ("3", "#a88c7f"), ("-", "#f44336"),
    ("0", "#a88c7f"), (".", "#142f44"), ("=", "#142f44"), ("+", "#f44336"),
]

# Create buttons
for i, (text, color) in enumerate(buttons):
    button = tk.Button(root, text=text, font=("Arial", 15), width=5, height=2, 
                       bg=color, fg="white", command=lambda t=text: on_click(t) if t != "=" else calculate())
    button.grid(row=(i // 4) + 1, column=i % 4, padx=5, pady=5)

# Clear button
clear_button = tk.Button(root, text="C", font=("Arial", 15), width=5, height=2, bg="#FFA500", fg="white", command=clear)
clear_button.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

# Run the app
root.mainloop()