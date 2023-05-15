import os.path as path
import sys

import pygame as pg

from button import Button
from dishes import START_GAME
from font import get_font
from vars import BASE_DIR, BG_DIR, BTNS_DIR, HEIGHT, WIDTH

SCREEN = pg.display.set_mode((WIDTH, HEIGHT))
BG = pg.image.load(path.join(BG_DIR, "2.jpg"))
BG = pg.transform.scale(BG, (WIDTH, HEIGHT))
pg.init()


def main_menu(screen):
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

    GAME_TITLE = get_font(40).render("SURVIVING COOK", True, (255, 0, 0), None)
    CENTER_IMG = pg.image.load(path.join(BASE_DIR, "icon 200x200.png")).convert_alpha()
    CENTER_IMG = pg.transform.scale(CENTER_IMG, (400, 400))
    starters_game = START_GAME(SCREEN)

    while True:
        screen.blit(BG, (0, 0))
        screen.blit(CENTER_IMG, (410, 2))
        screen.blit(GAME_TITLE, (430, 400))

        for button in [PLAY_BTN, OPTION_BTN, QUIT_BTN]:
            button.update(SCREEN)

        MENU_MOUSE_POS = pg.mouse.get_pos()

        if pg.mouse.get_pressed()[0]:
            if PLAY_BTN.rect.collidepoint(MENU_MOUSE_POS):
                starters_game.start()
            if QUIT_BTN.rect.collidepoint(MENU_MOUSE_POS):
                pg.quit()
                sys.exit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        pg.display.update()
