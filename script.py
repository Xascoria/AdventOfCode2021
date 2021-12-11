## Document IDs blurness detection

import cv2
import pickle
from skimage.filters import laplace, sobel, roberts, farid, scharr, prewitt
import numpy as np

## Note that the model might not be stored here depending on the structure of the frontend/backend
saved_model_path = "Result/gradient_desc_model.sav"
loaded_model = pickle.load(open(saved_model_path, 'rb'))

def get_image_data(image_path):
    image = cv2.imread(image_path)
    grayscaled_img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    output = []

    ## Farid
    far = farid(grayscaled_img)
    output.append(far.var())

    ## Laplace
    lap = laplace(grayscaled_img)
    output.extend([lap.var(), np.amax(lap)])

    ## Og laplace
    oglap = cv2.Laplacian(grayscaled_img, cv2.CV_64F).var()
    output.append(oglap)

    ## Sobel
    sob = sobel(grayscaled_img)
    output.extend([sob.mean(), sob.var()])

    ## Roberts
    rob = roberts(grayscaled_img)
    output.extend([rob.mean(), rob.var()])

    ## Scharr
    sch = scharr(grayscaled_img)
    output.extend([sch.mean(), sch.var()])

    ## Prewitt
    pre = prewitt(grayscaled_img)
    output.extend([pre.mean(), pre.var()])
    
    return output

def is_image_blur(image_path):
    return loaded_model.predict([get_image_data(image_path)])[0]
