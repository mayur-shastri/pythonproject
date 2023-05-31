from tkinter import *
from PIL import ImageTk, Image
import requests
from io import BytesIO
from package_maker import packageMaker

def btn_clicked():
    print("Button Clicked")
    # Add your code to switch to page 2

def page1(window):
    window.geometry("893x560")
    window.configure(bg="#ffffff")
    canvas = Canvas(
        window,
        bg="#ffffff",
        height=560,
        width=893,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)
    background_img = PhotoImage(file=f"background.png")
    background = canvas.create_image(
        446.5, 280.0,
        image=background_img)

    img0 = PhotoImage(file=f"img0.png")
    b0 = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    b0.place(
        x=579, y=464,
        width=219,
        height=46)

    days_img = PhotoImage(file=f"img_textBox0.png")
    days_bg = canvas.create_image(
        688.5, 311.5,
        image=days_img)

    days = Entry(
        bd=0,
        bg="#ebdfff",
        highlightthickness=0)

    days.place(
        x=594.5, y=296,
        width=188.0,
        height=29)

    budget_img = PhotoImage(file=f"img_textBox1.png")
    budget_bg = canvas.create_image(
        689.5, 224.5,
        image=budget_img)

    budget = Entry(
        bd=0,
        bg="#ebdfff",
        highlightthickness=0)

    budget.place(
        x=595.5, y=209,
        width=188.0,
        height=29)

    whereto_img = PhotoImage(file=f"img_textBox2.png")
    whereto_bg = canvas.create_image(
        688.5, 137.5,
        image=whereto_img)

    whereto = Entry(
        bd=0,
        bg="#ebdfff",
        highlightthickness=0)

    whereto.place(
        x=594.5, y=122,
        width=188.0,
        height=29)

    travelers_img = PhotoImage(file=f"img_textBox3.png")
    travelers_bg = canvas.create_image(
        687.5, 398.5,
        image=travelers_img)

    travelers = Entry(
        bd=0,
        bg="#ebdfff",
        highlightthickness=0)

    travelers.place(
        x=593.5, y=383,
        width=188.0,
        height=29)

def page2(window):
    window.geometry("880x575")
    window.configure(bg="#ffffff")
    canvas = Canvas(
        window,
        bg="#ffffff",
        height=575,
        width=880,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file="background.png")
    background = canvas.create_image(440.0, 287.5, image=background_img)

    img0 = PhotoImage(file="img0.png")
    b0 = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat"
    )
    b0.place(x=67, y=11, width=158, height=47)

    img1 = PhotoImage(file="img1.png")
    b1 = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat"
    )
    b1.place(x=361, y=11, width=158, height=47)

    img2 = PhotoImage(file="img2.png")
    b2 = Button(
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat"
    )
    b2.place(x=655, y=11, width=158, height=47)

    response = requests.get(
        "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1b/7e/71/7e/caption.jpg?w=300&;h=300&;s=1"
    )  # Replace with the URL of your network image
    image = Image.open(BytesIO(response.content))
    image = image.resize((346, 340), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    image_label = Label(window, image=image)
    image_label.place(x=95, y=149)

    text_label = Label(
        window,
        text="Dynamic Text",
        font=("Arial", 12, "bold"),
    )
    text_label.place(x=464, y=214, width=138, height=40)
    text_label.configure(foreground="white")  # Set text color to white
    text_label.configure(bg="blue")  # Set background color to blue

    text_label2 = Label(
        window,
        text="4.5/5",
        font=("Arial", 12, "bold"),
    )
    text_label2.place(x=507, y=432, width=35, height=22)
    text_label2.configure(foreground="white")  # Set text color to white
    text_label2.configure(bg="blue")  # Set background color to blue

    text_label3 = Label(
        window,
        text="6900 reviews",
        font=("Arial", 12, "bold"),
    )
    text_label3.place(x=648, y=430, width=98, height=22)
    text_label3.configure(foreground="white")  # Set text color to white
    text_label3.configure(bg="blue")  # Set background color to blue

    text_label4 = Label(
        window,
        text="₹69000",
        font=("Arial", 12, "bold"),
    )
    text_label4.place(x=687, y=176, width=71, height=26)
    text_label4.configure(foreground="white")  # Set text color to white
    text_label4.configure(bg="blue")  # Set background color to blue

    text_label5 = Label(
        window,
        text="Pondicherry",
        font=("Arial", 12, "bold"),
    )
    text_label5.place(x=492, y=173, width=122, height=24)
    text_label5.configure(foreground="white")  # Set text color to white
    text_label5.configure(bg="blue")

# Create the main window
window = Tk()

# Call the page1 function to show the initial page
page1(window)

# Start the main event loop
window.mainloop()
