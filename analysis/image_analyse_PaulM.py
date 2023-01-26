from PIL import Image
import numpy as np

image = Image.open("./Noise.png").convert('RGBA')
image_numpy = np.array(image)
image_numpy_R = image_numpy[:,:,0].astype(np.float64)/255
image_numpy_R_flattened = image_numpy_R.reshape((-1,))


# calculer moyenne
def mean(noiseArray:list)-> float:
    return np.average(noiseArray)

print(mean(image_numpy_R_flattened))


# calculer ecart-type
def std_gap(noiseArray:list) -> float:
    return np.std(noiseArray)

print(std_gap(image_numpy_R_flattened))
