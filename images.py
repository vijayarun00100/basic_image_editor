from PIL import Image , ImageFilter

img=Image.open("C:\\Users\\vijay arun\\Documents\\project\\pikachu.jpg") 
print(img)
print(img.format)
print(img.size)  
print(img.mode) 
# filtered_img=img.convert('RGB')
# #there are more filters , - BLUR , L , SHARPEN , SMOOTH 
# filtered_img.save("b.png","png")
#also you can save in different formats of picture . But note : it should support the filters that you make.
#print(dir(img)) - this gives all the imformation of the image 
# filtered_img.show()
img.show() 

# to rotate the object ,
box=(100,100,400,400) 
region=img.crop(box)
scrwed=img.resize((300,300))
region.save("new3.png",'png')