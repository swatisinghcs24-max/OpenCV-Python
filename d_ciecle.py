import cv2


image = cv2. imread("Image Resizing & Shapping\\pythonfeature.png")

if image is None:
   print("oops! Your image is not working")

else:
   print("Image loaded successfully!")


   cv2.circle(image , (150 , 150) , 50 , (255,0,0) , 5)

   cv2.imshow(  "Draw a circle",image)
   cv2.waitKey(0)
   cv2.destroyAllWindows()