import pygame

#Класс окна для его инициализации и обновления в случае измененеия размера окна
class Window:
    def __init__(self, width, height, color):
        self._width = width
        self._height = height
        self._color = color
        self._display = None

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def newWindow(self, title):
        self._display = pygame.display.set_mode((self._width, self._height), pygame.RESIZABLE)
        self._display.fill(self._color)
        pygame.display.set_caption(title)
        pygame.display.flip()
        return self._display
