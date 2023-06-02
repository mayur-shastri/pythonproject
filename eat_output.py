from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("880x575")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 575,
    width = 880,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"assets/eat_images/background.png")
background = canvas.create_image(
    526.5, 304.0,
    image=background_img)

img0 = PhotoImage(file = f"assets/eat_images/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 366, y = 10,
    width = 158,
    height = 48)

img1 = PhotoImage(file = f"assets/eat_images/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 660, y = 11,
    width = 158,
    height = 47)

img2 = PhotoImage(file = f"assets/eat_images/img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 72, y = 11,
    width = 158,
    height = 47)

img3 = PhotoImage(file = f"assets/eat_images/img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = 378, y = 514,
    width = 142,
    height = 61)

window.resizable(False, False)
window.mainloop()
