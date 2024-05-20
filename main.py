from PIL import Image
import numpy as np

ASCII_CHARS = "@#%?*=+:. "
#ASCII_CHARS = ''.join([chr(i) for i in range(32, 127)])

def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = np.array(image)
    ascii_str = ""
    for pixel_value in pixels:
        for pixel in pixel_value:
            ascii_str += ASCII_CHARS[pixel // 32]
        ascii_str += "\n"
    return ascii_str

def image_to_ascii(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return

    image = resize_image(image, new_width)
    image = grayify(image)

    ascii_str = pixels_to_ascii(image)
    return ascii_str

if __name__ == "__main__":
    image_path = r'C:\Users\Carlos\Projects\image-to-ascii-art\images\img2.png'
    ascii_art = image_to_ascii(image_path)
    print(ascii_art)

    with open("ascii_art.txt", "w") as f:
        f.write(ascii_art)
