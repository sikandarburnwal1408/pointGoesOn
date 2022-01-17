import pygame
import random


pygame.init()


display_width = 800
display_height = 500

# colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 255)

  # background image
bground=pygame.image.load("Project on Python\pointGoesOn\ourimage.jpg")
bground=pygame.transform.scale(bground, [display_width,display_height])
  # display
window = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("SNAKE MASTER")

# game specific variables
exitgame = False
gameover = False
snake_initX = 400
snake_initY = 250
snake_sizeX = 15
snake_sizeY = 15
vel_x = 0
vel_y = 0
initial_vel=5
fps = 30

# Food generating
fruit_x = random.randint(2, display_width-5)
fruit_y = random.randint(2, display_height-5)
score = 0

game_font=pygame.font.SysFont(None,20)
clock = pygame.time.Clock()

def printScore(score_text,color,cord_X,cord_Y):
    text=game_font.render(score_text, True, color)
    window.blit(text, [cord_X,cord_Y])


while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                gameover=True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                vel_x = -initial_vel
                vel_y = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                vel_x = initial_vel
                vel_y = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                vel_y = -initial_vel
                vel_x = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                vel_y = initial_vel
                vel_x = 0

    snake_initX += vel_x
    snake_initY += vel_y
    if abs(snake_initX-fruit_x) < 7 and abs(snake_initY-fruit_y) < 7:
        score += 100
        initial_vel+= 1
        fruit_x = random.randint(2, display_width-5)
        fruit_y = random.randint(2, display_height-5)

    # window.fill(green)
    window.blit(bground, (0,0))
    pygame.draw.rect( window, red, [snake_initX, snake_initY, snake_sizeX, snake_sizeY])
    pygame.draw.ellipse(window, black, [snake_initX, snake_initY, snake_sizeX, snake_sizeY])
    pygame.draw.rect(window,white, [fruit_x, fruit_y, snake_sizeX, snake_sizeY])
    pygame.draw.ellipse(window,black, [fruit_x, fruit_y, snake_sizeX-2, snake_sizeY-1])
    # pygame.draw.polygon(window, color2, 7)
    printScore("Score: "+str(score), red, 2, 2)
    pygame.display.update()
    clock.tick(fps)


pygame.quit()
quit()
