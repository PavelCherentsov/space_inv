from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from random import randint
from modules.barrier import Barrier


class BarrierQt(QGraphicsPixmapItem):
    def __init__(self, game, x, y):

        self.image1 = QPixmap("./images/barrier1.png")
        self.image2 = QPixmap("./images/barrier2.png")
        self.image3 = QPixmap("./images/barrier3.png")

        super().__init__(self.image1)

        self.game = game

        self.barrier = Barrier(x,
                               y,
                               self.image1.width(),
                               self.image1.height(),
                               self.game.window_width,
                               self.game.window_height)

        self.setPos(self.barrier.x, self.barrier.y)

        self.timer = QTimer()
        self.timer.timeout.connect(self.on_timeout)
        self.timer.start(2000)

    def barrier_damage(self):
        self.barrier.barrier_damage()
        if self.barrier.life == 2:
            self.setPixmap(self.image2)
        elif self.barrier.life == 1:
            self.setPixmap(self.image3)
        else:
            self.hide()

    def barrier_update(self):
        if self.barrier.life == 2:
            self.setPixmap(self.image1)
        elif self.barrier.life == 1:
            self.setPixmap(self.image2)

    def on_timeout(self):
        if self.barrier.chance_update():
            self.barrier_update()
