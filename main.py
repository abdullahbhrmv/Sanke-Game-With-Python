import pygame                       # pip install pygame
import time                         
import random

pygame.init()                      # Initialize pygame

                        # Define colors
white = (255, 255, 255)                 
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 900                # Define display width   
dis_height = 600            # Define display height

dis = pygame.display.set_mode((dis_width, dis_height))               # Define display
pygame.display.set_caption('Snake Game')                      # Display Caption

clock = pygame.time.Clock()                       # Define clock

snake_block = 10                # Define snake block
snake_speed = 15                # Define snake speed

font_style = pygame.font.SysFont("bahnschrift", 25)             # Define font style
score_font = pygame.font.SysFont("comicsansms", 35)             # Define font style of the score


def Your_score(score):          # Define score function
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):                  # Define snake function
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):               # Define message function
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop():                    # Define game loop function
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0                        # Define food position
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:                        # Game loop

        while game_close == True:               # Define game close function
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():                    # Define event function
                if event.type == pygame.KEYDOWN:                    # Define keydown function
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():                
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:                 # Define game over function
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])              # Define food function
        snake_Head = []                             # Define snake head function
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        
        if len(snake_List) > Length_of_snake:                   # Define snake length function
            del snake_List[0]

        for x in snake_List[:-1]:                   # Define snake list function
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)              # Call our_snake function
        Your_score(Length_of_snake - 1)                 # Call Your_score function

        pygame.display.update()                     # Update display

        if x1 == foodx and y1 == foody:                     # Define food eaten function
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)             

    pygame.quit()            # Quit pygame
    quit()


gameLoop()              # Call gameLoop function