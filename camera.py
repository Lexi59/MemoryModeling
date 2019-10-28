
		
from PIL import Image

userInput = input("name of picture: ")
img = Image.open(userInput)
img.show()
img.getdata()
pixelList = list(img.getdata())
pixelList2 = []
imgList = []


for i in pixelList: 
	end = False
	Red = str(i[0])
	Green = str(i[1])
	Blue = str(i[2])
			
	print(Red)
	print(Green)
	print(Blue)
			
	if Red == 'o': 
		Red = 0
	if Green == 'o': 
		Green = 0
	if Blue == 'o': 
		Blue = 0
	R = float(Red)
	G = float(Green)
	B = float(Blue)
			
	print(R)
	print(G)
	print(B)
			
	intensity = float(R + G + B)
	if intensity == 0: 
		RPercent = 0
		GPercent = 0
		BPercent = 0
	else:
		RPercent = R / intensity
		GPercent = G / intensity
		BPercent = B / intensity
print(Red)
print(Green)
print(Blue)
print(R)	
print(G)
print(B)
print(RPercent)
print(GPercent)
print(BPercent)