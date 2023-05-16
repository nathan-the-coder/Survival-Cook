import os.path as path
import sys
from random import randint

import pygame as pg

from font import get_font
from sprites import Sprite
from vars import (BASE_DIR, BG_DIR, HEIGHT, GAME_OVER, MAX_FALL_HEIGHT, MEALS, SPRITES,
                  STARTER_DIR, WIDTH, positions, velocities)

import ui
from button import Button
from music import play_music

play_music()

button_show = False
class Button1:
    def __init__(self, text, position):
        self.font = pg.font.Font('assets/font.ttf', 32)
        self.text = self.font.render(text, True, (255, 255, 255))
        self.rect = self.text.get_rect(center=position)


    def draw(self, screen):
        if button_show:
            screen.blit(self.text, self.rect)

    def is_clicked(self, position):
        return self.rect.collidepoint(position)

class Button2:
    def __init__(self, text, position):
        self.font = pg.font.Font('assets/font.ttf', 20)
        self.text = self.font.render(text, True, (255, 0, 0))
        self.rect = self.text.get_rect(center=position)


    def draw(self, screen):
        if button_show:
            screen.blit(self.text, self.rect)

    def is_clicked(self, position):
        return self.rect.collidepoint(position)

def options(screen):
    global button_show

    buttons = [
        Button2("How to play", (90, 100)),
        Button2("Game Mechanics", (90, 200)),
        Button2("Back", (90, 300))
    ]

    htp_img = pg.image.load(path.join(BG_DIR, "3.jpg"))
    htp_img = pg.transform.scale(htp_img, (WIDTH, HEIGHT))
    game_mechanics_img = pg.image.load(path.join(BG_DIR, "4.jpg"))
    game_mechanics_img = pg.transform.scale(game_mechanics_img, (WIDTH, HEIGHT))

    bg = pg.image.load(path.join(BG_DIR, "2.jpg"))
    bg = pg.transform.scale(bg, (WIDTH, HEIGHT))

    screen.blit(bg, (0, 0))

    while True:
        for button in buttons:
            button_show = True
            button.draw(screen)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                OPTION_MOUSE_POS = pg.mouse.get_pos()
                if buttons[0].is_clicked(OPTION_MOUSE_POS):
                   screen.blit(htp_img, (0, 0)) 
                   button_show = False
                   pg.display.flip()
                if buttons[1].is_clicked(OPTION_MOUSE_POS):
                   screen.blit(game_mechanics_img, (0, 0)) 
                   button_show = False
                   pg.display.flip()
                if buttons[2].is_clicked(OPTION_MOUSE_POS):
                    ui.main_menu(screen)


        
        pg.display.update()

def game_over_screen(screen):
    global button_show
    game_over_text = pg.font.Font(None, 48).render("Game Over", True, (255, 0, 0))
    main_menu_button = Button1("Main Menu", (400, 300))
    exit_button = Button1("Exit", (400, 350))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pg.mouse.get_pos()
                if main_menu_button.is_clicked(mouse_pos):
                    return "main_menu"
                elif exit_button.is_clicked(mouse_pos):
                    pg.quit()
                    sys.exit()

        screen.fill((0, 0, 0))
        screen.blit(game_over_text, (350, 200))
        button_show = True
        exit_button.draw(screen)
        pg.display.update()

class START_GAME:
    def __init__(self, screen):
        pg.display.set_caption("Survival Cook")
        starter_bg = pg.image.load(path.join(BG_DIR, "5.jpg"))
        self.starter_bg = pg.transform.scale(starter_bg, (WIDTH, HEIGHT))

        dish1_img = pg.image.load(path.join(STARTER_DIR, "2.png")).convert_alpha()
        self.dish1_img = pg.transform.scale(dish1_img, (215, 170))
        dish2_img = pg.image.load(path.join(STARTER_DIR, "1.png")).convert_alpha()
        self.dish2_img = pg.transform.scale(dish2_img, (230, 200))

        self.dish3_img = pg.image.load(path.join(STARTER_DIR, "3.png")).convert_alpha()

        self.screen = screen
        self.buttons = [
            Button(
                image=self.dish1_img,
                pos=(320, 510),
                text_input="",
                font=get_font(35),
                base_color="#d7fcd4",
                hovering_color="White",
            ),
            Button(
                image=self.dish2_img,
                pos=(598, 500),
                text_input="",
                font=get_font(35),
                base_color="#d7fcd4",
                hovering_color="White",
            ),
            Button(
                image=self.dish3_img,
                pos=(870, 500),
                text_input="",
                font=get_font(35),
                base_color="#d7fcd4",
                hovering_color="White",
            ),
        ]

        self.dish1 = DO_DISH1(self.screen, "Charcuterie")
        self.dish2 = DO_DISH2(self.screen, "Mushroom Soup")
        self.dish3 = DO_DISH3(self.screen, "French Fries")

    def start(self):
        while True:
            self.screen.blit(self.starter_bg, (0, 0))

            GAME_MOUSE_POS = pg.mouse.get_pos()
            for button in self.buttons:
                button.changeColor(GAME_MOUSE_POS)
                button.update(self.screen)

            if pg.mouse.get_pressed()[0]:
                if self.buttons[0].rect.collidepoint(GAME_MOUSE_POS):
                    self.dish1.run()
                if self.buttons[1].rect.collidepoint(GAME_MOUSE_POS):
                    self.dish2.run()
                if self.buttons[2].rect.collidepoint(GAME_MOUSE_POS):
                    self.dish3.run()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            pg.display.update()


class DISH_UI:
    def __init__(self, screen, dish_name):
        global GAME_OVER
        sgame_bg = pg.image.load(path.join(BG_DIR, "2.jpg"))
        self.sgame_bg = pg.transform.scale(sgame_bg, (WIDTH, HEIGHT))

        self.pot = Sprite(SPRITES, path.join(BASE_DIR, "cooking_pot.png"))
        self.screen = screen
        self.dish_name = dish_name

        self.count = 10
        self.pos_x = randint(10, 1100)
        self.current_dish = pg.image.load(
            path.join(STARTER_DIR, "2.png")
        ).convert_alpha()
        self.current_dish = pg.transform.scale(self.current_dish, (215, 170))
        self.game_over = False


    def run(self):
        global GAME_OVER
        while True:
            self.screen.blit(self.sgame_bg, (0, 0))

            # This make the ingredients move down and side
            self.count += 10
            try:
                for i in range(len(MEALS["Starter"][self.dish_name]["ingredients"])):
                    x, y = positions[i]
                    vel = velocities[i]
                    y += vel
                    if y >= MAX_FALL_HEIGHT:
                        GAME_OVER = True
                        y = 0
                        x = randint(10, 1100)
                    positions[i] = (x, y)
            except IndexError as e:
                raise e

            if GAME_OVER:
                result = game_over_screen(self.screen)
                if result == "exit":
                    # Exit the game
                    pg.quit()
                    sys.exit()

            # Draw and update the player sprite
            self.pot.draw(self.screen)
            self.pot.update()

            # This makes the ingredients to fall from top to bottom
            # TODO: if the item y position is player y position add it to the collected item
            # TODO: and remove that item in the list at the side of the screen
            for i in range(len(MEALS["Starter"][self.dish_name]["ingredients"])):
                ingredient = MEALS["Starter"][self.dish_name]["ingredients"][i]
                ingredient_img = pg.transform.scale(ingredient, (75, 75))
                x, y = positions[i]
                self.update_pos(x, y, ingredient_img)
                if y == self.pot.rect.y and x == self.pot.rect.x:
                    print(ingredient)
                    self.update_pos(x, y, ingredient_img)

            # Draw non-moving ingredients to show what need to be collected
            # TODO: remove the item that was collected by the player in the list of ingredients
            self.draw_ingredients()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                self.pot.handle_input(event)

            self.GAME_MOUSE_POS = pg.mouse.get_pos()

            # Display Current Dish
            self.cd_text = get_font(20).render("Current Dish:", True, (255, 0, 0))
            self.dish = get_font(20).render(f"   {self.dish_name}", True, (255, 0, 0))
            self.screen.blit(self.cd_text, (10, 10))
            self.screen.blit(self.dish, (10, 30))
            # -----
            pg.display.update()

    def draw_ingredients(self):
        y_pos = 30
        for i in range(len(MEALS["Starter"][self.dish_name]["ingredients"])):
            ingredient = MEALS["Starter"][self.dish_name]["ingredients"][i]
            ingredient_img = pg.transform.scale(ingredient, (64, 64))

            self.screen.blit(ingredient_img, (1120, y_pos))
            y_pos += 60

    def update_pos(self, x, y, image):
        # update image position
        self.screen.blit(image, (x, y))


class DO_DISH1(DISH_UI):
    def __init__(self, screen, dish_name):
        super().__init__(screen, dish_name)


class DO_DISH2(DISH_UI):
    def __init__(self, screen, dish_name):
        super().__init__(screen, dish_name)


class DO_DISH3(DISH_UI):
    def __init__(self, screen, dish_name):
        super().__init__(screen, dish_name)
