import cv2
img=cv2.imread(r"C:\Users\qsl\Desktop\unit4\01.jpg")
d1=cv2.medianBlur(img,3)
d2=cv2.medianBlur(img,5)
d3=cv2.medianBlur(img,9)
cv2.imshow('img',img)
cv2.imshow('3',d1)
cv2.imshow('5',d2)
cv2.imshow('9',d3)

cv2.waitKey()
cv2.destroyAllWindows()