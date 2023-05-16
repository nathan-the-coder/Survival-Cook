
import pygame as pg
from vars import BG_DIR, BTNS_DIR, WIDTH, HEIGHT
import os.path as path
import sys
from button import Button
from font import get_font

import ui

class GameOver:
    def __init__(self, screen: pg.Surface):
        self.screen = screen
        self.bg_image = pg.image.load(path.join(BG_DIR, '2.jpg'))
        self.bg_image = pg.transform.scale(self.bg_image, (WIDTH, HEIGHT))
        self.game_over_text = ui.get_font(30).render('GAME OVER', True, (255, 0, 0))

        main_menu_btn = pg.image.load(path.join(BTNS_DIR, "main_menu_btn.png"))
        main_menu_btn = pg.transform.scale(main_menu_btn, (206, 86))

        quit_btn = pg.image.load(path.join(BTNS_DIR, "quit_btn.png"))
        quit_btn = pg.transform.scale(quit_btn, (116, 86))

        self.buttons = [
            Button(
                image=main_menu_btn,
                pos=(400, 515),
                text_input="",
                font=get_font(35),
                base_color="#d7fcd4",
                hovering_color="White",
            ),
            Button(
                image=quit_btn,
                pos=(770, 515),
                text_input="",
                font=get_font(35),
                base_color="#d7fcd4",
                hovering_color="White",
            ) 
        ]

    def draw(self):
        self.screen.blit(self.bg_image, (0, 0))
        self.screen.blit(self.game_over_text, (500, 200))

    def show(self):
        self.running = True
        while self.running:
            self.draw()
            self.mouse_pos = pg.mouse.get_pos()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                    pg.quit()
                    sys.exit()
                elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    for button in self.buttons:
                        if button.rect.collidepoint(self.mouse_pos):
                            if button == self.buttons[0]:
                                ui.main_menu(self.screen)
                                return
                            elif button == self.buttons[1]:
                                pg.quit()
                                sys.exit()

            for button in self.buttons:
                button.changeColor(self.mouse_pos)
                button.update(self.screen)

            pg.display.update()

