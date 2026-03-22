import cv2

image = cv2.imread("file-photo-illustration-shows-new-google-logo.webp")

if image is None:
    print("Error: could not load image")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("gray_image.png", gray)
    print("Grayscale image saved as 'gray_image.png'")

    

if image is not None:
    cv2.imshow("Image showing", image) #open the window
    cv2.waitKey(0)  #wait for a key
    cv2.destroyAllWindows() #close the window
else:
    print("Cloud not load the image")



if image is not None:
    success = cv2.imwrite("output2_python.png", image)
    if success:
        print("Image saved successfully as 'output_python.png'")
    else:
        print("Failed to save image")
else:
    print("Error: could not load image")