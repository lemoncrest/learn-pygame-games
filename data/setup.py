import os
import pygame as pg
from data import tools
from constants import *

ORIGINAL_CAPTION = ORIGINAL_CAPTION

os.environ['SDL_VIDEO_CENTERED'] = '1'
pg.init()
pg.display.set_caption(ORIGINAL_CAPTION)
SCREEN = pg.display.set_mode(SCREEN_SIZE)
SCREEN_RECT = SCREEN.get_rect()

FONTS = tools.load_all_fonts(os.path.join("resources","fonts"))
MUSIC = tools.load_all_music(os.path.join("resources","music"))
GFX   = tools.load_all_gfx(os.path.join("resources","graphics"))
SFX   = tools.load_all_sfx(os.path.join("resources","sound"))
