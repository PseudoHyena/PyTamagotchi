import pygame
from Colors import Color
from Window import Window
from SplashScreen import SplashScreen
from  Button import Button

######################################

pygame.init()
pygame.font.init()

myFont = pygame.font.SysFont("Comic Sans Ms", 22)

#######################################

version = 0.1
displayWidth = 854
displayHeight = 480
title = "Tamagotchi PC ver %f" % version

#######################################

SplashScreen()

window = Window(displayWidth, displayHeight, Color().black)
display = window.newWindow(title, pygame.RESIZABLE)
background = pygame.image.load_extended("Sprites\\MenuBackground.png").convert()
logo = pygame.image.load_extended("Sprites\\Logo.png").convert_alpha()
logoWidth = logo.get_width()
logoHeight = logo.get_height()

#######################################

#Кнопки
buttonImage = pygame.image.load_extended("Sprites\\Button.png").convert_alpha()

#exit кнопка

exit_button = Button(buttonImage.copy(), "Exit", myFont, exit)
exit_button.x = (displayWidth - exit_button.width) // 2
exit_button.y = (displayHeight - exit_button.height) // 2 + 200

#Settings кнопка

settings_button = Button(buttonImage.copy(), "Settings", myFont, print)
settings_button.x = (displayWidth - settings_button.width) // 2
settings_button.y = (displayHeight - settings_button.height) // 2 + 140

#Play кнопка

play_button = Button(buttonImage.copy(), "Play", myFont, print)
play_button.x = (displayWidth - play_button.width) // 2
play_button.y = (displayHeight - play_button.height) // 2 + 80

#######################################

while True:
    for e in pygame.event.get():
        if (e.type == pygame.QUIT):
            raise SystemExit

        if (e.type == pygame.MOUSEBUTTONDOWN):
            if (pygame.mouse.get_pos()[0] > exit_button.x and pygame.mouse.get_pos()[0] < exit_button.x + exit_button.width):
                if (pygame.mouse.get_pos()[1] > exit_button.y and pygame.mouse.get_pos()[1] < exit_button.y + exit_button.height):
                    exit_button.func()

        if (e.type == pygame.VIDEORESIZE):
            displayWidth, displayHeight = e.size
            window = Window(displayWidth, displayHeight, Color().black)
            display = window.newWindow(title, pygame.RESIZABLE)

    display.blit(background, (0, 0))
    background.blit(logo, ((displayWidth - logoWidth) // 2, (displayHeight - logoHeight) // 2 - 150))

    background.blit(exit_button.object, (exit_button.x, exit_button.y))
    exit_button.object.blit(exit_button.text, (exit_button.textX, exit_button.textY))

    background.blit(settings_button.object, (settings_button.x, settings_button.y))
    settings_button.object.blit(settings_button.text, (settings_button.textX, settings_button.textY))

    background.blit(play_button.object, (play_button.x, play_button.y))
    play_button.object.blit(play_button.text, (play_button.textX, play_button.textY))

    pygame.display.update()