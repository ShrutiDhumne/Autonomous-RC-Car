"""Image helpers"""
import time
from PIL import Image

def save_image_with_direction(stream, direction):
    """Save image"""
    stream.seek(0)
    image = Image.open(stream)
    img = (str(time.time()) + "-" + direction + ".jpg")
    image.save('data/img', format="JPEG")
