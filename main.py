from tkinter import *


def miles_km():
    miles = int(miles_input.get())
    kilometer_result.config(text=f"{(miles * 1.60)}")


window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=10, pady=10)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result = Label(text="0")
kilometer_result.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
