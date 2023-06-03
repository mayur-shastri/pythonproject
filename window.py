from tkinter import *
from scrapper import scrapperFuncN
from package_maker import packageMaker
import threading


def explore_clicked(whereto, budget, days, travelers):
    days_contents = int(days.get())
    budget_contents = int(budget.get())
    whereto_contents = whereto.get()
    travelers_contents = int(travelers.get())
    print("-----------------------------")
    print("Destination: ", whereto_contents)
    print("-----------------------------")
    print("Budget: ", budget_contents)
    print("-----------------------------")
    print("Day: ", days_contents)
    print("---------------------")
    print("Travelers = ", travelers_contents)
    packageMaker(
        window, whereto_contents, budget_contents, days_contents, travelers_contents
    )


window = Tk()

window.geometry("893x560")
window.configure(bg="#ffffff")
canvas = Canvas(
    window,
    bg="#ffffff",
    height=560,
    width=893,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"assets/First_page/background.png")
background = canvas.create_image(446.5, 280.0, image=background_img)

img0 = PhotoImage(file=f"assets/First_page/img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: explore_clicked(whereto, budget, days, travelers),
    relief="flat",
)

b0.place(x=579, y=464, width=219, height=46)

days_img = PhotoImage(file=f"assets/First_page/img_textBox0.png")
days_bg = canvas.create_image(688.5, 311.5, image=days_img)

days = Entry(bd=0, bg="#ebdfff", highlightthickness=0)

days.place(x=594.5, y=296, width=188.0, height=29)

budget_img = PhotoImage(file=f"assets/First_page/img_textBox1.png")
budget_bg = canvas.create_image(689.5, 224.5, image=budget_img)

budget = Entry(bd=0, bg="#ebdfff", highlightthickness=0)

budget.place(x=595.5, y=209, width=188.0, height=29)

whereto_img = PhotoImage(file=f"assets/First_page/img_textBox2.png")
whereto_bg = canvas.create_image(688.5, 137.5, image=whereto_img)

whereto = Entry(bd=0, bg="#ebdfff", highlightthickness=0)

whereto.place(x=594.5, y=122, width=188.0, height=29)

travelers_img = PhotoImage(file=f"assets/First_page/img_textBox3.png")
travelers_bg = canvas.create_image(687.5, 398.5, image=travelers_img)

travelers = Entry(bd=0, bg="#ebdfff", highlightthickness=0)

travelers.place(x=593.5, y=383, width=188.0, height=29)

window.resizable(False, False)
window.mainloop()
