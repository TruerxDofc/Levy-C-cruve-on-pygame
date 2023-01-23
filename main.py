import pygame as pg  # import the "pygame" library as "pg" (for fewer letters in our code :) )

pg.font.init()  # initialize the font module

WIGHT, HEIGHT = 1366, 720  # set display size
display = pg.display.set_mode((WIGHT, HEIGHT))  # !!

WHITE = (255, 255, 255)  # for simplify
BLACK = (0, 0, 0)  # for simplify

ITERATION = 0  # set global variables
SCALE = 300  # set global variables
DELT_POS_X = 0  # set global variables
DELT_POS_Y = 0  # set global variables

FPS = 45  # set a frame per second limit (for understanding)
clock = pg.time.Clock()  #  !!

ITERATION_FONT = pg.font.SysFont('timesnewroman', 20)  # set font for our iteration text
TIP_FONT = pg.font.SysFont('timesnewroman', 20)  # set font for our tip(restart) text
TITLE_FONT = pg.font.SysFont('timesnewroman', 20)  # set font for our title text
FPS_FONT = pg.font.SysFont('timesnewroman', 20)  # set font for our fps counter text


def fractal(ITERATION, x1, x2, y1, y2):  # here our fractal function
    if ITERATION == 0:  #
        pg.draw.line(display, WHITE, (x1, y1), (x2, y2))  #
    else:  #
        x3 = (x1 + x2) / 2 + (y2 - y1) / 2  #
        y3 = (y1 + y2) / 2 - (x2 - x1) / 2  #

        fractal(ITERATION - 1, x1, x3, y1, y3)  #
        fractal(ITERATION - 1, x3, x2, y3, y2)  #


def main():  # here our main function
    global ITERATION, SCALE, DELT_POS_X, DELT_POS_Y  # calling global variables

    run = 1  # as long as it is TRUE, the program will work ("1" for small optimization)
    while run:  # main program loop

        clock.tick(FPS)  # immediate frame limit
        for event in pg.event.get():  # !!!
            if event.type == pg.QUIT:  # if you click on the cross next to the window, the program ends
                run = 0  # main loop is dead

        iteration_text = ITERATION_FONT.render(
            "iterations: " + str(ITERATION), True, WHITE)  # set value and color for iteration text
        display.blit(iteration_text, (10, 10))  # drawing text with given coordinates

        tip_text = TIP_FONT.render(
            "if you want to restart press \"R\"", True, WHITE)  # set value and color tip(restart) text
        display.blit(tip_text, (10, 30))  # drawing text with given coordinates

        title_text = TITLE_FONT.render(
            "Lévy C curve", True, WHITE)  # set value and color for title text
        display.blit(title_text, (WIGHT / 2, HEIGHT - 30))  # drawing text with given coordinates

        fps_text = FPS_FONT.render(
            f'FPS: {clock.get_fps() :.2f}', True, WHITE)  # set value and color for fps counter text
        display.blit(fps_text, (10, HEIGHT - 30))  # drawing text with given coordinates

        pressed_key = pg.key.get_pressed()  # button click check (every frame)
        if pressed_key[pg.K_UP] and ITERATION < 15:
            ITERATION += 1  # if the UP key is pressed, then we INCREASE the number of iterations
            pg.time.delay(100)

        if pressed_key[pg.K_DOWN] and ITERATION > 0:
            ITERATION -= 1  # if the DOWN key is pressed, then we DECREASE the number of iterations
            pg.time.delay(100)

        if pressed_key[pg.K_RIGHT]:
            SCALE += 5  # if the RIGHT key is pressed, then we INCREASE the fractal

        if pressed_key[pg.K_LEFT]:
            SCALE -= 5  # if the LEFT key is pressed, then we DECREASE the fractal

        if pressed_key[pg.K_w]:
            DELT_POS_Y -= 5  # if the "W" key is pressed, the fractal moves UP

        if pressed_key[pg.K_s]:
            DELT_POS_Y += 5  # if the "S" key is pressed, the fractal moves DOWN

        if pressed_key[pg.K_a]:
            DELT_POS_X -= 5  # if the "A" key is pressed, the fractal moves LEFT

        if pressed_key[pg.K_d]:
            DELT_POS_X += 5  # if the "D" key is pressed, the fractal moves RIGHT

        if pressed_key[pg.K_r]:
            ITERATION = 5  # if the "R" key, the fractal becomes the center (if the fractal flew to the borders)
            SCALE = 300
            DELT_POS_X = 0
            DELT_POS_Y = 0

        fractal(ITERATION, (WIGHT / 2) + DELT_POS_X, WIGHT / 2 + SCALE + DELT_POS_X, (HEIGHT / 2) + DELT_POS_Y,
                HEIGHT / 2 + DELT_POS_Y)  # calling the fractal function every frame
        pg.display.set_caption('Levy C curve on pygame')  # window title (optional)
        pg.display.update()  # display update every frame
        display.fill(BLACK)  # so that there is no echo effect

    pg.quit()  # for correctly exit the program


if __name__ == "__main__":  # for more correct code
    main()
