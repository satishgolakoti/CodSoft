import random
from tkinter import *

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+{[]}|\""

def generate_password():
  length = int(entry_length.get())
  password = "".join(random.sample(characters, length))
  label_password.config(text=password)

window = Tk()
window.title("Password Generator")
window.geometry("300x300")
window.configure(bg="lightblue")
label_length = Label(window, text="Password length:",bg=("lightblue"),font=('times 13'))
label_length.pack(pady=5)
entry_length = Entry(window,width=20)
entry_length.pack(padx=11,pady=5)
button_generate = Button(window, text="Generate Password",font=('times 9'),command=generate_password)
button_generate.pack(pady=4)
label_password = Label(window, text="",bg='lightblue')
label_password.pack(pady=7,padx=7)

window.mainloop()
