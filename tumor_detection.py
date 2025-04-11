import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import sys

args = sys.argv[1]
# load mri images
# read the image
image = cv.imread(args, cv.IMREAD_GRAYSCALE)

# preprocess for noise reduction
img = cv.medianBlur(image, 5)  # apply median blur to reduce noise

# adaptive threshold for multi-modes - image has different lighting conditions in different areas
# divide image into blocks
# then perform global thresholding on each of the blocks 
# by dividing, we get rid of the dominant modes 
# keep dividing until we get two dominant modes
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)  # adaptive mean thresholding
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)  # adaptive gaussian thresholding

titles = ['Original Image', 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th2, th3]

# visualize all thresholding results
for i in range(3):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

# use gaussian thresholding to visualize
plt.imshow(th3, cmap='gray')
plt.title('Initial Adaptive Gaussian Thresholding')
plt.xticks([]), plt.yticks([])
plt.show()

# tune parameters - change block and/or c values
# higher c subtracts more from the local mean, so fewer pixels get turned white
#th4 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 7)  
# inverted for white tumor on black background
th4 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                           cv.THRESH_BINARY_INV, 9, 5)

plt.imshow(th4, cmap='gray')
plt.title('Tuning Parameters Adaptive Gaussian Thresholding')
plt.xticks([]), plt.yticks([])
plt.show()


# find contours from thresholded image
contours, _ = cv.findContours(th4, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# convert image to BGR so we can draw colored contours
image_contour = cv.cvtColor(image, cv.COLOR_GRAY2BGR)

# optional: filter small or huge contours
#min_area = 500
#max_area = 5000

# draw contours
for cnt in contours:
    #area = cv.contourArea(cnt)
    #if min_area < area < max_area:
        cv.drawContours(image_contour, [cnt], -1, (0, 255, 0), 2)  # green contour

# plot the result
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Preprocessed MRI Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv.cvtColor(image_contour, cv.COLOR_BGR2RGB))
plt.title('Tumor Contour Highlighted')
plt.axis('off')

plt.tight_layout()
plt.show()

