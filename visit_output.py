from tkinter import *


def btn_clicked():
    print("Button Clicked")

def visitOutput(visiting_places):
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

    background_img = PhotoImage(file = f"assets/Visit_images/background.png")
    background = canvas.create_image(
        439.0, 292.5,
        image=background_img)

    img0 = PhotoImage(file = f"assets/Visit_images/img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b0.place(
        x = 68, y = 13,
        width = 140,
        height = 42)

    img1 = PhotoImage(file = f"assets/Visit_images/img1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b1.place(
        x = 361, y = 13,
        width = 140,
        height = 42)

    img2 = PhotoImage(file = f"assets/Visit_images/img2.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b2.place(
        x = 653, y = 13,
        width = 140,
        height = 41)

    img3 = PhotoImage(file = f"assets/Visit_images/img3.png")
    b3 = Button(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b3.place(
        x = 668, y = 72,
        width = 193,
        height = 38)

    img4 = PhotoImage(file = f"assets/Visit_images/img4.png")
    b4 = Button(
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b4.place(
        x = 699, y = 522,
        width = 141,
        height = 55)
    
    name1 = Label(
        window,
        text=f"{visiting_places[0]}",
        font=("Helvetica", 12, "bold"),
    )
    name1.place(x=218, y=205, width=169, height=22)
    name1.configure(foreground="white")  # Set text color to white
    name1.configure(bg="#002074")  # Set background color to blue

    name2 = Label(
        window,
        text=f"{visiting_places[1]}",
        font=("Helvetica", 12, "bold"),
    )
    name2.place(x=416, y=205, width=169, height=22)
    name2.configure(foreground="white")  # Set text color to white
    name2.configure(bg="#002074")  # Set background color to blue

    name3 = Label(
        window,
        text=f"{visiting_places[2]}",
        font=("Helvetica", 12, "bold"),
    )
    name3.place(x=102.25, y=439.58, width=169, height=22)
    name3.configure(foreground="white")  # Set text color to white
    name3.configure(bg="#002074")  # Set background color to blue
    window.resizable(False, False)

    name4 = Label(
        window,
        text=f"{visiting_places[3]}",
        font=("Helvetica", 12, "bold"),
    )
    name4.place(x=302, y=439.58, width=169, height=22)
    name4.configure(foreground="white")  # Set text color to white
    name4.configure(bg="#002074")  # Set background color to blue
    window.resizable(False, False)

    name5 = Label(
        window,
        text=f"{visiting_places[4]}",
        font=("Helvetica", 12, "bold"),
    )
    name5.place(x=502, y=439.58, width=169, height=22)
    name5.configure(foreground="white")  # Set text color to white
    name5.configure(bg="#002074")  # Set background color to blue
    window.resizable(False, False)

    window.mainloop()
