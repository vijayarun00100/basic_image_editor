import sys 
import os 
from PIL import Image, ImageFilter 

path = sys.argv[1] 
path2= sys.argv[2] 

if not os.path.exists(path2):
	os.makedirs(path2) 

for i in os.listdir(path):
	img=Image.open(f'{path}{i}')
	clean_now=os.path.splitext(i)[0]
	img.save(f'{path2}{clean_now}.png','png') 
	print("all done!") 




 

