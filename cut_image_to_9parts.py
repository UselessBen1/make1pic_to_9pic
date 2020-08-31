from cv2 import cv2
img = cv2.imread("Annotation 2020-08-30 183214.png")


list1=(list(img.shape))
#img1=img[100:300,125:375] #需要保留的区域--裁剪

block1_x= [0,(list1[0]//3)] #block1 pixel x 0~33
block1_y= [0,(list1[1]//3)] #block1 pixel y 0~33

block2_x= [(list1[0]//3),(list1[0]*2//3)]
block2_y= [0,(list1[1]//3)]

block3_x= [(list1[0]*2//3),(list1[0])]
block3_y= [0,(list1[1]//3)]

block4_x= [0,(list1[0]//3)]
block4_y= [(list1[1]//3),(list1[1]*2//3)]

block5_x= [(list1[0]//3),(list1[0]*2//3)]
block5_y= [(list1[1]//3),(list1[1]*2//3)]

block6_x= [(list1[0]*2//3),(list1[0])]
block6_y= [(list1[1]//3),(list1[1]*2//3)]

block7_x= [0,(list1[0]//3)]
block7_y= [(list1[1]*2//3),(list1[1])]

block8_x= [(list1[0]//3),(list1[0]*2//3)]
block8_y= [(list1[1]*2//3),(list1[1])]

block9_x= [(list1[0]*2//3),(list1[0])]
block9_y= [(list1[1]*2//3),(list1[1])]

img1=img[block1_x[0]:block1_x[1],block1_y[0]:block1_y[1]]
img2=img[block2_x[0]:block2_x[1],block2_y[0]:block2_y[1]]
img3=img[block3_x[0]:block3_x[1],block3_y[0]:block3_y[1]]
img4=img[block4_x[0]:block4_x[1],block4_y[0]:block4_y[1]]
img5=img[block5_x[0]:block5_x[1],block5_y[0]:block5_y[1]]
img6=img[block6_x[0]:block6_x[1],block6_y[0]:block6_y[1]]
img7=img[block7_x[0]:block7_x[1],block7_y[0]:block7_y[1]]
img8=img[block8_x[0]:block8_x[1],block8_y[0]:block8_y[1]]
img9=img[block9_x[0]:block9_x[1],block9_y[0]:block9_y[1]]

#print(img1)

#QQ个人资料图片顺序是321654987
cv2.imwrite("new1.jpg", img3)
cv2.imwrite("new2.jpg", img2)
cv2.imwrite("new3.jpg", img1)
cv2.imwrite("new4.jpg", img6)
cv2.imwrite("new5.jpg", img5)
cv2.imwrite("new6.jpg", img4)
cv2.imwrite("new7.jpg", img9)
cv2.imwrite("new8.jpg", img8)
cv2.imwrite("new9.jpg", img7)







'''
cv2.imshow("img1",3)
cv2.waitKey(5000)
cv2.destroyAllWindows()  
cv2.imwrite("NEW",img1)
'''
