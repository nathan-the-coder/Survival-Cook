import os.path as path
import sys

import pygame as pg
from pygame_menu.themes import THEME_ORANGE

from button import Button
from dishes import GAME_OVER, START_GAME, options
from font import get_font

import pygame_menu as pgmenu
from vars import BASE_DIR, BG_DIR, BTNS_DIR, HEIGHT, WIDTH
from music import play_music

play_music()

BG = pg.image.load(path.join(BG_DIR, "2.jpg"))
BG = pg.transform.scale(BG, (WIDTH, HEIGHT))
pg.init()


pbtn = pg.image.load(path.join(BTNS_DIR, "play_btn.png"))
pbtn = pg.transform.scale(pbtn, (116, 86))

opt_btn = pg.image.load(path.join(BTNS_DIR, "options_btn.png"))
opt_btn = pg.transform.scale(opt_btn, (156, 86))

quit_btn = pg.image.load(path.join(BTNS_DIR, "quit_btn.png"))
quit_btn = pg.transform.scale(quit_btn, (116, 86))


def main_menu(screen):
    global GAME_OVER

    GAME_OVER = False
    PLAY_BTN = Button(
        image=pbtn,
        pos=(430, 515),
        text_input="",
        font=get_font(35),
        base_color="#d7fcd4",
        hovering_color="White",
    )

    OPTION_BTN = Button(
        image=opt_btn,
        pos=(600, 515),
        text_input="",
        font=get_font(35),
        base_color="#d7fcd4",
        hovering_color="White",
    )

    QUIT_BTN = Button(
        image=quit_btn,
        pos=(770, 515),
        text_input="",
        font=get_font(35),
        base_color="#d7fcd4",
        hovering_color="White",
    )

    GAME_TITLE = get_font(40).render("SURVIVING COOK", True, (255, 0, 0), None)
    CENTER_IMG = pg.image.load(path.join(BASE_DIR, "icon 200x200.png")).convert_alpha()
    CENTER_IMG = pg.transform.scale(CENTER_IMG, (400, 400))
    starters_game = START_GAME(screen)

    while True:
        screen.blit(BG, (0, 0))
        screen.blit(CENTER_IMG, (410, 2))
        screen.blit(GAME_TITLE, (430, 400))

        for button in [PLAY_BTN, OPTION_BTN, QUIT_BTN]:
            button.update(screen)

        MENU_MOUSE_POS = pg.mouse.get_pos()

        if pg.mouse.get_pressed()[0]:
            if PLAY_BTN.rect.collidepoint(MENU_MOUSE_POS):
                starters_game.start()
            if OPTION_BTN.rect.collidepoint(MENU_MOUSE_POS):
                options(screen)
            if QUIT_BTN.rect.collidepoint(MENU_MOUSE_POS):
                pg.quit()
                sys.exit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        pg.display.update()
