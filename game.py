import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up the title of the window
pygame.display.set_caption("Running Game")

# Load the boy and bus images
boy_image = pygame.image.load("boy.png")
bus_image = pygame.image.load("bus.png")

# Set up the boy and bus positions
boy_x = 50
boy_y = screen_height - 50
bus_x = screen_width + 100
bus_y = screen_height - 50

# Set up the boy's speed
boy_speed = 5

# Set up the game clock
clock = pygame.time.Clock()

while True:
	# Handle events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	# Move the boy
	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP]:
		boy_y -= boy_speed
	if keys[pygame.K_DOWN]:
		boy_y += boy_speed

	# Move the bus
	bus_x -= 5

	# Check for collision
	if boy_x < bus_x + 100 and boy_x + 50 > bus_x and boy_y < bus_y + 50 and boy_y + 50 > bus_y:
		print("Game Over")
		break

	# Draw everything
	screen.fill((255, 255, 255))
	screen.blit(boy_image, (boy_x, boy_y))
	screen.blit(bus_image, (bus_x, bus_y))

	# Update the screen
	pygame.display.flip()

	# Cap the frame rate
	clock.tick(60)

# Restart the game
while True:
	# Handle events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				# Reset the game
				boy_x = 50
				boy_y = screen_height - 50
				bus_x = screen_width + 100
				bus_y = screen_height - 50
				break
