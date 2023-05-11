import pygame as pg
from os import path

WIDTH = 1200
HEIGHT = 650

ROUND1_SPEED = 10
ROUND2_SPEED = 20
ROUND3_SPEED = 30

BASE_DIR = "assets"
STARTER_DIR = path.join(BASE_DIR, "meals", "starter")
MAIN_DIR = path.join(BASE_DIR, "meals", "main")
DESSERT_DIR = path.join(BASE_DIR, "meals", "dessert")
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
                "Cutted Meats": pg.image.load(path.join(STARTER_DIR, "starter_ing13.png")),
                "Olive Oil": pg.image.load(path.join(STARTER_DIR, "starter_ing14.png")),
                }
        },
        "Mushroom Soup": {
            "ing_count": 7,
            "ingredients": {
                "Seasoning": pg.image.load(path.join(STARTER_DIR, "starter_ing1.png")),
                "Bread": pg.image.load(path.join(STARTER_DIR, "starter_ing2.png")),

                "Mushroom": pg.image.load(path.join(STARTER_DIR, "starter_ing3.png")),
                "Vegatable Stock": pg.image.load(path.join(STARTER_DIR, "starter_ing4.png")),
                "Butter": pg.image.load(path.join(STARTER_DIR, "starter_ing5.png")),
                "Cream and Flour": pg.image.load(path.join(STARTER_DIR, "starter_ing6.png")),
                "Herbs": pg.image.load(path.join(STARTER_DIR, "starter_ing7.png")),
                }
        },
    },
    "Main Course": {
        "Steak": {
            "ing_count": 6,
            "ingredients": {
                "Seasoning": pg.image.load(path.join(MAIN_DIR, "main_ing1.png")),
                "Butter": pg.image.load(path.join(MAIN_DIR, "main_ing2.png")),
                "Garlic": pg.image.load(path.join(MAIN_DIR, "main_ing3.png")),
                "Herbs": pg.image.load(path.join(MAIN_DIR, "main_ing4.png")),

                "T-Bone": pg.image.load(path.join(MAIN_DIR, "main_ing5.png")),
                "Asparagus": pg.image.load(path.join(MAIN_DIR, "main_ing6.png")),
            }
        },
        "Baked Salmon": {
            "ing_count": 6,
            "ingredients": {
                "Seasoning": pg.image.load(path.join(MAIN_DIR, "main_ing1.png")),
                "Butter": pg.image.load(path.join(MAIN_DIR, "main_ing2.png")),
                "Garlic": pg.image.load(path.join(MAIN_DIR, "main_ing3.png")),
                "Herbs": pg.image.load(path.join(MAIN_DIR, "main_ing4.png")),
                     
                "Salmon": pg.image.load(path.join(MAIN_DIR, "main_ing7.png")),
                "Asparagus": pg.image.load(path.join(MAIN_DIR, "main_ing6.png")),
            }
        },
        "Spaghetti": {
            "ing_count": 6,
            "ingredients": {
                "Seasoning": pg.image.load(path.join(MAIN_DIR, "main_ing1.png")),
                "Garlic": pg.image.load(path.join(MAIN_DIR, "main_ing3.png")),

                "Pasta Noodles": pg.image.load(path.join(MAIN_DIR, "main_ing8.png")),
                "Onion": pg.image.load(path.join(MAIN_DIR, "main_ing9.png")),
                "Tomato Sauce": pg.image.load(path.join(MAIN_DIR, "main_ing10.png")),
                "Protein of Choice": pg.image.load(path.join(MAIN_DIR, "main_ing11.png")),        
            }
        }
    },
    "Dessert": {
        "Sliced Cake": pg.image.load(path.join(DESSERT_DIR, "dessert_dish1.png")),
        "Ice Cream": pg.image.load(path.join(DESSERT_DIR, "dessert_dish2.png")),
        "Pudding": pg.image.load(path.join(DESSERT_DIR, "dessert_dish3.png")),
    }
}
