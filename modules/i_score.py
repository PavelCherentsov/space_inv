from PyQt5.QtWidgets import QGraphicsTextItem
from PyQt5.QtGui import QColor, QFont, QTextDocument


class Score(QGraphicsTextItem):
    def __init__(self, game):
        super().__init__()
        self.count = 0
        self.size = 100
        self.setPlainText("SCORE: {}".format(self.count))
        self.setFont(QFont("Space Invaders", self.size))
        self.setDefaultTextColor(QColor(255, 255, 255))
        self.game = game
        self.doc = self.document()
        self.window_width = self.game.window_width
        self.window_height = self.game.window_height
        self.set_size()
        self.x = 100
        self.y = 100 - self.document().size().height()
        self.setPos(self.x, self.y)

    def set_size(self):
        defaul_size = self.window_width / 7
        while self.doc.size().width() > defaul_size:
            self.size -= 1
            self.setFont(QFont("Space Invaders", self.size))

    def add_count(self, count):
        self.count += count
        self.setPlainText("SCORE: {}".format(self.count))
        if self.game.player.player.killings == self.game.monsters.size*3:
            self.game.Win("YOU WIN")
