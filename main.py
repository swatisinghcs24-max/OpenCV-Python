import cv2

image = cv2.imread("image-optimisation-scaled.jpg")

if image is None:
    print("Error: Image not found")
else:
    print("Image loaded successfully")