import pygame as pg
import os.path as path
from vars import BASE_DIR

pg.mixer.init()
pg.mixer.music.set_volume(10)
pg.mixer.music.load(path.join(BASE_DIR, "music", "Roa-Innocence.mp3"))

def play_music():
    pg.mixer.music.play()
