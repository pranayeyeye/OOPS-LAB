import random
import string
import tkinter as tk
from tkinter import messagebox

class PasswordGenerator:
    def __init__(self, length, use_lowercase, use_uppercase, use_numbers, use_symbols):
        self.length = length
        self.use_lowercase = use_lowercase
        self.use_uppercase = use_uppercase
        self.use_numbers = use_numbers
        self.use_symbols = use_symbols
        self.characters = ""
        self._set_characters()

    def _set_characters(self):
        if self.use_lowercase:
            self.characters += string.ascii_lowercase
        if self.use_uppercase:
            self.characters += string.ascii_uppercase
        if self.use_numbers:
            self.characters += string.digits
        if self.use_symbols:
            self.characters += string.punctuation

    def generate(self):
        if not self.characters:
            return "Select at least one character type"
        
        password = "".join(random.choice(self.characters) for _ in range(self.length))
        return password

class PasswordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.label = tk.Label(root, text="Password Length:")
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.length_entry = tk.Entry(root)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        self.lowercase_var = tk.BooleanVar()
        self.uppercase_var = tk.BooleanVar()
        self.numbers_var = tk.BooleanVar()
        self.symbols_var = tk.BooleanVar()

        self.lowercase_check = tk.Checkbutton(root, text="Include lowercase alphabets", variable=self.lowercase_var)
        self.lowercase_check.grid(row=1, column=0, padx=10, pady=10)

        self.uppercase_check = tk.Checkbutton(root, text="Include uppercase alphabets", variable=self.uppercase_var)
        self.uppercase_check.grid(row=2, column=0, padx=10, pady=10)

        self.numbers_check = tk.Checkbutton(root, text="Include numbers", variable=self.numbers_var)
        self.numbers_check.grid(row=3, column=0, padx=10, pady=10)

        self.symbols_check = tk.Checkbutton(root, text="Include symbols", variable=self.symbols_var)
        self.symbols_check.grid(row=4, column=0, padx=10, pady=10)

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=5, column=0, columnspan=2, pady=20)

        self.password_label = tk.Label(root, text="Generated Password: ")
        self.password_label.grid(row=6, column=0, padx=10, pady=10)

        self.password_display = tk.Entry(root)
        self.password_display.grid(row=6, column=1, padx=10, pady=10)

        self.copy_button = tk.Button(root, text="Copy", command=self.copy_to_clipboard)
        self.copy_button.grid(row=7, column=0, columnspan=2, pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            use_lowercase = self.lowercase_var.get()
            use_uppercase = self.uppercase_var.get()
            use_numbers = self.numbers_var.get()
            use_symbols = self.symbols_var.get()

            password_generator = PasswordGenerator(length, use_lowercase, use_uppercase, use_numbers, use_symbols)
            password = password_generator.generate()

            self.password_display.delete(0, tk.END) 
            self.password_display.insert(0, password)
        except ValueError:
            messagebox.showerror("Invalid input")

    def copy_to_clipboard(self):
        password = self.password_display.get()
        if password:
            self.root.clipboard_clear()  
            self.root.clipboard_append(password)  
            self.root.update()  
            messagebox.showinfo("Copied")
        else:
            messagebox.showwarning("No password generated to copy")

root = tk.Tk()
app = PasswordApp(root)
root.mainloop()
