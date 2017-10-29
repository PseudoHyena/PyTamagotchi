import pygame
from GameObjects import GameObject

class Button(GameObject):
    def __init__(self, image, text, font):
        GameObject.__init__(self)
        self._image = image
        self._object = self._image
        self._textObj = font.render(text, False, (0, 0, 0)).convert()
        self.x = 0
        self.y = 0
        self._width = image.get_width()
        self._height = image.get_height()
        self.textX = (self._width - self._textObj.get_width()) // 2
        self.textY = (self._height - self._textObj.get_height()) // 2

    @property
    def text(self):
        return self._textObj

    def setText(self, string, font):
        self._textObj = font.render(string, False, (0, 0, 0)).convert()



