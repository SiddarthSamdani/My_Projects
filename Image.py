import cv2
img = cv2.imread("a.jpg", 1)
resized_image = cv2.resize(img, (int(img.shape[1]/5), int(img.shape[0]/9)))
cv2.imshow("enrique-aguilar-gqzcHoW6vQk-unsplash", resized_image)
cv2.waitKey(100000)
cv2.destroyAllWindows()

