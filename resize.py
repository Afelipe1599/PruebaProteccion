"""Modulo PIL."""
from PIL import Image

def resize(name):
    """Fuction resize."""
    image = Image.open(name)
    width, height = image.size
    if height > width:
        size = 796, 1123
        image.thumbnail(size, Image.ANTIALIAS)
        image.save(name, "JPEG")
    else:
        size = 1123, 796
        image.thumbnail(size, Image.ANTIALIAS)
        image.save(name, "JPEG")