from PIL import Image
import pygame 

pygame.init()

userInput = input("name of picture: ")
quit = False

NumOfGreen = 0
NumOfBlack = 0
NumOfGrey = 0
NumOfWhite = 0
NumOfRed = 0
NumOfYellow = 0
NumOfOrange = 0
NumOfPink = 0
NumOfPurple = 0
NumOfBlue = 0
alzheimers = False

if userInput == 'quit': 
	quit == True
elif userInput == 'Alzheimers':
	alzheimers = True
	userInput = input("name of picture: ")

while quit == False:
	img = Image.open(userInput+ ".jpg")
	pixelList = list(img.getdata())
	pixelList2 = []


	GreenNum = 0
	BlackNum = 0
	GreyNum = 0
	WhiteNum = 0
	RedNum = 0
	YellowNum = 0
	OrangeNum = 0
	PinkNum = 0
	PurpleNum = 0	
	BlueNum = 0


	print("Hmm....")
	
	
	for i in pixelList:
		end = False
		Red = str(i[0])
		Green = str(i[1])
		Blue = str(i[2])
		
		if Red == 'o' or Red == 'r' or Red == 'a' or Red == 'y': 
			Red = None
		if Green == 'o' or Green == 'r' or Green == 'a': 
			Green = None
		if Blue == 'o' or Blue == 'r' or Blue == 'a': 
			Blue = None
		if Red != None and Green != None and Blue != None:
			R = float(Red)
			G = float(Green)
			B = float(Blue)
			intensity = float(R + G + B)
			if intensity == 0: 
				RPercent = 0
				GPercent = 0
				BPercent = 0
			else:
				RPercent = R / intensity
				GPercent = G / intensity	
				BPercent = B / intensity
				
			if GPercent > RPercent and GPercent > BPercent and end == False:
				if GPercent > RPercent and BPercent > RPercent and intensity < 100:
					pixelList2.append("cyan")
				else:
					pixelList2.append("green")
					GreenNum += 1
					end = True
					
			if R - G < 8 and R - B < 8 and B - G < 8 and end == False:
				if R < 250 and B < 250 and G < 250: 
					if R == G and R == B and B == G and end == False: 
						if R < 4: 
							pixelList2.append("black")
							BlackNum += 1
							end == True
					elif intensity > 250: 
						pixelList2.append("grey")
						GreyNum += 1
						end = True
				else: 
					pixelList2.append("white")
					WhiteNum += 1
					end == True
							
			if RPercent > GPercent and RPercent > BPercent and end == False: 
				if RPercent > 0.9 and end == False: 
					pixelList2.append("red")
					RedNum += 1
					end = True
				elif GPercent > BPercent and intensity > 500 and end == False: 
					pixelList2.append("yellow")
					YellowNum += 1
					end = True	
				elif GPercent > BPercent and end == False: 
					pixelList2.append("orange")
					OrangeNum += 1
					end = True
				elif end == False: 
					pixelList2.append("pink")
					PinkNum += 1
					end = True
					
				
			if BPercent > RPercent and BPercent > GPercent and end == False: 
				if RPercent > GPercent and BPercent > GPercent and end == False:
					pixelList2.append("purple")
					PurpleNum += 1
					end = True
				else: 
					pixelList2.append("blue")
					BlueNum += 1
					end = True

	NumList = [GreenNum, BlackNum, GreyNum, WhiteNum, RedNum, YellowNum, OrangeNum, PinkNum, PurpleNum, BlueNum]
	maximum = max(NumList)
	finish = False
	quitEval = False


	if GreenNum == maximum and finish == False: 
		NumOfGreen += 1	
		if NumOfGreen == 1:
			img = Image.open("green.jpg")
			img.show()
			print("I don't think I've seen this color before.")
			userInputColor1 = input("What color is it? ")
		elif NumOfGreen == 2: 
			greenEval = input("I think you showed this to me before. It is " + userInputColor1 + ", right?")
			if greenEval.lower() == 'no':
				userInput1 = input("Sorry, I must have been confused. What is this color?")
				NumOfGreen = 1
		else:
			print("This color is " + userInputColor1 + "! I've seen this color " + str(NumOfGreen) + " times.")
		finish = True
		
	if BlackNum == maximum and finish == False: 
		NumOfBlack += 1
		if NumOfBlack == 1:
			img = Image.open("black.jpg")		
			img.show()
			print("TI don't think I've seen this color before.")
			userInputColor2 = input("What color is it? ")
		elif NumOfBlack == 2: 
			blackEval = input("I think you showed this to me before. It is " + userInputColor2 + ", right?")
			if blackEval.lower() == 'no':
				userInput2 = input("Sorry, I must have been confused. What is this color?")
				NumOfBlack = 1
		else:
			print("This color is " + userInputColor2 + "! I've seen this color " + str(NumOfBlack) + " times.")
		finish = True
		
	if GreyNum == maximum and finish == False: 
		NumOfGrey += 1
		if NumOfGrey == 1:
			img = Image.open("greyL.jpg")
			img.show()
			print("I don't think I've seen this color before.")
			userInputColor3 = input("What color is it? ")
		elif NumOfGrey == 2: 
			greyEval = input("I think you showed this to me before. It is " + userInputColor3 + ", right?")
			if greyEval.lower() == 'no':
				userInput3 = input("Sorry, I must have been confused. What is this color?")
				NumOfGrey = 1
		else:
			print("This color is " + userInputColor3 + "! I've seen this color " + str(NumOfGrey) + " times.")
		finish = True
		
	if WhiteNum == maximum and finish == False: 
		NumOfWhite += 1
		if NumOfWhite == 1:
			img = Image.open("white.jpg")
			img.show()
			print("I don't think I've seen this color before.")
			userInputColor4 = input("What color is it? ")
		elif NumOfWhite == 2: 
			blueEval = input("I think you showed this to me before. It is " + userInputColor4 + ", right?")
			if blueEval.lower() == 'no':
				userInput4 = input("Sorry, I must have been confused. What is this color?")
				NumOfWhite = 1
		else:
			print("This color is " + userInputColor4 + "! I've seen this color " + str(NumOfWhite) + " times.")
		finish = True
		
	if RedNum == maximum and finish == False:
		NumOfRed += 1
		if NumOfRed == 1: 
			img = Image.open("red.jpg")
			img.show()
			print("I don't think I've seen this color before.")
			userInputColor5 = input("What color is it? ")
		elif NumOfRed == 2: 
			redEval = input("I think you showed this to me before. It is " + userInputColor5 + ", right?")
			if redEval.lower() == 'no':
				userInput5 = input("Sorry, I must have been confused. What is this color?")
				NumOfRed = 1
		else:
			print("This color is " + userInputColor5 + "! I've seen this color " + str(NumOfRed) + " times.")
		finish = True
		
	if YellowNum == maximum and finish == False: 
		NumOfYellow += 1
		if NumOfYellow == 1:
			img = Image.open("yellow.jpg")
			img.show()
			print("I don't think I've seen this color before.")
			userInputColor7 = input("What color is it? ")
		elif NumOfYellow == 2: 
			yellowEval = input("I think you showed this to me before. It is " + userInputColor7 + ", right?")
			if yellowEval.lower() == 'no':
				userInput7 = input("Sorry, I must have been confused. What is this color?")
				NumOfYellow = 1
		else:
			print("This color is " + userInputColor7 + "! I've seen this color " + str(NumOfYellow) + " times.")
		finish = True
		
	if OrangeNum == maximum and finish == False: 
		NumOfOrange += 1
		if NumOfOrange == 1:
			img = Image.open("orange.jpg")
			img.show()
			print("I don't think I've seen this color before.")
			userInputColor8 = input("What color is it? ")
		elif NumOfOrange == 2: 
			orangeEval = input("I think you showed this to me before. It is " + userInputColor8 + ", right?")
			if orangeEval.lower() == 'no':
				userInput8 = input("Sorry, I must have been confused. What is this color?")
				NumOfOrange = 1
		else:
			print("This color is " + userInputColor8 + "! I've seen this color " + str(NumOfOrange) + " times.")
		finish = True
		
	if PinkNum == maximum and finish == False: 
		NumOfPink += 1
		if NumOfPink== 1: 
			img = Image.open("pink.jpg")
			img.show()
			print("I don't think I've seen this color before.")
			userInputColor9 = input("What color is it? ")
		elif NumOfPink == 2: 
			pinkEval = input("I think you showed this to me before. It is " + userInputColor9 + ", right?")
			if pinkEval.lower() == 'no':
				userInput9 = input("Sorry, I must have been confused. What is this color?")
				NumOfPink = 1
		else:
			print("This color is " + userInputColor9 + "! I've seen this color " + str(NumOfPink) + " times.")
		finish = True
		
	if PurpleNum == maximum and finish == False: 
		NumOfPurple += 1
		if NumOfPurple == 1: 
			img = Image.open("purple.jpg")
			img.show()
			print("I don't think I've seen this color before.")
			userInputColor10 = input("What color is it? ")
		elif NumOfPurple == 2: 
			purpleEval = input("I think you showed this to me before. It is " + userInputColor10 + ", right?")
			if purpleEval.lower() == 'no':
				userInput10 = input("Sorry, I must have been confused. What is this color?")
				NumOfPurple = 1
		else:
			print("This color is " + userInputColor10 + "! I've seen this color " + str(NumOfPurple) + " times.")
		finish = True
		
	if BlueNum == maximum and finish == False:
		NumOfBlue += 1
		if NumOfBlue == 1:
			img = Image.open("blue.jpg")
			img.show()
			print("I don't think I've seen this color before.")
			userInputColor11 = input("What color is it? ")
		elif NumOfBlue == 2: 
			blueEval = input("I think you showed this to me before. It is " + userInputColor11 + ", right?")
			if blueEval.lower() == 'no':
				userInput11 = input("Sorry, I must have been confused. What is this color?")
				NumOfBlue = 1
		else:
			print("This color is " + userInputColor11 + "! I've seen this color " + str(NumOfBlue) + " times.")
		finish = True
		
	thickList = [NumOfGreen, NumOfBlack, NumOfGrey, NumOfWhite, NumOfRed, NumOfYellow, NumOfOrange, NumOfPink, NumOfPurple, NumOfBlue]
	screenWidth = 800
	screenHeight = 550
	screenSize = (screenWidth, screenHeight)
	screen = pygame.display.set_mode(screenSize)
	black = (0,0,0)
	white = (255,255,255)
	done = False 
	clock = pygame.time.Clock()
	clock.tick(60)
	background = pygame.image.load('HumanBrain.jpg')
	while not done: 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
		screen.fill(black)
		screen.blit(background, (0,0))
		if thickList[0] != 0 and alzheimers == False: 
			pygame.draw.line(screen, white, (200,50), (600,50), (thickList[0]*2))
		elif thickList[0] != 0 and alzheimers == True: 
			pygame.draw.line(screen, white, (200,50), (350,50), 1)
			pygame.draw.line(screen, white, (450,50), (600,50), 1)
			NumOfGreen = 0
			
		if thickList[1] != 0 and alzheimers == False: 
			pygame.draw.line(screen, white, (200,100), (600,100), (thickList[1]*2))
		elif thickList[1] != 0 and alzheimers == True: 
			pygame.draw.line(screen, white, (200,100), (350,100), 1)
			pygame.draw.line(screen, white, (450,100), (600,100), 1)
			NumOfBlack = 0
			
		if thickList[2] != 0 and alzheimers == False: 
			pygame.draw.line(screen, white, (200,150), (600,150), (2*thickList[2]))
		elif thickList[2] != 0 and alzheimers == True: 
			pygame.draw.line(screen, white, (200,150), (350,150), 1)
			pygame.draw.line(screen, white, (450,150), (600,150), 1)
			NumOfGrey = 0
			
		if thickList[3] != 0 and alzheimers == False: 
			pygame.draw.line(screen, white, (200,200), (600,200), (2*thickList[3]))
		elif thickList[3] != 0 and alzheimers == True: 
			pygame.draw.line(screen, white, (200,200), (350,200), 1)
			pygame.draw.line(screen, white, (450,200), (600,200), 1)
			NumOfWhite = 0
			
		if thickList[4] != 0 and alzheimers == False: 
			pygame.draw.line(screen, white, (200,250), (600,250), (2*thickList[4]))
		elif thickList[4] != 0 and alzheimers == True: 
			pygame.draw.line(screen, white, (200,250), (350,250), 1)
			pygame.draw.line(screen, white, (450,250), (600,250), 1)
			NumOfRed = 0
			
		if thickList[5] != 0 and alzheimers == False: 
			pygame.draw.line(screen, white, (200,300), (600,300), (2*thickList[5]))
		elif thickList[5] != 0 and alzheimers == True: 
			pygame.draw.line(screen, white, (200,300), (350,300), 1)
			pygame.draw.line(screen, white, (450,300), (600,300), 1)
			NumOfYellow = 0
			
		if thickList[6] != 0 and alzheimers == False: 
			pygame.draw.line(screen, white, (200,350), (600,350), (2*thickList[6]))
		elif thickList[6] != 0 and alzheimers == True: 
			pygame.draw.line(screen, white, (200,350), (350,350), 1)
			pygame.draw.line(screen, white, (450,350), (600,350), 1)
			NumOfOrange = 0
			
		if thickList[7] != 0 and alzheimers == False: 
			pygame.draw.line(screen, white, (200,400), (600,400), (2*thickList[7]))
		elif thickList[7] != 0 and alzheimers == True: 
			pygame.draw.line(screen, white, (200,400), (350,400), 1)
			pygame.draw.line(screen, white, (450,400), (600,400), 1)
			NumOfPink = 0
			
		if thickList[8] != 0 and alzheimers == False: 
			pygame.draw.line(screen, white, (200,450), (600,450), (2*thickList[8]))
		elif thickList[8] != 0 and alzheimers == True: 
			pygame.draw.line(screen, white, (200,450), (350,450), 1)
			pygame.draw.line(screen, white, (450,450), (600,450), 1)
			NumOfPurple = 0
			
		if thickList[9] != 0 and alzheimers == False: 
			pygame.draw.line(screen, white, (200,500), (600,500), (2*thickList[9]))
		elif thickList[9] != 0 and alzheimers == True: 
			pygame.draw.line(screen, white, (200,500), (350,500), 1)
			pygame.draw.line(screen, white, (450,500), (600,500), 1)
			NumOfBlue = 0
			
		pygame.display.flip()
	pygame.quit()	
	
	
	while quitEval == False: 
		userInputQuit = input("Do you want to quit?: ")
		if userInputQuit == 'Yes' or userInputQuit == 'yes' or userInputQuit == 'YES': 
			print("Okay. I'll see you next time.")
			quit = True
			quitEval = True
		elif userInputQuit == 'No' or userInputQuit == 'no' or userInputQuit == 'NO': 
			quit = False
			quitEval = True
			userInput = input("name of picture: ")
			if userInput == 'Alzheimers':
				alzheimers = True
				userInput = input("name of picture: ")
		elif userInputQuit == 'Do you?' or userInputQuit == 'Do You' or userInputQuit == 'Do you' or userInputQuit == 'Do You?' or userInputQuit == "do you?" or userInputQuit =="do you":
			print("I could do this all day.")
		else: 
			print("Please enter 'Yes' or 'No'.")
			

	





