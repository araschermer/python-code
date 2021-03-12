from tkinter import *
from tkinter import messagebox
from generate_password import password_generator
import pyperclip


# DISCLAIMER: PLEASE DO NOT USE ANY PASSWORD THAT THIS PASSWORD MANAGER GENERATES IF YOU STORE THEM LOCALLY.
# THEY ARE NOT HASHED OR PROTECTED AND CAN BE ACCESSIBLE EASILY, SINCE THEY'RE JUST STORED IN A data.txt FILE

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def fill_password():
    password_entry.delete(0, END)  # to clear up the field from any previously generated passwords
    generated_password = password_generator()
    pyperclip.copy(generated_password)  # copy the generated password tp the clipboard
    password_entry.insert(END, generated_password)  # insert the generated  password into the password entry


# ---------------------------- SAVE PASSWORD ------------------------------- #
def store_data():
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()
    if "" in [password, email, website]:
        messagebox.showwarning("Empty field!", message = " Please do not leave any of the fields empty!")
    else:
        # show user the info-to-save and give him a chance to cancel/edit
        if messagebox.askokcancel(title = website, message = f"Do you want to save these information:\nEmail: {email}\n"
                                                             f"password: {password}\n"):
            with open("data.txt", "a") as data_file:
                data_file.write(f"\n{website} | {email} | {password}\n")
            password_entry.delete(0, END)
            website_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
canvas = Canvas(width = 200, height = 200)
window.title('Password Manager')
window.config(padx = 50, pady = 50)
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = logo_img)  # centered position on the screen, x=100, y=100
canvas.grid(column = 1, row = 0)

# for the website label and entry
website_label = Label(text = "Website:")
website_label.grid(column = 0, row = 1)
website_entry = Entry(width = 40)
website_entry.focus()  # focus on the website entry
website_entry.grid(column = 1, row = 1, columnspan = 2)

# email label and entry
email_label = Label(text = "Email/Username:")
email_label.grid(column = 0, row = 2)
email_entry = Entry(width = 40)
email_entry.insert(END, "email@email.com")
email_entry.grid(column = 1, row = 2, columnspan = 2)

# password label and entry
password_label = Label(text = "Password:")
password_label.grid(column = 0, row = 3)
password_entry = Entry(width = 25)
password_entry.grid(column = 1, row = 3)
# generate password
generate_password_button = Button(text = " Generate Password", width = 15, command = fill_password)
generate_password_button.grid(column = 2, row = 3)

# add to database
add_button = Button(text = "Add", width = 35, command = store_data)
add_button.grid(column = 1, row = 4, columnspan = 2)
window.mainloop()
# DISCLAIMER: PLEASE DO NOT USE ANY PASSWORD THAT THIS PASSWORD MANAGER GENERATES IF YOU STORE THEM LOCALLY.
# THEY ARE NOT HASHED OR PROTECTED AND CAN BE ACCESSIBLE EASILY, SINCE THEY'RE JUST STORED IN A data.txt FILE
