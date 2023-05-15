import random
from os import path

import pygame as pg

WIDTH = 1200
HEIGHT = 650

ROUND1_SPEED = 10

BASE_DIR = "assets"
STARTER_DIR = path.join(BASE_DIR, "meals", "starter")
BG_DIR = path.join(BASE_DIR, "bg_images")
BTNS_DIR = path.join(BASE_DIR, "buttons")

SPRITES = pg.sprite.Group()
positions = [(100, 0), (300, 0), (500, 0), (700, 0), (900, 0), (1100, 0)]
velocities = [10, 10, 10, 10, 10, 10]

MAX_FALL_HEIGHT = 650
MEALS = {
    "Starter": {
        "Dishes": ["Charcuterie", "Mushroom Soup", "French Fries"],
        "French Fries": {
            "ing_count": 6,
            "ingredients": [
                pg.image.load(path.join(STARTER_DIR, "starter_ing1.png")),
                pg.image.load(path.join(STARTER_DIR, "starter_ing2.png")),
                pg.image.load(path.join(STARTER_DIR, "starter_ing8.png")),
                pg.image.load(path.join(STARTER_DIR, "starter_ing9.png")),
                pg.image.load(path.join(STARTER_DIR, "starter_ing10.png")),
                pg.image.load(path.join(STARTER_DIR, "starter_ing11.png")),
            ],
        },
        "Charcuterie": {
            "ing_count": 6,
            "ingredients": [
                pg.image.load(path.join(STARTER_DIR, "starter_ing1.png")),
                pg.image.load(path.join(STARTER_DIR, "starter_ing2.png")),
                pg.image.load(path.join(STARTER_DIR, "starter_ing12.png")),
                pg.image.load(path.join(STARTER_DIR, "starter_ing15.png")),
                pg.image.load(path.join(STARTER_DIR, "starter_ing13.png")),
                pg.image.load(path.join(STARTER_DIR, "starter_ing14.png")),
            ],
        },
        "Mushroom Soup": {
            "ing_count": 7,
            "ingredients": [
                pg.image.load(path.join(STARTER_DIR, "starter_ing1.png")),
                pg.image.load(path.join(STARTER_DIR, "starter_ing2.png")),
                pg.image.load(path.join(STARTER_DIR, "starter_ing3.png")),
                pg.image.load(path.join(STARTER_DIR, "starter_ing4.png")),
                pg.image.load(path.join(STARTER_DIR, "starter_ing5.png")),
                pg.image.load(path.join(STARTER_DIR, "starter_ing6.png")),
                pg.image.load(path.join(STARTER_DIR, "starter_ing7.png")),
            ],
        },
    },
}
