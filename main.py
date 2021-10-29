#Libraries
import pygame
from pygame import image
from pygame.constants import MOUSEBUTTONDOWN
pygame.font.init()
pygame.init()
#Function Files
from Engine import constants
from Engine import functions


#Screen and global variables
MOUSE_POS = pygame.mouse.get_pos()
POND_DIM = 128
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Exploding Kacti")

#####################################################################################
#-----------------------------------Draws the Game----------------------------------#
#####################################################################################

#Draws Background Image
def draw_background():
	image_dim = 500
	BACKGROUND = pygame.image.load('Images/sand_background.png').convert_alpha()
	BACKGROUND = pygame.transform.scale(BACKGROUND, (image_dim, image_dim))
	for y in range(0, SCREEN_HEIGHT, image_dim):
		for x in range(0, SCREEN_WIDTH, image_dim):
			SCREEN.blit(BACKGROUND, (x, y))

#Draws pond in middle of screen
def draw_pond():
	POND = pygame.image.load('Images/ponds/pond10.png')
	POND = pygame.transform.scale(POND, (POND_DIM, POND_DIM))
	offsetX = SCREEN_WIDTH / 2 - POND_DIM / 2
	offsetY = SCREEN_HEIGHT / 2 - POND_DIM / 2
	SCREEN.blit(POND, (offsetX, offsetY))

def draw_meters():
	bar_height = 15
	bar_width = 100
	barX = SCREEN_WIDTH / 2 - POND_DIM / 2 
	barY = SCREEN_HEIGHT / 2 + POND_DIM / 2
	pygame.draw.rect(SCREEN, (0, 0, 0), (barX, barY, bar_width, bar_height), 3)
	barY = barY + bar_height
	functions.createText('Health', 15, barX - 13, barY)
	barY = barY + 20
	pygame.draw.rect(SCREEN, (0, 0, 0), (barX, barY, bar_width, bar_height), 3)
	barY = barY + bar_height
	functions.createText('Water', 15, barX - 13, barY)


draw_background()
draw_pond()
draw_meters()
pygame.display.update()
#####################################################################################
#----------------------------------------Cacti--------------------------------------#
#####################################################################################

def draw_cactus():
	image_dim = 64
	cactus = pygame.image.load('Images/sprites/normal_cacti.png').convert_alpha()
	cactus = pygame.transform.scale(cactus, (image_dim, image_dim))
	SCREEN.blit(cactus, (150, 150))




#####################################################################################
#------------------------------------Click Events-----------------------------------#
#####################################################################################

def click_events(event):
	global MOUSE_POS
	global index
	MOUSE_POS = pygame.mouse.get_pos()
	if functions.between(MOUSE_POS[0], SCREEN_WIDTH/2 - POND_DIM/2, SCREEN_WIDTH/2 + POND_DIM/2) and functions.between(MOUSE_POS[1], SCREEN_HEIGHT/2 - POND_DIM/2, SCREEN_HEIGHT/2 + POND_DIM/2):
			print("THIS RAN")
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
			click_events(event)
			run = False

pygame.quit()


