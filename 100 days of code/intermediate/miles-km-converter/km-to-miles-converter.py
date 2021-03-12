from tkinter import *


def km_to_miles():
    if miles_input.get() == "" or miles_spinbox.focus_force():
        miles = float(miles_spinbox.get())
        km = miles / 1.609344
        km_result.config(text = round(km, 2))
    else:
        miles = float(miles_input.get())
        km = miles / 1.609344
        km_result.config(text = f"{round(km, 2)}")


window = Tk()
window.title("Kilometers to Miles Converter")
window.config(padx = 15, pady = 15, )

miles_spinbox = Spinbox(from_ = float(0), to = float(1000), width = 10, command = km_to_miles)
miles_spinbox.grid(column = 0, row = 0)
miles_input = Entry(width = 7)
miles_input.grid(column = 1, row = 0)

miles_label = Label(text = "Km")
miles_label.grid(column = 2, row = 0)
is_equal = Label(text = "is equal to")
is_equal.grid(column = 0, row = 1)

km_label = Label(text = "Miles")
km_label.grid(column = 2, row = 1)

km_result = Label(text = "0")
km_result.grid(column = 1, row = 1)

calculate_button = Button(text = "Calculate", command = km_to_miles)
calculate_button.grid(column = 1, row = 2)

window.mainloop()
