from tkinter import *
from PIL import ImageTk, Image
import requests
from io import BytesIO

def btn_clicked():
    print("Button Clicked")

# placeName,hotelName,stars,reviews,hotel_image,hotel_price
def stayOutput(root, placeName, hotelName, hotel_image, hotel_price,hotel_rating_reviews):
    window = Toplevel(root)  # Create a Toplevel window
    hotel_stars=hotel_rating_reviews[0:3]
    hotel_reviews=hotel_rating_reviews[16:]
    print(hotel_stars)
    print(hotel_reviews)
    
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

    background_img = PhotoImage(file="assets/Stay_Output_Page/background.png")
    background = canvas.create_image(440.0, 287.5, image=background_img)

    img0 = PhotoImage(file="assets/Stay_Output_Page/img0.png")
    b0 = Button(window,
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat"
    )
    b0.place(x=67, y=11, width=158, height=47)

    img1 = PhotoImage(file="assets/Stay_Output_Page/img1.png")
    b1 = Button(window,
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat"
    )
    b1.place(x=361, y=11, width=158, height=47)

    img2 = PhotoImage(file="assets/Stay_Output_Page/img2.png")
    b2 = Button(window,
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat"
    )
    b2.place(x=655, y=11, width=158, height=47)

    response = requests.get(f"{hotel_image}")  # Replace with the URL of your network image
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

    text_label2=Label(
        window,
        text=f"{hotel_stars}/5",
        font=("Helvetica", 12, "bold"),
    )
    text_label2.place(x=497, y=434, width=43, height=21)
    text_label2.configure(foreground="white")  # Set text color to white
    text_label2.configure(bg="#002074")  # Set background color to blue

    text_label3=Label(
        window,
        text=f"{hotel_reviews}",
        font=("Helvetica", 12, "bold"),
    )
    text_label3.place(x=667, y=433, width=102, height=22)
    text_label3.configure(foreground="white")  # Set text color to white
    text_label3.configure(bg="#002074")  # Set background color to blue

    text_label4=Label(
        window,
        text=f"₹{hotel_price}",
        font=("Helvetica", 12, "bold"),
    )
    text_label4.place(x=687, y=176, width=71, height=26)
    text_label4.configure(foreground="white")  # Set text color to white
    text_label4.configure(bg="#002074")  # Set background color to blue

    text_label5=Label(
        window,
        text=f"{placeName}",
        font=("Helvetica", 12, "bold"),
    )
    text_label5.place(x=490, y=176, width=122, height=24)
    #text_label5.place(x=492, y=173, width=122, height=24)
    text_label5.configure(foreground="white")  # Set text color to white
    text_label5.configure(bg="#002074")  # Set background color to blue
    window.resizable(False, False)
    window.mainloop()
#stayOutput('pondicherry','hotelName','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmX8VjCUeVbyF-0pBN0BSmLJ5_mJ4Z4pcDsckmNoeH&s',85)