import pygame
import time
from Window import Window
from Colors import Color
from Pets import Goose

#209x234
#Заставка
def SplashScreen():
    #Инициализация окна
    window = Window(900, 500, Color().white)
    display = window.newWindow("Start")

    ####################################################

    #Загрузка анимации гуся
    img1 = []
    img1.append(pygame.image.load_extended("Sprites\\GooseStand.png").convert())
    img1.append(pygame.image.load_extended("Sprites\\GooseAnim1.png").convert())
    img1.append(pygame.image.load_extended("Sprites\\GooseAnim2.png").convert())

    titleImg = pygame.image.load_extended("Sprites\\title.png")

    ####################################################

    #Инициализация гуся
    startPosX = 50
    startPosY = 100

    goose = Goose(img1, startPosX, startPosY)

    goose.object[0] = pygame.transform.flip(goose.object[0], True, False)
    goose.object[1] = pygame.transform.flip(goose.object[1], True, False)
    goose.object[2] = pygame.transform.flip(goose.object[2], True, False)

    gooseAnimationNumber = 0
    gooseStepDirection = 1

    #####################################################

    #Инициализация звуков ходьбы
    pygame.mixer.music.load("Sound\\shagi_po_pesku.mp3")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)

    #####################################################

    _time = time.time()

    #Цикл заставки
    while True:
        #Зарисовка окна
        display.fill(Color().white)

        #Обработка событий
        for e in pygame.event.get():
            #Обработка события пропуска заставки
            if (e.type == pygame.KEYDOWN):
                pygame.mixer.music.stop()
                pygame.display.quit()
                return

        #Анимация гуся
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

                pygame.display.quit()
                return

            gooseAnimationNumber += 1 if gooseAnimationNumber == 1 or gooseAnimationNumber == 0 else -1
            _time = time.time()

        #Отрисовка и обновление
        display.blit(goose.object[gooseAnimationNumber], (goose.x, goose.y))
        pygame.display.update()

