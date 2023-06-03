from tkinter import *
from PIL import ImageTk, Image
import requests
from io import BytesIO

def clicked():
    pass
def btn_clicked(
    f,
    root,
    placeName,
    hotelName,
    hotel_image,
    hotel_price,
    hotel_rating_reviews,
    resturant_names,
    resturant_stars,
    resturant_images,
    visiting_places,
):
    if f == 1:
        stayOutput(
            root,
            placeName,
            hotelName,
            hotel_image,
            hotel_price,
            hotel_rating_reviews,
           resturant_names,
           resturant_images,
           resturant_stars,
           visiting_places,
        )
    if f == 2:
        eatOutput(
            root,
            placeName,
            hotelName,
            hotel_image,
            hotel_price,
            hotel_rating_reviews,
           resturant_names,
           resturant_images,
           resturant_stars,
            visiting_places,
        )
    if f == 3:
        visitOutput(
            root,
            placeName,
            hotelName,
            hotel_image,
            hotel_price,
            hotel_rating_reviews,
            resturant_names,
            resturant_images,
            resturant_stars,
            visiting_places,
        )


def stayOutput(
    root,
    placeName,
    hotelName,
    hotel_image,
    hotel_price,
    hotel_rating_reviews,
    resturant_names,
    resturant_images,
    resturant_stars,
    visiting_places,
):
    root.withdraw()
    window = Toplevel(root)  # Create a Toplevel window
    hotel_stars = hotel_rating_reviews[0:3]
    hotel_reviews = hotel_rating_reviews[16:]

    window.geometry("880x575")
    window.configure(bg="#ffffff")
    canvas = Canvas(
        window,
        bg="#ffffff",
        height=575,
        width=880,
        bd=0,
        highlightthickness=0,
        relief="ridge",
    )
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file="assets/Stay_Output_Page/background.png")
    background = canvas.create_image(440.0, 287.5, image=background_img)

    img0 = PhotoImage(file="assets/Stay_Output_Page/img0.png")
    b0 = Button(
        window,
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: btn_clicked(
            1,
            window,
            placeName,
            hotelName,
            hotel_image,
            hotel_price,
            hotel_rating_reviews,
            resturant_names,
            resturant_images,
            resturant_stars,
            visiting_places,
        ),
        relief="flat",
    )
    b0.place(x=67, y=11, width=158, height=47)

    img1 = PhotoImage(file="assets/Stay_Output_Page/img1.png")
    b1 = Button(
        window,
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: btn_clicked(
            2,
            window,
            placeName,
            hotelName,
            hotel_image,
            hotel_price,
            hotel_rating_reviews,
            resturant_names,
            resturant_images,
            resturant_stars,
            visiting_places,
        ),
        relief="flat",
    )
    b1.place(x=361, y=11, width=158, height=47)

    img2 = PhotoImage(file="assets/Stay_Output_Page/img2.png")
    b2 = Button(
        window,
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: btn_clicked(
            3,
            window,
            placeName,
            hotelName,
            hotel_image,
            hotel_price,
            hotel_rating_reviews,
            resturant_names,
            resturant_images,
            resturant_stars,
            visiting_places,
        ),
        relief="flat",
    )
    b2.place(x=655, y=11, width=158, height=47)

    response = requests.get(
        f"{hotel_image}"
    )  # Replace with the URL of your network image
    image = Image.open(BytesIO(response.content))
    image = image.resize((346, 340), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    image_label = Label(window, image=image)
    image_label.place(x=95, y=149)

    text_label = Label(
        window,
        text=f"{hotelName}",
        font=("Helvetica", 12, "bold"),
    )
    text_label.place(x=464, y=214, width=298, height=40)
    text_label.configure(foreground="white")  # Set text color to white
    text_label.configure(bg="#002074")  # Set background color to blue

    text_label2 = Label(
        window,
        text=f"{hotel_stars}/5",
        font=("Helvetica", 12, "bold"),
    )
    text_label2.place(x=497, y=434, width=43, height=21)
    text_label2.configure(foreground="white")  # Set text color to white
    text_label2.configure(bg="#002074")  # Set background color to blue

    text_label3 = Label(
        window,
        text=f"{hotel_reviews}",
        font=("Helvetica", 12, "bold"),
    )
    text_label3.place(x=667, y=433, width=102, height=22)
    text_label3.configure(foreground="white")  # Set text color to white
    text_label3.configure(bg="#002074")  # Set background color to blue

    text_label4 = Label(
        window,
        text=f"₹{hotel_price}",
        font=("Helvetica", 12, "bold"),
    )
    text_label4.place(x=687, y=176, width=71, height=26)
    text_label4.configure(foreground="white")  # Set text color to white
    text_label4.configure(bg="#002074")  # Set background color to blue

    text_label5 = Label(
        window,
        text=f"{placeName}",
        font=("Helvetica", 12, "bold"),
    )
    text_label5.place(x=490, y=176, width=122, height=24)
    # text_label5.place(x=492, y=173, width=122, height=24)
    text_label5.configure(foreground="white")  # Set text color to white
    text_label5.configure(bg="#002074")  # Set background color to blue
    window.resizable(False, False)
    window.mainloop()


# stayOutput('pondicherry','hotelName','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmX8VjCUeVbyF-0pBN0BSmLJ5_mJ4Z4pcDsckmNoeH&s',85)


def visitOutput(
    root,
    placeName,
    hotelName,
    hotel_image,
    hotel_price,
    hotel_rating_reviews,
    resturant_names,
    resturant_images,
    resturant_stars,
    visiting_places,
):
    root.withdraw()
    window = Toplevel(root)

    window.geometry("880x575")
    window.configure(bg="#ffffff")
    canvas = Canvas(
        window,
        bg="#ffffff",
        height=575,
        width=880,
        bd=0,
        highlightthickness=0,
        relief="ridge",
    )
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=f"assets/Visit_images/background.png")
    background = canvas.create_image(439.0, 292.5, image=background_img)

    img0 = PhotoImage(file=f"assets/Visit_images/img0.png")
    b0 = Button(
        window,
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: btn_clicked(
            1,
            window,
            placeName,
            hotelName,
            hotel_image,
            hotel_price,
            hotel_rating_reviews,
            visiting_places,
        ),
        relief="flat",
    )

    b0.place(x=68, y=13, width=140, height=42)

    img1 = PhotoImage(file=f"assets/Visit_images/img1.png")
    b1 = Button(
        window,
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: btn_clicked(
            2,
            window,
            placeName,
            hotelName,
            hotel_image,
            hotel_price,
            hotel_rating_reviews,
            visiting_places,
        ),
        relief="flat",
    )

    b1.place(x=361, y=13, width=140, height=42)

    img2 = PhotoImage(file=f"assets/Visit_images/img2.png")
    b2 = Button(
        window,
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: btn_clicked(
            3,
            window,
            placeName,
            hotelName,
            hotel_image,
            hotel_price,
            hotel_rating_reviews,
            visiting_places,
        ),
        relief="flat",
    )

    b2.place(x=653, y=13, width=140, height=41)

    img3 = PhotoImage(file=f"assets/Visit_images/img3.png")
    b3 = Button(
        window,
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        command=clicked,
        relief="flat",
    )

    b3.place(x=668, y=72, width=193, height=38)

    img4 = PhotoImage(file=f"assets/Visit_images/img4.png")
    b4 = Button(
        window,
        image=img4,
        borderwidth=0,
        highlightthickness=0,
        command=clicked,
        relief="flat",
    )

    b4.place(x=699, y=522, width=141, height=55)

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


def eatOutput(
    root,
    placeName,
    hotelName,
    hotel_image,
    hotel_price,
    hotel_rating_reviews,
    resturant_names,
    resturant_images,
    resturant_stars,
    visiting_places,
):
    root.withdraw()
    window = Toplevel(root)

    window.geometry("880x575")
    window.configure(bg="#ffffff")
    canvas = Canvas(
        window,
        bg="#ffffff",
        height=575,
        width=880,
        bd=0,
        highlightthickness=0,
        relief="ridge",
    )
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=f"assets/eat_images/background.png")
    background = canvas.create_image(526.5, 304.0, image=background_img)

    img0 = PhotoImage(file=f"assets/eat_images/img0.png")
    b0 = Button(
        window,
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: btn_clicked(
            2,
            window,
            placeName,
            hotelName,
            hotel_image,
            hotel_price,
            hotel_rating_reviews,
            visiting_places,
        ),
        relief="flat",
    )

    b0.place(x=366, y=10, width=158, height=48)

    img1 = PhotoImage(file=f"assets/eat_images/img1.png")
    b1 = Button(
        window,
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: btn_clicked(
            3,
            window,
            placeName,
            hotelName,
            hotel_image,
            hotel_price,
            hotel_rating_reviews,
            visiting_places,
        ),
        relief="flat",
    )

    b1.place(x=660, y=11, width=158, height=47)

    img2 = PhotoImage(file=f"assets/eat_images/img2.png")
    b2 = Button(
        window,
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: btn_clicked(
            1,
            window,
            placeName,
            hotelName,
            hotel_image,
            hotel_price,
            hotel_rating_reviews,
            visiting_places,
        ),
        relief="flat",
    )

    b2.place(x=72, y=11, width=158, height=47)

    img3 = PhotoImage(file=f"assets/eat_images/img3.png")
    b3 = Button(
        window,
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        command=clicked,
        relief="flat",
    )

    b3.place(x=378, y=514, width=142, height=61)

    #resturant 1 name: 
    name1 = Label(
        window,
        text=f"{resturant_names[0]}",
        font=("Helvetica", 12, "bold"),
    )
    name1.place(x=61, y=326, width=201, height=23)
    name1.configure(foreground="white")  # Set text color to white
    name1.configure(bg="#002074")


    #resturant 2 name: 
    name2 = Label(
        window,
        text=f"{resturant_names[1]}",
        font=("Helvetica", 12, "bold"),
    )
    name2.place(x=341.83, y=327.32, width=86, height=30)
    name2.configure(foreground="white")  # Set text color to white
    name2.configure(bg="#002074")
    #resturant 3 name: 
    name3 = Label(
        window,
        text=f"{resturant_names[2]}",
        font=("Helvetica", 12, "bold"),
    )
    name3.place(x=621.83, y=328.32, width=86, height=30)
    name3.configure(foreground="white")  # Set text color to white
    name3.configure(bg="#002074")
    

    window.resizable(False, False)
    window.mainloop()
