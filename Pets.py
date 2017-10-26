import pygame
from GameObjects import GameObject

#Класс гуся из заставки :)
class Goose(GameObject):
    def __init__(self, images, posX, posY):
        GameObject.__init__(self)
        self.object = images
        self.x = posX
        self.y = posY
        self.width = images[0].get_width
        self.height = images[0].get_height
