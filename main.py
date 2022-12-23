#Imports & Inits
import pygame
from pygame.locals import *
import random, time

pygame.init()
clock = pygame.time.Clock()

#Setting up game window
screen_dimensions = (500, 500)
screen = pygame.display.set_mode(screen_dimensions)
pygame.display.set_caption("  Snake On A Diet")

pygame.font.init()
MAIN_MENU_FONT = pygame.font.Font('koverwatch.ttf', 100)
SMALL_MAIN_MENU_FONT = pygame.font.Font('koverwatch.ttf', 45)
BUTTON_FONT = pygame.font.Font('bignoodletoo.ttf', 46)
END_FONT = pygame.font.Font('bignoodletoo.ttf', 24)

SPOOKY_FONT = pygame.font.Font('ghastly_panic.ttf', 240)
SMALL_SPOOKY_FONT = pygame.font.Font('ghastly_panic.ttf', 50)

SMALL_DWARF_FONT = pygame.font.Font('Erebor.ttf', 20)
PINK_COLOR = (255, 22, 148)

#Sets snake starter position and movement
vt_movement = 0  #Insert Code for Snake initial vertical movement
hz_movement = 10  #Insert Code for Snake initial horizontal movement
snake_x = 50  #Insert Code for Snake starting x position
snake_y = 50  #Insert Code for Snake starting y position
points = 0

easy = False  #5 tick long body 15
medium = False  #default tick, and longer body 20
hard = False  #15 tick. longerer body 25

snake_segments = [(snake_x, snake_y)]  # list, index 0 is the first item


def set_difficulty():
    if easy:
        while len(snake_segments) != 25:
            snake_segments.insert(0,
                                  (snake_segments[0][0], snake_segments[0][1]))
    elif medium:
        while len(snake_segments) != 100:
            snake_segments.insert(0,
                                  (snake_segments[0][0], snake_segments[0][1]))
    elif hard:
        while len(snake_segments) != 200:
            snake_segments.insert(0,
                                  (snake_segments[0][0], snake_segments[0][1]))


#Pre-Generates apple location
apple_x = random.randrange(0, screen.get_width()) // 10 * 10
apple_y = random.randrange(0, screen.get_height()) // 10 * 10
apple2_x = random.randrange(0, screen.get_width()) // 10 * 10
apple2_y = random.randrange(0, screen.get_height()) // 10 * 10
apple3_x = random.randrange(0, screen.get_width()) // 10 * 10
apple3_y = random.randrange(0, screen.get_height()) // 10 * 10

RED_COLOR = (175, 0, 0)

orange_x = random.randrange(0, screen.get_width()) // 10 * 10
orange_y = random.randrange(0, screen.get_height()) // 10 * 10
ORANGE_COLOR = (255, 127, 43)

# (a_x, a_y) => list fixed size of 2

head = pygame.Rect(
    snake_segments[-1][0], snake_segments[-1][1], 10, 10
)  #Intuplet code, This variable should store the front of the snake in pygame.Rect() format (Hint: Use snake_segments)
apple = pygame.Rect(apple_x, apple_y, 10, 10)
apple2 = pygame.Rect(apple2_x, apple2_y, 10, 10)
apple3 = pygame.Rect(apple3_x, apple3_y, 10, 10)
orange = pygame.Rect(orange_x, orange_y, 10, 10)


def fruits(x, y):
    '''
  Function to generate new apples after current one is eaten.

  Inputs:
  x: x value of the current apple
  y: y value of the current apple

  Outputs:
  food_x: x value of the new apple
  food_y: y value of the new apple
  '''
    while ((x, y) in snake_segments):
        x = random.randrange(0, screen.get_width()) // 10 * 10
        y = random.randrange(0, screen.get_height()) // 10 * 10

    return x, y


def game_over():
    '''
  Checks for all possible ways the snake could die and ends the program if one is true
    1. Snake runs off edge of screen
    2. Snake hits its own body (HINT: DON'T USE RECTANGLE COLLISIONS FOR THIS)
  No Inputs/Outputs
  
  screen.fill((0,0,0))
  draw_text('You Died', SPOOKY_FONT, RED_COLOR, screen, 200, 100)
  death_noise.play()
  time.sleep(15)
    
  pygame.quit()
  quit()
  '''
    # head => (x,y,w,h)
    dead = False
    death_noise = pygame.mixer.Sound("Game_Assets/Sounds/death.mp3")
    #print(death_noise.get_volume())
    for body in snake_segments[:-1]:
        if body == (head[0], head[1]):
            print("Collided with self")
            dead = True
    if head[0] < 0 or head[0] > screen.get_width():
        print("Off Screen X")
        dead = True
    if head[1] < 0 or head[1] > screen.get_height():
        print("Off Screen Y")
        dead = True

    if dead:
        death_noise.play()
        screen.fill((0, 0, 0))
        for degree in range(720):
            screen.fill((0, 0, 0))
            draw_text('You Died', SPOOKY_FONT, PINK_COLOR, screen, 50, 150,
                      degree)
            draw_text('his grandmother could do better', SMALL_SPOOKY_FONT,
                      RED_COLOR, screen, 20, 0, 0)
            draw_text("Points: " + str(points), SMALL_MAIN_MENU_FONT,
                      (255, 255, 255), screen, 25, 450, 0)
            pygame.display.update()
        pygame.display.update()
        time.sleep(15)

        pygame.quit()
        quit()


def draw_text(text, font, color, surface, x, y, angle):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(pygame.transform.rotate(textobj, angle), textrect)


def print_text_size(text, font):
    textobj = font.render(text, 1, (0, 0, 0))
    print(textobj.get_rect()[2:])


apples = []
for i in range(5):
    tempx = random.randrange(0, screen.get_width()) // 10 * 10
    tempy = random.randrange(0, screen.get_height()) // 10 * 10
    apples.append(pygame.Rect(tempx, tempy, 10, 10))

click = None
menu = True
while True:
    while menu:
        screen.fill((0, 0, 0))

        mx, my = pygame.mouse.get_pos()
        #textobj = BUTTON_FONT.render("MEDIUM", 1, (0, 0, 0))
        #print(textobj.get_rect())
        #print_text_size("his grandmother did this faster though", END_FONT)

        draw_text("Snake On A Diet", MAIN_MENU_FONT, (255, 255, 255), screen,
                  17, 0, 0)
        draw_text("(It's for their grandma)", SMALL_MAIN_MENU_FONT,
                  (255, 255, 255), screen, 82, 80, 0)
        easy_button = pygame.Rect(125, 200, 250, 50)
        medium_button = pygame.Rect(125, 300, 250, 50)
        hard_button = pygame.Rect(125, 400, 250, 50)

        pygame.draw.rect(screen, (255, 255, 255), easy_button, 0, 10)
        pygame.draw.rect(screen, (255, 255, 255), medium_button, 0, 10)
        pygame.draw.rect(screen, (255, 255, 255), hard_button, 0, 10)

        if easy_button.collidepoint((mx, my)):
            pygame.draw.rect(screen, (50, 200, 50), easy_button, 0, 10)
            if click:
                easy = True
                medium = False
                hard = False
                set_difficulty()
                menu = False
        if medium_button.collidepoint((mx, my)):
            pygame.draw.rect(screen, (255, 94, 5), medium_button, 0, 10)
            if click:
                easy = False
                medium = True
                hard = False
                set_difficulty()
                menu = False
        if hard_button.collidepoint((mx, my)):
            pygame.draw.rect(screen, (225, 25, 25), hard_button, 0, 10)
            if click:
                easy = False
                medium = False
                hard = True
                set_difficulty()
                menu = False
        draw_text("EASY", BUTTON_FONT, (0, 0, 0), screen, 214, 200, 0)
        draw_text("MEDIUM", BUTTON_FONT, (0, 0, 0), screen, 195, 300, 0)
        draw_text("HARD", BUTTON_FONT, (0, 0, 0), screen, 214, 400, 0)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    #print("CLICKING")
                    #print(str(mx) + " and " + str(my))
                    #print("Easy:" + str(easy))
                    #print(easy_button.collidepoint(mx, my))
                    #print("Medium:" + str(medium))
                    #print("Hard:" + str(hard))
                    #print("In Menu: " + str(menu))
                    click = True

        pygame.display.update()
        clock.tick(10)

    screen.fill((66, 100, 40))
    
    for i in range(0,510,10):
        for j in range(0, 510,10):
            pygame.draw.rect(screen, (72, 110, 44), (0, 0, i, j), 1)
    
    #print("Easy:" + str(easy))
    #print("Medium:" + str(medium))
    #print("Hard:" + str(hard))
    #print("In Menu: " + str(menu))
    #Draws food
    '''
    INSERT CODE (Use pygame.draw.rect() and food_x/food_y)
    '''
    # Surface, (R,G,B), Rect (x,y,10,10)
    pygame.draw.rect(screen, RED_COLOR, (apple_x, apple_y, 10, 10), 0, 2)
    pygame.draw.rect(screen, RED_COLOR, (apple2_x, apple2_y, 10, 10), 0, 2)
    pygame.draw.rect(screen, RED_COLOR, (apple3_x, apple3_y, 10, 10), 0, 2)
    pygame.draw.rect(screen, ORANGE_COLOR, (orange_x, orange_y, 10, 10), 0, 5)

    #Snake movement
    snake_x = snake_x + hz_movement
    snake_y = snake_y + vt_movement

    #Draws snake
    for (a, b) in snake_segments:
        pygame.draw.rect(screen, (255, 255, 255), [a, b, 10, 10])

    #Appends new snake pos.
    '''
    INSERT CODE
    '''
    snake_segments.append((snake_x, snake_y))

    #Remakes food (apple) and head(front on snake) variables

    #for applet in apples:
    #print(apples)
    #pygame.draw.rect(screen, RED_COLOR, applet)

    orange = pygame.Rect(orange_x, orange_y, 10, 10)
    fruit_sound = pygame.mixer.Sound("eating.wav")

    head = pygame.Rect(snake_segments[-1][0], snake_segments[-1][1], 10, 10)
    if hard:  #if hard
        if pygame.Rect.colliderect(head, apple):
            apple_x, apple_y = fruits(apple_x, apple_y)
            fruit_sound.play()
            points -= 200  #Generates new position for apples
        elif pygame.Rect.colliderect(head, orange):
            fruit_sound.play()
            orange_x, orange_y = fruits(orange_x, orange_y)
            points += 1000  #Generates new position for oranges
            del snake_segments[:21]  # [start=0:stop=end:step=1]
        elif pygame.Rect.colliderect(head, apple2):
            apple2_x, apple2_y = fruits(apple2_x, apple2_y)
            fruit_sound.play()
            points -= 200  #Generates new position for apples
        elif pygame.Rect.colliderect(head, apple3):
            apple3_x, apple3_y = fruits(apple3_x, apple3_y)
            fruit_sound.play()
            points -= 200  #Generates new position for apples
        else:
            del snake_segments[0]  #Deletes old position
    elif medium:  #if medium
        if pygame.Rect.colliderect(head, apple):
            fruit_sound.play()
            apple_x, apple_y = fruits(
                apple_x, apple_y)  #Generates new position for apples

            points -= 50
        elif pygame.Rect.colliderect(head, orange):
            fruit_sound.play()
            orange_x, orange_y = fruits(
                orange_x, orange_y)  #Generates new position for oranges
            points += 1000
            del snake_segments[:11]  # [start=0:stop=end:step=1]
        elif pygame.Rect.colliderect(head, apple2):
            apple2_x, apple2_y = fruits(apple2_x, apple2_y)
            fruit_sound.play()
            points -= 200  #Generates new position for apples
        elif pygame.Rect.colliderect(head, apple3):
            apple3_x, apple3_y = fruits(apple3_x, apple3_y)
            fruit_sound.play()
            points -= 200  #Generates new position for apples
        else:
            del snake_segments[0]  #Deletes old position
    else:  # easy mode
        if pygame.Rect.colliderect(head, apple):
            fruit_sound.play()
            apple_x, apple_y = fruits(
                apple_x, apple_y)  #Generates new position for apples
            points -= 10
        elif pygame.Rect.colliderect(head, orange):
            fruit_sound.play()
            orange_x, orange_y = fruits(
                orange_x, orange_y)  #Generates new position for oranges
            points += 1000
            del snake_segments[:6]  # [start=0:stop=end:step=1]
        elif pygame.Rect.colliderect(head, apple2):
            apple2_x, apple2_y = fruits(apple2_x, apple2_y)
            fruit_sound.play()
            points -= 200  #Generates new position for apples
        elif pygame.Rect.colliderect(head, apple3):
            apple3_x, apple3_y = fruits(apple3_x, apple3_y)
            fruit_sound.play()
            points -= 200  #Generates new position for apples
        else:
            del snake_segments[0]  #Deletes old position

    if not snake_segments:
        win_noise = pygame.mixer.Sound("Game_Assets/Sounds/jump.wav")
        screen.fill(PINK_COLOR)
        draw_text("you win i guess", MAIN_MENU_FONT, (255, 255, 255),
                  screen, 8, 150, 0)
        draw_text("Points: " + str(points), SMALL_MAIN_MENU_FONT,
                      (255, 255, 255), screen, 25, 450, 0)
        draw_text('his grandmother did this faster though', END_FONT,
                  (255, 255, 255), screen, 10, 0, 0)
        pygame.display.update()
        win_noise.play()
        print("You Win!")

        time.sleep(15)
        pygame.quit()
        quit()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            #Enter movement code here
            if event.key == pygame.K_LEFT:
                if hz_movement != 10:
                    hz_movement = -10  #Remember the Snake can't go left if it's currently going right, which means you need another if statement!
                    vt_movement = 0
            if event.key == pygame.K_RIGHT:
                if hz_movement != -10:
                    hz_movement = 10  #Remember the Snake can't go right if it's currently going left.
                    vt_movement = 0
            if event.key == pygame.K_UP:
                if vt_movement != 10:
                    vt_movement = -10  #Remember the Snake can't go up if it's currently going down.
                    hz_movement = 0
            if event.key == pygame.K_DOWN:
                if vt_movement != -10:
                    vt_movement = 10  #Remember the Snake can't go down if it's currently going up.
                    hz_movement = 0
            if event.key == pygame.K_p:
                time.sleep(30)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    if hz_movement != 0 or vt_movement != 0:
        game_over()
    if points != 0:
        points -= 1
    draw_text("Points: " + str(points), SMALL_MAIN_MENU_FONT, (255, 255, 255),
                  screen, 0, 0, 0)
    pygame.display.update()
    if easy:
        clock.tick(15)
    if hard:
        clock.tick(25)
    else:
        clock.tick(20)
