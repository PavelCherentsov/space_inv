from PyQt5.QtWidgets import QGraphicsTextItem
from PyQt5.QtGui import QFont, QColor


class Life(QGraphicsTextItem):
    def __init__(self, game, size):
        super().__init__()
        self.game = game
        self.size = size
        self.setPlainText("LIFE: {}".format(self.game.player.player.life))
        self.setFont(QFont("Space Invaders", self.size))
        self.setDefaultTextColor(QColor(255, 255, 255))
        self.doc = self.document()
        self.window_width = self.game.window_width
        self.window_height = self.game.window_height
        self.x = self.window_width - 100 - self.document().size().width()
        self.y = 100 - self.document().size().height()
        self.setPos(self.x, self.y)

    def update_life(self):
        self.setPlainText("LIFE: {}".format(self.game.player.player.life))
        if self.game.player.player.life == 0:
            self.game.Win("GAME OVER")
