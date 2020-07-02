import os

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HEIGHT)

ORIGINAL_CAPTION = "Lesson 02"

BACKGROUND_PATH = os.path.join('resources/images','background.png')
MUSHROOM_PATH = os.path.join('resources/images','mushroom.png')
BACKGROUND_MUSIC_PATH = os.path.join('resources/music','init.ogg')


## COLORS ##

#                  R    G    B
GRAY            = (100, 100, 100)
NAVYBLUE        = ( 60,  60, 100)
WHITE           = (255, 255, 255)
RED             = (255,   0,   0)
GREEN           = (  0, 255,   0)
FOREST_GREEN    = ( 31, 162,  35)
BLUE            = (  0,   0, 255)
YELLOW          = (255, 255,   0)
ORANGE          = (255, 128,   0)
PURPLE          = (255,   0, 255)
CYAN            = (  0, 255, 255)
BLACK           = (  0,   0,   0)
NEAR_BLACK      = ( 19,  15,  48)
COMBLUE         = (233, 232, 255)
GOLD            = (255, 215,   0)
BACKGROUND_BLUE = (106, 150, 252)

BGCOLOR = BACKGROUND_BLUE

SIZE_MULTIPLIER = 2.5
BACK_SIZE_MULTIPLER = 2.67 #depends on first_level.png quality
GROUND_HEIGHT = 63
GRAVITY = .4

#Mario States

STAND = 'standing'
WALK = 'walk'
JUMP = 'jump'
FALL = 'fall'
