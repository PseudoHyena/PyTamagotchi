import pygame
from Colors import Color
from Window import Window
from SplashScreen import SplashScreen

#######################################
version = 0.1
displayWidth = 800
displayHeight = 600
title = "Tamagotchi PC ver %f" % version

#######################################

pygame.init()

SplashScreen()

window = Window(displayWidth, displayHeight, Color().black)
display = window.newWindow(title)

while True:
    for e in pygame.event.get():
        if (e.type == pygame.QUIT):
            raise SystemExit

        if (e.type == pygame.VIDEORESIZE):
            displayWidth, displayHeight = e.size
            window = Window(displayWidth, displayHeight, Color().black)
            display = window.newWindow(title)

    pygame.display.update()