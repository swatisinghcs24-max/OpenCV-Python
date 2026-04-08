import cv2


image = cv2. imread("Image Resizing & Shapping\\pythonfeature.png")

if image is None:
   print("oops! Your image is not working")

else:
   print("Image loaded successfully!")

   pt1 = (50 , 100)
   pt2 = (300 , 100)
   color = (255 , 0 ,0)
   thickness = 4

   cv2.line(image , pt1 ,pt2 , color , thickness)

   cv2.imshow(  "Line Drwaing",image)
   cv2.waitKey(0)
   cv2.destroyAllWindows()