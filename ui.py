import os.path as path
import sys

import pygame as pg

from button import Button
from dishes import START_GAME
from font import get_font
from vars import (BASE_DIR, BG_DIR, BTNS_DIR, HEIGHT, WIDTH)

SCREEN = pg.display.set_mode((WIDTH, HEIGHT))
BG = pg.image.load(path.join(BG_DIR, "2.jpg"))
BG = pg.transform.scale(BG, (WIDTH, HEIGHT))
pg.init()


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
                    START_GAME(SCREEN)
                if QUIT_BTN.checkForInput(MENU_MOUSE_POS):
                    pg.quit()
                    sys.exit()

        pg.display.update()
