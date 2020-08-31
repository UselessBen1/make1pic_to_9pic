from cv2 import cv2
img = cv2.imread("Annotation 2020-08-30 200518.png")


list1=(list(img.shape))#[x,y,2]

if (list1[0]>=list1[1]):#x>y
    a=list1[0]-list1[1]#a=x-y
    b=a//2              #居中数据
    #list1[1]=temp #  y=t
    big_image=img[b:list1[0]-b,0:list1[1]]
    list2=(list(big_image.shape))

    block1_x= [0,(list2[0]//3)] #block1 pixel x 0~33
    block1_y= [0,(list2[1]//3)] #block1 pixel y 0~33
    block2_x= [(list2[0]//3),(list2[0]*2//3)]
    block2_y= [0,(list2[1]//3)] 
    block3_x= [(list2[0]*2//3),(list2[0])]
    block3_y= [0,(list2[1]//3)]
    block4_x= [0,(list2[0]//3)]
    block4_y= [(list2[1]//3),(list2[1]*2//3)]
    block5_x= [(list2[0]//3),(list2[0]*2//3)]
    block5_y= [(list2[1]//3),(list2[1]*2//3)]
    block6_x= [(list2[0]*2//3),(list2[0])]
    block6_y= [(list2[1]//3),(list2[1]*2//3)]
    block7_x= [0,(list2[0]//3)]
    block7_y= [(list2[1]*2//3),(list2[1])]
    block8_x= [(list2[0]//3),(list2[0]*2//3)]
    block8_y= [(list2[1]*2//3),(list2[1])]
    block9_x= [(list2[0]*2//3),(list2[0])]
    block9_y= [(list2[1]*2//3),(list2[1])]

    img1=img[block1_x[0]:block1_x[1],block1_y[0]:block1_y[1]]
    img2=img[block2_x[0]:block2_x[1],block2_y[0]:block2_y[1]]
    img3=img[block3_x[0]:block3_x[1],block3_y[0]:block3_y[1]]
    img4=img[block4_x[0]:block4_x[1],block4_y[0]:block4_y[1]]
    img5=img[block5_x[0]:block5_x[1],block5_y[0]:block5_y[1]]
    img6=img[block6_x[0]:block6_x[1],block6_y[0]:block6_y[1]]
    img7=img[block7_x[0]:block7_x[1],block7_y[0]:block7_y[1]]
    img8=img[block8_x[0]:block8_x[1],block8_y[0]:block8_y[1]]
    img9=img[block9_x[0]:block9_x[1],block9_y[0]:block9_y[1]]

    cv2.imwrite("new1.jpg", img3)
    cv2.imwrite("new2.jpg", img2)
    cv2.imwrite("new3.jpg", img1)
    cv2.imwrite("new4.jpg", img6)
    cv2.imwrite("new5.jpg", img5)
    cv2.imwrite("new6.jpg", img4)
    cv2.imwrite("new7.jpg", img9)
    cv2.imwrite("new8.jpg", img8)
    cv2.imwrite("new9.jpg", img7)
#img1=img[100:300,125:375] #需要保留的区域--裁剪
else:
    a1=list1[1]-list1[0]#a=y-x
    b1=a1//2              #居中数据
    #list1[1]=temp #  y=t
    big_image2=img[0:list1[0],b1:list1[1]-b1]
    list3=(list(big_image2.shape))

    block1_x= [0,(list3[0]//3)] #block1 pixel x 0~33
    block1_y= [0,(list3[1]//3)] #block1 pixel y 0~33

    block2_x= [(list3[0]//3),(list3[0]*2//3)]
    block2_y= [0,(list3[1]//3)]

    block3_x= [(list3[0]*2//3),(list3[0])]
    block3_y= [0,(list3[1]//3)]

    block4_x= [0,(list3[0]//3)]
    block4_y= [(list3[1]//3),(list3[1]*2//3)]

    block5_x= [(list3[0]//3),(list3[0]*2//3)]
    block5_y= [(list3[1]//3),(list3[1]*2//3)]

    block6_x= [(list3[0]*2//3),(list3[0])]
    block6_y= [(list3[1]//3),(list3[1]*2//3)]

    block7_x= [0,(list3[0]//3)]
    block7_y= [(list3[1]*2//3),(list3[1])]

    block8_x= [(list3[0]//3),(list3[0]*2//3)]
    block8_y= [(list3[1]*2//3),(list3[1])]

    block9_x= [(list3[0]*2//3),(list3[0])]
    block9_y= [(list3[1]*2//3),(list3[1])]

    img1=img[block1_x[0]:block1_x[1],block1_y[0]:block1_y[1]]
    img2=img[block2_x[0]:block2_x[1],block2_y[0]:block2_y[1]]
    img3=img[block3_x[0]:block3_x[1],block3_y[0]:block3_y[1]]
    img4=img[block4_x[0]:block4_x[1],block4_y[0]:block4_y[1]]
    img5=img[block5_x[0]:block5_x[1],block5_y[0]:block5_y[1]]
    img6=img[block6_x[0]:block6_x[1],block6_y[0]:block6_y[1]]
    img7=img[block7_x[0]:block7_x[1],block7_y[0]:block7_y[1]]
    img8=img[block8_x[0]:block8_x[1],block8_y[0]:block8_y[1]]
    img9=img[block9_x[0]:block9_x[1],block9_y[0]:block9_y[1]]

    cv2.imwrite("new1.jpg", img3)
    cv2.imwrite("new2.jpg", img2)
    cv2.imwrite("new3.jpg", img1)
    cv2.imwrite("new4.jpg", img6)
    cv2.imwrite("new5.jpg", img5)
    cv2.imwrite("new6.jpg", img4)
    cv2.imwrite("new7.jpg", img9)
    cv2.imwrite("new8.jpg", img8)
    cv2.imwrite("new9.jpg", img7)
#print(img1)
'''
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






'''
cv2.imshow("img1",3)
cv2.waitKey(5000)
cv2.destroyAllWindows()  
cv2.imwrite("NEW",img1)
'''
