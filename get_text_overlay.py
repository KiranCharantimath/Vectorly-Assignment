import cv2
import numpy as np

def getTextOverlay(input_image):
    output = np.zeros(input_image.shape, dtype=np.uint8)
     
    # Write your code here for output
    output[np.where((input_image!=[0,0,0]).all(axis=2))] = [255,255,255] #Update all pixels which r not black to white
    return output

if __name__ == '__main__':
    image = cv2.imread('simpsons_frame0.png')
    output = getTextOverlay(image)
    cv2.imwrite('simpons_text.png', output)
