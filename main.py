from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=400)
window.config(padx=50, pady=50)
new_value = Label(text="0", font=("Arial", 20))
new_value.grid(column=1, row=0)

mile_label = Label(text="Miles", font=("Arial", 20))
mile_label.grid(column=2, row=0)

equal_to = Label(text="is equal to ", font=("Arial", 20))
equal_to.grid(column=0, row=1)

unit = Label(text="Km", font=("Arial", 20))
unit.grid(column=2, row=1)


def button_clicked():
    answer = round(int(input.get())*1.609)
    new_value.config(text=f"{answer}")


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

input = Entry(width=30)
input.grid(column=1, row=1)

window.mainloop()
