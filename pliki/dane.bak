from tkinter import messagebox


def pracownik(login, password, root):
    global konsultant
    konsultant = login.replace('@', '.')
    konsultant = konsultant.split('.')
    konsultant = konsultant[0].capitalize(
    ) + " " + konsultant[1].capitalize()
    messagebox.showinfo("Login", "Zalogowano jako: " + konsultant)
    root.destroy()
    return
