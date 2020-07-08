# python2 issues, div with float, not int
from __future__ import division

import os,sys
import pygame

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
handler = logging.FileHandler(os.path.join(os.getcwd(), "log.txt"))
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

from data.main import main

if __name__=='__main__':

    main()
    pygame.quit()
    sys.exit()
