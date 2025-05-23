from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json

def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    entry_3.delete(0, END)
    entry_3.insert(0, password)
    pyperclip.copy(password)

def password_search():
    website = entry_1.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Ooops", message="There is no such file")
    else:
        messagebox.showinfo(title="Info", message=f"email = {data[website]["email"]}\n"
                                                  f"password = {data[website]["password"]}")


def add_password():
    website = entry_1.get()
    email = entry_2.get()
    password = entry_3.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(entry_3.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave eny fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=entry_1.get(),message=f"These are the details entered: \nEmail: {entry_2.get()}"
                                                       f"\nPassword: {entry_3.get()} \nIs it okay to save?")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                entry_1.delete(0,END)
                entry_3.delete(0, END)

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200,height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=photo)
canvas.grid(column=1,row=1)

label_1 = Label(text="Website:")
label_1.grid(column=0,row=2)

label_2 = Label(text="Email/Username:")
label_2.grid(column=0,row=3)

label_3 = Label(text="Password:")
label_3.grid(column=0,row=4)

entry_1 = Entry(width=21)
entry_1.focus()
entry_1.grid(row=2,column=1,columnspan=1)

entry_2 = Entry(width=37)
entry_2.insert(0,"pauliberacko@gmail.com")
entry_2.grid(row=3,column=1,columnspan=2)

entry_3 = Entry(width=21)
entry_3.grid(row=4,column=1)

gen_button = Button(text="Generate Password",width=11, command=gen_pass)
gen_button.grid(row=4,column=2)

add_button = Button(text="Add",width=35, command=add_password)
add_button.grid(row=5,column=1,columnspan=2)

search_button = Button(text="Search", width=11, command=password_search)
search_button.grid(row=2, column=2)

window.mainloop()