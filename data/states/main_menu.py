import pygame
import os
from data import setup, tools
from data.constants import *

class Menu(tools._State):
    
    def __init__(self):
        tools._State.__init__(self)
        self.refresh = True
        self.next = "LOAD_SCREEN"
        self.surface = pygame.Surface(SCREEN_SIZE)
        self.rect = self.surface.get_rect()
        text = 'Main Menu placeholder'
        self.font = pygame.font.Font(setup.FONTS['Fixedsys500c'], 15)
        self.rendered_text = self.font.render(text, 1, BLACK)
        self.text_rect = self.rendered_text.get_rect()
        self.text_rect.center = self.rect.center

        self.menuX = 225
        #this part will decide which coordinate (just Y axe)
        self.lastMenuY = 405
        self.firstMenuY = 360
        self.menuY = self.firstMenuY

        self.screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
        self.backdrop = pygame.image.load(BACKGROUND_PATH).convert()
        self.mushroom = pygame.image.load(MUSHROOM_PATH).convert()
        self.backScreen = self.screen.get_rect()


    def update(self, surface, keys, current_time):
        if self.refresh:
            self.backdrop = pygame.image.load(BACKGROUND_PATH).convert() #refresh with background image
            self.backdrop.blit(self.mushroom,(self.menuX,self.menuY))
            self.refresh = False

        #draw part
        self.screen.blit(self.backdrop, self.backScreen)
        pygame.display.flip()


    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.done = True

        #push keyboard button event
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                self.menuY = self.lastMenuY if self.menuY==self.firstMenuY else self.firstMenuY
                self.refresh = True
            elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                self.menuY = self.lastMenuY if self.menuY==self.firstMenuY else self.firstMenuY
                self.refresh = True
            elif event.key == pygame.K_UP or event.key == ord('w'):
                self.menuY = self.lastMenuY if self.menuY==self.firstMenuY else self.firstMenuY
                self.refresh = True
            elif event.key == pygame.K_DOWN or event.key == ord('s'):
                self.menuY = self.lastMenuY if self.menuY==self.firstMenuY else self.firstMenuY
                self.refresh = True
            elif event.key == pygame.K_RETURN or event.key == ord('q'): #exit
                self.done = True
