import pygame as pg
import os.path as path
from vars import *


def get_font(fontSize: int) -> pg.font.Font:
    font = pg.font.Font(path.join(BASE_DIR, 'font.ttf', fontSize)

    return font
