import cv2
img=cv2.imread(r"C:\Users\qsl\Desktop\unit4\01.jpg")
dst1=cv2.blur(img,(3,3))
dst2=cv2.blur(img,(5,5))
dst3=cv2.blur(img,(9,9))

a=cv2.GaussianBlur(img,(5,5),0,0)

b=cv2.GaussianBlur(img,(9,9),0,0)

c=cv2.GaussianBlur(img,(15,15),0,0)

cv2.imshow('img',img)
cv2.imshow("3*3",dst1)
cv2.imshow("5*5",dst2)
cv2.imshow("9*9",dst3)

cv2.imshow("a",a)
cv2.imshow("b",b)
cv2.imshow("c",c)
cv2.waitKey()
cv2.destroyAllWindows()