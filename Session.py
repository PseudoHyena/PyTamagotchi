import pygame
from Window import Window
from Colors import Color
from Pets import Pet
from Button import Button

def gameLoop(displayWidth, displayHeight, isFullscreen, title):
    images = []

    petsSizeX = int(displayWidth / 7.112962963)
    petsSizeY = int(displayHeight / 4)

    images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Pets\\BlueBird.png").convert_alpha(), (petsSizeX, petsSizeY)))
    images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Pets\\Chicken.png").convert_alpha(), (petsSizeX, petsSizeY)))
    images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Pets\\Eagle.png").convert_alpha(), (petsSizeX, petsSizeY)))
    images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Pets\\Owl.png").convert_alpha(), (petsSizeX, petsSizeY)))
    images.append(pygame.transform.scale(pygame.image.load_extended("Sprites\\Pets\\YellowBird.png").convert_alpha(), (petsSizeX, petsSizeY)))

    window = Window(displayWidth, displayHeight, Color().black)
    display = window.newWindow(title, pygame.FULLSCREEN if isFullscreen else 0)
    background = pygame.image.load_extended("Sprites\\Room.png").convert()
    background = pygame.transform.scale(background, (displayWidth, displayHeight))


    pet = Pet(images[0])
    pet.x = (displayWidth - pet.width) // 2
    pet.y = (displayHeight - pet.height) // 2

    while True:
        for e in pygame.event.get():
            if (e.type == pygame.QUIT):
                exit()

        display.blit(background, (0, 0))
        background.blit(pet.object, (pet.x, pet.y))
        pygame.display.update()
