import pygame
import random

pygame.init()

W = (255, 255, 255)
B = (0, 0, 0)
R = (255, 0, 0)
Y = (225, 255, 0)
BL = (0, 0, 255)
G = (0, 255, 0)
wt, hg = 800, 600
win = pygame.display.set_mode((wt, hg))
seconds = 0
scorecapt = 'Змейка, название изменится'

pygame.display.set_caption(scorecapt)

sblock = 10
clock = pygame.time.Clock()
FPS = 20
font_style = pygame.font.SysFont(None, 30)
game_over = False
game_close = False
x1 = wt / 2
y1 = hg / 2
x1_change = 0
y1_change = 0
snake_List = []
Length_of_snake = 1
foodx = round(random.randrange(0, wt - sblock) / 10.0) * 10.0
foody = round(random.randrange(0, wt - sblock) / 10.0) * 10.0
score_font = pygame.font.SysFont("comicsansms", 35)
splashes = ['Теперь со сплешами!', 'Было потрачено много часов чтобы сделать эту игру.', 'Требую болгарку!', 'Распилите меня болгаркой', 'аможносплеши?', 'Великий рандом, спасибо за то, что ты есть. Благодаря тебе тут есть сплеши!', 'Требую высшей оценки!', 'Гульнара.', 'Помогите!!!!!', 'Спасибо, pygame!']


def Your_score(score):
    value = score_font.render("Ваш счёт: " + str(score), True, B)
    win.blit(value, [0, 0])



def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(win, B, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [wt / 6.5, hg / 2])


while not game_over:
    colors = (random.randrange(0, 255, 1), random.randrange(0, 255, 1), random.randrange(0, 255, 1))
    print(colors)
    while game_close:
        win.fill(R)
        scorecapt = 'Вы проиграли!'
        pygame.display.set_caption(scorecapt)
        message("Нажмите Escape для выхода или R для повторной игры", W)
        Your_score(Length_of_snake - 1)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True
                    game_close = False
                if event.key == pygame.K_r:
                    game_over = False
                    game_close = False
                    x1 = wt / 2
                    y1 = hg / 2
                    x1_change = 0
                    y1_change = 0
                    snake_List = []
                    Length_of_snake = 1
                    scorecapt = 'Змейка, название изменится'

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -sblock
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = sblock
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -sblock
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = sblock
                x1_change = 0

    if x1 >= wt or x1 < 0 or y1 >= hg or y1 < 0:
        game_close = True
    x1 += x1_change
    y1 += y1_change
    win.fill(W)
    pygame.draw.rect(win, G, [foodx, foody, sblock, sblock])
    snake_Head = []

    snake_Head.append(x1)
    snake_Head.append(y1)
    snake_List.append(snake_Head)

    if len(snake_List) > Length_of_snake:
        del snake_List[0]
    for x in snake_List[:-1]:
        if x == snake_Head:
            game_close = True
    snake(sblock, snake_List)
    Your_score(Length_of_snake - 1)
    clock.tick(FPS)
    pygame.display.set_caption(scorecapt)

    if x1 == foodx and y1 == foody:
        scorecapt = random.choice(splashes)
        win.fill(colors)
        foodx = round(random.randrange(0, wt - sblock) / 10.0) * 10.0
        foody = round(random.randrange(0, hg - sblock) / 10.0) * 10.0
        Length_of_snake += 1
    pygame.display.update()

pygame.quit()
quit()
