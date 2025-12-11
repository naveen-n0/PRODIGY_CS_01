import tkinter as tk
from tkinter import messagebox

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result


# Button functions
def encrypt_text():
    message = entry_message.get()
    if not shift_value.get().isdigit():
        messagebox.showerror("Error", "Shift value must be a number!")
        return
    shift = int(shift_value.get())
    encrypted = encrypt(message, shift)
    output_text.delete(0, tk.END)
    output_text.insert(0, encrypted)

def decrypt_text():
    message = entry_message.get()
    if not shift_value.get().isdigit():
        messagebox.showerror("Error", "Shift value must be a number!")
        return
    shift = int(shift_value.get())
    decrypted = decrypt(message, shift)
    output_text.delete(0, tk.END)
    output_text.insert(0, decrypted)


# GUI Setup
root = tk.Tk()
root.title("Caesar Cipher Tool")
root.geometry("400x300")
root.config(bg="#2b2b2b")


# Widgets
tk.Label(root, text="Caesar Cipher", font=("Arial", 16, "bold"), fg="white", bg="#2b2b2b").pack(pady=10)

tk.Label(root, text="Enter Message:", fg="white", bg="#2b2b2b").pack()
entry_message = tk.Entry(root, width=40)
entry_message.pack(pady=5)

tk.Label(root, text="Shift Value:", fg="white", bg="#2b2b2b").pack()
shift_value = tk.Entry(root, width=10)
shift_value.pack(pady=5)

tk.Button(root, text="Encrypt", width=15, command=encrypt_text).pack(pady=5)
tk.Button(root, text="Decrypt", width=15, command=decrypt_text).pack(pady=5)

tk.Label(root, text="Output:", fg="white", bg="#2b2b2b").pack()
output_text = tk.Entry(root, width=40)
output_text.pack(pady=5)

# Start GUI loop
root.mainloop()