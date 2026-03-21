import cv2

image = cv2.imread("python_image.png")

if image is None:
    print("Error: could not load image")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("gray_image.png", gray)
    print("Grayscale image saved as 'gray_image.png'")
