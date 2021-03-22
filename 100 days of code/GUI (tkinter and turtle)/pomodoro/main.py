from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_sessions():
    global timer
    global reps
    if reps > 0:
        reps -= 1
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    timer_label.config(text = "Timer")
    checkmarks.config(text = "")


def restart_timer():
    global timer
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    timer_label.config(text = "Timer")
    checkmarks.config(text = "")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    # to fix the bug of clicking the start button multiple times
    # count_down(0)
    # reset_timer()
    global reps
    reps += 1
    if reps % 2 != 0:  # first, third, 4th,... etc rep
        if reps == 1:
            work_sessions = reps
        elif reps % 2 != 0:
            work_sessions = reps // 2 + reps % 2
        else:
            work_sessions = reps // 2
        timer_label.config(text = f"Work Session:{work_sessions}", fg = GREEN)
        count_down(60 * WORK_MIN)
        work_sessions += 1

    elif reps % 8 == 0:  # after 4 sets of work, and three mini breaks,  time for a long break
        timer_label.config(text = "Take a Break", fg = RED)
        count_down(60 * LONG_BREAK_MIN)

    elif reps % 2 == 0:  # after each work set, time for a  short break (won't get here if it's the 8th rep)
        timer_label.config(text = "Short Break", fg = PINK)
        count_down(60 * SHORT_BREAK_MIN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text, text = f"{count // 60}:{count_seconds}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        work_sessions = reps // 2
        marks = ""
        for _ in range(0, work_sessions):
            marks += "✅\n"
        checkmarks.config(text = f"{marks}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx = 50, pady = 50, bg = YELLOW)  # set the padding, and the window's background color

# adding the timer label
timer_label = Label(text = "Timer", fg = GREEN, bg = YELLOW, font = (FONT_NAME, 35))
timer_label.grid(row = 0, column = 1)
# set up the canvas with the background picture
canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato_image = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = tomato_image)
timer_text = canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME, 30, "bold"))
canvas.grid(row = 1, column = 1)

# adding the start and reset Buttons
start = Button(text = "Start", font = (FONT_NAME, 15), command = start_timer)
start.grid(row = 2, column = 0)
reset = Button(text = "Reset", font = (FONT_NAME, 15), command = reset_sessions)
reset.grid(row = 2, column = 1, pady = 20)
restart = Button(text = "Restart", font = (FONT_NAME, 15), command = restart_timer)
restart.grid(row = 2, column = 2)

# adding checkmarks
checkmarks = Label(text = "", fg = GREEN, bg = YELLOW, font = (FONT_NAME, 10))
checkmarks.grid(row = 3, column = 1)

window.mainloop()
