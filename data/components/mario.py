import pygame as pg
from data import setup, tools
from data.constants import *

class Mario(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.sprite_sheet = setup.GFX['mario_bros']

        self.right_frames = []
        self.left_frames = []
        self.frame_index = 0
        self.x_vel = 0
        self.y_vel = 0
        self.max_x_vel = 4
        self.x_accel = .15
        self.max_y_vel = 4
        self.gravity = GRAVITY
        self.load_from_sheet()

        self.state = STAND
        self.image = self.right_frames[self.frame_index]
        self.rect = self.image.get_rect()

        self.facing_right = True
        self.walking_timer = 0




    def update(self, keys, current_time):
        self.handle_state(keys, current_time)
        self.update_position()
        self.animation()


    def update_position(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel


    def handle_state(self, keys, current_time):
        if self.state == STAND:
            self.standing(keys, current_time)
        elif self.state == WALK:
            self.walking(keys, current_time)
        elif self.state == JUMP:
            self.jumping(keys, current_time)
        elif self.state == FALL:
            self.falling(keys)


    def animation(self):
        if self.facing_right:
            self.image = self.right_frames[self.frame_index]
        else:
            self.image = self.left_frames[self.frame_index]




    def get_image(self, x, y, width, height):
        image = pg.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(BLACK)
        image = pg.transform.scale(image,
                                   (int(rect.width*SIZE_MULTIPLIER),
                                    int(rect.height*SIZE_MULTIPLIER)))
        return image


    def load_from_sheet(self):
        self.right_frames.append(
            self.get_image(178, 32, 12, 16)) #right
        self.right_frames.append(
            self.get_image(80,  32, 15, 16)) #right walking 1
        self.right_frames.append(
            self.get_image(99,  32, 15, 16)) #right walking 2
        self.right_frames.append(
            self.get_image(114, 32, 15, 16)) #right walking 3
        self.right_frames.append(
            self.get_image(144, 32, 16, 16)) #right jump
        self.right_frames.append(
            self.get_image(130, 32, 14, 16)) #right skid

        #The left image frames are numbered the same as the right
        #frames but are simply reversed.

        for frame in self.right_frames:
            new_image = pg.transform.flip(frame, True, False)
            self.left_frames.append(new_image)


    """
    This function is called if Mario is standing still
    """
    def standing(self, keys, current_time):

        self.frame_index = 0

        if keys[pg.K_LEFT]:
            self.facing_right = False
            self.state = WALK
        elif keys[pg.K_RIGHT]:
            self.facing_right = True
            self.state = WALK
        elif keys[pg.K_a]:
            self.state = JUMP
            self.y_vel = -10
        else:
            self.state = STAND


    """
    This function is called when Mario is in a walking state
    It changes the frame, checks for holding down the run button,
    checks for a jump, then adjusts the state if necessary
    """
    def walking(self, keys, current_time):

        if self.frame_index == 0:
            self.frame_index += 1
            self.walking_timer = current_time
        else:
            if (current_time - self.walking_timer >
                    self.calculate_animation_speed()):
                if self.frame_index < 3:
                    self.frame_index += 1
                else:
                    self.frame_index = 1

                self.walking_timer = current_time


        if keys[pg.K_s]:
            self.max_x_vel = 6
        else:
            self.max_x_vel = 4


        if keys[pg.K_a]:
            self.state = JUMP
            self.y_vel = -10


        if keys[pg.K_LEFT]:
            self.facing_right = False
            if self.x_vel > 0:
                self.frame_index = 5
            if self.x_vel > (self.max_x_vel * -1):
                self.x_vel -= self.x_accel

        elif keys[pg.K_RIGHT]:
            self.facing_right = True
            if self.x_vel < 0:
                self.frame_index = 5
            if self.x_vel < self.max_x_vel:
                self.x_vel += self.x_accel


        else:
            if self.facing_right:
                if self.x_vel > 0:
                    self.x_vel -= self.x_accel
                else:
                    self.x_vel = 0
                    self.state = STAND
            else:
                if self.x_vel < 0:
                    self.x_vel += self.x_accel
                else:
                    self.x_vel = 0
                    self.state = STAND


    def jumping(self, keys, current_time):
        self.frame_index = 4
        self.y_vel += self.gravity
        if (self.rect.bottom > (SCREEN_HEIGHT - GROUND_HEIGHT)):
            self.y_vel = 0
            self.state = WALK


        if keys[pg.K_LEFT]:
            self.facing_right = False
            if self.x_vel > (self.max_x_vel * - 1):
                self.x_vel -= self.x_accel

        elif keys[pg.K_RIGHT]:
            self.facing_right = True
            if self.x_vel < self.max_x_vel:
                self.x_vel += self.x_accel



    def calculate_animation_speed(self):
        if self.x_vel == 0:
            animation_speed = 115
        elif self.x_vel > 0:
            animation_speed = 115 - (self.x_vel * 12)
        else:
            animation_speed = 115 - (self.x_vel * 12 * -1)

        return animation_speed
