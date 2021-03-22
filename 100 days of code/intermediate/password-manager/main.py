from tkinter import *
from tkinter import messagebox
from generate_password import password_generator
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def fill_password():
    password_entry.delete(0, END)  # to clear up the field from any previously generated passwords
    generated_password = password_generator()
    pyperclip.copy(generated_password)  # copy the generated password tp the clipboard
    password_entry.insert(END, generated_password)  # insert the generated  password into the password entry


# ---------------------------- SAVE PASSWORD ------------------------------- #
def store_data():
    website = website_entry.get().item()
    email = email_entry.get()
    password = password_entry.get()
    new_data_dict = {website: {
        "email": email,
        "password": password}}
    if "" in [password, email, website]:
        messagebox.showwarning("Empty field!", message = " Please do not leave any of the fields empty!")
    else:
        # show user the info-to-save and give him a chance to cancel/edit
        if messagebox.askokcancel(title = website, message = f"Do you want to save these information:\nEmail: {email}\n"
                                                             f"password: {password}\n"):
            try:
                with open("data.json", "r") as data_file:
                    # to read/load from the file
                    data = json.load(data_file)
                    # to update the DB with the new entry:
            except FileNotFoundError:
                create_db(new_data_dict)
            else:
                data.update(new_data_dict)
                create_db(data)

                # data_file.write(f"\n{website} | {email} | {password}\n") # no longer needed to save the data,
                # since json DB is used here
            finally:
                password_entry.delete(0, END)
                website_entry.delete(0, END)


def create_db(data):
    with open("data.json", "w") as data_file:
        # to write the data to  file
        json.dump(data, data_file, indent = 4)


# ---------------------------- FINDING PASSWORD  ------------------------------- #
def find_password():
    try:
        # to read/load from the file
        data_file = open("data.json", "r")

    except FileNotFoundError:
        messagebox.showwarning("No data File Found!", message = " No data has been saved yet!")
    else:
        website = website_entry.get().item()
        email = email_entry.get()
        password = password_entry.get()
        data = json.load(data_file)
        if website in data:
            password = data[website]['password']
            email = data[website]['email']
            messagebox.showinfo(title = website, message = f"Website:{website}\n Email: {email}\n password: {password}")
        else:
            if website != "":
                print(f"No {website} account is stored in the database. ")
            data_list = []
            continue_search = False
            if website == "" and "" != email:
                if messagebox.askokcancel(f"No data for {website} is stored in the database!",
                                          message = "Do you want to look in the database for accounts stored with "
                                                    "this Email!"):
                    continue_search = True
            if "" in [email, website] and "" != password:
                if messagebox.askokcancel(f"No data for {website} is stored in the database!",
                                          message = "Do you want to look in the database for accounts stored with "
                                                    "this Password!"):
                    continue_search = True
            if continue_search:
                # Handling searches for given email/password and getting returning the full  relevant data entry to
                # the user
                for entry in data.keys():
                    if email != "" and data[entry]["email"] == email:  # if the searched email is not empty
                        website = entry
                        password = data[entry]["password"]
                        data_list.append((website, email, password))
                        # return all relevant entries, in which the user used this email
                        messagebox.showinfo(title = "For this Email we have: ",
                                            message = f"website: {website}\nEmail:{email}\n password: {password}")
                    # return all relevant entries, in which the user used this password,
                    # when the searched password is not empty
                    elif password != "" and data[entry]["password"] == password:
                        website = entry
                        email = data[entry]["email"]
                        data_list.append([website, email, password])
                        messagebox.showinfo(title = "For this Password we have: ",
                                            message = f"website: {website}\nEmail: {email}\n password: {password}")
                if data_list:
                    messagebox.showinfo(item = "For this Email/password we have: ",
                                        message = f"For the searched Email/password we have the following Entries: "
                                                  f"{[(website, email, password) for [(website, email, password)] in data_list]}")

        data_file.close()
        return website, email, password


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
canvas = Canvas(width = 200, height = 200)
window.title('Password Manager')
window.config(padx = 50, pady = 50)
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = logo_img)  # centered position on the screen, x=100, y=100
canvas.grid(column = 1, row = 0)

# Labels
# for the website label
website_label = Label(text = "Website:")
website_label.grid(column = 0, row = 1)
# email label
email_label = Label(text = "Email/Username:")
email_label.grid(column = 0, row = 2)
# Password label
password_label = Label(text = "Password:")
password_label.grid(column = 0, row = 3)

# # Entries
website_entry = Entry(width = 21)
website_entry.grid(column = 1, row = 1)
website_entry.focus()  # focus on the website entry
email_entry = Entry(width = 40)
# Email entry
email_entry.grid(column = 1, row = 2, columnspan = 2)
# email_entry.insert(END, "email@email.com")
# password entry
password_entry = Entry(width = 21)
password_entry.grid(column = 1, row = 3)

# Buttons
# generate password
generate_password_button = Button(text = " Generate Password", width = 15, command = fill_password)
generate_password_button.grid(column = 2, row = 3)

# add to database
add_button = Button(text = "Add", width = 36, command = store_data)
add_button.grid(column = 1, row = 4, columnspan = 2)

# Search button
search_button = Button(text = "Search", width = 15, command = find_password)
search_button.grid(column = 2, row = 1)
window.mainloop()
# DISCLAIMER: PLEASE DO NOT USE ANY PASSWORD THAT THIS PASSWORD MANAGER GENERATES IF YOU STORE THEM LOCALLY.
# THEY ARE NOT HASHED OR PROTECTED AND CAN BE ACCESSIBLE EASILY BY ANYONE,
# SINCE THEY'RE JUST STORED IN PLAINTEXT IN A LOCAL  FILE
