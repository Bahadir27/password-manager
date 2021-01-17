from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # messagebox.showinfo(title="Title", message="Message")
    is_ok = messagebox.askokcancel(title=website,
                                   message=f"These are the details entered: \nEmail: {email=} "
                                           f"\nPassword: {password=} \nIs it ok to save?")

    if len(website) < 3 or len(email) < 5 or len(password) < 5:
        messagebox.showinfo(title= "Error", message="The requirements are not sufficient to save")
        is_ok = False

    if is_ok:
        with open("demo_passwords.txt", "a") as file_object:
            # Append password at the end in demo_password text file
            file_object.write(f"{website} | {email} | {password} \n")
        website_entry.delete(0, 'end')
        # email_entry.delete(0, 'end')
        password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# create the canvas, size in pixels
canvas = Canvas(width=200, height=200, bg='white')

# load the .gif image file
logo_image = PhotoImage(file='logo.png')

# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
canvas.create_image(100, 100, image=logo_image)

# pack the canvas into a frame/form
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
password_label = Label(text="password")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

# Buttons

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
