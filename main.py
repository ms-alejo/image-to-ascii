from PIL import Image


def get_pixel_matrix(image, height):
    try:
        image.thumbnail((height, 200))
        pixels = list(image.getdata())
        return [pixels[i : i + image.width] for i in range(0, len(pixels), image.width)]
    except Exception as e:
        raise RuntimeError(f"Error generating pixel matrix: {e}")


# load image
try:
    with Image.open("./asset/cat1.jpg") as img:
        print("Successfully loaded image!")
        print(f"Image size: {img.size[0]} x {img.size[1]}")

        # get pixel matrix
        pixel_matrix = get_pixel_matrix(img, 100)
        print("Iterating through the pixels:")
        for row in pixel_matrix:
            print(row)

except FileNotFoundError:
    print("Error: Image file not found.")
    exit()
except Exception as e:
    print(f"Error: Unable to open image. {e}")
    exit()
