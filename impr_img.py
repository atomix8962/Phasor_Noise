import matplotlib.pyplot as plt
import numpy as np

def impr_img(imgArray:list) -> None:
    img = imgArray
    plt.title("Phasor Noise Generator")
    plt.imshow(img, cmap='gray')
    plt.show()