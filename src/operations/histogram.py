import cv2
import matplotlib.pyplot as plt

def show_histogram(image):

    hist = cv2.calcHist([image],[0],None,[256],[0,256])

    plt.plot(hist)
    plt.title("Histogram")
    plt.xlabel("Intensity")
    plt.ylabel("Pixels")

    plt.show()