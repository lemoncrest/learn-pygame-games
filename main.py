import os,sys
import pygame

if __name__=='__main__':

    SCREENX = 800
    SCREENY = 600

    menuX = 225
    lastMenuY = 405
    firstMenuY = 360

    fps = 25        # frame rate
    clock = pygame.time.Clock()
    pygame.init()
    main = True

    BLUE  = (25,25,200)
    BLACK = (23,23,23 )
    WHITE = (254,254,254)
    ALPHA = (0,255,0)

    screen = pygame.display.set_mode([SCREENX,SCREENY])
    backdrop = pygame.image.load(os.path.join('resources/images','background.png')).convert()
    seta = pygame.image.load(os.path.join('resources/images','seta.png')).convert()
    backScreen = screen.get_rect()

    player_list = pygame.sprite.Group()
    #player_list.add(player)

    '''
    Main loop
    '''
    menuY = firstMenuY
    refresh = False
    while main == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
                main = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    print('left p')
                    menuY = lastMenuY if menuY==firstMenuY else firstMenuY
                    refresh = True
                elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                    print('right p')
                elif event.key == pygame.K_UP or event.key == ord('w'):
                    print('up p')
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    print('down p')

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    print('left r')
                elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                    print('right r')
                elif event.key == pygame.K_UP or event.key == ord('w'):
                    print('up r')
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    print('down r')
                elif event.key == ord('q'): #exit
                    pygame.quit()
                    sys.exit()
                    main = False

    #    screen.fill(BLACK)
        #screen.blit(screen, backScreen)
        if refresh:
            backdrop = pygame.image.load(os.path.join('images','background.png')).convert()
            refresh = False
        backdrop.blit(seta,(menuX,menuY))
        screen.blit(backdrop, backScreen)
        #player.update()
        player_list.draw(screen) #refresh player position
        pygame.display.flip()
        clock.tick(fps)
