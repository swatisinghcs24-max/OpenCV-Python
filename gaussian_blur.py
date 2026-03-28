import cv2

image = cv2.imread(r"C:\Users\Sumit\Desktop\opencv-python\video Proccessing\Image filtering\free-nature-images.jpg")

if image is None:
    print("Error: Image not loaded. Check file path!")
    exit()

blurred = cv2.GaussianBlur(image, (7, 7), 0)

cv2.imshow("Blurred Image", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()