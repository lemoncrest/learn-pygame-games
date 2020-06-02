import os,sys
import pygame

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
handler = logging.FileHandler(os.path.join(os.getcwd(), "log.txt"))
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


if __name__=='__main__':

    logger.info("init lesson 1")
    SCREENX = 800
    SCREENY = 600

    BACKGROUND_PATH = os.path.join('resources/images','background.png')
    MUSHROOM_PATH = os.path.join('resources/images','mushroom.png')
    BACKGROUND_MUSIC_PATH = os.path.join('resources/music','init.ogg')

    menuX = 225
    #this part will decide which coordinate (just Y axe)
    lastMenuY = 405
    firstMenuY = 360

    fps = 25 # frame rate
    clock = pygame.time.Clock()

    pygame.init()
    main = True # flag to control program exit without breaks or exits

    BLUE  = (25,25,200)
    BLACK = (23,23,23 )
    WHITE = (254,254,254)
    ALPHA = (0,255,0)

    screen = pygame.display.set_mode([SCREENX,SCREENY])
    backdrop = pygame.image.load(BACKGROUND_PATH).convert()
    mushroom = pygame.image.load(MUSHROOM_PATH).convert()
    backScreen = screen.get_rect()

    #init music
    logger.debug("load music")
    pygame.mixer.init()
    pygame.mixer.music.load(BACKGROUND_MUSIC_PATH)
    pygame.mixer.music.play()

    #Main loop
    menuY = firstMenuY
    refresh = False
    while main == True:

        #manage events
        for event in pygame.event.get():
            logger.debug("some event happened")
            if event.type == pygame.QUIT:
                main = False

            #push keyboard button event
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    menuY = lastMenuY if menuY==firstMenuY else firstMenuY
                    refresh = True
                elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                    menuY = lastMenuY if menuY==firstMenuY else firstMenuY
                    refresh = True
                elif event.key == pygame.K_UP or event.key == ord('w'):
                    menuY = lastMenuY if menuY==firstMenuY else firstMenuY
                    refresh = True
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    menuY = lastMenuY if menuY==firstMenuY else firstMenuY
                    refresh = True

            # release key q for exit
            elif event.type == pygame.KEYUP:
                if event.key == ord('q'): #exit
                    main = False

        #redraw background if necessary to clean screen
        if refresh:
            logger.debug("refresh backdrop!")
            backdrop = pygame.image.load(BACKGROUND_PATH).convert() #refresh with background image
            refresh = False

        #draw part
        backdrop.blit(mushroom,(menuX,menuY))
        screen.blit(backdrop, backScreen)
        pygame.display.flip()
        clock.tick(fps)

    #finish part
    logger.info("end lesson 1")
    print("bye!")
    #pygame.quit()
    #sys.exit()
