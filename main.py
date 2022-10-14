import pygame          # pip install pygame
import random

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)

pygame.init()          # initialize pygame

# create a screen
screen_width = 800           # width of the screen
screen_height = 600          # height of the screen

screen = pygame.display.set_mode((screen_width, screen_height))      # create a screen

pygame.display.set_caption("Snake Game")        # set the title of the screen

clock = pygame.time.Clock()         # create a clock

snake_line = 20
snake_speed = 10

def our_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_line, snake_line])

def message(msg, color):                    # message function
    font_style = pygame.font.SysFont("bahnschrift", 25)     # set the font style and size
    mesg = font_style.render(msg, True, color)                # render the message
    screen.blit(mesg, [screen_width//5, screen_height/3])          # display the message

def game():                            # game function
    game_over = False                  # game over flag
    game_close = False                 # game close flag

    x1 = screen_width // 2             # x1 coordinate of the snake
    y1 = screen_height // 2            # y1 coordinate of the snake

    x1_change = 0                      # change in x1
    y1_change = 0                      # change in y1 

    foodx = random.randrange(0, screen_width-snake_line, snake_line)        # x coordinate of the food
    foody = random.randrange(0, screen_height-snake_line, snake_line)       # y coordinate of the food

    snake_list = []                    # list of snake
    snake_length = 1                   # length of the snake

    while not game_over:                          # game loop
        while game_close:                                   # game close loop
            screen.fill(white)                    # fill the screen with white color
            message("You Lost! Press C-Play Again or Q-Quit", red)        # display the message
            pygame.display.update()                 # update the screen

            for event in pygame.event.get():                # event loop
                if event.type == pygame.QUIT:                     # if user clicks on the close button
                    game_over = True                                    # set game over flag to true

                if event.type == pygame.KEYDOWN:                   # if user presses a key
                    if event.key == pygame.K_q:                        # if user presses left arrow key
                        game_over = True                                    # set game over flag to true
                        game_close = False                                  # set game close flag to false

                    elif event.key == pygame.K_c:              # if user presses right arrow key
                        game()                                          # call the game function


        for event in pygame.event.get():                # event loop
            if event.type == pygame.QUIT:                     # if user clicks on the close button
                game_over = True                                    # set game over flag to true

            if event.type == pygame.KEYDOWN:                   # if user presses a key
                if event.key == pygame.K_LEFT:                        # if user presses left arrow key
                    x1_change = -snake_line                                  # change in x1 is -snake_line
                    y1_change = 0                                                     # change in y1 is 0
                
                elif event.key == pygame.K_RIGHT:              # if user presses right arrow key
                    x1_change = snake_line                            # change in x1 is snake_line
                    y1_change = 0                                             # change in y1 is 0

                elif event.key == pygame.K_UP:                 # if user presses up arrow key
                    x1_change = 0                                       # change in x1 is 0
                    y1_change = -snake_line                                     # change in y1 is -snake_line

                elif event.key == pygame.K_DOWN:                # if user presses down arrow key
                    x1_change = 0                                       # change in x1 is 0
                    y1_change = snake_line                                          # change in y1 is snake_line

        screen.fill(white)                               # fill the screen with white color
        
        pygame.draw.rect(screen, blue, [foodx, foody, snake_line, snake_line])        # draw the food

        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:        # if snake goes out of the screen
            game_close = True                                                       # set game close flag to true
        

        x1 += x1_change                                     # change in x1
        y1 += y1_change                                             # change in y1
        snake_list.append((x1, y1))                                     # append the new coordinates of the snake to the list
        if len(snake_list) > snake_length:                                     # if length of the snake list is greater than snake length
            del snake_list[0]                                                       # delete the first element of the list
        
        our_snake(snake_list)

        pygame.display.update()                                                                 # update the screen
        
        if x1 == foodx and y1 == foody:                             # if snake eats the food
            foodx = random.randrange(0, screen_width-snake_line, snake_line)        # generate new x coordinate of the food
            foody = random.randrange(0, screen_height-snake_line, snake_line)       # generate new y coordinate of the food
            snake_length += 1                                                                       # increase the length of the snake
        clock.tick(snake_speed)                                                                 # set the speed of the game
    pygame.quit()                                                                       # quit the game
    quit()

game()                                                  # call the game function