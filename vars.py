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

MEALS = {
    "Starter": {
        "Dishes": ["Charcuterie", "Mushroom Soup", "French Fries"],
        "French Fries": {
            "ing_count": 6,
            "ingredients": {
                "Seasoning": pg.image.load(path.join(STARTER_DIR, "starter_ing1.png")),
                "Bread": pg.image.load(path.join(STARTER_DIR, "starter_ing2.png")),
                "Potato": pg.image.load(path.join(STARTER_DIR, "starter_ing8.png")),
                "Oil": pg.image.load(path.join(STARTER_DIR, "starter_ing9.png")),
                "Ketchup": pg.image.load(path.join(STARTER_DIR, "starter_ing10.png")),
                "Water": pg.image.load(path.join(STARTER_DIR, "starter_ing11.png")),
            },
        },
        "Charcuterie": {
            "ing_count": 6,
            "ingredients": {
                "Seasoning": pg.image.load(path.join(STARTER_DIR, "starter_ing1.png")),
                "Bread": pg.image.load(path.join(STARTER_DIR, "starter_ing2.png")),
                "Tomato": pg.image.load(path.join(STARTER_DIR, "starter_ing12.png")),
                "Cheese": pg.image.load(path.join(STARTER_DIR, "starter_ing15.png")),
                "Cutted Meats": pg.image.load(
                    path.join(STARTER_DIR, "starter_ing13.png")
                ),
                "Olive Oil": pg.image.load(path.join(STARTER_DIR, "starter_ing14.png")),
            },
        },
        "Mushroom Soup": {
            "ing_count": 7,
            "ingredients": {
                "Seasoning": pg.image.load(path.join(STARTER_DIR, "starter_ing1.png")),
                "Bread": pg.image.load(path.join(STARTER_DIR, "starter_ing2.png")),
                "Mushroom": pg.image.load(path.join(STARTER_DIR, "starter_ing3.png")),
                "Vegatable Stock": pg.image.load(
                    path.join(STARTER_DIR, "starter_ing4.png")
                ),
                "Butter": pg.image.load(path.join(STARTER_DIR, "starter_ing5.png")),
                "Cream and Flour": pg.image.load(
                    path.join(STARTER_DIR, "starter_ing6.png")
                ),
                "Herbs": pg.image.load(path.join(STARTER_DIR, "starter_ing7.png")),
            },
        },
    },
}
