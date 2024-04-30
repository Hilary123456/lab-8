import cv2
import numpy as np

image_path = 'variant-6.png'
image = cv2.imread(image_path)

# Get the original dimensions
height, width = image.shape[:2]

# Double the dimensions
new_height = height * 2
new_width = width * 2

# Resize the image
resized_image = cv2.resize(image, (new_width, new_height))

# Save or display the resized image
cv2.imwrite('resized_image.jpg', resized_image)
cv2.imshow('resized_image.jpg', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
