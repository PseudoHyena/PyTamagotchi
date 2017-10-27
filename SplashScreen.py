import pygame
import time
from Window import Window
from Colors import Color
from Pets import Goose

#209x234
#Заставка
def SplashScreen():

    window = Window(900, 500, Color().white)
    display = window.newWindow("Start")

    img1 = []
    img1.append(pygame.image.load_extended("Sprites\\GooseStand.png").convert())
    img1.append(pygame.image.load_extended("Sprites\\GooseAnim1.png").convert())
    img1.append(pygame.image.load_extended("Sprites\\GooseAnim2.png").convert())

    titleImg = pygame.image.load_extended("Sprites\\title.png")

    ####################################################

    startPosX = 50
    startPosY = 100

    goose = Goose(img1, startPosX, startPosY)

    goose.object[0] = pygame.transform.flip(goose.object[0], True, False)
    goose.object[1] = pygame.transform.flip(goose.object[1], True, False)
    goose.object[2] = pygame.transform.flip(goose.object[2], True, False)

    gooseAnimationNumber = 0
    gooseStepDirection = 1

    #####################################################

    pygame.mixer.music.load("Sound\\shagi_po_pesku.mp3")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)

    #####################################################

    _time = time.time()

    while True:
        display.fill(Color().white)

        for e in pygame.event.get():
            if (e.type == pygame.KEYDOWN):
                return

        if (time.time() - _time >= 0.6):
            goose.x += 50 * gooseStepDirection

            if (goose.x > 640):
                goose.object[0] = pygame.transform.flip(goose.object[0], True, False)
                goose.object[1] = pygame.transform.flip(goose.object[1], True, False)
                goose.object[2] = pygame.transform.flip(goose.object[2], True, False)

                display.blit(goose.object[0], (goose.x, goose.y))
                pygame.display.update()

                pygame.mixer.music.pause()
                _time = time.time()
                while time.time() - _time < 0.4:
                    pass
                pygame.mixer.music.unpause()

                gooseStepDirection = -1

            if (goose.x < 400 and gooseStepDirection == -1):
                pygame.mixer.music.stop()

                display.blit(goose.object[0], (goose.x, goose.y))
                display.blit(titleImg, (223, 354))
                pygame.display.update()

                pygame.mixer.music.load("Sound\\goose1.mp3")
                pygame.mixer.music.play()

                while time.time() - _time <= 3:
                    pass

                return

            gooseAnimationNumber += 1 if gooseAnimationNumber == 1 or gooseAnimationNumber == 0 else -1
            _time = time.time()

        display.blit(goose.object[gooseAnimationNumber], (goose.x, goose.y))
        pygame.display.update()

