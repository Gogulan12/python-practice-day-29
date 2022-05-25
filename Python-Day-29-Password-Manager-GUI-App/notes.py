# window = Tk()
# window.title("Password Manager")
# window.config(padx=50, pady=50)
#
# canvas = Canvas(width=200, height=200)
# logo_img = PhotoImage(file="logo.png")
# canvas.create_image(100, 100, image=logo_img)
# canvas.grid(column=1, row=0)
#
# website_label = Label(text="Website:")
# website_label.grid(column=0, row=1)
#
# website_entry = Entry(width=35)
# website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
#
# email_label = Label(text="Email/Username:")
# email_label.grid(column=0, row=2)
#
# email_entry = Entry(width=35)
# email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
#
# password_label = Label(text="Password:")
# password_label.grid(column=0, row=3)
#
# password_entry = Entry(width=24)
# password_entry.grid(column=1, row=3, sticky="W")
#
# password_button = Button(text="Generate Password")
# password_button.grid(column=2, row=3, sticky="EW")
#
# add_button = Button(text="Add", width=36)
# add_button.grid(column=1, row=4, columnspan=2, sticky="EW")
#
# window.mainloop()



#Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# nr_letters = random.randint(8, 10)
# nr_symbols = random.randint(2, 4)
# nr_numbers = random.randint(2, 4)
#
# password_list = []
#
# for char in range(nr_letters):
#   password_list.append(random.choice(letters))
#
# for char in range(nr_symbols):
#   password_list += random.choice(symbols)
#
# for char in range(nr_numbers):
#   password_list += random.choice(numbers)
#
# random.shuffle(password_list)
#
# password = ""
# for char in password_list:
#   password += char
#
# print(f"Your password is: {password}")



# #Password Generator Project
# def generate_password():
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
#     password_letters = [choice(letters) for _ in range(randint(8, 10))]
#     password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
#     password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
#
#     password_list = password_letters + password_symbols + password_numbers
#     shuffle(password_list)
#
#     password = "".join(password_list)
#     if len(password_entry.get()) == 0:
#         password_entry.insert(0, password)
#     else:
#         password_entry.delete(0,END)
#         password_entry.insert(0,password)
#     # password_entry.clipboard_clear()
#     # password_entry.clipboard_append(password)