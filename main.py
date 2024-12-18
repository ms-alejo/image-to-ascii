from PIL import Image


def get_pixel_matrix(image, height):
    try:
        image.thumbnail((height, 200))
        pixels = list(image.getdata())
        return [pixels[i : i + image.width] for i in range(0, len(pixels), image.width)]

    except Exception as e:
        raise RuntimeError(f"Error generating pixel matrix: {e}")


def convert_pixels(matrix):
    new_matrix = []

    for row in matrix:
        new_matrix_row = []
        for pixel in row:
            average = (pixel[0] + pixel[1] + pixel[2]) / 3
            new_matrix_row.append(average)

        new_matrix.append(new_matrix_row)

    return new_matrix


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

        brightness_matrix = convert_pixels(pixel_matrix)
        print("Iterating through converted pixels:")
        for row in brightness_matrix:
            print(row)

except FileNotFoundError:
    print("Error: Image file not found.")
    exit()
except Exception as e:
    print(f"Error: Unable to open image. {e}")
    exit()
