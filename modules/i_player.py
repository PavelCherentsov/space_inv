from modules.i_player_shots import ShotPlayerQt
from modules.vector import Vector
from modules.player import Player, Constants
from PyQt5.QtWidgets import QGraphicsPixmapItem, QGraphicsItem
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QTransform
from math import fabs


class PlayerQt(QGraphicsPixmapItem):
    def __init__(self, game):
        self.image = QPixmap("./images/ship.png")
        super().__init__(self.image)
        self.game = game
        self.player = \
            Player(self.game.window_width / 2,
                   self.game.window_height - 100 - self.image.height() / 2,
                   self.image.width(), self.image.height(),
                   self.game.window_width, self.game.window_height)
        self.setPos(self.player.x, self.player.y)
        self.setFlag(QGraphicsItem.ItemIsFocusable)
        self.delay = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.on_timeout)
        self.timer.start(20)

    def on_timeout(self):
        if not self.player.is_dead:
            a = self.player.get_acceleration()
            self.player.set_movement(a)
            r = fabs(self.player.f) <= fabs(self.player.f_old)
            if self.delay % 10 == 0 and r:
                self.player.f = self.player.f_old = 0
            self.player.f_old = self.player.f
            self.delay += 1
            self.player.check_inf(a)
            self.setPos(self.player.x, self.player.y)
            self.Rotate()

    def Kill(self):
        self.player.death()
        self.Rotate()
        self.game.life.update_life()
        if self.player.life == 0:
            self.player.set_x(-100)
        self.setPos(self.player.x, self.player.y)

    def Shot(self):
        if self.player.shot():
            p = ShotPlayerQt(self.player, self.game, self.player.angle)
            self.game.addItem(p)

    def Rotate(self):
        self.player.get_angle()
        t = QTransform().rotate(self.player.angle)
        self.setPixmap(QPixmap("./images/ship.png").transformed(t))

    def keyPressEvent(self, e):
        key = e.key()
        if key == Qt.Key_Left:
            self.player.f += self.player.constants.F
            self.Rotate()
        elif key == Qt.Key_Right:
            self.player.f -= self.player.constants.F
            self.Rotate()
        elif key == Qt.Key_Space:
            self.Shot()
