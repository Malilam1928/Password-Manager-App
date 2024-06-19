from tkinter import *
from tkinter import messagebox
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Password Generator Project
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_text.insert(0, password)


# ---------------------------- SEARCH ENGINE ------------------------------- #
def search():
    website = website_textbox.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email : {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Warning", message="The website can not found")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_name = website_textbox.get()
    email_name = email_text.get()
    password_name = password_text.get()
    new_data = {
        website_name: {"email": email_name,
                       "password": password_name
                       }
    }

    if len(website_name) == 0 or len(password_name) == 0 or len(email_name) == 0:
        messagebox.showinfo(title="Warning", message="Pleaser enter all the required data !!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        except ValueError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old date with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_textbox.delete(0, END)
            password_text.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

website_textbox = Entry(width=35)
website_textbox.grid(row=1, column=1, columnspan=2)
website_textbox.focus()
email_text = Entry(width=35)
email_text.grid(row=2, column=1, columnspan=2)
email_text.insert(0, "mali@gmail.com")
password_text = Entry(width=17)
password_text.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, height=1, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)
add_search_button = Button(text="Search", width=5, command=search)
add_search_button.grid(row=1, column=2)

window.mainloop()
