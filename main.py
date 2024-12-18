from PIL import Image

with Image.open("./asset/cat1.jpg") as img:
    if img is None:
        print("Error: failed loading image file")
    else:
        print("Successfully loaded image!")
        print(f"Image size: {img.size[0]} x {img.size[1]}")
