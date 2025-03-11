import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
width, height = 800, 800 #defined screen width
screen = pygame.display.set_mode((width, height)) # Variable is used to create a window, which is used later in the func
pygame.display.set_caption("Move the Dot") # Window title

# Defined Colors
WHITE = (255, 255, 255)
BLUE = (80, 208, 255)

# Dot settings
dot_radius = 10 
x_pos = width // 2 # Floor division method
y_pos = height // 2 # Floor division method
speed = 1 # Speed

# Game loop
running = True # checks if window is running ?
while running:
    screen.fill(WHITE) #fills the screen with white which has width and height

    for event in pygame.event.get(): # for loop which is used to get all events till running is false
        if event.type == pygame.QUIT: # Checks till the close button is pressed
            running = False # update running is false and while loop is exited

    # Movement controls
    keys = pygame.key.get_pressed() # variable which is used to store the key pressed 
    if keys[pygame.K_RIGHT]: #checks if right is pressed
        x_pos += speed   # updates  x pos to right by adding speed to x_pos 
        print("Right is pressed")
    if keys[pygame.K_LEFT]: #checks if left is pressed
        x_pos -= speed # updates  x pos to left by adding speed to x_pos
        print("Left is pressed")

    # Draw the dot
    pygame.draw.circle(screen, BLUE, (x_pos, y_pos), dot_radius)

    # Update the screen
    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()