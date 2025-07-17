from tkinter import *
from tkinter import ttk

def caesar_cipher():
    try:
        shift = int(shift_entry.get())
        mode = mode_entry.get().lower()
        msg = msg_entry.get().lower()

        if not (1 <= shift <= 25):
            label_result.config(text="Shift must be between 1 and 25.")
            return

        keys = "abcdefghijklmnopqrstuvwxyz"
        result = ""

        for char in msg:
            if char in keys:
                index = keys.index(char)
                if mode == 'encrypt':
                    new_index = (index + shift) % 26
                elif mode == 'decrypt':
                    new_index = (index - shift) % 26
                else:
                    label_result.config(text="Invalid mode. Use encrypt or decrypt.")
                    return
                result += keys[new_index]
            else:
                result += char

        label_result.config(text="Result: " + result)

    except ValueError:
        label_result.config(text="Please enter a valid number for shift.")

# Main Window
root = Tk()
root.geometry('640x480')
root.title("Caesar Cipher")
root.configure(bg="light gray")

# Heading
label_head = Label(root, text="Caesar Cipher Tool", bg="steel blue", fg="white", font=('Arial', 20, 'bold'), pady=10)
label_head.pack(fill=X)

# Form Frame
form_frame = Frame(root, bg="light gray", padx=20, pady=20, relief="groove", bd=1)
form_frame.pack(pady=20)

# Shift
ttk.Label(form_frame, text="Shift (1-25):", font=('Arial', 12)).grid(row=0, column=0, sticky=W, pady=5)
shift_entry = ttk.Entry(form_frame, width=30)
shift_entry.grid(row=0, column=1, pady=5)

# Mode
ttk.Label(form_frame, text="Mode (encrypt/decrypt):", font=('Arial', 12)).grid(row=1, column=0, sticky=W, pady=5)
mode_entry = ttk.Entry(form_frame, width=30)
mode_entry.grid(row=1, column=1, pady=5)

# Message
ttk.Label(form_frame, text="Message:", font=('Arial', 12)).grid(row=2, column=0, sticky=W, pady=5)
msg_entry = ttk.Entry(form_frame, width=50)
msg_entry.grid(row=2, column=1, pady=5)

# Button
button = Button(form_frame, text="Encrypt / Decrypt", command=caesar_cipher,
                bg="LIGHT sea green", fg="white", font=('Arial', 12, 'bold'), padx=5, pady=5)
button.grid(row=3, column=0, columnspan=2, pady=10)

# Result
label_result = Label(form_frame, text="Result will appear here", font=('Arial', 12, 'bold'),
                     bg="light gray", fg="midnight blue", wraplength=400, justify=LEFT)
label_result.grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()



        
        
        


    

 
