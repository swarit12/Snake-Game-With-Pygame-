import pygame
from pygame import mixer
import random
pygame.init()

screen_width = 500
screen_height = 500
# yellow = (255, 239, 0)
color = (200, 200, 200)
yellow= (255,195,11)
white = (250, 250, 250)
black = (0, 0, 0)
blue = (0, 0, 250)
green = (0, 200, 0)
red = (250, 0, 0)
RED= (250, 100, 0)

mixer.init()

# Screen Set Up
screen=pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("SNAKE GAME")
font = pygame.font.SysFont("Comic Sans MS", 25)
font1 = pygame.font.SysFont("Helvetica", 30)
font2 = pygame.font.SysFont("Helvetica", 35)

bg_img=pygame.image.load("C:\\Users\Shashank-dt\Desktop\\background.jpeg")
bg_img= pygame.transform.scale(bg_img, (screen_width, screen_height)).convert_alpha()
main_img= pygame.image.load("C:\\Users\Shashank-dt\Desktop\main.jpeg")
main_img= pygame.transform.scale(main_img, (screen_width, screen_height))
welcome = pygame.image.load("C:\\Users\Shashank-dt\Desktop\main.jpeg")
welcome = pygame.transform.scale(welcome, (screen_width, screen_height)).convert_alpha()

def display_text(text, color, x, y):
    screen_text= font.render(text, True, color)
    screen.blit(screen_text,[x, y])

def display_text1(text, color, x, y):
    screen_text= font1.render(text, True, color)
    screen.blit(screen_text,[x, y])

def display_text2(text, color, x, y):
    screen_text= font2.render(text, True, color)
    screen.blit(screen_text,[x, y])

def add_segment(screen, color, snk_list, snake_size):
    for x,y in snk_list:
        global body
        body=pygame.draw.rect(screen, color,[ x, y, snake_size, snake_size])


def welcome_screen():
    exit= False
    mixer.music.load("C:\\Users\Shashank-dt\Downloads\welcome_music.mp3")
    mixer.music.play()
    while not exit:
        screen.fill(white)
        screen.blit(welcome, (0,0))
        display_text1("SNAKE BY SWARIT", red, 135, 100)
        display_text1("PRESS 'SPACEBAR' TO PLAY", red, 85, 150)
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                exit=True
            if event.type== pygame.KEYDOWN:
                if event.key== pygame.K_SPACE:
                    game_loop()

        pygame.display.update()

def game_loop():
    # Game Specific Variables
    game_over = False
    exit = False
    current_score = 0
    fps = 30
    velocity_x = 0
    velocity_y = 0
    snake_head_x = 250
    snake_head_y= 280
    snake_size = 17
    fruit_size = 17
    fruit_x = 250
    fruit_y = 200
    clock = pygame.time.Clock()
    snk_list = []
    snk_lenght = 1
    with open("C:\\Users\Shashank-dt\Desktop\coding\projects\python\other files\high_score.txt", "r") as f:
        high_score = f.read()

    while not exit:
        if game_over:
            screen.fill(white)
            screen.blit(bg_img, (0, 0))
            display_text("LAST SCORE: "+ str(current_score)+ "   HIGH SCORE: "+ str(high_score), blue, 50, 5)
            display_text2("GAME OVER!! ", red, 160, 150)
            display_text2("press 'SPACEBAR' to continue", red, 60, 200)
            with open("C:\\Users\Shashank-dt\Desktop\coding\projects\python\other files\high_score.txt", "w") as f:
                f.write(str(high_score))
            for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    exit= True

                if body== snake_head_x or snake_head_y:
                    game_over=True
                    if event.type== pygame.KEYDOWN:
                        if event.key== pygame.K_SPACE:
                            mixer.music.load(
                                "C:\\Users\Shashank-dt\Downloads\welcome_music.mp3")
                            mixer.music.play()
                            game_loop()

        else:
            for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    exit= True
                elif event.type== pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x= 6
                        velocity_y= 0

                    elif event.key==pygame.K_LEFT:
                        velocity_x= -6
                        velocity_y= 0

                    elif event.key==pygame.K_DOWN:
                        velocity_y= 6
                        velocity_x= 0

                    elif event.key==pygame.K_UP:
                        velocity_y= -6
                        velocity_x= 0


            if abs(snake_head_x - fruit_x) < 8 and abs(snake_head_y - fruit_y) < 8:
                fruit_x = random.randint(20, 400 / int(1.5))
                fruit_y = random.randint(20, 400 / int(1.5))
                current_score= current_score+1
                snk_lenght+=4
                if current_score > int(high_score):
                    high_score = current_score

            snake_head_x= snake_head_x+ velocity_x
            snake_head_y= snake_head_y+ velocity_y
            screen.fill(green)
            screen.blit(bg_img, (0, 0))
            display_text("CURRENT SCORE: "+ str(current_score)+ "   HIGH SCORE: "+ str(high_score), blue, 20, 5)
            pygame.draw.ellipse(screen, red,[fruit_x, fruit_y, fruit_size, fruit_size])
            head = []
            head.append(snake_head_x)
            head.append(snake_head_y)
            snk_list.append(head)

            if len(snk_list)>snk_lenght:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over= True
                mixer.music.load("C:\\Users\Shashank-dt\Desktop\mixkit-failure-arcade-alert-notification-240.wav")
                mixer.music.play()
            if snake_head_x >= screen_width or snake_head_x < 0 or snake_head_y >= screen_height or snake_head_y \
                    < 0:
                game_over= True
                mixer.music.load("C:\\Users\Shashank-dt\Desktop\mixkit-failure-arcade-alert-notification-240.wav")
                mixer.music.play()

            add_segment(screen, color, snk_list, snake_size)
            pygame.draw.rect(screen, black,[snake_head_x, snake_head_y, snake_size, snake_size])
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome_screen()