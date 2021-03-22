from tkinter import *
import pandas as pd
from random import choice

FRENCH_WORDS = "data/french_words.csv"
APP_NAME = "Flash Card"
BACKGROUND_COLOR = "#B1DDC6"
RIGHT_PATH = "images/right.png"
WRONG_PATH = "images/wrong.png"
CARD_BACK_PATH = "images/card_back.png"
CARD_FRONT_PATH = "images/card_front.png"
CARD_WIDTH = 800
CARD_HEIGHT = 526
LANGUAGE1 = "FRENCH"
LANGUAGE2 = "ENGLISH"

TEXT_COLOR_LANGUAGE1 = "black"
TEXT_COLOR_LANGUAGE2 = "white"
TIME_BEFORE_FLIPPING_CARD = 4000  # 4 SECONDS
# ----------------FUNCTIONALITY------------------------##
to_learn = {}
current_card = {}


def reset_db():
    global to_learn
    french_words = pd.read_csv(FRENCH_WORDS)
    to_learn = french_words.to_dict(orient = "records")


try:
    to_learn_data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    reset_db()
else:
    to_learn = to_learn_data.to_dict(orient = "records")


def next_card():
    global flip_timer, current_card
    screen.after_cancel(flip_timer)
    current_card = choice(to_learn)
    french_word = current_card[LANGUAGE1.title()]
    canvas.itemconfig(card_title, text = LANGUAGE1, fill = TEXT_COLOR_LANGUAGE1)
    canvas.itemconfig(card_word, text = french_word, fill = TEXT_COLOR_LANGUAGE1)
    canvas.itemconfig(card_bg, image = card_front)
    screen.after(TIME_BEFORE_FLIPPING_CARD, func = flip_card)  # to  start over the waiting period again


def flip_card():
    english_word = current_card[LANGUAGE2.title()]
    canvas.itemconfig(card_title, text = LANGUAGE2, fill = TEXT_COLOR_LANGUAGE2)
    canvas.itemconfig(card_word, text = english_word, fill = TEXT_COLOR_LANGUAGE2)
    canvas.itemconfig(card_bg, image = card_back)


def known_word():
    screen.after_cancel(flip_timer)
    # the current functionality in the next lines resets the database of to_learn to the french_words database,
    # vut with the commented lines in to_learn_is_empty it would show the user a notification that the db is empty
    # and that it starts  over.
    # a few bugs are still to fix
    if to_learn_is_empty():
        reset_db()
    else:
        to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index = False)
    next_card()


def to_learn_is_empty():
    if LANGUAGE1.title() not in to_learn:
        # screen.after_cancel(flip_timer)
        # canvas.itemconfig(card_title, text = "You have gone through all the cards", fill = TEXT_COLOR_LANGUAGE1)
        # canvas.itemconfig(card_word, text = "we will start over", fill = TEXT_COLOR_LANGUAGE1)
        # screen.after(TIME_BEFORE_FLIPPING_CARD, func = next_card)  #
        return True
    return False

# ------------------- UI DESIGN ------------------------ #
screen = Tk()
screen.title(APP_NAME)
screen.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)
flip_timer = screen.after(TIME_BEFORE_FLIPPING_CARD, func = flip_card)
canvas = Canvas(width = CARD_WIDTH, height = CARD_HEIGHT)
card_front = PhotoImage(file = CARD_FRONT_PATH)
card_bg = canvas.create_image(CARD_WIDTH / 2, CARD_HEIGHT / 2, image = card_front)

card_title = canvas.create_text(CARD_WIDTH / 2, CARD_HEIGHT / 3, font = ("Ariel", 40, "italic"))
card_word = canvas.create_text(CARD_WIDTH / 2, CARD_HEIGHT / 2, font = ("Ariel", 70, "bold"))
canvas.config(bg = BACKGROUND_COLOR, highlightthickness = 0)
canvas.grid(row = 0, column = 0, columnspan = 2)
# Back card
card_back = PhotoImage(file = CARD_BACK_PATH)
# adding the right/learned button (to the right)
right_img = PhotoImage(file = RIGHT_PATH)
known_word_button = Button(image = right_img, highlightthickness = 0, command = known_word)
known_word_button.grid(row = 1, column = 1)
# adding the wrong/to-learn button (to the left)
cross_img = PhotoImage(file = WRONG_PATH)
to_learn_button = Button(image = cross_img, highlightthickness = 0,command=next_card)
to_learn_button.grid(row = 1, column = 0)
next_card()
screen.mainloop()
