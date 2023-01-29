from typing import Union

import pygame
from pygame.locals import *
import random
import pygame.font
import sqlite3

# shape parameters
from pygame.surface import Surface, SurfaceType

size = width, height = (600, 1200)
road_w = int(width / 1.6)
road_h = int(height / 3)
roadmark_w = int(width / 80)
# location parameters
right_lane = width / 2 + road_w / 4
left_lane = width / 2 - road_w / 4
# animation parameters
speed = 1

# initiallize the app
pygame.init()
pygame.font.init()
font = pygame.font.SysFont("Ariel", 30)
running = True
game_over = False

# connect to the database
conn = sqlite3.connect('score_board.db')
cursor = conn.cursor()
# cursor.execute("CREATE TABLE scores (name TEXT, score INTEGER)")
conn.commit()

# set window size
screen = pygame.display.set_mode(size)
# set window title
pygame.display.set_caption("Sepehr's car game")
# set background colour
screen.fill((60, 220, 0))
# apply changes
pygame.display.update()

# load player vehicle
car = pygame.image.load("myCar.png")
# resize image
car = pygame.transform.scale(car, (150, 250))
car_loc = car.get_rect()
car_loc.center = left_lane, height * 0.8

# load enemy vehicle
car2 = pygame.image.load("theyCar.png")
car2 = pygame.transform.scale(car2, (150, 250))
car2_loc = car2.get_rect()
car2_loc.center = right_lane, height * 0.2

counter = 0
# game loop
while running:
    counter += 1

    # increase game difficulty overtime
    if counter == 3000:
        speed += 1
        counter = 0
        print("level up", speed)

    # create a Surface with the level number
    level_text = font.render("Level: " + str(speed), True, (255, 255, 255))
    level_text_rect = level_text.get_rect()
    level_text_rect.x = width - level_text_rect.width - 10
    level_text_rect.y = 10


    # animate enemy vehicle
    car2_loc[1] += speed
    if car2_loc[1] > height:
        # randomly select lane
        if random.randint(0, 1) == 0:
            car2_loc.center = right_lane, -200
        else:
            car2_loc.center = left_lane, -200

    # end game logic
    car_rect = pygame.Rect(car_loc)
    car2_rect = pygame.Rect(car2_loc)
    if car_rect.colliderect(car2_rect):
        game_over = True

    # game over
    if game_over:
        print("GAME OVER! YOU LOST!")
        # get user's name and score
        userName = "Sepehr"
        userScore = speed

        # insert data into table
        cursor.execute("INSERT INTO scores (name, score) VALUES (?, ?)", (userName, userScore))
        conn.commit()

        # fetch the database to show the scores
        cursor.execute("SELECT * FROM scores ORDER BY score DESC LIMIT 10")
        scores = cursor.fetchall()

        # Create rectangles for each score and render the score values
        show_scores_rect = pygame.Rect(width / 2 - 150, height / 2 - 400, 300, 300)
        pygame.draw.rect(screen, (255, 255, 255), show_scores_rect)
        scores_table = font.render(str(scores), True, (0, 0, 0))
        screen.blit(scores_table, (width / 2 - scores_table.get_width() / 2, height / 2))

        # draw play again button
        play_again_rect = pygame.Rect(width / 2 - 50, height / 2 + 50, 100, 50)
        pygame.draw.rect(screen, (255, 255, 255), play_again_rect)
        play_again_text = font.render("Play Again", True, (0, 0, 0))
        game_over_text = font.render("Game Over!", True, (255, 0, 0))
        screen.blit(play_again_text, (width / 2 - play_again_text.get_width() / 2, height / 2 + 60))
        screen.blit(game_over_text, (width / 2 - game_over_text.get_width() / 2, height / 2))
        pygame.display.update()

        # check if button is clicked
        while True:
            event = pygame.event.wait()
            if event.type == QUIT:
                running = False
                game_over = False
                pygame.quit()
                break
            if event.type == MOUSEBUTTONDOWN:
                if play_again_rect.collidepoint(event.pos):
                    game_over = False
                    speed = 1
                    car_loc.center = left_lane, height * 0.8
                    car2_loc.center = right_lane, height * 0.2
                    break

    # event listeners
    for event in pygame.event.get():
        if event.type == QUIT:
            # collapse the app
            running = False
            game_over = False
        if event.type == KEYDOWN:
            # move user car to the left
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_w / 2), 0])
            # move user car to the right
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_w / 2), 0])
            if event.key in [K_w, K_UP]:
                car_loc = car_loc.move([0, -int(road_h / 2)])
            if event.key in [K_s, K_DOWN]:
                car_loc = car_loc.move([0, int(road_h / 2)])
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
    screen.blit(level_text, level_text_rect)
    # apply changes
    pygame.display.update()

# collapse application window
pygame.quit()
conn.close()