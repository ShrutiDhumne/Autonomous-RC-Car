import os
import numpy as np
import cv2
import re

f = open("lables.txt","w+")

#We call this function during training the model
def conv_images_to_array_train():
    inputs = []
    for filename in os.listdir('data'):
        if "forward_left" in filename:
            f.write("0 0 0 0 0 1\n")
        elif "forward_right" in filename:
            f.write("0 0 0 0 1 0\n")
        elif "left" in filename:
            f.write("0 1 0 0 0 0\n")
        elif "right" in filename:
            f.write("0 0 1 0 0 0\n")
        elif "forward" in filename:
            f.write("1 0 0 0 0 0\n")
        else:
            f.write("0 0 0 0 1 0\n")
        image_array = cv2.imread('data/filename')
        image_array = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
        inputs.append(np.resize(image_array, (28*28)))
    f.close()
    return inputs

#We call the function during prediction
def conv_image_to_array_pred(img):
    inputs = []
    image_array = cv2.imread(img)
    inputs.append(np.resize(image_array,(28*28)).flatten())
    return (np.array(inputs))


