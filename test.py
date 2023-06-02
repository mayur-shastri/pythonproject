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
# import tkinter as tk

# def process_data():
#     input_data = entry.get()
#     processed_data = input_data[::-1]
#     show_processed_data(processed_data)

# def show_processed_data(data):
#     top = tk.Toplevel(root)
#     top.title("Processed Data")
#     label = tk.Label(top, text="Processed Data: " + data)
#     label.pack()

# root = tk.Tk()
# root.title("Data Processing App")

# entry = tk.Entry(root)
# entry.pack()

# process_button = tk.Button(root, text="Process Data", command=process_data)
# process_button.pack()

# root.mainloop()
