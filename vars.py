import random
from os import path

import pygame as pg

WIDTH = 1200
HEIGHT = 650

ROUND = 3

BASE_DIR = "assets"
STARTER_DIR = path.join(BASE_DIR, "meals", "starter")
MAIN_COURSE_DIR = path.join(BASE_DIR, "meals", "main_course")
DESSERT_DIR = path.join(BASE_DIR, "meals", "dessert")

BG_DIR = path.join(BASE_DIR, "bg_images")
BTNS_DIR = path.join(BASE_DIR, "buttons")


GAME_OVER = False
SPRITES = pg.sprite.Group()

positions = [(100, 0), (300, 0), (500, 0), (700, 0), (900, 0), (1100, 0)]
starters_velocities = [5, 7, 9, 4, 6, 5]
main_course_velocities = [10, 14, 13, 11, 15, 16]
dessert_velocities = [17, 22, 21, 19, 18, 20]

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
    "Main Course": {
        "Steak": {
            "ingredients_count": 6,
            "ingredients": [
                pg.image.load(path.join(MAIN_COURSE_DIR, "main_course_ing1.png")),
                pg.image.load(path.join(MAIN_COURSE_DIR, "main_course_ing2.png")),
                pg.image.load(path.join(MAIN_COURSE_DIR, "main_course_ing3.png")),
                pg.image.load(path.join(MAIN_COURSE_DIR, "main_course_ing4.png")),
                pg.image.load(path.join(MAIN_COURSE_DIR, "main_course_ing5.png")),
                pg.image.load(path.join(MAIN_COURSE_DIR, "main_course_ing6.png")),
            ],
        },
        "Baked Salmon": {
            "ingredients_count": 6,
            "ingredients": [
                pg.image.load(path.join(MAIN_COURSE_DIR, "main_course_ing7.png")),
                pg.image.load(path.join(MAIN_COURSE_DIR, "main_course_ing2.png")),
                pg.image.load(path.join(MAIN_COURSE_DIR, "main_course_ing3.png")),
                pg.image.load(path.join(MAIN_COURSE_DIR, "main_course_ing4.png")),
                pg.image.load(path.join(MAIN_COURSE_DIR, "main_course_ing5.png")),
                pg.image.load(path.join(MAIN_COURSE_DIR, "main_course_ing6.png")),
            ],
        },
        "Spaghetti": {
            "ingredients_count": 6,
            "ingredients": [
                pg.image.load(path.join(MAIN_COURSE_DIR, "main_course_ing8.png")),
                pg.image.load(path.join(MAIN_COURSE_DIR, "main_course_ing5.png")),
                pg.image.load(path.join(MAIN_COURSE_DIR, "main_course_ing9.png")),
                pg.image.load(path.join(MAIN_COURSE_DIR, "main_course_ing3.png")),
                pg.image.load(path.join(MAIN_COURSE_DIR, "main_course_ing10.png")),
                pg.image.load(path.join(MAIN_COURSE_DIR, "main_course_ing11.png")),
            ],
        },
    },
    "Dessert": [
        pg.image.load(path.join(DESSERT_DIR, "dessert_dish1.png")), 
        pg.image.load(path.join(DESSERT_DIR, "dessert_dish2.png")), 
        pg.image.load(path.join(DESSERT_DIR, "dessert_dish3.png")), 
    ],
}
