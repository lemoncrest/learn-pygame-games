import pygame as pg
from data import setup, tools
from data.constants import *
from data.components import mario, collider
import json
import copy

"""
This class defines where are all the things in the first level
"""
class First_Level(tools._State):

    def __init__(self):
        tools._State.__init__(self)

    def startup(self, current_time, persistant):
        self.persistant = persistant
        self.setup_ground()
        self.setup_pipes()
        self.setup_steps()
        self.collide_group = pg.sprite.Group(self.ground_group,
                                             self.pipe_group,
                                             self.step_group)
        self.background = setup.GFX['first_level']
        self.back_rect = self.background.get_rect()
        self.back_rect.x = 0
        self.back_rect.y = 0
        self.background = pg.transform.scale(self.background,
                                   (int(self.back_rect.width * BACK_SIZE_MULTIPLER),
                                    int(self.back_rect.height * BACK_SIZE_MULTIPLER)))
        self.mario = mario.Mario()
        self.setup_mario_location()
        self.all_sprites = pg.sprite.Group(self.mario)
        self.camera_adjust = 0

    def setup_mario_location(self):
        self.mario.rect.x = 110
        self.mario.rect.bottom = GROUND_HEIGHT

    def setup_ground(self):
        self.ground_rect1 = collider.Collider(0, GROUND_HEIGHT,    2940, 60)
        self.ground_rect2 = collider.Collider(3040, GROUND_HEIGHT,  629, 60)
        self.ground_rect3 = collider.Collider(3811, GROUND_HEIGHT, 2724, 60)
        self.ground_rect4 = collider.Collider(6631, GROUND_HEIGHT, 2992, 60)

        self.ground_group = pg.sprite.Group(self.ground_rect1,
                                           self.ground_rect2,
                                           self.ground_rect3,
                                           self.ground_rect4)

    def setup_pipes(self):
        pipes_path = setup.MAP['pipes']

        with open(pipes_path) as json_file:

            collinders = json.load(json_file)

            self.pipe_group = pg.sprite.Group()

            for col in collinders:
                x = col["x"]
                y = col["y"]
                width = col["width"]
                height = col["height"]
                element = collider.Collider(x, y, width, height)
                self.pipe_group.add(element)

    def setup_steps(self):

        steps_path = setup.MAP['steps']

        with open(steps_path) as json_file:

            collinders = json.load(json_file)

            self.step_group = pg.sprite.Group()

            for col in collinders:
                x = col["x"]
                y = col["y"]
                width = col["width"]
                height = col["height"]
                element = collider.Collider(x, y, width, height)
                self.step_group.add(element)

    def camera(self):
        if self.mario.rect.right > SCREEN_WIDTH / 3:
            self.camera_adjust = int(self.mario.rect.right - SCREEN_WIDTH / 3)
        else:
            self.camera_adjust = 0

        self.back_rect.x -= self.camera_adjust

        for collider in self.collide_group:
            collider.rect.x -= self.camera_adjust

        for sprite in self.all_sprites:
            sprite.rect.x -= self.camera_adjust



    def update_mario_position(self, keys):
        self.mario.rect.y += self.mario.y_vel

        collider = pg.sprite.spritecollideany(self.mario, self.collide_group)

        if collider:
            if self.mario.y_vel > 0:
                self.mario.y_vel = 0
                self.mario.rect.bottom = collider.rect.top
                self.mario.state = WALK
        else:
            try:
                test_sprite = copy.deepcopy(self.mario)
            except:
                test_sprite = self.mario.copy() #TODO see where/how python3 miss decimals
                pass
            test_sprite.rect.y += 1
            if not pg.sprite.spritecollideany(test_sprite, self.collide_group):
                if self.mario.state != JUMP:
                    self.mario.state = FALL

        self.mario.rect.x += self.mario.x_vel

        collider = pg.sprite.spritecollideany(self.mario, self.collide_group)

        if collider:
            if self.mario.x_vel > 0:
                self.mario.rect.right = collider.rect.left
            else:
                self.mario.rect.left = collider.rect.right

            self.mario.x_vel = 0

        if self.mario.rect.y > SCREEN_HEIGHT:
            self.startup(keys, self.persistant)

        if self.mario.rect.x < 5:
            self.mario.rect.x = 5


    """
    Updates level
    """
    def update(self, surface, keys, current_time):
        self.current_time = current_time
        self.all_sprites.update(keys, current_time)
        self.update_mario_position(keys)
        self.camera()
        surface.blit(self.background, self.back_rect)
        self.all_sprites.draw(surface)

        self.step_group.draw(surface)
