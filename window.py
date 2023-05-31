from tkinter import *
from scrapper import scrapperFuncN
from package_maker import packageMaker

def btn_clicked(entry1, entry2, entry3):
    entry1_contents = entry1.get()
    entry2_contents = int(entry2.get())
    entry3_contents = int(entry3.get())
    print(entry1_contents)
    print(entry2_contents)
    print(entry3_contents)
    # scrapperOutput=scrapperFuncN(entry1_contents)
    # for ele in scrapperOutput:
    #     print(ele)
    packageMaker(entry1_contents,entry2_contents,entry3_contents)

window = Tk()

window.geometry("893x560")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 560,
    width = 893,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    446.5, 280.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command=lambda: btn_clicked(destinationInput, budgetInput,stayDurationInput ),
    relief = "flat")

b0.place(
    x = 576, y = 453,
    width = 219,
    height = 46)

stayDurationInput_img = PhotoImage(file = f"img_textBox0.png")
stayDurationInput_bg = canvas.create_image(
    686.5, 377.5,
    image = stayDurationInput_img)

stayDurationInput = Entry(
    bd = 0,
    bg = "#ebdfff",
    highlightthickness = 0)

stayDurationInput.place(
    x = 592.5, y = 362,
    width = 188.0,
    height = 29)

budgetInput_img = PhotoImage(file = f"img_textBox1.png")
budgetInput_bg = canvas.create_image(
    686.5, 275.5,
    image = budgetInput_img)

budgetInput = Entry(
    bd = 0,
    bg = "#ebdfff",
    highlightthickness = 0)

budgetInput.place(
    x = 592.5, y = 260,
    width = 188.0,
    height = 29)

destinationInput_img = PhotoImage(file = f"img_textBox2.png")
destinationInput_bg = canvas.create_image(
    686.0, 173.5,
    image = destinationInput_img)

destinationInput = Entry(
    bd = 0,
    bg = "#ebdfff",
    highlightthickness = 0)

destinationInput.place(
    x = 592.5, y = 158,
    width = 187.0,
    height = 29)

window.resizable(False, False)
window.mainloop()
