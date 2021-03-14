from tkinter import *
import requests


def get_quote(itemconfig=True):
    response = requests.get(url = "https://api.kanye.rest/")
    response.raise_for_status()
    data = response.json()
    text = data["quote"]
    save_kanye_quotes(text)
    if itemconfig:
        canvas.itemconfig(quote_text, text = text)
    return text

    # https://api.kanye.rest/
    # Write your code here.


def save_kanye_quotes(kanye_quote):
    with open('kanye_quotes.txt', 'a') as f:
        f.write(f"{kanye_quote}\n")


window = Tk()
window.title("Kanye Says...")
window.config(padx = 50, pady = 50)

canvas = Canvas(width = 300, height = 414)
background_img = PhotoImage(file = "background.png")
canvas.create_image(150, 207, image = background_img)
quote_text = canvas.create_text(150, 207, width = 250, font = ("Arial", 20, "bold"), fill = "white")
canvas.itemconfig(quote_text, text = get_quote())
canvas.grid(row = 0, column = 0)

kanye_img = PhotoImage(file = "kanye.png")
kanye_button = Button(image = kanye_img, highlightthickness = 0, command = get_quote)
kanye_button.grid(row = 1, column = 0)

window.mainloop()
