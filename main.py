import pygame
import random
import Sprite

pygame.init()
# Define some colors






BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


KEY_A = 97
KEY_B = 98
KEY_DOWN = 274
KEY_UP = 273






# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My First Game")


carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
color = WHITE




spriteGroup = pygame.sprite.Group()
laneGroup = pygame.sprite.Group()






# GAME INITIALIZATION VARIABLES
DIFFICULTY = 5

num_lanes = DIFFICULTY + 3
lanes = []

cur_lane = num_lanes // 2

# DEFINTE PLAYABLE CHARACTER
main_character = Sprite.Rocket_Player(0,0, int(size[1] // num_lanes))
spriteGroup.add(main_character)




for i in range(num_lanes):
	cur_pos = (0, (size[1] // num_lanes) * i)
	nl = Sprite.Lane(cur_pos[0], cur_pos[1], (size[0], size[1] // num_lanes))
	laneGroup.add(nl)
	lanes.append(cur_pos)


# -------- Main Program Loop -----------
while carryOn:
	# --- Main event loop

	for event in pygame.event.get():  # User did something
		if event.type == pygame.QUIT:  # If user clicked close
			carryOn = False  # Flag that we are done so we exit this loop


		# --- Game logic should go here
		if event.type == pygame.KEYDOWN:
			keymask = pygame.key.get_pressed()
			print(keymask.index(1))
			if keymask[KEY_A]:
				# color = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
				main_character.move_to((50,50))
			if keymask[KEY_B]:
				# color = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
				main_character.move_to((100,100))
			if keymask[KEY_DOWN] and keymask[KEY_UP]:
				pass
			elif keymask[KEY_DOWN]:
				# cur_lane = min(len(lanes) - 1, cur_lane + 1)
				cur_lane = (cur_lane + 1) % len(lanes)
				main_character.move_to(lanes[cur_lane])

			elif keymask[KEY_UP]:
				# cur_lane = max(0, cur_lane - 1)
				cur_lane = (cur_lane - 1) % len(lanes)
				main_character.move_to(lanes[cur_lane])





		# --- Drawing code should go here
		# First, clear the screen to white.
	screen.fill(color)  # The you can draw different shapes and lines or add text to your background stage.
	main_character.update()
	laneGroup.draw(screen)
	spriteGroup.draw(screen)

	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(1000)  # Once we have exited the main program loop we can stop the game engine:
pygame.quit()
