# from tkinter import Tk, Label
# from PIL import ImageTk, Image
# import requests
# from io import BytesIO

# # Create a Tkinter window
# window = Tk()

# # URL of the image
# image_url = "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1b/7e/71/7e/caption.jpg?w=300&;h=300&;s=1"
# # Request the image from the URL
# response = requests.get(image_url)
# image_data = response.content

# # Convert the image data into a format that Tkinter can use
# image = Image.open(BytesIO(image_data))
# tk_image = ImageTk.PhotoImage(image)

# # Create a label and display the image
# image_label = Label(window, image=tk_image)
# image_label.pack()

# # Start the Tkinter event loop
# window.mainloop()