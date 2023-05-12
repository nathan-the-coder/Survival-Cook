import os.path as path
import sys

import pygame as pg

from button import Button
from dishes import DO_DISH1, DO_DISH2, DO_DISH3, START_GAME
from font import get_font
from vars import (BASE_DIR, BG_DIR, BTNS_DIR, DESSERT_DIR, HEIGHT, MAIN_DIR,
                  MEALS, STARTER_DIR, WIDTH)

SCREEN = pg.display.set_mode((WIDTH, HEIGHT))
BG = pg.image.load(path.join(BG_DIR, "2.jpg"))
BG = pg.transform.scale(BG, (WIDTH, HEIGHT))
pg.init()


def play():
    pg.display.set_caption("Survival Cook")
    counter = 0

    while True:
        PLAY_MOUSE_POS = pg.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        back_img = pg.image.load(path.join(BTNS_DIR, "right_btn.png"))
        back_img = pg.transform.scale(back_img, (64, 64))

        for i in range(400):
            START_GAME(SCREEN)

        # Starter()

        back_btn = Button(
            image=back_img,
            pos=(1155, 50),
            text_input="",
            font=get_font(75),
            base_color="#d7fcd4",
            hovering_color="White",
        )

        back_btn.changeColor(PLAY_MOUSE_POS)
        back_btn.update(SCREEN)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    main_menu()

            if event.type == pg.MOUSEBUTTONDOWN:
                if back_btn.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pg.display.update()


def options():
    pg.display.set_caption("Survival Cook - Options")

    while True:
        OPTION_MOUSE_POS = pg.mouse.get_pos()

        SCREEN.fill("black")

        OPTION_TEXT = get_font(45).render("This is a OPTIONS screen.", True, "white")
        OPTION_RECT = OPTION_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTION_TEXT, OPTION_RECT)

        OPTION_BACK = Button(
            image=None,
            pos=(640, 460),
            text_input="BACK",
            font=get_font(75),
            base_color="Black",
            hovering_color="Green",
        )

        OPTION_BACK.update(SCREEN)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if OPTION_BACK.checkForInput(OPTION_MOUSE_POS):
                    main_menu()

        pg.display.update()


def main_menu():
    pg.display.set_caption("Survival Cook")

    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pg.mouse.get_pos()

        CENTER_IMG = pg.image.load(
            path.join(BASE_DIR, "icon 200x200.png")
        ).convert_alpha()
        CENTER_IMG = pg.transform.scale(CENTER_IMG, (400, 400))
        SCREEN.blit(CENTER_IMG, (410, 2))

        GAME_TITLE = get_font(40).render("SURVIVING COOK", True, (255, 0, 0), None)
        SCREEN.blit(GAME_TITLE, (430, 400))

        PLAY_BTN = Button(
            image=pg.image.load(path.join(BTNS_DIR, "play_btn.png")),
            pos=(450, 515),
            text_input="",
            font=get_font(35),
            base_color="#d7fcd4",
            hovering_color="White",
        )

        OPTION_BTN = Button(
            image=pg.image.load(path.join(BTNS_DIR, "settings.png")),
            pos=(600, 515),
            text_input="",
            font=get_font(35),
            base_color="#d7fcd4",
            hovering_color="White",
        )

        QUIT_BTN = Button(
            image=pg.image.load(path.join(BTNS_DIR, "exit.png")),
            pos=(800, 515),
            text_input="",
            font=get_font(35),
            base_color="#d7fcd4",
            hovering_color="White",
        )

        for button in [PLAY_BTN, OPTION_BTN, QUIT_BTN]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BTN.checkForInput(MENU_MOUSE_POS):
                    play()
                    SCREEN.blit(pg.image.load(path.join(MAIN_DIR, "2.jpg"), (0, 0)))
                if QUIT_BTN.checkForInput(MENU_MOUSE_POS):
                    pg.quit()
                    sys.exit()

        pg.display.update()
