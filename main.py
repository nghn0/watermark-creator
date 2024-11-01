import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image, ImageFont, ImageDraw

file = ""
img = None


def upload_pic():
    global file
    file = filedialog.askopenfilename()
    img = Image.open(file)
    img = img.resize((int(img.width * 0.23), int(img.height * 0.23)))
    im = ImageTk.PhotoImage(img)
    image_label = tk.Label(upload, image=im)
    image_label.image = im
    image_label.grid(row=2, column=0)
    label.config(text="Uploaded Image")


def watermark_creator():
    global img
    if not file:
        messagebox.showinfo("Upload image", "You have not uploaded an Image")
    else:
        img = Image.open(file)
        size = (img.width % img.height) / 10
        font = ImageFont.truetype("Arial", size)
        draw = ImageDraw.Draw(img)
        for y in range(0, img.height, int(img.height * 0.45)):
            for x in range(0, img.width, int(img.width * 0.45)):
                draw.text((x, y), f"{water_entry.get()}", (156, 155, 152), font=font)


        preview()


def preview():
    preview_label.config(text="Preview of watermarked image")
    img_p = img.resize((int(img.width * 0.15), int(img.height * 0.15)))
    im = ImageTk.PhotoImage(img_p)
    image_label = tk.Label(watermarked, image=im)
    image_label.image = im
    image_label.grid(row=1, column=0, columnspan=2)
    show_full.grid(row=2, column=0, columnspan=2)


def save_img():
    if not file:
        messagebox.showinfo("Upload image", "You have not uploaded an Image")
    else:
        img.save(f"{save_entry.get()}")
        messagebox.showinfo("Successful", "Image was saved Successfully")


def show_full_img():
    img.show()


root = tk.Tk()
root.title("WaterMark-Creator")

upload = tk.LabelFrame(root, text="Upload Image", padx=10, pady=10, height=100, width=100)

upload_button = tk.Button(upload, text="Upload", command=upload_pic)
upload_button.grid(row=3, column=0)

label = tk.Label(upload, text="Upload An Image")
label.grid(row=0, column=0)

upload.grid(row=0, column=0)

watermark = tk.LabelFrame(root, text="WaterMark Text")

water_label = tk.Label(watermark, text="Enter a text to WaterMark: ")
water_label.grid(row=0, column=0)

water_entry = tk.Entry(watermark)
water_entry.grid(row=0, column=1)

water_button = tk.Button(watermark, text="Submit", command=watermark_creator)
water_button.grid(row=1, column=0, columnspan=2)

watermark.grid(row=0, column=1, padx=10, pady=10)

watermarked = tk.LabelFrame(root, text="WaterMarked Image", pady=10, padx=10)

preview_label = tk.Label(watermarked, text="Upload image to preview watermarked image")
preview_label.grid(row=0, column=0, columnspan=2)

show_full = tk.Button(watermarked, text="Show Full Image", command=show_full_img)

watermarked.grid(row=1, column=0)

save_lf = tk.LabelFrame(root, text="Save Image", padx=10, pady=10)

save_label = tk.Label(save_lf, text="Enter file name with extension (jpg, png): ")
save_label.grid(row=0, column=0)

save_entry = tk.Entry(save_lf)
save_entry.grid(row=0, column=1)

save = tk.Button(save_lf, text="Save", command=save_img)
save.grid(row=1, column=0, columnspan=2)

save_lf.grid(row=1, column=1)




root.mainloop()
