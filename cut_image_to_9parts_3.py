from cv2 import cv2
img = cv2.imread("006.jpg")
list1=(list(img.shape))#[y,x,3]

x=list1[1]
y=list1[0]
#x is column , y is row

if (x>y):
    temp=x-y
    start_x = temp//2
    x_no_end=(x-start_x)
    new_img=img[0:y, start_x:x_no_end]
    list3=(list(new_img.shape))
    #list3 = [1080, 1080, 3] when 1920x1080
    #square succcessful

    div_len_by_3= (x_no_end-start_x)//3 # divide new square length by 3. Used to calculate blocks cooridnate the new 3x3 table
    first_line= start_x + div_len_by_3
    second_line= first_line + div_len_by_3  # the second line inside new square 3x3

# math of distence on each block
    block1_r= [0,(list3[0]//3)] 
    block1_c= [start_x,first_line]

    block2_r= [0,(list3[0]//3)]
    block2_c= [first_line,second_line]

    block3_r= [0,(list3[0]//3)]
    block3_c= [second_line,x_no_end]

    block4_r= [(list3[0]//3),(list3[0]*2//3)]
    block4_c= [start_x,first_line]

    block5_r= [(list3[0]//3),(list3[0]*2//3)]
    block5_c=[first_line,second_line]

    block6_r= [(list3[0]//3),(list3[0]*2//3)]
    block6_c= [second_line,x_no_end]

    block7_r= [(list3[0]*2//3),list3[0]]
    block7_c= [start_x,first_line]

    block8_r= [(list3[0]*2//3),list3[0]]
    block8_c=[first_line,second_line]

    block9_r= [(list3[0]*2//3),list3[0]]
    block9_c=[second_line,x_no_end]


    img1=img[block1_r[0]:block1_r[1],block1_c[0]:block1_c[1]]

    #img[row,column] match [block_r,  block_c]
    img1=img[block1_r[0]:block1_r[1],block1_c[0]:block1_c[1]]
    img2=img[block2_r[0]:block2_r[1],block2_c[0]:block2_c[1]]
    img3=img[block3_r[0]:block3_r[1],block3_c[0]:block3_c[1]]
    img4=img[block4_r[0]:block4_r[1],block4_c[0]:block4_c[1]]
    img5=img[block5_r[0]:block5_r[1],block5_c[0]:block5_c[1]]
    img6=img[block6_r[0]:block6_r[1],block6_c[0]:block6_c[1]]
    img7=img[block7_r[0]:block7_r[1],block7_c[0]:block7_c[1]]
    img8=img[block8_r[0]:block8_r[1],block8_c[0]:block8_c[1]]
    img9=img[block9_r[0]:block9_r[1],block9_c[0]:block9_c[1]]
#output 9 image
    cv2.imwrite("new1.jpg", img1)
    cv2.imwrite("new2.jpg", img2)
    cv2.imwrite("new3.jpg", img3)
    cv2.imwrite("new4.jpg", img4)
    cv2.imwrite("new5.jpg", img5)
    cv2.imwrite("new6.jpg", img6)
    cv2.imwrite("new7.jpg", img7)
    cv2.imwrite("new8.jpg", img8)
    cv2.imwrite("new9.jpg", img9)

else:# height>weidth 
    temp2=y-x
    start_y = temp2//2
    y_no_end=(y-start_y)

    new2_img=img[start_y:y_no_end,0:x]
    list2=(list(new2_img.shape))
    
    div_len_by_3_y= (y_no_end-start_y)//3
    first_line_y= start_y + div_len_by_3_y
    second_line_y= first_line_y + div_len_by_3_y

    block1_r_y= [start_y,first_line_y]
    block1_c_y= [0,(list2[1]//3)]

    block2_r_y= [start_y,first_line_y]
    block2_c_y= [(list2[1]//3),(list2[1]*2//3)]

    block3_r_y= [start_y,first_line_y]
    block3_c_y= [(list2[1]*2//3),list2[1]]

    block4_r_y= [first_line_y,second_line_y]
    block4_c_y= [0,(list2[1]//3)]

    block5_r_y= [first_line_y,second_line_y]
    block5_c_y= [(list2[1]//3),(list2[1]*2//3)]

    block6_r_y= [first_line_y,second_line_y]
    block6_c_y= [(list2[1]*2//3),list2[1]]

    block7_r_y= [second_line_y, y_no_end]
    block7_c_y= [0,(list2[1]//3)]

    block8_r_y= [second_line_y, y_no_end]
    block8_c_y= [(list2[1]//3),(list2[1]*2//3)]

    block9_r_y= [second_line_y, y_no_end]
    block9_c_y= [(list2[1]*2//3),list2[1]]
        #img[row,column] match [block_r,  block_c]
    img1=img[block1_r_y[0]:block1_r_y[1],block1_c_y[0]:block1_c_y[1]]
    img2=img[block2_r_y[0]:block2_r_y[1],block2_c_y[0]:block2_c_y[1]]
    img3=img[block3_r_y[0]:block3_r_y[1],block3_c_y[0]:block3_c_y[1]]
    img4=img[block4_r_y[0]:block4_r_y[1],block4_c_y[0]:block4_c_y[1]]
    img5=img[block5_r_y[0]:block5_r_y[1],block5_c_y[0]:block5_c_y[1]]
    img6=img[block6_r_y[0]:block6_r_y[1],block6_c_y[0]:block6_c_y[1]]
    img7=img[block7_r_y[0]:block7_r_y[1],block7_c_y[0]:block7_c_y[1]]
    img8=img[block8_r_y[0]:block8_r_y[1],block8_c_y[0]:block8_c_y[1]]
    img9=img[block9_r_y[0]:block9_r_y[1],block9_c_y[0]:block9_c_y[1]]
#output 9 image
    cv2.imwrite("new1.jpg", img1)
    cv2.imwrite("new2.jpg", img2)
    cv2.imwrite("new3.jpg", img3)
    cv2.imwrite("new4.jpg", img4)
    cv2.imwrite("new5.jpg", img5)
    cv2.imwrite("new6.jpg", img6)
    cv2.imwrite("new7.jpg", img7)
    cv2.imwrite("new8.jpg", img8)
    cv2.imwrite("new9.jpg", img9)