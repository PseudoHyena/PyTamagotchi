import pygame
import os
from Colors import Color
from Window import Window
from SplashScreen import SplashScreen
from Session import gameLoop
from  Button import Button
from Save import User

######################################

#Игровая информация
version = 0.6
title = "Tamagotchi PC ver %f - demo" % version

######################################

#Режимы видео
WVGA = (854, 480,)
HD = (1280, 720,)
FULLHD = (1920, 1080,)

displayWidth = 0
displayHeight = 0
isFullscreen = False

#######################################

#Работа с config.ini файлом
config_file = None

if (os.path.exists("Config\\config.ini") == False):
    config_file = open("Config\\config.ini", 'w')
    config_file.write("resolution=%dx%d\n" % (WVGA[0], WVGA[1]))
    config_file.write("fullscreen=False")
    config_file.close()
else:
    config_file = open("Config\\config.ini", "r+")
    for line in config_file:
        if (line.find("resolution") != -1):
            cfgResX = ""
            cfgResY = ""
            flag = False
            for ch in line:
                if (ch == 'x'):
                    flag = True

                elif (ch.isdigit() == True):
                    if (flag == False):
                        cfgResX += ch
                    else:
                        cfgResY += ch

            displayWidth = int(cfgResX)
            displayHeight = int(cfgResY)

        elif (line.find("fullscreen") != -1):
            if (line.find("True") != -1):
                isFullscreen = True
            else:
                isFullscreen = False

    config_file.close()
    config_file = open("Config\\config.ini", "w")

    if (displayWidth == WVGA[0] and displayHeight == WVGA[1]):
        config_file.write("resolution=%dx%d\n" % (displayWidth, displayHeight))

    elif (displayWidth == HD[0] and displayHeight == HD[1]):
        config_file.write("resolution=%dx%d\n" % (displayWidth, displayHeight))

    elif (displayWidth == FULLHD[0] and displayHeight == FULLHD[1]):
        config_file.write("resolution=%dx%d\n" % (displayWidth, displayHeight))

    else:
        config_file.write("resolution=%dx%d\n" % (WVGA[0], WVGA[1]))
        displayWidth = WVGA[0]
        displayHeight = WVGA[1]

    if (isFullscreen == True):
        config_file.write("fullscreen=True")
    else:
        config_file.write("fullscreen=False")

config_file.close()
######################################

#Инициализация движка и шрифта
pygame.init()
pygame.font.init()

myFont = pygame.font.SysFont("Comic Sans Ms", 22)

#######################################

#Заставка
SplashScreen()

#######################################

#Инициализация окна, фона, логотипа
window = Window(displayWidth, displayHeight, Color().black)
display = window.newWindow(title, (pygame.FULLSCREEN if isFullscreen == True else 0))

background_image = pygame.transform.scale(pygame.image.load_extended("Sprites\\MenuBackground.png").convert(), (displayWidth, displayHeight))

logo = pygame.image.load_extended("Sprites\\Logo.png").convert_alpha()
logoWidth = logo.get_width()
logoHeight = logo.get_height()

#######################################

#Кнопки
button_image = pygame.image.load_extended("Sprites\\Button.png").convert_alpha()
miniButton_image = pygame.image.load_extended("Sprites\\MiniButton.png").convert_alpha()

mainMenu_active = True
resolutionSettings_active = False
choiseSaveMenu_active = False
choisePetMenu_active = False

#Settings кнопка

settings_button = Button(button_image.copy(), "Settings", myFont)

#####

resWVGA_button = Button(button_image.copy(), "854x480", myFont)

resHD_button = Button(button_image.copy(), "1280x720", myFont)

resFULLHD_button = Button(button_image.copy(), "1920x1080", myFont)

resFullScreen_button = Button(button_image.copy(), "Fullscreen: " + ("on" if isFullscreen else "off"), myFont)

#####

#exit кнопка

exit_button = Button(button_image.copy(), "Exit", myFont)

#Play кнопка

play_button = Button(button_image.copy(), "Play", myFont)

#####

saveOne_button = Button(button_image.copy(), "Save 1", myFont)

saveTwo_button = Button(button_image.copy(), "Save 2", myFont)

saveThree_button = Button(button_image.copy(), "Save 3", myFont)

#####

back_button = Button(miniButton_image.copy(), "Back", myFont)

next_button = Button(miniButton_image.copy(), "Next", myFont)

confirm_button = Button(button_image.copy(), "Confirm", myFont)

#######################################

def locateButtons():
    play_button.x = (displayWidth - play_button.width) // 2
    play_button.y = (displayHeight - play_button.height) // 2

    settings_button.x = (displayWidth - settings_button.width) // 2
    settings_button.y = (displayHeight - settings_button.height) // 2 + 60

    exit_button.x = (displayWidth - exit_button.width) // 2
    exit_button.y = (displayHeight - exit_button.height) // 2 + 120

    resWVGA_button.x = (displayWidth - resWVGA_button.width) // 2
    resWVGA_button.y = (displayHeight - resWVGA_button.height) // 2

    resHD_button.x = (displayWidth - resHD_button.width) // 2
    resHD_button.y = (displayHeight - resHD_button.height) // 2 + 60

    resFULLHD_button.x = (displayWidth - resFULLHD_button.width) // 2
    resFULLHD_button.y = (displayHeight - resFULLHD_button.height) // 2 + 120

    resFullScreen_button.x = (displayWidth - resFullScreen_button.width) // 2
    resFullScreen_button.y = (displayHeight - resFullScreen_button.height) // 2 + 180

    saveOne_button.x = (displayWidth - saveOne_button.width) // 2
    saveOne_button.y = (displayHeight - saveOne_button.height) // 2

    saveTwo_button.x = (displayWidth - saveTwo_button.width) // 2
    saveTwo_button.y = (displayHeight - saveTwo_button.height) // 2 + 60

    saveThree_button.x = (displayWidth - saveThree_button.width) // 2
    saveThree_button.y = (displayHeight - saveThree_button.height) // 2 + 120

    back_button.x = (displayWidth - button_image.get_width()) // 2
    back_button.y = (displayHeight - back_button.height) // 2 + displayHeight // 4

    next_button.x = back_button.x + back_button.width + 40
    next_button.y = (displayHeight - next_button.height) // 2 + displayHeight // 4

    confirm_button.x = (displayWidth - confirm_button.width) // 2
    confirm_button.y = (displayHeight - next_button.height) // 2 + displayHeight // 4 + 60

locateButtons()

#######################################

def loadPets():
    pet_images = []

    petsSizeX = int(displayWidth / 7.112962963)
    petsSizeY = int(displayHeight / 4)

    pet_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Pets\\BlueBird.png").convert_alpha(),
                                             (petsSizeX, petsSizeY)))
    pet_images.append(
        pygame.transform.scale(pygame.image.load_extended("Sprites\\Pets\\BlueBirdNM.png").convert_alpha(),
                               (petsSizeX, petsSizeY)))

    pet_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Pets\\Chicken.png").convert_alpha(),
                                             (petsSizeX, petsSizeY)))
    pet_images.append(
        pygame.transform.scale(pygame.image.load_extended("Sprites\\Pets\\ChickenNM.png").convert_alpha(),
                               (petsSizeX, petsSizeY)))
    pet_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Pets\\Eagle.png").convert_alpha(),
                                             (petsSizeX, petsSizeY)))
    pet_images.append(
        pygame.transform.scale(pygame.image.load_extended("Sprites\\Pets\\EagleNM.png").convert_alpha(),
                               (petsSizeX, petsSizeY)))

    pet_images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Pets\\Owl.png").convert_alpha(),
                                             (petsSizeX, petsSizeY)))
    pet_images.append(
        pygame.transform.scale(pygame.image.load_extended("Sprites\\Pets\\OwlNM.png").convert_alpha(),
                               (petsSizeX, petsSizeY)))

    pet_images.append(
        pygame.transform.scale(pygame.image.load_extended("Sprites\\Pets\\YellowBird.png").convert_alpha(),
                               (petsSizeX, petsSizeY)))
    pet_images.append(
        pygame.transform.scale(pygame.image.load_extended("Sprites\\Pets\\YellowBirdNM.png").convert_alpha(),
                               (petsSizeX, petsSizeY)))

    return pet_images

#######################################

#Игровой цикл меню
while True:
    #Обработка событий
    for e in pygame.event.get():
        if (e.type == pygame.QUIT):
            exit()

        if (e.type == pygame.KEYDOWN):
            #Обработка события возвращения в меню
            if (e.key == pygame.K_ESCAPE):
                resolutionSettings_active = False
                choiseSaveMenu_active = False
                choisePetMenu_active = False
                mainMenu_active = True

        #Обработка событий нажатия на кнопки
        if (e.type == pygame.MOUSEBUTTONDOWN):

            #Обработка события нажатия на основные кнопки меню
            if (mainMenu_active):

                if (pygame.mouse.get_pos()[0] >= exit_button.x and pygame.mouse.get_pos()[0] <= exit_button.x + exit_button.width):
                    if (pygame.mouse.get_pos()[1] >= exit_button.y and pygame.mouse.get_pos()[1] <= exit_button.y + exit_button.height):
                        exit()

                if (pygame.mouse.get_pos()[0] >= settings_button.x and pygame.mouse.get_pos()[0] <= settings_button.x + settings_button.width):
                    if (pygame.mouse.get_pos()[1] >= settings_button.y and pygame.mouse.get_pos()[1] <= settings_button.y + settings_button.height):
                        resolutionSettings_active = True
                        mainMenu_active = False

                if (pygame.mouse.get_pos()[0] >= play_button.x and pygame.mouse.get_pos()[0] <= play_button.x + play_button.width):
                    if (pygame.mouse.get_pos()[1] >= play_button.y and pygame.mouse.get_pos()[1] <= play_button.y + play_button.height):
                        choiseSaveMenu_active = True
                        mainMenu_active = False

            #Обработка событий выбора разрешения и фуллскрина, переназначение положений кнопок
            elif (resolutionSettings_active):

                if (pygame.mouse.get_pos()[0] >= resWVGA_button.x and pygame.mouse.get_pos()[0] <= resWVGA_button.x + resWVGA_button.width):
                    if (pygame.mouse.get_pos()[1] >= resWVGA_button.y and pygame.mouse.get_pos()[1] <= resWVGA_button.y + resWVGA_button.height):
                        displayWidth, displayHeight = WVGA
                        window = Window(displayWidth, displayHeight, Color().black)
                        display = window.newWindow(title, pygame.FULLSCREEN if isFullscreen else 0)

                        config_file = open("Config\\config.ini", 'w')
                        config_file.write("resolution=%dx%d\n" % (WVGA[0], WVGA[1]))
                        config_file.write("fullscreen=" + str(isFullscreen))
                        config_file.close()

                        background_image = pygame.image.load_extended("Sprites\\MenuBackground.png").convert()
                        background_image = pygame.transform.scale(background_image, WVGA)

                        locateButtons()

                if (pygame.mouse.get_pos()[0] >= resHD_button.x and pygame.mouse.get_pos()[0] <= resHD_button.x + resHD_button.width):
                    if (pygame.mouse.get_pos()[1] >= resHD_button.y and pygame.mouse.get_pos()[1] <= resHD_button.y + resHD_button.height):
                        displayWidth, displayHeight = HD
                        window = Window(displayWidth, displayHeight, Color().black)
                        display = window.newWindow(title, pygame.FULLSCREEN if isFullscreen else 0)

                        config_file = open("Config\\config.ini", 'w')
                        config_file.write("resolution=%dx%d\n" % (HD[0], HD[1]))
                        config_file.write("fullscreen=" + str(isFullscreen))
                        config_file.close()

                        background_image = pygame.image.load_extended("Sprites\\MenuBackground.png").convert()
                        background_image = pygame.transform.scale(background_image, HD)

                        locateButtons()

                if (pygame.mouse.get_pos()[0] >= resFULLHD_button.x and pygame.mouse.get_pos()[0] <= resFULLHD_button.x + resFULLHD_button.width):
                    if (pygame.mouse.get_pos()[1] >= resFULLHD_button.y and pygame.mouse.get_pos()[1] <= resFULLHD_button.y + resFULLHD_button.height):
                        displayWidth, displayHeight = FULLHD
                        window = Window(displayWidth, displayHeight, Color().black)
                        display = window.newWindow(title, pygame.FULLSCREEN if isFullscreen else 0)

                        config_file = open("Config\\config.ini", 'w')
                        config_file.write("resolution=%dx%d\n" % (FULLHD[0], FULLHD[1]))
                        config_file.write("fullscreen=" + str(isFullscreen))
                        config_file.close()

                        background_image = pygame.image.load_extended("Sprites\\MenuBackground.png").convert()
                        background_image = pygame.transform.scale(background_image, FULLHD)

                        locateButtons()

                if (pygame.mouse.get_pos()[0] >= resFullScreen_button.x and pygame.mouse.get_pos()[0] <= resFullScreen_button.x + resFullScreen_button.width):
                    if (pygame.mouse.get_pos()[1] >= resFullScreen_button.y and pygame.mouse.get_pos()[1] <= resFullScreen_button.y + resFullScreen_button.height):
                        window = Window(displayWidth, displayHeight, Color().black)

                        if (isFullscreen == False):
                            display = window.newWindow(title, pygame.FULLSCREEN)
                            text = "Fullscreen: on"
                            isFullscreen = True
                        else:
                            display = window.newWindow(title, 0)
                            text = "Fullscreen: off"
                            isFullscreen = False

                        resFullScreen_button = Button(button_image.copy(), text, myFont)

                        config_file = open("Config\\config.ini", 'w')
                        config_file.write("resolution=%dx%d\n" % (displayWidth, displayHeight))
                        config_file.write("fullscreen=" + str(isFullscreen))
                        config_file.close()

                        background_image = pygame.image.load_extended("Sprites\\MenuBackground.png").convert()
                        background_image = pygame.transform.scale(background_image, (displayWidth, displayHeight))

                        locateButtons()

            #Обработка событий выбора сохранений
            elif (choiseSaveMenu_active):

                if (pygame.mouse.get_pos()[0] >= saveOne_button.x and pygame.mouse.get_pos()[0] <= saveOne_button.x + saveOne_button.width):
                    if (pygame.mouse.get_pos()[1] >= saveOne_button.y and pygame.mouse.get_pos()[1] <= saveOne_button.y + saveOne_button.height):
                        pets = loadPets()
                        petNumber = 0

                        user = User("Saves\\save_1.xml", pets)

                        if (user.object == None):
                            choisePetMenu_active = True
                            choiseSaveMenu_active = False

                        else:
                            gameLoop(user, displayWidth, displayHeight, isFullscreen, title, myFont)

                if (pygame.mouse.get_pos()[0] >= saveTwo_button.x and pygame.mouse.get_pos()[0] <= saveTwo_button.x + saveTwo_button.width):
                    if (pygame.mouse.get_pos()[1] >= saveTwo_button.y and pygame.mouse.get_pos()[1] <= saveTwo_button.y + saveTwo_button.height):
                        pets = loadPets()
                        petNumber = 0

                        user = User("Saves\\save_2.xml", pets)

                        if (user.object == None):
                            choisePetMenu_active = True
                            choiseSaveMenu_active = False

                        else:
                            gameLoop(user, displayWidth, displayHeight, isFullscreen, title, myFont)

                if (pygame.mouse.get_pos()[0] >= saveThree_button.x and pygame.mouse.get_pos()[0] <= saveThree_button.x + saveThree_button.width):
                    if (pygame.mouse.get_pos()[1] >= saveThree_button.y and pygame.mouse.get_pos()[1] <= saveThree_button.y + saveThree_button.height):
                        pets = loadPets()
                        petNumber = 0

                        user = User("Saves\\save_3.xml", pets)

                        if (user.object == None):
                            choisePetMenu_active = True
                            choiseSaveMenu_active = False

                        else:
                            gameLoop(user, displayWidth, displayHeight, isFullscreen, title, myFont)

    #Отрисовка и обновление
    background = background_image.copy()
    background.blit(logo, ((displayWidth - logoWidth) // 2, (displayHeight - logoHeight) // 2 - 150))

    if (mainMenu_active):
        background.blit(exit_button.object, (exit_button.x, exit_button.y))
        exit_button.object.blit(exit_button.text, (exit_button.textX, exit_button.textY))

        background.blit(settings_button.object, (settings_button.x, settings_button.y))
        settings_button.object.blit(settings_button.text, (settings_button.textX, settings_button.textY))

        background.blit(play_button.object, (play_button.x, play_button.y))
        play_button.object.blit(play_button.text, (play_button.textX, play_button.textY))

    elif (resolutionSettings_active):
        background.blit(resWVGA_button.object, (resWVGA_button.x, resWVGA_button.y))
        resWVGA_button.object.blit(resWVGA_button.text, (resWVGA_button.textX, resWVGA_button.textY))

        background.blit(resHD_button.object, (resHD_button.x, resHD_button.y))
        resHD_button.object.blit(resHD_button.text, (resHD_button.textX, resHD_button.textY))

        background.blit(resFULLHD_button.object, (resFULLHD_button.x, resFULLHD_button.y))
        resFULLHD_button.object.blit(resFULLHD_button.text, (resFULLHD_button.textX, resFULLHD_button.textY))

        background.blit(resFullScreen_button.object, (resFullScreen_button.x, resFullScreen_button.y))
        resFullScreen_button.object.blit(resFullScreen_button.text, (resFullScreen_button.textX, resFullScreen_button.textY))

    elif (choiseSaveMenu_active):
        background.blit(saveOne_button.object, (saveOne_button.x, saveOne_button.y))
        saveOne_button.object.blit(saveOne_button.text, (saveOne_button.textX, saveOne_button.textY))

        background.blit(saveTwo_button.object, (saveTwo_button.x, saveTwo_button.y))
        saveTwo_button.object.blit(saveTwo_button.text, (saveTwo_button.textX, saveTwo_button.textY))

        background.blit(saveThree_button.object, (saveThree_button.x, saveThree_button.y))
        saveThree_button.object.blit(saveThree_button.text, (saveThree_button.textX, saveThree_button.textY))

    elif (choisePetMenu_active):
        background.blit(back_button.object, (back_button.x, back_button.y))
        back_button.object.blit(back_button.text, (back_button.textX, back_button.textY))

        background.blit(next_button.object, (next_button.x, next_button.y))
        next_button.object.blit(next_button.text, (next_button.textX, next_button.textY))

        background.blit(confirm_button.object, (confirm_button.x, confirm_button.y))
        confirm_button.object.blit(confirm_button.text, (confirm_button.textX, confirm_button.textX))

    display.blit(background, (0, 0))
    pygame.display.update()