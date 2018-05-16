import pygame
import os

class Rocket_Player(pygame.sprite.Sprite):
	# Constructor. Pass in the color of the block,
	# and its x and y position
	def __init__(self,  x, y, new_height, movespeed = 10):
		# Call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)


		print(x, y, new_height)
		# Create an image of the block, and fill it with a color.
		# This could also be an image loaded from the disk.
		image = pygame.image.load(os.path.join("Sprites",  "rocket.png"))
		width = image.get_rect().width
		height = image.get_rect().height

		ratio = width / height

		self.image = pygame.transform.scale(image, (int(new_height * ratio), new_height))


		# Fetch the rectangle object that has the dimensions of the image
		# Update the position of this object by setting the values of rect.x and rect.y
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.x = x

		self.dest = None
		self.movespeed = movespeed
		self.pathspeed = None
	def move_to(self, coords):
		self.dest = coords
		# self.pathspeed = distance()

	def down(self):
		self.rect.y += 1;

	def up(self):
		self.rect.y -= 1;

	def update(self):
		if self.dest != None:
			dist = distance(self.dest, (self.rect.x, self.rect.y))
			if dist < self.movespeed:
				self.rect.x = self.dest[0]
				self.rect.y = self.dest[1]
				self.dest = None
				return


			if (abs(self.dest[0] - self.rect.x)):
				self.rect.x += (self.dest[0] - self.rect.x) // abs(self.dest[0] - self.rect.x) * (dist // 3)
			if (abs(self.dest[1] - self.rect.y)):

				self.rect.y += (self.dest[1] - self.rect.y)  // abs(self.dest[1] - self.rect.y) * (dist // 3)


def distance(coord1, coord2):

	return ((coord1[1] - coord2[1])**2 + (coord1[0] - coord2[0])**2)**.5
class Lane(pygame.sprite.Sprite):
	def __init__(self,  x, y, size):

		# Call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)

		# Create an image of the block, and fill it with a color.
		# This could also be an image loaded from the disk.
		self.image = pygame.transform.scale(pygame.image.load(os.path.join("Sprites",  "lane.png")), size)


		# Fetch the rectangle object that has the dimensions of the image
		# Update the position of this object by setting the values of rect.x and rect.y
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.x = x
