import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Title and Icon
pygame.display.set_caption("Car Race Game")

# Load the car image
car_img = pygame.image.load('car.png')
car_size = car_img.get_rect().size  # Get the size of the car
car_width = car_size[0]
car_height = car_size[1]
car_x = (screen_width * 0.45)
car_y = (screen_height * 0.8)

# Load the obstacle image
obstacle_img = pygame.image.load('obstacle.png')
obstacle_startx = random.randrange(0, screen_width)
obstacle_starty = -600  # start off-screen
obstacle_speed = 7
obstacle_width = obstacle_img.get_rect().size[0]
obstacle_height = obstacle_img.get_rect().size[1]

score = 0

def car(x, y):
    screen.blit(car_img, (x, y))

def obstacles(obstaclex, obstacley):
    screen.blit(obstacle_img, (obstaclex, obstacley))

def show_score(x, y, score):
    font = pygame.font.SysFont(None, 35)
    text = font.render("Score: " + str(score), True, (255,255,255))
    screen.blit(text, (x, y))

# Game Loop
running = True
x_change = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Movement event handling
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

    car_x += x_change

    # Prevent the car from going out of bounds
    if car_x > screen_width - car_width:
        car_x = screen_width - car_width
    elif car_x < 0:
        car_x = 0

    screen.fill((0, 0, 0))  # Clear screen

    obstacles(obstacle_startx, obstacle_starty)
    obstacle_starty += obstacle_speed
    if obstacle_starty > screen_height:
        obstacle_starty = -obstacle_height
        obstacle_startx = random.randrange(0, screen_width)
        score += 1  # Update score when passing an obstacle

    car(car_x, car_y)  # Display the car

    show_score(0, 0, score)

    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()
