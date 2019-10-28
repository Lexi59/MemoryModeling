import pygame

pygame.init()
	
screenWidth = 800
screenHeight = 1000
screenSize = (screenWidth, screenHeight)
screen = pygame.display.set_mode(screenSize)
done = False 
xPos = [100,100]
yPos = [200,100]
white = (255,255,255)
black = (0,0,0)
clock = pygame.time.Clock()
clock.tick(60)

while not done: 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	screen.fill(black)
	pygame.draw.line(screen, white, xPos, yPos, 5)
	pygame.display.flip()
pygame.quit()
