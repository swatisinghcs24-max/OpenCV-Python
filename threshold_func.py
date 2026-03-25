import cv2

image = cv2.imread(r"C:\Users\Sumit\Desktop\opencv-python\file-photo-illustration-shows-new-google-logo.webp" , cv2.IMREAD_GRAYSCALE)

ret , thresh_image = cv2.threshold(image , 120 , 255 , cv2.THRESH_BINARY)

cv2.imshow("Original Image" , image)
cv2.imshow("Threshholded image" ,  thresh_image)
cv2.waitKey(0)
cv2.destroyAllWindows()