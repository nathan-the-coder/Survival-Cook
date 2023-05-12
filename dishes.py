import os.path as path
import sys
from random import randint

import pygame as pg

from button import Button
from font import get_font
from sprites import Sprite
from vars import (BG_DIR, BTNS_DIR, DESSERT_DIR, HEIGHT, MAIN_DIR, MEALS,
                  ROUND1_SPEED, ROUND2_SPEED, ROUND3_SPEED, SPRITES,
                  STARTER_DIR, WIDTH, BASE_DIR)


class START_GAME:
    def __init__(self, screen):
        pg.display.set_caption("Survival Cook")
        starter_bg = pg.image.load(path.join(BG_DIR, "5.jpg"))
        starter_bg = pg.transform.scale(starter_bg, (WIDTH, HEIGHT))
        round = "STARTER"

        while True:
            screen.blit(starter_bg, (0, 0))

            GAME_MOUSE_POS = pg.mouse.get_pos()

            if round == "STARTER":
                dish1_img = pg.image.load(
                    path.join(STARTER_DIR, "2.png")
                ).convert_alpha()
                dish1_img = pg.transform.scale(dish1_img, (215, 170))

                dish2_img = pg.image.load(
                    path.join(STARTER_DIR, "1.png")
                ).convert_alpha()
                dish2_img = pg.transform.scale(dish2_img, (230, 200))

                dish3_img = pg.image.load(
                    path.join(STARTER_DIR, "3.png")
                ).convert_alpha()
                dish3_img = pg.transform.scale(dish3_img, (225, 200))
            elif round == "MAIN COURSE":
                dish1_img = pg.image.load(path.join(MAIN_DIR, "2.png")).convert_alpha()
                dish1_img = pg.transform.scale(dish1_img, (215, 170))

                dish2_img = pg.image.load(path.join(MAIN_DIR, "1.png")).convert_alpha()
                dish2_img = pg.transform.scale(dish2_img, (230, 200))

                dish3_img = pg.image.load(path.join(MAIN_DIR, "3.png")).convert_alpha()
            dish3_img = pg.transform.scale(dish3_img, (225, 200))

            DISH1_BTN = Button(
                image=dish1_img,
                pos=(320, 510),
                text_input="",
                font=get_font(35),
                base_color="#d7fcd4",
                hovering_color="White",
            )

            DISH2_BTN = Button(
                image=dish2_img,
                pos=(598, 500),
                text_input="",
                font=get_font(35),
                base_color="#d7fcd4",
                hovering_color="White",
            )

            DISH3_BTN = Button(
                image=dish3_img,
                pos=(870, 500),
                text_input="",
                font=get_font(35),
                base_color="#d7fcd4",
                hovering_color="White",
            )

            for button in [DISH1_BTN, DISH2_BTN, DISH3_BTN]:
                button.changeColor(GAME_MOUSE_POS)
                button.update(screen)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if DISH1_BTN.checkForInput(GAME_MOUSE_POS):
                        if round == "STARTER":
                            DO_DISH1(screen, "", "charcuterie")
                        elif round == "MAIN COURSE":
                            DO_DISH1(screen, "", "steak")
                        elif round == "DESSERT":
                            DO_DISH1(screen, "", "sliced_cake")
                    if DISH2_BTN.checkForInput(GAME_MOUSE_POS):
                        if round == "STARTER":
                            DO_DISH2(screen, "", "mushroom_soup")
                        elif round == "MAIN COURSE":
                            DO_DISH2(screen, "", "baked_salmon")
                        elif round == "DESSERT":
                            DO_DISH2(screen, "", "ice_cream")
                    if DISH3_BTN.checkForInput(GAME_MOUSE_POS):
                        if round == "STARTER":
                            DO_DISH3(screen, "", "french_fries")
                        elif round == "MAIN COURSE":
                            DO_DISH3(screen, "", "spaghetti")
                        elif round == "DESSERT":
                            DO_DISH3(screen, "", "pudding")

            pg.display.update()

class Starter:
    def __init__(self, screen):
        self.screen = screen

        starter_bg = pg.image.load(path.join(BG_DIR, "5.jpg"))
        starter_bg = pg.transform.scale(starter_bg, (WIDTH, HEIGHT))

        self.round = "STARTER"

        self.mouse_position = pg.mouse.get_pos()

        dishes = self.show_dishes()

        for dish in dishes:
            dish.update(self.screen)

    def show_dishes(self):
        charcuterie_img = pg.image.load(path.join(STARTER_DIR, "2.png")).convert_alpha()
        charcuterie_img = pg.transform.scale(charcuterie_img, (215, 170))

        mushroom_soup_img = pg.image.load( path.join(STARTER_DIR, "1.png")).convert_alpha()
        mushroom_soup_img = pg.transform.scale(mushroom_soup_img, (230, 200))

        french_fries_img = pg.image.load(path.join(STARTER_DIR, "3.png")).convert_alpha()

        # Make the dish image act as a Button
        self.charcuterie = self.setup_dish(charcuterie_img, (320, 510))

        self.mushroom_soup = self.setup_dish(mushroom_soup_img, (598, 500))

        self.french_fries = self.setup_dish(french_fries_img, (870, 500))

        self.dishes = [self.charcuterie, self.mushroom_soup, self.french_fries]
        return dishes

    def setup_dish(self, dish_image, pos):
        self.dish = Button(
            image=dish_image,
            pos=pos,
            text_input="",
            font=get_font(35),
            base_color="",
            hovering_color="",
        )
        return dish

    def start(self):
        while True:
            screen.blit(starter_bg, (0, 0))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.charcuterie.checkForInput(GAME_MOUSE_POS):
                        DO_DISH1(screen, "", "charcuterie")
                        elif round == "MAIN COURSE":
                            DO_DISH1(screen, "", "steak")
                        elif round == "DESSERT":
                            DO_DISH1(screen, "", "sliced_cake")
                    if DISH2_BTN.checkForInput(GAME_MOUSE_POS):
                        if round == "STARTER":
                            DO_DISH2(screen, "", "mushroom_soup")
                        elif round == "MAIN COURSE":
                            DO_DISH2(screen, "", "baked_salmon")
                        elif round == "DESSERT":
                            DO_DISH2(screen, "", "ice_cream")
                    if DISH3_BTN.checkForInput(GAME_MOUSE_POS):
                        if round == "STARTER":
                            DO_DISH3(screen, "", "french_fries")
                        elif round == "MAIN COURSE":
                            DO_DISH3(screen, "", "spaghetti")
                        elif round == "DESSERT":
                            DO_DISH3(screen, "", "pudding")


class MainCourse:
    pass

class Dessert:
    pass

class DISH_UI:
    def __init__(self, screen, dish_img, dish_name):
        pg.display.set_caption("Survival Cook")
        sgame_bg = pg.image.load(path.join(BG_DIR, "2.jpg"))
        sgame_bg = pg.transform.scale(sgame_bg, (WIDTH, HEIGHT))

        pot = Sprite(SPRITES, path.join(BASE_DIR, "cooking_pot.png"))

        while True:
            screen.blit(sgame_bg, (0, 0))

            GAME_MOUSE_POS = pg.mouse.get_pos()

            self.current_dish = pg.image.load(path.join(STARTER_DIR, "2.png")).convert_alpha()
            self.current_dish = pg.transform.scale(self.current_dish, (215, 170))

            back_img = pg.image.load(path.join(BTNS_DIR, "right_btn.png"))
            back_img = pg.transform.scale(back_img, (32, 32))

            cd_text = get_font(20).render("Current Dish:", True, (255, 0, 0))
            dish = get_font(20).render(f"   {dish_name}", True, (255, 0, 0))
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
        if dish_name == "charcuterie":
            pos_y = 0
            # ingredients = MEALS.get("Starter").get("Charcuterie")

            for ingredients in MEALS.get("Starter"):
                print(ingredients)

            # for ingredient_name in ingredients:
            #     ingredient = MEALS.get("Starter").get("Charcuterie").get("ingredients").get(ingredient_name)
            #     print(ingredient)

                # ingredient_img = pg.transform.scale(ingredient, (64, 64))
                # screen.blit(ingredient_img, (randint(5, WIDTH - 50), pos_y))
                # pos_y += 10

            y_pos = 30
            for ing in MEALS["Starter"]["Charcuterie"]["ingredients"]:
                ingredient = MEALS["Starter"]["Charcuterie"]["ingredients"][ing]
                ingredient_img = pg.transform.scale(ingredient, (64, 64))
                screen.blit(ingredient_img, (1120, y_pos))
                y_pos += 60


class DO_DISH1(DISH_UI):
    def __init__(self, screen, dish_img, dish_name):
        super().__init__(screen, dish_img, dish_name)


class DO_DISH2(DISH_UI):
    def __init__(self, screen, dish_img, dish_name):
        super().__init__(screen, dish_img, dish_name)


class DO_DISH3(DISH_UI):
    def __init__(self, screen, dish_img, dish_name):
        super().__init__(screen, dish_img, dish_name)
