#Коллекция цветов
class Color:
    def __init__(self):
        self._white = (255, 255, 255,)
        self._black = (0, 0, 0,)
        self._red = (255, 0, 0,)
        self._green = (0, 255, 0,)
        self._blue = (0, 0, 255,)
        self._yellow = (255, 255, 0,)
        self._grey = (190, 190, 190)
        self._lightGrey = (211, 211, 211,)

    @property
    def white(self):
        return self._white

    @property
    def black(self):
        return self._black

    @property
    def red(self):
        return self._red

    @property
    def green(self):
        return self._green

    @property
    def blue(self):
        return self._blue

    @property
    def yellow(self):
        return self._yellow

    @property
    def grey(self):
        return self._grey

    @property
    def lightGrey(self):
        return self._lightGrey






