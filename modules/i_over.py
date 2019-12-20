from PyQt5.QtWidgets import QGraphicsTextItem
from PyQt5.QtGui import QFont, QColor


class End(QGraphicsTextItem):
    def __init__(self, game, message):
        super().__init__(message)
        self.game = game
        self.size = 200
        self.setFont(QFont("Space Invaders", self.size))
        self.setDefaultTextColor(QColor(250, 10, 50))
        self.window_width = self.game.window_width
        self.window_height = self.game.window_height
        self.doc = self.document()
        self.set_size()
        self.x = self.window_width / 2 - self.doc.size().width() / 2
        self.y = self.window_height / 2 - self.doc.size().height() / 2
        self.setPos(self.x, self.y)

    def set_size(self):
        defaul_size = self.window_width - 200
        while self.doc.size().width() > defaul_size:
            self.size -= 1
            self.setFont(QFont("Space Invaders", self.size))
