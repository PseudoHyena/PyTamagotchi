import pygame
from Window import Window
from Colors import Color
from Pets import Pets
from Button import Button

def gameLoop(displayWidth, displayHeight, isFullscreen, title):
    images = []

    """images.append(pygame.image.load_extended("Sprites\\Pets\\Blue Bird.png").convert_alpha)
    images.append(pygame.image.load_extended("Sprites\\Pets\\Chicken.png").convert_alpha)
    images.append(pygame.image.load_extended("Sprites\\Pets\\Eagle.png").convert_alpha)
    images.append(pygame.image.load_extended("Sprites\\Pets\\Owl.png").convert_alpha)
    images.append(pygame.image.load_extended("Sprites\\Pets\\Yellow Bird.png").convert_alpha)"""

    window = Window(displayWidth, displayHeight, Color().black)
    display = window.newWindow(title, pygame.FULLSCREEN if isFullscreen else 0)
    background = pygame.image.load_extended("Sprites\\Room.png").convert()
    background = pygame.transform.scale(background, (displayWidth, displayHeight))


    #pet = Pets(images)
    #pet.x = (displayWidth - pet.width) // 2
    #pet.y = (displayHeight - pet.height) // 2

    while True:
        for e in pygame.event.get():
            if (e.type == pygame.QUIT):
                exit()

        display.blit(background, (0, 0))
        #background.blit(pet.object, (pet.x, pet.y))
        pygame.display.update()
