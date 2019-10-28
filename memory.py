import pygame 
import random 

quit = False

userInputList = []
repeat2 = []
repeat3 = []
repeat4 = []
repeat5 = []
repeat6 = []
repeat7 = []
repeat8 = []

while quit == False:
	two = False
	three = False
	four = False
	five = False
	six = False
	seven = False
	userInput = input("Input something: ")
	
	if userInput == "quit":
		quit = True
		
	for i in range(len(repeat7)):
		if repeat7[i] == userInput:
			print("I've heard this more than 7 times now!")
			seven = True
			repeat8.append(userInput)
			
	for i in range(len(repeat6)):
		if repeat6[i] == userInput and seven == False:
			print("I've heard this six times now!")
			six = True
			repeat7.append(userInput)
			
	for i in range(len(repeat5)):
		if repeat5[i] == userInput and six == False and seven == False:
			print("I've heard this five times now!")
			five = True
			repeat6.append(userInput)
	
	for i in range(len(repeat4)):
		if repeat4[i] == userInput and five == False and six == False and seven == False:
			print("I've heard this four times now!")
			four = True
			repeat5.append(userInput)
	
	for i in range(len(repeat3)):
		if repeat3[i] == userInput and four == False and five == False and six == False and seven == False:
			print("I've heard this three times now!")
			three = True
			repeat4.append(userInput)
			
	
	for i in range(len(userInputList)): 
		if userInputList[i] == userInput and five == False and three == False and four == False and six == False and seven == False: 
			print("I've heard that before")
			two = True
			repeat3.append(userInput)
			

	userInputList.append(userInput)
	print(userInputList)
	


WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (142,229,238)
LTGREY = (168,168,168)
colors = [WHITE, BLUE, LTGREY]

pygame.init()


screenWidth = 800
screenHeight = 600
screenSize = (screenWidth, screenHeight)
screen = pygame.display.set_mode(screenSize)

size = 5

pygame.display.set_caption("Snow")

wind = random.choice([True,False])


class SnowFlake():

	def __init__(self, screen, size, xPos, yPos, chosenColor, wind=False):
		self.size = size
		self.screen = screen
		self.xPos = xPos
		self.yPos = yPos
		self.chosenColor = chosenColor
		self.wind = wind
   
	def fall(self, speed):
		self.speed = speed 
		self.yPos += self.speed
		
		if self.wind == True: 
			self.xPos -= random.randint(1,7)
			
	def draw(self): 
		pygame.draw.circle(self.screen, self.chosenColor, (self.xPos,self.yPos), self.size)


done = False
clock = pygame.time.Clock()

snow = []

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	screen.fill(BLACK)
	
	for i in range(len(snow)):
		snow[i].draw()
		snow[i].fall(random.randint(0,10))
		
	xPos = random.randint(0,700)
	
	snow.append(SnowFlake(screen, size, random.randint(0,screenWidth), 0, colors[random.randint(0,len(colors)-1)],wind))
	
	pygame.display.flip()
	clock.tick(60)
pygame.quit()