import pygame as game
from random import randrange

game.init()
WINDOW = 700
SNAKESIZE = 200
screen = game.display.set_mode([WINDOW]*2) 
clock = game.time.Clock()
snake = [(200, 200)]
direction = (20,0)
food = (randrange(0, 400, 20), randrange(0, 400, 20))

while True: 
    for event in game.event.get(): 
        if event.type == game.QUIT:
            exit()
        if event.type == game.KEYDOWN:
            if event.key == game.K_UP: direction = (0, -20)
            if event.key == game.K_DOWN: direction = (0, 20)
            if event.key == game.K_RIGHT: direction = (20, 0)
            if event.key == game.K_LEFT: direction = (-20, 0)

    snake = [(snake[0][0] + direction[0], snake [0][1] + direction[1])] + snake[:-1]
    if snake[0] == food:
        food = (randrange(0, 400, 20), randrange(0, 400, 20))
        snake.append(snake[-1])
    screen.fill('black')
    segment_width = 20  # Define the width of a snake segment
    segment_height = 20  # Define the height of a snake segment

    for segment in snake:
        game.draw.rect(screen, (0, 255, 0), (segment[0], segment[1], segment_width, segment_height))
        game.draw.rect(screen, (255, 0, 0), (food[0], food[1], 20, 20))
    game.display.flip()
    clock.tick(10)