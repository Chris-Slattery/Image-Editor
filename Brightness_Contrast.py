import cv2 as cv
import numpy as np
import sys

#Read in image
img = cv.imread(r'C:\Users\chris\Desktop\Dark\s.png')

#Change values to configure brightness and contrast
#Brightness
alpha = 1

#Contrast
beta = 20

#Perform brightness and contrast
result = cv.addWeighted(img, alpha, np.zeros(img.shape, img.dtype), 0, beta)

#Filtering
#hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

#Hue, Saturation values
#lower = np.array([0,0,0])
#upper = np.array([100,100,100])

#mask = cv.inRange(hsv, lower, upper)
#result = cv.bitwise_and(img, img, mask=mask)


#cv.imshow('image', img)
#cv.waitKey(0)




#Used for blurring image
#kernel = np.ones((10,10), np.float32)/100
#smoothed = cv.filter2D(img, -1, kernel)

#Perfor gaussian blur
#blur = cv.GaussianBlur(img, (5, 5), 0)

#Show image with blur, contrast and brightness
#cv.imshow('blur', result)

#Let image show on screen until button is pressed
#cv.waitKey(0)

#Save image to desktop
cv.imwrite('New_Image1.png', result)