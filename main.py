import pygame
import os
from Colors import Color
from Window import Window
from SplashScreen import SplashScreen
from  Button import Button

######################################

version = 0.5
title = "Tamagotchi PC ver %f" % version

######################################

#Video modes
WVGA = (854, 480,)
HD = (1280, 720,)
FULLHD = (1920, 1080,)

displayWidth = 0
displayHeight = 0
isFullscreen = False

#######################################

#Работа с config.ini файлом
config_file = None
configs = []

if (os.path.exists("Config\\config.ini") == False):
    config_file = open("Config\\config.ini", 'w')
    config_file.write("resolution=%dx%d\n" % (WVGA[0], WVGA[1]))
    config_file.write("fullscreen=False")
    config_file.close()
else:
    config_file = open("Config\\config.ini", "r+")
    for line in config_file:
        configs.append(line)
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

    if (cfgResX == WVGA[0] and cfgResY == WVGA[1]):
        config_file.write("resolution=%dx%d\n" % (cfgResX, cfgResY))
        displayWidth = cfgResX
        displayHeight = cfgResY
    elif (cfgResX == HD[0] and cfgResY == HD[1]):
        config_file.write("resolution=%dx%d\n" % (cfgResX, cfgResY))
        displayWidth = cfgResX
        displayHeight = cfgResY
    elif (cfgResX == FULLHD[0] and cfgResY == FULLHD[1]):
        config_file.write("resolution=%dx%d\n" % (cfgResX, cfgResY))
        displayWidth = cfgResX
        displayHeight = cfgResY
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

pygame.init()
pygame.font.init()

myFont = pygame.font.SysFont("Comic Sans Ms", 22)

#######################################

SplashScreen()

window = Window(displayWidth, displayHeight, Color().black)
display = window.newWindow(title, (pygame.FULLSCREEN if isFullscreen == True else 0))

background = pygame.image.load_extended("Sprites\\MenuBackground.png").convert()
background = pygame.transform.scale(background, (displayWidth, displayHeight))

logo = pygame.image.load_extended("Sprites\\Logo.png").convert_alpha()
logoWidth = logo.get_width()
logoHeight = logo.get_height()

#######################################

#Кнопки
buttonImage = pygame.image.load_extended("Sprites\\Button.png").convert_alpha()

mainMenu_active = True
resolutionSettings_active = False

#Settings кнопка

settings_button = Button(buttonImage.copy(), "Settings", myFont)
settings_button.x = (displayWidth - settings_button.width) // 2
settings_button.y = (displayHeight - settings_button.height) // 2 + 60

#####

resWVGA_button = Button(buttonImage.copy(), "854x480", myFont)
resWVGA_button.x = (displayWidth - resWVGA_button.width) // 2
resWVGA_button.y = (displayHeight - resWVGA_button.height) // 2

resHD_button = Button(buttonImage.copy(), "1280x720", myFont)
resHD_button.x = (displayWidth - resHD_button.width) // 2
resHD_button.y = (displayHeight - resHD_button.height) // 2 + 60

resFULLHD_button = Button(buttonImage.copy(), "1920x1080", myFont)
resFULLHD_button.x = (displayWidth - resFULLHD_button.width) // 2
resFULLHD_button.y = (displayHeight - resFULLHD_button.height) // 2 + 120

resFullScreen_button = Button(buttonImage.copy(), "Fullscreen: " + ("on" if isFullscreen else "off"), myFont)
resFullScreen_button.x = (displayWidth - resFullScreen_button.width) // 2
resFullScreen_button.y = (displayHeight - resFullScreen_button.height) // 2 + 180

#####

#exit кнопка

exit_button = Button(buttonImage.copy(), "Exit", myFont)
exit_button.x = (displayWidth - exit_button.width) // 2
exit_button.y = (displayHeight - exit_button.height) // 2 + 120


#Play кнопка

play_button = Button(buttonImage.copy(), "Play", myFont)
play_button.x = (displayWidth - play_button.width) // 2
play_button.y = (displayHeight - play_button.height) // 2
#######################################

while True:
    for e in pygame.event.get():
        if (e.type == pygame.QUIT):
            exit()

        if (e.type == pygame.KEYDOWN):
            if (e.key == pygame.K_ESCAPE):
                if (resolutionSettings_active):
                    background = pygame.image.load_extended("Sprites\\MenuBackground.png").convert()
                    background = pygame.transform.scale(background, (displayWidth, displayHeight))
                    resolutionSettings_active = False
                    mainMenu_active = True

        if (e.type == pygame.MOUSEBUTTONDOWN):
            if (mainMenu_active):

                if (pygame.mouse.get_pos()[0] >= exit_button.x and pygame.mouse.get_pos()[0] <= exit_button.x + exit_button.width):
                    if (pygame.mouse.get_pos()[1] >= exit_button.y and pygame.mouse.get_pos()[1] <= exit_button.y + exit_button.height):
                        exit()

                if (pygame.mouse.get_pos()[0] >= settings_button.x and pygame.mouse.get_pos()[0] <= settings_button.x + settings_button.width):
                    if (pygame.mouse.get_pos()[1] >= settings_button.y and pygame.mouse.get_pos()[1] <= settings_button.y + settings_button.height):
                        background = pygame.image.load_extended("Sprites\\MenuBackground.png").convert()
                        background = pygame.transform.scale(background, (displayWidth, displayHeight))
                        resolutionSettings_active = True
                        mainMenu_active = False

                if (pygame.mouse.get_pos()[0] >= play_button.x and pygame.mouse.get_pos()[0] <= play_button.x + play_button.width):
                    if (pygame.mouse.get_pos()[1] >= play_button.y and pygame.mouse.get_pos()[1] <= play_button.y + play_button.height):
                        pass

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

                        background = pygame.image.load_extended("Sprites\\MenuBackground.png").convert()
                        background = pygame.transform.scale(background, WVGA)

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

                if (pygame.mouse.get_pos()[0] >= resHD_button.x and pygame.mouse.get_pos()[0] <= resHD_button.x + resHD_button.width):
                    if (pygame.mouse.get_pos()[1] >= resHD_button.y and pygame.mouse.get_pos()[1] <= resHD_button.y + resHD_button.height):
                        displayWidth, displayHeight = HD
                        window = Window(displayWidth, displayHeight, Color().black)
                        display = window.newWindow(title, pygame.FULLSCREEN if isFullscreen else 0)

                        config_file = open("Config\\config.ini", 'w')
                        config_file.write("resolution=%dx%d\n" % (HD[0], HD[1]))
                        config_file.write("fullscreen=" + str(isFullscreen))
                        config_file.close()

                        background = pygame.image.load_extended("Sprites\\MenuBackground.png").convert()
                        background = pygame.transform.scale(background, HD)

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

                if (pygame.mouse.get_pos()[0] >= resFULLHD_button.x and pygame.mouse.get_pos()[0] <= resFULLHD_button.x + resFULLHD_button.width):
                    if (pygame.mouse.get_pos()[1] >= resFULLHD_button.y and pygame.mouse.get_pos()[1] <= resFULLHD_button.y + resFULLHD_button.height):
                        displayWidth, displayHeight = FULLHD
                        window = Window(displayWidth, displayHeight, Color().black)
                        display = window.newWindow(title, pygame.FULLSCREEN if isFullscreen else 0)

                        config_file = open("Config\\config.ini", 'w')
                        config_file.write("resolution=%dx%d\n" % (FULLHD[0], FULLHD[1]))
                        config_file.write("fullscreen=" + str(isFullscreen))
                        config_file.close()

                        background = pygame.image.load_extended("Sprites\\MenuBackground.png").convert()
                        background = pygame.transform.scale(background, FULLHD)

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

                if (pygame.mouse.get_pos()[0] >= resFullScreen_button.x and pygame.mouse.get_pos()[0] <= resFullScreen_button.x + resFullScreen_button.width):
                    if (pygame.mouse.get_pos()[1] >= resFullScreen_button.y and pygame.mouse.get_pos()[1] <= resFullScreen_button.y + resFullScreen_button.height):
                        window = Window(displayWidth, displayHeight, Color().black)

                        if (isFullscreen == False):
                            display = window.newWindow(title, pygame.FULLSCREEN)
                            resFullScreen_button.setText("Fullscreen: " + "on", myFont)
                            isFullscreen = True
                        else:
                            display = window.newWindow(title, 0)
                            resFullScreen_button.setText("Fullscreen: " + "off", myFont)
                            isFullscreen = False

                        config_file = open("Config\\config.ini", 'w')
                        config_file.write("resolution=%dx%d\n" % (displayWidth, displayHeight))
                        config_file.write("fullscreen=" + str(isFullscreen))
                        config_file.close()

                        background = pygame.image.load_extended("Sprites\\MenuBackground.png").convert()
                        background = pygame.transform.scale(background, (displayWidth, displayHeight))
                        resFullScreen_button.object.blit(buttonImage, (0, 0))

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

    display.blit(background, (0, 0))
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

    pygame.display.update()
