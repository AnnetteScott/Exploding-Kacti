#Libraries
import pygame
from pygame import image
from pygame.constants import MOUSEBUTTONDOWN
pygame.font.init()
pygame.init()
#Function Files
from GAME.Settings import constants
from GAME.Engine import functions
from GAME.Engine import routines


#Screen and global variables
SCREEN = constants.SCREEN
MOUSE_POS = pygame.mouse.get_pos()
POND_DIM = 128
SCREEN_CENTER = constants.SCREEN_CENTER
SCREEN_HEIGHT = constants.SCREEN_HEIGHT
SCREEN_WIDTH = constants.SCREEN_WIDTH
pygame.display.set_caption("Exploding Kacti")

#####################################################################################
#-----------------------------------Draws the Game----------------------------------#
#####################################################################################

#Draws Background Image
def draw_background():
	image_dim = 500
	BACKGROUND = pygame.image.load('GAME/Images/sand_background.png').convert_alpha()
	BACKGROUND = pygame.transform.scale(BACKGROUND, (image_dim, image_dim))
	for y in range(0, SCREEN_HEIGHT, image_dim):
		for x in range(0, SCREEN_WIDTH, image_dim):
			SCREEN.blit(BACKGROUND, (x, y))

#Draws pond in middle of screen
def draw_pond():
	POND = pygame.image.load('GAME/Images/ponds/pond10.png')
	POND = pygame.transform.scale(POND, (POND_DIM, POND_DIM))
	pond_offsetX = SCREEN_WIDTH / 2 - POND_DIM / 2
	pond_offsetY = SCREEN_HEIGHT / 2 - POND_DIM / 2
	SCREEN.blit(POND, (pond_offsetX, pond_offsetY))

def draw_meters():
	bar_height = 15
	bar_width = POND_DIM
	barX = SCREEN_CENTER['x'] - POND_DIM / 2 
	barY = SCREEN_CENTER['y'] + POND_DIM / 2
	pygame.draw.rect(SCREEN, (0, 0, 0), (barX, barY, bar_width, bar_height), 3)
	routines.createText('Health', 15, barX + POND_DIM / 2 - 26, barY - 1)
	barY += bar_height
	pygame.draw.rect(SCREEN, (0, 0, 0), (barX, barY, bar_width, bar_height), 3)
	routines.createText('Water', 15, barX + POND_DIM / 2 - 21, barY - 1)
	# barY = barY + 20
	# pygame.draw.rect(SCREEN, (0, 0, 0), (barX, barY, bar_width, bar_height), 3)
	# routines.createText('Water', 15, barX - 13, barY)


draw_background()
draw_pond()
draw_meters()
pygame.display.update()
#####################################################################################
#----------------------------------------Cacti--------------------------------------#
#####################################################################################

def draw_cactus():
	image_dim = 64
	cactus = pygame.image.load('GAME/Images/sprites/normal_cacti.png').convert_alpha()
	cactus = pygame.transform.scale(cactus, (image_dim, image_dim))
	SCREEN.blit(cactus, (150, 150))




#####################################################################################
#------------------------------------Click Events-----------------------------------#
#####################################################################################

def click_events():
	print(functions.checkObjectClick(POND_DIM, POND_DIM, SCREEN_CENTER['x'], SCREEN_CENTER['y']))
	if functions.checkObjectClick(POND_DIM, POND_DIM, SCREEN_CENTER['x'], SCREEN_CENTER['y']):
		draw_cactus()		
		pygame.display.update()
		pygame.time.delay(1000)


#PUT EVERYTHING BEFORE THIS
#####################################################################################
#--------------------------------------MAIN GAME------------------------------------#
#####################################################################################
#MAIN GAME
	
run = True
while run:
	pygame.time.delay(100)
	for event in pygame.event.get():
		if event.type == MOUSEBUTTONDOWN:		
			click_events()
			run = False

pygame.quit()


