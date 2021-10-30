import pygame
import math
import random
from ..Settings import constants
from ..Settings import cactus_items
from ..Settings import player
from ..Engine import functions

#####################################################################################
#-----------------------------------Called Routines---------------------------------#
#####################################################################################

def createText(text, font_size, x, y):
	myfont = pygame.font.SysFont('Courier New', font_size)
	textsurface = myfont.render(text, False, (0, 0, 0))
	constants.SCREEN.blit(textsurface,(x,y))

def generateCactus(cacti_type = "normal_cacti"):
	if len(cactus_items.all_cacti.keys()) < cactus_items.max_num_of_cacti:
		pos = {'x': constants.SCREEN_CENTER['x'], 'y': constants.SCREEN_CENTER['y']}

		while functions.getLinearDistance(pos, constants.SCREEN_CENTER) < cactus_items.cacti_min_spawn_distance or functions.between(pos['x'], (constants.SCREEN_CENTER['x'] - constants.POND_DIM / 2), (constants.SCREEN_CENTER['x'] + constants.POND_DIM / 2)):
			pos = {'x': random.randrange(0, constants.SCREEN_WIDTH), 'y': random.randrange(0, constants.SCREEN_HEIGHT)}

		id = functions.generateID()
		new_cactus_object = {
			'id': id,
			'cacti_type': cacti_type,
			'pos': pos,
			'dim': {'width': cactus_items.cacti_dim, 'height': cactus_items.cacti_dim},
			'hit_radius': cactus_items.cacti_dim / 2,
			'total_health': cactus_items.cacti_types[cacti_type]['health'],
			'remaining_health': cactus_items.cacti_types[cacti_type]['health']
		}
		new_cactus_object['pos'] = pos = functions.coordToCenter(new_cactus_object['pos'], new_cactus_object['dim']['width'], new_cactus_object['dim']['height'])
		cactus_items.all_cacti[id] = new_cactus_object

		cacti_item = new_cactus_object
		return cacti_item

def moveAllCacti():
	for cacti_id in list(cactus_items.all_cacti.keys()):
		current_pos = cactus_items.all_cacti[cacti_id]['pos']
		new_x = 0
		if current_pos['x'] < constants.SCREEN_CENTER['x']:
			new_x = current_pos['x'] + cactus_items.cacti_movement_speed
		else:
			new_x = current_pos['x'] - cactus_items.cacti_movement_speed

		new_y = functions.getPosAlongHypo(current_pos, constants.SCREEN_CENTER, new_x)
		new_pos = {'x': new_x, 'y': new_y}
		cactus_items.all_cacti[cacti_id]['pos'] = new_pos

		cactus = pygame.image.load('GAME/Images/sprites/'+ cactus_items.all_cacti[cacti_id]['cacti_type'] +'.png').convert_alpha()
		cactus = pygame.transform.scale(cactus, (cactus_items.cacti_dim, cactus_items.cacti_dim))
		constants.SCREEN.blit(cactus, (new_pos['x'], new_pos['y']))

		cactusAttack(cacti_id)


#####################################################################################
#------------------------------------Game Play--------------------------------------#
#####################################################################################

def changeHealth(modifier):
	current_amount = player.player['health']
	if(current_amount + modifier < 0):
		current_amount = 0
	elif current_amount + modifier > 100:
		current_amount = 100
	else:
		current_amount = current_amount + modifier

	#health_bar_elem.style.height = current_amount + "%";
	#health_bar_text_elem.innerHTML = current_amount + "%";
	player.player['health'] = current_amount
	#pondDamage(current_amount)

def changeWater(modifier):
	current_amount = player.pond_item['water_amount']
	if current_amount + modifier < 0:
		current_amount = 0
	elif current_amount + modifier >= 100:
		current_amount = 100
	else:
		current_amount = current_amount + modifier

	player.pond_item['water_amount'] = current_amount
	#pondDamage(current_amount)

def check_game_over():
	a_bool = player.player['health'] <= 0
	return a_bool

def gameOver():
	if check_game_over():
		showEndScreen()

    # pond_elem.classList.add("noafter");
    # window.clearInterval(anim_intervals['spawn_cacti']);
    # window.clearInterval(anim_intervals['move_cacti']);
    # document.querySelectorAll('cactus').forEach((elem) => {
    #   elem.classList.add("a_cactus_celebration");
    # });
    # spawnHitText({x: center_of_game.x - 125, y: center_of_game.y - 100}, '202020', 36, "GAME&nbsp;OVER");



def showEndScreen():
	cactus_items.cacti_movement_speed = 0
	createText('GAME OVER', 40, constants.SCREEN_CENTER['x'], constants.SCREEN_CENTER['y'])
	#final_score = createText('0000')



#####################################################################################
#----------------------------------Routine Functions--------------------------------#
#####################################################################################

def cactusAttack(cacti_id):
	if functions.checkCollision(cactus_items.all_cacti[cacti_id], player.pond_item):
		changeHealth(-10)
		del cactus_items.all_cacti[cacti_id]
		#spawnHitText({x: center_of_game.x - 14, y: center_of_game.y - 100}, 'FF0000', 20, "-10")
		#explode(center_of_game, 'ff0000')
		gameOver()