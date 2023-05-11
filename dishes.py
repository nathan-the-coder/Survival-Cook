import pygame as pg
from vars import WIDTH, HEIGHT, MEALS, SPRITES
from vars import ROUND1_SPEED, ROUND2_SPEED, ROUND3_SPEED
import sys
from font import get_font
from button import Button
from sprites import Sprite
from random import randint
import os.path as path
from vars import BG_DIR


class START_GAME:
    def __init__(self, screen):
        pg.display.set_caption("Survival Cook")
        starter_bg = pg.image.load(path.join(BG_DIR, "5.jpg"))
        starter_bg = pg.transform.scale(starter_bg, (WIDTH, HEIGHT))
        round = 'STARTER'

        while True:
            screen.blit(starter_bg, (0, 0))

            GAME_MOUSE_POS = pg.mouse.get_pos()

            if round == 'STARTER': 
                dish1_img = pg.image.load(
                        "assets\\meals\\Starter\\2.png").convert_alpha()
                dish1_img = pg.transform.scale(dish1_img, (215, 170))

                dish2_img = pg.image.load(
                        "assets\\meals\\Starter\\1.png").convert_alpha()
                dish2_img = pg.transform.scale(dish2_img, (230, 200))

                dish3_img = pg.image.load(
                        "assets\\meals\\Starter\\3.png").convert_alpha()
                dish3_img = pg.transform.scale(dish3_img, (225, 200))
            elif round == 'MAIN COURSE':
                dish1_img = pg.image.load(
                        "assets\\meals\\MainCourse\\2.png").convert_alpha()
                dish1_img = pg.transform.scale(dish1_img, (215, 170))

                dish2_img = pg.image.load(
                        "assets\\meals\\MainCourse\\1.png").convert_alpha()
                dish2_img = pg.transform.scale(dish2_img, (230, 200))

                dish3_img = pg.image.load(
                        "assets\\meals\\MainCourse\\3.png").convert_alpha()
            dish3_img = pg.transform.scale(dish3_img, (225, 200))

            DISH1_BTN = Button(image=dish1_img, pos=(320, 510),
                               text_input="", font=get_font(35),
                               base_color="#d7fcd4", hovering_color="White")

            DISH2_BTN = Button(image=dish2_img, pos=(598, 500),
                               text_input="", font=get_font(35),
                               base_color="#d7fcd4", hovering_color="White")

            DISH3_BTN = Button(image=dish3_img, pos=(870, 500),
                               text_input="", font=get_font(35),
                               base_color="#d7fcd4", hovering_color="White")

            for button in [DISH1_BTN, DISH2_BTN, DISH3_BTN]:
                button.changeColor(GAME_MOUSE_POS)
                button.update(screen)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if DISH1_BTN.checkForInput(GAME_MOUSE_POS):
                        DO_DISH1(screen,
                                 'assets\\meals\\Starter\\charcuterie.png',
                                 'charcuterie')
                    if DISH2_BTN.checkForInput(GAME_MOUSE_POS):
                        DO_DISH2(screen, '', 'mushroom_soup')
                    if DISH3_BTN.checkForInput(GAME_MOUSE_POS):
                        DO_DISH3()

            pg.display.update()




class DISH_UI():
    def __init__(self, screen, dish_img, dish_name):
        pg.display.set_caption("Survival Cook")
        sgame_bg = pg.image.load("assets\\bg_image\\2.jpg")
        sgame_bg = pg.transform.scale(sgame_bg, (WIDTH, HEIGHT))

        pot = Sprite(SPRITES, "assets\\cooking_pot.png")

        while True:
            screen.blit(sgame_bg, (0, 0))

            GAME_MOUSE_POS = pg.mouse.get_pos()

            self.current_dish = pg.image.load("assets\\meals\\Starter\\2.png").convert_alpha()
            self.current_dish = pg.transform.scale(self.current_dish, (215, 170))

            back_img = pg.image.load('assets\\buttons\\right_btn.png')
            back_img = pg.transform.scale(back_img, (32, 32))

            cd_text = get_font(20).render('Current Dish:', True, (255, 0, 0))
            dish = get_font(20).render(f'   {dish_name}', True, (255, 0, 0))
            screen.blit(cd_text, (10, 10))
            screen.blit(dish, (10, 30))

            self.check_for_ingredients(screen, dish_name)

            # Draw the pot which the player
            # has in control
            pot.draw(screen)
            pot.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                pot.handle_input(event)

            pg.display.update()

    def check_for_ingredients(self, screen, dish_name):
        if dish_name == 'charcuterie':
            pos_y = 0

            for ing in MEALS['Starter']['Charcuterie']['ingredients']:
                ingredient = MEALS['Starter']['Charcuterie']['ingredients'][ing]

                ingredient_img = pg.transform.scale(ingredient, (64, 64))
                screen.blit(ingredient_img, (randint(5, WIDTH - 50), pos_y))
                pos_y += 10

            y_pos = 30
            for ing in MEALS['Starter']['Charcuterie']['ingredients']:
                ingredient = MEALS['Starter']['Charcuterie']['ingredients'][ing]
                ingredient_img = pg.transform.scale(ingredient, (64, 64))
                screen.blit(ingredient_img, (1120, y_pos))
                y_pos += 60


class DO_DISH1(DISH_UI):
    def __init__(self, screen, dish_img, dish_name):
        super().__init__(screen, dish_img, dish_name)

def DO_DISH2():
    def __init__(self, screen, dish_img, dish_name):
        super().__init__(screen, dish_img, dish_name)

def DO_DISH3():
    def __init__(self, screen, dish_img, dish_name):
        super().__init__(screen, dish_img, dish_name)

