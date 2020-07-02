import pygame as pg
from data import setup, tools
from data.constants import *


class Load_Screen(tools._State):
    def __init__(self):
        tools._State.__init__(self)

    def startup(self, current_time, persistant):
        self.next = "LEVEL1"
        self.surface = pg.Surface(SCREEN_SIZE)
        self.rect = self.surface.get_rect()
        text = "Cargando..."
        self.font = pg.font.Font(setup.FONTS['Fixedsys500c'], 15)
        self.rendered_text = self.font.render(text, 1, BLACK)
        self.text_rect = self.rendered_text.get_rect()
        self.text_rect.center = self.rect.center

    def update(self, surface, keys, current_time):
        self.current_time = current_time
        surface.fill(BACKGROUND_BLUE)
        surface.blit(self.rendered_text, self.text_rect)

        if (self.current_time - self.start_time) > 4000:
            print("done2")
            self.done = True


    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            print("done")
            self.done = True
