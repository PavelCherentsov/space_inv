from PyQt5.QtWidgets import QGraphicsTextItem
from PyQt5.QtGui import QColor, QFont


class Head(QGraphicsTextItem):
    def __init__(self, game):
        super().__init__("SPACE INVADERS")

        self.size = 100
        self.setFont(QFont("Space Invaders", self.size))
        self.setDefaultTextColor(QColor(0, 255, 247))

        self.game = game

        self.doc = self.document()

        self.window_width = self.game.window_width
        self.window_height = self.game.window_height

        self.set_size()

        self.x = self.window_width / 2 - self.doc.size().width() / 2
        self.y = 100 - self.doc.size().height()

        self.setPos(self.x, self.y)

    def set_size(self):
        default_size = 3 * self.window_width / 7
        while self.doc.size().width() > default_size \
                or self.doc.size().height() > 100:
            self.size -= 1
            self.setFont(QFont("Space Invaders", self.size))
