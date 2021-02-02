#Python 2.7.16 64-bit
import pygame
import math
import random

# ---------------- ALL GLOBAL VARIABLES USED THROUGHOUT THE PROGRAM ----------------
# ---------------- DISPLAY SETUP ----------------
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")
FPS = 60
clock = pygame.time.Clock()
run = True
terminate = False
menu = False

# ---------------- BUTTON VARIABLES ----------------
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
	x = startx + GAP *2 + ((RADIUS * 2 + GAP) * (i % 13))
	y = starty +((i // 13) * (GAP + RADIUS * 2))
	letters.append([x,y, chr(A+i), True])

# ---------------- FONTS ----------------
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

# ---------------- LOAD IMAGES ----------------
images = []
for i in range(7):
	image = pygame.image.load("hangman" + str(i) + ".png")
	images.append(image)

# ---------------- GAME VAIABLES ----------------
hangman_status = 0
words = ["A", "AB", "ABC", "ABCD", "ABCDE", "ABCDEF"]
word = ""
guessed = []

# ---------------- COLORS ----------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)








# ---------------- ALL FUNCTIONS USED THROUGHOUT THE PROGRAM ----------------
# ---------------- DRAW FUNCTION ----------------
def draw():
	win.fill(WHITE)
	#Draw title
	text = TITLE_FONT.render("Hangman", 1, BLACK)
	win.blit(text, (WIDTH/2 - text.get_width()/2, 20)) 

	# Draw word
	display_word = ""
	for letter in word:
		if letter in guessed:
			display_word += letter + " "
		else:
			display_word += "_ "
	text = WORD_FONT.render(display_word, 1, BLACK)
	win.blit(text,(400,200))
		

	# Draw buttons
	for letter in letters:
		x, y, ltr, visible = letter
		if visible:
			pygame.draw.circle(win, BLACK, (x,y), RADIUS, 3)
			text = LETTER_FONT.render(ltr, 1, BLACK)
			win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

	win.blit(images[hangman_status], (150, 100))
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
	global menu, run, guessed, terminate, word, hangman_status
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			terminate = True
			menu = True
			# pygame.quit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			m_x, m_y = pygame.mouse.get_pos()
			if menu == True:
				x, y = 400, 350
				dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
				if dis < 60:
					menu = False
					for letter in letters:
						x, y, ltr, visible = letter
						letter[3] = True
						guessed = []
						hangman_status = 0
			else:
				for letter in letters:
					x, y, ltr, visible = letter
					if visible:
						dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
						if dis < RADIUS:
							letter[3] = False
							guessed.append(ltr)
							if ltr not in word:
								hangman_status += 1
		
		


# ---------------- MAIN PROGRAM FUNCTION ----------------
def main():
	global menu, word, hangman_status

	word = random.choice(words)
	while run:
		clock.tick(FPS)
		events()
		draw()

		won = True
		for letter in word:
			if letter not in guessed:
				won = False
				break
		
		if won:
			display_message("You WON!")
			menu = True
			break
		if hangman_status == 6:
			display_message("You LOST :(")
			menu = True
			break
		
# ---------------- MAIN MENU FUNCTION ----------------
def main_menu():
	global menu, terminate
	menu = True
	# DISPLAY MENU TITLE
	while main:
		clock.tick(FPS)
		events()
		win.fill(WHITE)
		text = TITLE_FONT.render("WELCOME TO HANGMAN", 1, BLACK)
		win.blit(text,(WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))

		# DRAW BUTTON
		x, y = 400,400
		pygame.draw.circle(win, BLACK, (x,y), 60, 3)
		text = LETTER_FONT.render("START", 1, BLACK)
		win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
		pygame.display.update()

		
		if menu == False:
			main()
		elif menu == True and terminate == True :
			break
		else:
			continue

	

main_menu()
pygame.quit()