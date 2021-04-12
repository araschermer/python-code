from tkinter import *
import requests
from random import choice


def get_quote() -> str:
    """ returns a kanye quote either from the kanye.rest api or from the cached  quote in the data file"""
    try:
        read_cached = False
        response = requests.get(url="https://api.kanye.rest/")
        # print(response.status_code)
        response.raise_for_status()
    except:
        read_cached = True
        # ignore any link/connection errors, since it some quotes are cached that can be shown if an error occurs

    else:
        if response.status_code == 200:
            data = response.json()
            # get the quote/text from the response
            text = data["quote"]
            print(text)
            # caching the quotes to view in case no internet connection is available or a bad response is returned
            save_kanye_quotes(text)
            #  update the canvas text with the new quote
            canvas.itemconfig(quote_text, text=text)
            return text
    if read_cached:
        with open('kanye_quotes.txt', 'r') as f:
            kanye_quotes = f.readlines()
            text = choice(kanye_quotes)
            canvas.itemconfig(quote_text, text=text)
            return text


def save_kanye_quotes(kanye_quote: str):
    """ save kanye quotes in a local file"""
    with open('kanye_quotes.txt', 'a') as f:
        f.write(f"{kanye_quote}\n")


# create window
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)
# create canvas
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
# add background_img to canvas
canvas.create_image(150, 207, image=background_img)
# add text field to show the quote
quote_text = canvas.create_text(150, 207, width=250, font=("Arial", 20, "bold"), fill="white")
# retrieve a random quote from the get_quote method
canvas.itemconfig(quote_text, text=get_quote())
# add canvas to the window grid
canvas.grid(row=0, column=0)
# create button
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
