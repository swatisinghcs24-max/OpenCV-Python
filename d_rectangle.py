import cv2


image = cv2. imread("Image Resizing & Shapping\\pythonfeature.png")

if image is None:
   print("oops! Your image is not working")

else:
   print("Image loaded successfully!")

   pt1 = (50 , 50)
   pt2 = (250 , 200)
   color = (0 , 0 , 255)
   thickness = 3

   cv2.rectangle(image , pt1 ,pt2 , color , thickness)

   cv2.imshow(  "Rectangle Drwaing",image)
   cv2.waitKey(0)
   cv2.destroyAllWindows()