import pygame as pg

from vars import WIDTH


class Sprite(pg.sprite.Sprite):
    def __init__(self, groups: pg.sprite.Group, image):
        super().__init__(groups)

        self.image = pg.image.load(image)
        self.rect = self.image.get_rect()
        self.leftPressed, self.rightPressed = False, False
        self.h_speed = 20

        self.collected_ingredients = []
        self.rect.x = 500

    def draw(self, screen):
        # print(help(self.image))
        screen.blit(self.image, (self.rect.x, 450))

    def handle_input(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                self.leftPressed = True
            elif event.key == pg.K_RIGHT:
                self.rightPressed = True

        elif event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                self.leftPressed = False
            elif event.key == pg.K_RIGHT:
                self.rightPressed = False

    def update(self):
        if self.rect.x < 0:
            self.rect.x = 5
        elif self.rect.x > WIDTH:
            self.rect.x = WIDTH - 300

        if self.leftPressed and not self.rightPressed:
            self.rect.x -= self.h_speed
        elif self.rightPressed and not self.leftPressed:
            self.rect.x += self.h_speed
