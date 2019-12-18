import numpy as np 
import cv2 
import math
#Hard thresholding function
def thresh_hard (img_in, eps):
    #Divides image by max pixel value in 8 bit which is 255
    img_out = img_in/255
    #Loops through dimensions of the image
    for i in range (0, img_out.shape[0]):     
        for j in range (0, img_out.shape[1]):     
            #Compares the pixel intensity to epsilon
            #If the intensity is greater, its assigned a max value of 1
            if img_out[i][j] > eps:
                img_out[i][j] = 1
            else:
            #Else, its assigned minimum value of 0
                img_out[i][j] = 0
    #image is returned and multiplied by 255 so it can be used as a grayscale and displayed
    return (img_out * 255)
#Soft thresholding fuction
def thresh_soft (img_in, eps, phi):
    #Divides image by max pixel value in 8 bit which is 255
    img_out = img_in/255
    #Loops through dimensions of the image
    for i in range (0, img_out.shape[0]):     
        for j in range (0, img_out.shape[1]):     
            #Compares the pixel intensity to epsilon
            #If the intensity is greater, its assigned a max value of 1
            if img_out[i][j] > eps:
                img_out[i][j] = 1
            else:
            #Else, image intensity is passed through a tan hyperbolic function and added to 1, for smoother intensity transition
                img_out[i][j] = 1 + np.tanh(phi * (img_out[i][j] - eps))
    #image is returned and multiplied by 255 so it can be used as a grayscale and displayed
    return (img_out * 255)
#Reads the input image
image_in = cv2.imread('XDoG_orca.png',0)
#Calls Upon the hard thresholding function
hard_thresh_img = thresh_hard(image_in, 0.5)
cv2.imwrite("Orca_hard.png", hard_thresh_img)
#Calls Upon soft thresholding function
soft_thresh_img = thresh_soft(image_in, 0.5, 6)
cv2.imwrite("Orca_soft.png", soft_thresh_img)

