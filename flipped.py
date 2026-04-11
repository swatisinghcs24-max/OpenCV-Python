import cv2

image = cv2. imread("Image Resizing & Shapping\\pythonfeature.png")

if image is None:
    print("Could not load image")

else:
    flipped_horizontal = cv2.flip(image , 1)
    flipped_vertical = cv2.flip(image , 0)
    flipped_both = cv2.flip(image , -1)

    cv2.imshow("original" , image)
    cv2.imshow("Flipped Horizontal" ,flipped_horizontal)
    cv2.imshow("Flipped vertical" ,flipped_vertical)
    cv2.imshow("Flipped  both" , flipped_both)

    cv2.waitKey(0)
    cv2.destroyAllWindows