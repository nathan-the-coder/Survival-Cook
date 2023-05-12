import os.path as path

import pygame as pg

from ui import main_menu
from vars import BG_DIR, HEIGHT, WIDTH


class Game:
    def __init__(self, width, height):
        pg.init()

        # Set the game icon
        pg.display.set_icon(pg.image.load("assets/icon.png"))

        # Set the splash image and add a interval to tell
        # when the image will not be rendered
        self.bg_file = path.join(BG_DIR, "1.jpg")
        bg_img = pg.image.load(self.bg_file).convert_alpha()
        self.bg_img = pg.transform.scale(bg_img, (width, height))

        self.counter = 0
        # ---------------------------

        # Define screen where we render sprites and animations
        self.screen = pg.display.set_mode((width, height))

        # Set program title
        pg.display.set_caption("Survival Cook")

        # Boolean value to determine if game is running or not
        self.is_running = True

        # Define clock for setting up fps
        self.clock = pg.time.Clock()

    def draw(self):
        # Fill the screen with black background
        self.screen.fill((0, 0, 0))

        self.screen.blit(self.bg_img, (0, 0))

        if self.counter == 40:
            self.start()

        # Set 60 fps on the clock
        self.clock.tick(60)

        # Update the display window
        pg.display.flip()

    def handle_events(self, event):
        # Check for events
        if event.type == pg.QUIT:
            self.is_running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.is_running = False
            if event.key == pg.K_RETURN:
                self.start()

    def start(self):
        main_menu()

    def change_bg(self, bg_file_index):
        self.bg_file = f"assets/bg_image\\{bg_file_index}.jpg"
        bg_img = pg.image.load(self.bg_file)
        self.bg_img = pg.transform.scale(bg_img, (WIDTH, HEIGHT))

    def run(self):
        while self.is_running:
            for event in pg.event.get():
                self.handle_events(event)

            self.draw()
            self.counter += 1


if __name__ == "__main__":
    game = Game(WIDTH, HEIGHT)
    game.run()
