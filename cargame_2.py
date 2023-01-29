import pygame
from pygame.locals import *
import random

# Initialize pygame
pygame.init()

# Set game window size and caption
size = width, height = (600, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mariya's car game")

# Set background color
screen.fill((60, 220, 0))
pygame.display.update()

# Create a car class for the player and enemy vehicles
class Car:
    def __init__(self, img_path, x, y):
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
        self.rect.center = x, y

# Create instances of the car class
player_car = Car("car.png", right_lane, height * 0.8)
enemy_car = Car("otherCar.png", left_lane, height * 0.2)

# Game loop function
def game_loop():
    running = True
    speed = 1
    counter = 0

    while running:
        counter += 1

        # Increase game difficulty over time
        if counter == 5000:
            speed += 0.5
            counter = 0
            print("level up", speed)

        # Animate enemy vehicle
        enemy_car.rect.y += speed
        if enemy_car.rect.y > height:
            if random.randint(0, 1) == 0:
                enemy_car.rect.center = right_lane, -200
            else:
                enemy_car.rect.center = left_lane, -200

        # Check for collision
        if player_car.rect.colliderect(enemy_car.rect):
            print("GAME OVER! YOU LOST!")
            running = False

            # event listeners
            for event in pygame.event.get():
                if event.type == QUIT:
                    # collapse the app
                    running = False
                if event.type == KEYDOWN:
                    # move user car to the left
                    if event.key in [K_a, K_LEFT]:
                        car_loc = car_loc.move([-int(road_w / 2), 0])
                    # move user car to the right
                    if event.key in [K_d, K_RIGHT]:
                        car_loc = car_loc.move([int(road_w / 2), 0])

            # draw road
            pygame.draw.rect(
                screen,
                (50, 50, 50),
                (width / 2 - road_w / 2, 0, road_w, height))
            # draw centre line
            pygame.draw.rect(
                screen,
                (255, 240, 60),
                (width / 2 - roadmark_w / 2, 0, roadmark_w, height))
            # draw left road marking
            pygame.draw.rect(
                screen,
                (255, 255, 255),
                (width / 2 - road_w / 2 + roadmark_w * 2, 0, roadmark_w, height))
            # draw right road marking
            pygame.draw.rect(
                screen,
                (255, 255, 255),
                (width / 2 + road_w / 2 - roadmark_w * 3, 0, roadmark_w, height))

            # place car images on the screen
            screen.blit(car, car_loc)
            screen.blit(car2, car2_loc)
            # apply changes
            pygame.display.update()

        # collapse application window
        pygame.quit()