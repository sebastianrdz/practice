import pygame
import math
import time


# ---------------- DISPLAY SETUP ----------------
pygame.init()
WIDTH, HEIGHT = 300, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIK-TAK-TOE!")
FPS = 60
clock = pygame.time.Clock()
run = True
menu = False
player = -1
count = 0


# ---------------- SQUARES VARIABLES ----------------
SIZE = 100
squares = []
startx = 0
starty = 100
A = 65
ltr = ['O', 'X']
for i in range(9):
	x = startx + (SIZE * (i % 3))
	y = starty +((i // 3) * SIZE)
	squares.append([x,y, ltr, True])


# ---------------- FONTS ---------------- $ Posibly not
LETTER_FONT = pygame.font.SysFont('comicsans', 20)
WORD_FONT = pygame.font.SysFont('comicsans', 30)
TITLE_FONT = pygame.font.SysFont('comicsans', 40)
GAME_FONT = pygame.font.SysFont('comicsans', 100)


# ---------------- LOAD IMAGES ---------------- $ X and O



# ---------------- COLORS ----------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# ---------------- ALL FUNCTIONS USED THROUGHOUT THE PROGRAM ----------------
# ---------------- DRAW FUNCTION ----------------
def draw(player):
	win.fill(WHITE)
	# #Draw title
	text = TITLE_FONT.render("TIK-TAK-TOE", 1, BLACK)
	win.blit(text, (WIDTH/2 - text.get_width()/2, 20)) 

	# Draw squares
	for square in squares:
		x, y, ltr, visible = square
		if visible:
			pygame.draw.rect(win, WHITE, (x,y, SIZE, SIZE))
			text = GAME_FONT.render(ltr[player], 1, BLACK)
			win.blit(text, (x + text.get_width()/2, y + text.get_height()/2))

	pygame.display.update()


# ---------------- CENTER DISPALY MESSAGE (WON & LOST) ----------------
def display_message(message):
	pygame.time.delay(1000)
	win.fill(WHITE)
	text = WORD_FONT.render(message, 1, BLACK)
	win.blit(text,(WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
	pygame.display.update()
	pygame.time.delay(3000)


# ---------------- WINDOW EVENTS FUNCTION ----------------
def events():
	global menu
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			m_x, m_y = pygame.mouse.get_pos()
			if menu == True:
				x, y = 150,200
				dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
				if dis < 60:
					menu = False
			# 		reset values
			# else:
			# 	for square in squares:
			# 		x, y, ltr, visible = square
			# 		if visible:
			# 			dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
			# 			if dis < (SIZE/2):
            #                 draw(player)
                                
def winer():
    # VALIDATE WHO IS THE WINER

    # won = True
    # for letter in word:
    # 	if letter not in guessed:
    # 		won = False
    # 		break

    # if won:
    # 	display_message("You WON!")
    # 	menu = True
    # 	break
    # if hangman_status == 6:
    # 	display_message("You LOST :(")
    # 	menu = True
    # 	break
    return False


# ---------------- MAIN PROGRAM FUNCTION ----------------
def main():
	global run, count, menu
	while run:
		clock.tick(FPS)
		events()
        if count %2 ==0:
            player = 0
        else:
            player = 1

	    draw(player)

        if winer() == True:
            menu = True
            return
        else:
            count +=1


# ---------------- MAIN MENU FUNCTION ----------------
def main_menu():
	global menu
	menu = True
	
	while menu:
		clock.tick(FPS)
		events()
		win.fill(WHITE)
		
		# DISPLAY MENU TITLE
		text = TITLE_FONT.render("TIK-TAK-TOE!", 1, BLACK)
		win.blit(text,(WIDTH/2 - text.get_width()/2, 20))

		# DRAW 1 v 1 BUTTON
		x, y = 150,200
		pygame.draw.circle(win, BLACK, (x,y), 60, 3)
		text = WORD_FONT.render("START", 1, BLACK)
		win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
		pygame.display.update()

		if menu == False:
			main()
		else:
			continue


main_menu()