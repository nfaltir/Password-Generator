from tkinter import *
from random import randint


root = Tk()
root.title("Password Generator")
# root.iconbitmap("")
root.geometry("700x400")

my_password = chr(randint(33, 126))

# ---------------------Functions--------------------------

# reset inputs and outputs


def reset_values():
    var = IntVar(root)
    var.set("")
    pw_entry.config(textvariable=var)

    var1 = IntVar(root)
    var1.set("")
    my_entry.config(textvariable=var1)


# password script
def new_rand():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_-=+`~[{]}\\|:;,./?"
    pw_entry.delete(0, END)
    # get pass length
    passowrd_length = int(my_entry.get())
    # create var to hold password
    my_password = ''
    # loop through password length
    for x in range(passowrd_length):
        my_password += chr(randint(33, 126))

    # output password
    pw_entry.insert(0, my_password)

# copy password


def copy_password():
    root.clipboard_clear()
    # copy
    root.clipboard_append(pw_entry.get())


# -------------------------------- UI -------------------------------------------------
# label frame
lf = LabelFrame(root, text="Enter password length", labelanchor=N, bd=0)
lf.pack(pady=20)

# label entry for password length
my_entry = Entry(lf, font=("Helvetica", 24), relief="sunken", bd=0.5)
my_entry.pack(pady=30, padx=20)

# Create Entry Box for our returned password

text = Label(text="New Password 👇")
text.place(x=300, y=130)

pw_entry = Entry(root, text='', font=("Sans", 30), bd=1,
                 highlightthickness=0, bg="whitesmoke")
pw_entry.pack(pady=20)


# button frame
my_frame = Frame(root,  bd=0)
my_frame.pack(pady=20)

# Create Buttons
my_button = Button(my_frame, text="Generate Password",
                   command=new_rand, bd=0, foreground="#00917C", padx=15, pady=10)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Copy Password", command=copy_password,
                     foreground="#325288", padx=15, pady=10, background="red")
clip_button.grid(row=0, column=1, padx=10)

reset_button = Button(my_frame, text="Reset", command=reset_values,
                      foreground="#FA1E0E", padx=15, pady=10)
reset_button.grid(row=0, column=2, padx=10)


root.mainloop()
