import pygame
from pygame.locals import *
rect_time = 180
#lifes = 3
points = 0
sleep_time = 200
screen_x = 448
screen_y = 515


class Game(object):
	def __init__(self):
		None
	def show(self):
		return pygame.display.set_mode((screen_x,screen_y))


class Object(object):
	def __init__(self,_x,_y):
		self.x = _x
		self.y = _y
	def image(self):
		None
	def getRect(self):
		None
	def setDefault(self):
		None

class Frog(Object):
	def __init__(self,_x=screen_x/2,_y=screen_y - 60,_orient='up',_jump_v=28,_jump_h=20,_lifes=3):
		super().__init__(_x,_y)
		self.orient = _orient
		self.jump_v = _jump_v
		self.jump_h = _jump_h
		self.lifes = _lifes
	def image(self):
		if self.orient == 'up':
			return pygame.image.load('images/frog1.png')
		elif self.orient == 'down':
			return pygame.image.load('images/frog1_down.png')
		elif self.orient == 'left':
			return pygame.image.load('images/frog1_left.png')
		elif self.orient == 'right':
			return pygame.image.load('images/frog1_right.png')
	def getRect(self):
		return self.image().get_rect()
	def setDefault(self):
		self.x = screen_x/2
		self.x = screen_y - 60
		self.orient = 'up'
		self.jump_v = 28
		self.jump_h = 20
		#self.lifes = 3

class Car(Object):
	def __init__(self,_x,_y,_orient,_type,_speed):
		super().__init__(_x,_y)
		self.orient = _orient
		self.type = _type
		self.speed = _speed
	def image(self):
		if self.orient == 'right' and self.type == 'normal':
			return pygame.image.load('images/car_right.png')
		elif self.orient == 'left' and self.type == 'normal':
			return pygame.image.load('images/car_left.png')
		elif self.orient == 'right' and self.type == 'racing':
			return pygame.image.load('images/racing_right.png')
		elif self.orient == 'left' and self.type == 'racing':
			return pygame.image.load('images/racing_left.png')
	def getRect(self):
		return self.image().get_rect()

class Wood(Object):
	def __init__(self, _x,_y,_speed):
		super().__init__(_x,_y)
		self.speed = _speed
	def image(self):
		return pygame.image.load('images/wood_long1.png')
