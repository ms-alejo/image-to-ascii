# Image to ASCII Art

This Python script converts images (JPEG format) into ASCII art. It handles image resizing, brightness conversion, and EXIF orientation to ensure accurate output. It also provides an option to invert the image's brightness for different visual effects.

![Screenshot 2024-12-18 004846](https://github.com/user-attachments/assets/642cd86f-9bae-4ebd-9751-41bdf32e4a46)

## Features

*   **Brightness Conversion:** Converts pixel data to brightness values using a weighted average for more accurate grayscale representation.
*   **ASCII Conversion:** Maps brightness values to a defined set of ASCII characters.
*   **Inversion Option:** Allows inverting the image brightness for a different visual effect via command-line argument.

## How to Use

1.  **Clone the repository (optional):**

    ```bash
    git clone https://github.com/ms-alejo/image-to-ascii.git
    cd image-to-ascii
    pip install -r requirements.txt
    ```

2.  **Place your image:** Put the image you want to convert (JPEG format) in the `./asset/` directory. You can change this in the `main()` function if needed.

3.  **Run the script:**

    *   **Normal conversion:**

        ```bash
        python main.py
        ```

    *   **Inverted conversion:**

        ```bash
        python main.py invert
        ```
