from PIL import Image

from resize import resize

def test_resize():
    resize("../PruebaCarga/1.jpg")
    image = Image.open("../PruebaCarga/1.jpg")
    assert image.width == 1123

    resize("../PruebaCarga/2.jpg")
    image = Image.open("../PruebaCarga/2.jpg")
    assert image.width == 1123

    resize("../PruebaCarga/3.jpg")
    image = Image.open("../PruebaCarga/3.jpg")
    assert image.height == 1123

    resize("../PruebaCarga/4.jpg")
    image = Image.open("../PruebaCarga/4.jpg")
    assert image.width == 1123

    resize("../PruebaCarga/5.jpg")
    image = Image.open("../PruebaCarga/5.jpg")
    assert image.width == 1123

    resize("../PruebaCarga/6.jpg")
    image = Image.open("../PruebaCarga/6.jpg")
    assert image.width == 1123    
