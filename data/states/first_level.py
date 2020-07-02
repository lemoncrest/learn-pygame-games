import pygame as pg
from data import setup, tools
from data import constants as c
from data.components import mario

class First_Level(tools._State):

    def __init__(self):
        tools._State.__init__(self)

    def startup(self, current_time, persistant):
        self.setup_ground()
        self.mario = mario.Mario()
        self.setup_mario_location()
        self.all_sprites = pg.sprite.Group(self.mario)

    def setup_mario_location(self):
        self.mario.rect.x = 10
        self.mario.rect.bottom = c.SCREEN_HEIGHT - self.mario.rect.height

    def setup_ground(self):
        pass

    """
    Updates level
    """
    def update(self, surface, keys, current_time):
        self.current_time = current_time
        setup.SCREEN.fill(c.BGCOLOR)
        self.all_sprites.update(keys, current_time)
        self.all_sprites.draw(surface)
