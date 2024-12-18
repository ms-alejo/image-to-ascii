from PIL import Image, ImageOps

# constants
ASCII_CHARS = '`^",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'


def get_pixel_matrix(image, target_height):
    try:
        image = ImageOps.exif_transpose(image)
        if image is None:
            raise ValueError("Image is not loaded properly.")

        # resize
        aspect_ratio = image.width / image.height
        target_width = int(target_height * aspect_ratio)
        image = image.resize((target_width, target_height))

        pixels = list(image.getdata())
        return [pixels[i : i + image.width] for i in range(0, len(pixels), image.width)]

    except Exception as e:
        raise RuntimeError(f"Error generating pixel matrix: {e}")


def convert_to_brightness(matrix):
    new_matrix = []

    for row in matrix:
        new_matrix_row = []
        for pixel in row:
            average = (pixel[0] + pixel[1] + pixel[2]) / 3
            new_matrix_row.append(average)

        new_matrix.append(new_matrix_row)

    return new_matrix


def convert_to_ascii(matrix):
    new_matrix = []

    for row in matrix:
        new_matrix_row = []
        for pixel in row:
            ascii_as_pixel = int((pixel / 255) * (len(ASCII_CHARS) - 1))
            new_matrix_row.append(ASCII_CHARS[ascii_as_pixel])

        new_matrix.append(new_matrix_row)

    return new_matrix


# load image
try:
    with Image.open("./asset/cat1.jpg") as img:
        print("Successfully loaded image!")
        print(f"Image size: {img.size[0]} x {img.size[1]}")

        # get pixel matrix
        pixel_matrix = get_pixel_matrix(img, 100)
        # print("Iterating through the pixels:")
        # for row in pixel_matrix:
        # print(row)

        # get brightness matrix
        brightness_matrix = convert_to_brightness(pixel_matrix)
        # print("Iterating through converted pixels:")
        # for row in brightness_matrix:
        # print(row)

        # get ascii matrix
        ascii_matrix = convert_to_ascii(brightness_matrix)
        for row in ascii_matrix:
            print("".join(row))

except FileNotFoundError:
    print("Error: Image file not found.")
    exit()
except Exception as e:
    print(f"Error: Unable to open image. {e}")
    exit()
