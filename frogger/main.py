import pygame, sys, time, random
from pygame.locals import *
from classes import *


pygame.init()
pygame.mixer.init()

'''pygame.mixer.music.load('frogger-ringtone/frogger-ringtone.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)'''




screen = pygame.display.set_mode((screen_x,screen_y))
#game = Game()



frog = Frog()
background = pygame.image.load('images/background.png')

car_left = Car(screen_x - 30,screen_y/1.21,'left','normal',0.5)



racing_right = Car(0,screen_y/1.3,'right','racing',0.7)


wood = pygame.image.load('images/wood_long1.png')
wood_left = Wood(screen_x - 30,screen_y/2.25,car_left.speed)

wood_right = Wood(0,screen_y/2.55,car_left.speed)

score = pygame.image.load('images/score.png')
time_image = pygame.image.load('images/time.png')


game_over = pygame.image.load('images/over.png')
menu = pygame.image.load('images/menu_start.jpg')
yes = pygame.image.load('images/yes.png')
no = pygame.image.load('images/no.png')
play = pygame.image.load('images/play.png')
#play_pos = pygame.image.load('images/play_press.png')

yes_pos = pygame.image.load('images/yes_pos.png')
no_pos = pygame.image.load('images/no_pos.png')

myfont = pygame.font.SysFont("monospace", 20)

label = myfont.render(str(points), 1, (255,255,0))
#screen.blit(label, (100, 100))


menu_x = 0
menu_y = 0

game_over_x = 0
game_over_y = 0

max_distance_y = 20


pygame.display.set_caption('Frogger game')

const_pos = []

car_left_pos = [[car_left.x - random.randrange(100,200)],[car_left.x - random.randrange(50,100)],[car_left.x - random.randrange(100,200)]]
#car_left_pos2 = [car_left_x]
racing_right_pos = [[racing_right.x],[racing_right.x + random.randrange(50,200)],[racing_right.x + random.randrange(100,200)]]

wood_left_pos = [[wood_left.x - random.randrange(100,200)],[wood_left.x - random.randrange(50,100)],[wood_left.x - random.randrange(100,200)]]
wood_right_pos = [[wood_right.x + random.randrange(100,200)],[wood_right.x + random.randrange(50,100)],[wood_right.x + random.randrange(100,200)]]

for i in range(0,3):
	for j in range(1,5):
		car_left_pos[i].append(car_left_pos[i][j-1] + random.randrange(100,200))
		racing_right_pos[i].append(racing_right_pos[i][j-1] - random.randrange(100,200))
		wood_left_pos[i].append(wood_left_pos[i][j-1] + random.randrange(150,250))
		wood_right_pos[i].append(wood_right_pos[i][j-1] - random.randrange(150,250))


flag = 0
start_game = 0

while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit(0)

	if start_game == 0:
		start_game = 1
		screen.blit(menu,(menu_x,menu_y))
		screen.blit(play,(180,245))
		pygame.display.flip()

		event = pygame.event.poll()
		mouse_x, mouse_y = pygame.mouse.get_pos()
			
		

		#time.sleep(3)
		while True:
			event = pygame.event.poll()
			keys = pygame.key.get_pressed()
			if event.type == pygame.QUIT:
				sys.exit(0)
			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse_x > 180 and mouse_x < 280 and mouse_y > 245 and mouse_y < 280:
				#print("You pressed the left mouse button at (%d, %d)", event.pos)
				break
			elif event.type == KEYDOWN and event.key == K_RETURN:
				break


		#screen.fill((0,0,255))
	if flag == 0:
		current_time = pygame.time.get_ticks()
		flag = 1
	keys = pygame.key.get_pressed()
	if keys[pygame.K_RIGHT] and frog.x < screen_x - 30 and pygame.time.get_ticks() - current_time > sleep_time:
		frog.x += frog.jump_h
		#time = pygame.time.get_ticks()
		flag = 0
		frog.orient = 'right'

	if keys[pygame.K_LEFT] and frog.x > 10 and pygame.time.get_ticks() - current_time > sleep_time:
		#if CHOICE == 'u' or CHOICE == 'd':
			#frog_y -= 1
		frog.x -= frog.jump_h
		flag = 0
		frog.orient = 'left'

	if keys[pygame.K_UP] and frog.y > 30 and pygame.time.get_ticks() - current_time > sleep_time:
		if frog.orient == 'left' or frog.orient == 'right':
			frog.y -= 0.1
		frog.y -= frog.jump_v
		flag = 0
		frog.orient = 'up'
		points += 10
		label = myfont.render(str(points), 1, (255,255,0))

	if keys[pygame.K_DOWN] and frog.y < screen_y - 50 and pygame.time.get_ticks() - current_time > sleep_time:
		if frog.orient == 'left' or frog.orient == 'right':
			frog.y -= 0.1
		frog.y += frog.jump_v
		flag = 0
		frog.orient = 'down'

	if frog.y < 80 and (frog.x > 11 and frog.x < 48 or frog.x > 108 and frog.x < 145 or frog.x > 205 and frog.x < 242 or frog.x > 302 and frog.x < 339 or frog.x > 399 and frog.x < 436): 
	
		#print("aaaaaaaaa")
		orient = frog.orient
		const_pos.append(frog.x)
		const_pos.append(frog.y)
		for i in range(0,len(const_pos),2):
			frog.orient = 'up'
			screen.blit(frog.image(),(const_pos[i],const_pos[i+1]))
		screen.blit(background,(0,0))
		screen.blit(score,(screen_x/2.4,5))
		screen.blit(time_image,(390,494))

		frog.orient = orient

		for i in range(0,3):
			k = i
			for j in range(0,5):	
				screen.blit(wood,(wood_left_pos[i][j],wood_left.y-i*53))
				screen.blit(wood,(wood_right_pos[i][j],wood_right.y-i*53))
				screen.blit(car_left.image(),(car_left_pos[i][j],car_left.y-i*53))
				screen.blit(racing_right.image(),(racing_right_pos[i][j],racing_right.y-i*53))
		
		
		screen.blit(frog.image(), (frog.x, frog.y))

		for i in range(0,3):
			for j in range(0,5):
				car_left_pos[i][j] -= car_left.speed
				racing_right_pos[i][j] += racing_right.speed
				wood_left_pos[i][j] -= (i/2+1)*wood_left.speed
				wood_right_pos[i][j] += (i/2+1)*wood_right.speed

		rect_time = 180
		pygame.draw.rect(screen,(255,255,0),pygame.Rect(380, 495, -rect_time , 15))
		pygame.display.flip()


		#keys = pygame.key.get_pressed()
		#lifes -= 1
		
		#frog.orient = 'up'
		event = pygame.event.poll()
		mouse_x, mouse_y = pygame.mouse.get_pos()
			
		

		#time.sleep(3)

		while True:
			event = pygame.event.poll()
			if event.type == pygame.QUIT:
				sys.exit(0)
			if event.type == KEYDOWN and event.key == K_RETURN:
			#elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				frog.x = screen_x/2
				frog.y = screen_y - 60
				#frog.setDefault()
				car_left.x = screen_x - 30
				car_left.y = screen_y/1.21


				racing_right.x = 0
				racing_right.y = screen_y/1.3
			#print("You pressed the left mouse button at (%d, %d)", event.pos)
				break

	#frog.jump_v = 28

	if frog.y < 230:
		frog.jump_v = 26.3 #26.5

	for i in range(0,3):
		for j in range(1,5):
			if car_left_pos[i][0] < -70 :
				#car_left = pygame.image.load('car.png')
				car_left_pos[i][0] = car_left_pos[i][4] + random.randrange(100,200)
			if car_left_pos[i][j] < -70 :
				#car_left_y = screen_y/1.22
				car_left_pos[i][j] = car_left_pos[i][j-1] + random.randrange(100,200)
		
			if racing_right_pos[i][0] > screen_x + 70:
				#car_left = pygame.image.load('car.png')
				racing_right_pos[i][0] = racing_right_pos[i][4] - random.randrange(100,200)
			if racing_right_pos[i][j] > screen_x + 70:
				#car_left_y = screen_y/1.22
				racing_right_pos[i][j] = racing_right_pos[i][j-1] - random.randrange(100,200)

			if wood_left_pos[i][0] < -70 :
				#car_left = pygame.image.load('car.png')
				wood_left_pos[i][0] = wood_left_pos[i][4] + random.randrange(100,200)
			if wood_left_pos[i][j] < -70 :
				#car_left_y = screen_y/1.22
				wood_left_pos[i][j] = wood_left_pos[i][j-1] + random.randrange(100,200)

			if wood_right_pos[i][0] > screen_x + 70:
				#car_left = pygame.image.load('car.png')
				wood_right_pos[i][0] = wood_right_pos[i][4] - random.randrange(100,200)
			if wood_right_pos[i][j] > screen_x + 70:
				#car_left_y = screen_y/1.22
				wood_right_pos[i][j] = wood_right_pos[i][j-1] - random.randrange(100,200)

	rect_wood = wood.get_rect()
	rect_wood.left = wood_left.x
	rect_wood.top = wood_left.y

	f = 0
	fl0 = fl1 = fl2 = 0

	for i in range(0,3):
		for j in range(0,5):
			rect_wood.left = wood_left_pos[i][j]
			rect_wood.top = wood_left.y-i*53
			rect = frog.getRect()
			rect.top = frog.y
			rect.left = frog.x
			if rect_wood.contains(rect) or rect_time < 1:
				#print("aaaaaaaaaaaa")
				if i == 0:
					fl0 = 1
				elif i == 1:
					fl1 = 1
				elif i == 2:
					fl2 = 1
				f = 1
				break
			
	
	rect_wood.left = wood_right.x
	rect_wood.top = wood_right.y

	fr0 = fr1 = fr2 = 0

	if f == 0:
		for i in range(0,3):
			for j in range(0,5):
				rect_wood.left = wood_right_pos[i][j]
				rect_wood.top = wood_right.y-i*53
				rect = frog.getRect()
				rect.top = frog.y
				rect.left = frog.x
				if rect_wood.contains(rect) or rect_time < 1:
					if i == 0:
						fr0 = 1
					elif i == 1:
						fr1 = 1
					elif i == 2:
						fr2 = 1
					f = 1
					break
				
				
	if(f == 0 and frog.y < 250):


		rect_time = 180
		screen.blit(background,(0,0))
		screen.blit(score,(screen_x/2.4,5))
		screen.blit(time_image,(390,494))
		orient = frog.orient
		for i in range(0,frog.lifes):
			frog.orient = 'up'
			screen.blit(frog.image(),(10+i*30,494))
		frog.orient = orient
		for i in range(0,3):
			k = i
			for j in range(0,5):
	
				screen.blit(wood,(wood_left_pos[i][j],wood_left.y-i*53))
				screen.blit(wood,(wood_right_pos[i][j],wood_right.y-i*53))
				screen.blit(car_left.image(),(car_left_pos[i][j],car_left.y-i*53))
				screen.blit(racing_right.image(),(racing_right_pos[i][j],racing_right.y-i*53))


		screen.blit(frog.image(), (frog.x, frog.y))
		frog.setDefault()

		for i in range(0,3):
			for j in range(0,5):
				car_left_pos[i][j] -= car_left.speed
				racing_right_pos[i][j] += racing_right.speed
				wood_left_pos[i][j] -= (i/2+1)*wood_left.speed
				wood_right_pos[i][j] += (i/2+1)*wood_right.speed

		pygame.display.flip()


		keys = pygame.key.get_pressed()
		frog.lifes -= 1
		frog.orient = 'up'
		if frog.lifes >= 0:
			while True:
				event = pygame.event.poll()
				if event.type == pygame.QUIT:
					sys.exit(0)
				if event.type == KEYDOWN and event.key == K_RETURN:
				#elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					frog.x = screen_x/2
					frog.y = screen_y - 60
					car_left.x = screen_x - 30
					car_left.y = screen_y/1.21

					racing_right.x = 0
					racing_right.y = screen_y/1.3
				#print("You pressed the left mouse button at (%d, %d)", event.pos)
					break

		if frog.lifes == 0:
			#time.sleep(0.5)
			points = 0
			label = myfont.render(str(points), 1, (255,255,0))
			const_pos = []
			while True:
				frog.x = screen_x/2
				frog.y = screen_y - 60
				#frog.setDefault()
				car_left.x = screen_x - 30
				event = pygame.event.poll()
				mouse_x, mouse_y = pygame.mouse.get_pos()
	
				if mouse_x > 158 and mouse_x < 210 and mouse_y > 440 and mouse_y < 488:
					screen.blit(yes_pos,(155,430))
					pygame.display.flip()
					time.sleep(0.1)

				if mouse_x > 240 and mouse_x < 270 and mouse_y > 442 and mouse_y < 488:
					screen.blit(no_pos,(220,425))
					pygame.display.flip()
					time.sleep(0.1)
	
				if event.type == pygame.QUIT:
					sys.exit(0)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse_x > 158 and mouse_x < 210 and mouse_y > 442 and mouse_y < 488:
				#print("You pressed the left mouse button at (%d, %d)", event.pos)
					frog.lifes = 3
					break
				elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse_x > 240 and mouse_x < 270 and mouse_y > 442 and mouse_y < 488:
					sys.exit(0)

				screen.blit(game_over,(game_over_x,game_over_y))
				screen.blit(yes,(155,430))
				screen.blit(no,(220,425))
				pygame.display.flip()


	rect_car_left = car_left.getRect()
	rect_car_left.left = car_left.x
	rect_car_left.top = car_left.y

	rect_racing_right = racing_right.getRect()
	rect_racing_right.left = racing_right.x
	rect_racing_right.top = racing_right.y

	f2 = 0


	for i in range(0,3):
		for j in range(0,5):
			rect = frog.getRect()
			rect.top = frog.y
			rect.left = frog.x
			if rect_car_left.colliderect(rect) or rect_racing_right.colliderect(rect) or rect_time < 1:
				f2 = 1
				break
			rect_car_left.left = car_left_pos[i][j]
			rect_car_left.top = car_left.y-i*53
			rect_racing_right.left = racing_right_pos[i][j]
			rect_racing_right.top = racing_right.y-i*53


	if f2 == 1:
		rect_time = 180

		screen.blit(background,(0,0))
		screen.blit(score,(screen_x/2.4,5))
		screen.blit(time_image,(390,494))
		

		for i in range(0,3):
			k = i
			for j in range(0,5):
				screen.blit(wood,(wood_left_pos[i][j],wood_left.y-i*53))
				screen.blit(wood,(wood_right_pos[i][j],wood_right.y-i*53))
				screen.blit(car_left.image(),(car_left_pos[i][j],car_left.y-i*53))
				screen.blit(racing_right.image(),(racing_right_pos[i][j],racing_right.y-i*53))
		screen.blit(frog.image(), (frog.x, frog.y))

			
		for i in range(0,3):
			for j in range(0,5):
				car_left_pos[i][j] -= car_left.speed
				racing_right_pos[i][j] += racing_right.speed
				wood_left_pos[i][j] -= (i/2+1)*wood_left.speed
				wood_right_pos[i][j] += (i/2+1)*wood_right.speed

		for i in range(0,frog.lifes):
			frog.orient = 'up'
			screen.blit(frog.image(),(10+i*30,494))

		pygame.display.flip()


		keys = pygame.key.get_pressed()
		frog.lifes -= 1
		frog.orient = 'up'
		frog.setDefault()
		if frog.lifes >= 0:
			while True:
				event = pygame.event.poll()
				if event.type == pygame.QUIT:
					sys.exit(0)
				if event.type == KEYDOWN and event.key == K_RETURN:
				#elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					frog.x = screen_x/2
					frog.y = screen_y - 60
					car_left.x = screen_x - 30
					car_left.y = screen_y/1.21

					racing_right.x = 0
					racing_right.y = screen_y/1.3
				#print("You pressed the left mouse button at (%d, %d)", event.pos)
					break

		if frog.lifes == 0:
			const_pos = []
			points = 0
			label = myfont.render(str(points), 1, (255,255,0))
			while True:
				frog.x = screen_x/2
				frog.y = screen_y - 60
				car_left.x = screen_x - 30
				event = pygame.event.poll()
				mouse_x, mouse_y = pygame.mouse.get_pos()
	
				if mouse_x > 158 and mouse_x < 210 and mouse_y > 440 and mouse_y < 488:
					screen.blit(yes_pos,(155,430))
					pygame.display.flip()
					time.sleep(0.1)

				if mouse_x > 240 and mouse_x < 270 and mouse_y > 442 and mouse_y < 488:
					screen.blit(no_pos,(220,425))
					pygame.display.flip()
					time.sleep(0.1)
	
				if event.type == pygame.QUIT:
					sys.exit(0)
				elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse_x > 158 and mouse_x < 210 and mouse_y > 442 and mouse_y < 488:
					frog.lifes = 3
					break
				elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse_x > 240 and mouse_x < 270 and mouse_y > 442 and mouse_y < 488:
					sys.exit(0)

				screen.blit(game_over,(game_over_x,game_over_y))
				screen.blit(yes,(155,430))
				screen.blit(no,(220,425))
				pygame.display.flip()
		

	for i in range(0,3):
		for j in range(0,5):
			if fl0 == 1:
				frog.x -= wood_left.speed/15 #/15
			elif fl1 == 1:
				frog.x -= wood_left.speed/10
			elif fl2 == 1:
				frog.x -= wood_left.speed/7.5
			elif fr0 == 1:
				frog.x += wood_left.speed/15
			elif fr1 == 1:
				frog.x += wood_left.speed/10
			elif fr2 == 1:
				frog.x += wood_left.speed/7.5
			car_left_pos[i][j] -= car_left.speed
			racing_right_pos[i][j] += racing_right.speed
			wood_left_pos[i][j] -= (i/2+1)*wood_left.speed
			wood_right_pos[i][j] += (i/2+1)*wood_right.speed
		

	screen.blit(background,(0,0))
	screen.blit(score,(screen_x/2.4,5))
	screen.blit(label,(screen_x/2.05, 25))
	screen.blit(time_image,(390,494))
	orient = frog.orient
	for i in range(0,len(const_pos),2):
			frog.orient = 'up'
			screen.blit(frog.image(),(const_pos[i],const_pos[i+1]))
	for i in range(0,frog.lifes):
		frog.orient = 'up'
		screen.blit(frog.image(),(10+i*30,494))

	frog.orient = orient

	for i in range(0,3):
		k = i
		for j in range(0,5):
			#if i < 1: #2
				#screen.blit(wood,(wood_left_pos[i][j],wood_left_y-i*27))
			#else:
			screen.blit(wood,(wood_left_pos[i][j],wood_left.y-i*53))
			'''if k < 1:
				screen.blit(wood,(wood_right_pos[i][j],wood_right_y-i*27))
			elif k == 1:
				screen.blit(wood,(wood_right_pos[i][j],wood_right_y-i*53))
			else:
				screen.blit(wood,(wood_right_pos[i][j],wood_right_y-i*39))'''
			screen.blit(wood,(wood_right_pos[i][j],wood_right.y-i*53))
			screen.blit(car_left.image(),(car_left_pos[i][j],car_left.y-i*53))
			screen.blit(racing_right.image(),(racing_right_pos[i][j],racing_right.y-i*53))

	screen.blit(frog.image(), (frog.x, frog.y))

	pygame.draw.rect(screen,(255,255,0),pygame.Rect(380, 495, -rect_time , 15))
	rect_time -= 0.1
	pygame.display.flip()
	



