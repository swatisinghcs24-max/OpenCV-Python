import cv2

image = cv2.imread(r"C:\Users\Sumit\Desktop\opencv-python\video Proccessing\Image filtering\free-nature-images.jpg")


blurred = cv2.medianBlur(image , 11)

cv2.imshow("Original" , image)
cv2.imshow("Clean Image" , blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()