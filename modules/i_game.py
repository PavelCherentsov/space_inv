from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtMultimedia import QSound
from modules.i_player import PlayerQt
from modules.i_monsters import MonstersQt
from modules.i_score import Score
from modules.i_life import Life
from modules.i_headline import Head
from modules.i_over import End
from modules.barriers import Barriers


class Game(QGraphicsScene):
    def __init__(self, window):
        super().__init__()

        self.window = window

        self.window_width = window.window_width
        self.window_height = self.window.window_height

        self.setSceneRect(0, 0, self.window_width-5, self.window_height-40)

        self.back = QPixmap("./images/background1.jpg")

        self.qp = QPainter(self.back)
        self.qp.fillRect(0, 0, 100, self.window_height, QColor(0, 0, 0))
        self.qp.fillRect(0, 0, self.window_width, 100, QColor(0, 0, 0))
        self.qp.fillRect(self.window_width - 100, 0, 100, self.window_height,
                         QColor(0, 0, 0))
        self.qp.fillRect(0, self.window_height - 100, self.window.window_width,
                         100, QColor(0, 0, 0))
        self.qp.end()

        self.addPixmap(self.back)

        self.player = PlayerQt(self)
        self.addItem(self.player)

        self.monsters = MonstersQt(self)
        self.addItem(self.monsters)

        self.barriers = Barriers(self)
        self.addItem(self.barriers)

        self.head = Head(self)
        self.addItem(self.head)

        self.score = Score(self)
        self.addItem(self.score)

        self.life = Life(self, self.score.size)
        self.addItem(self.life)

    def keyPressEvent(self, e):
        key = e.key()
        if key == Qt.Key_R or key == 1050:
            self.window.restart()

        self.player.keyPressEvent(e)

    def Win(self, message):
        self.addItem(End(self, message))
