from src.core.display import show_image
from src.core.path import image_path
from src.core.loader import load_image
from src.operations.histogram import show_histogram

def run():

    path = image_path("image.png")
    img = load_image(path, grayscale=True)

    show_image("Image", img)
    show_histogram(img)