from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QGraphicsPixmapItem, QGraphicsItem
from PyQt5.QtGui import QPixmap
from modules.player_shots import ShotPlayer


class ShotPlayerQt(QGraphicsPixmapItem):
    def __init__(self, player, game, angle):
        self.player = player
        self.game = game
        self.image = QPixmap("./images/laser.png")
        super().__init__(self.image)
        self.shot = ShotPlayer(self.player.center_x, self.player.center_y,
                               angle,
                               self.image.width(), self.image.height(),
                               self.game.window_width, self.game.window_height)
        self.setPos(self.shot.x, self.shot.y)
        self.setFlag(QGraphicsItem.ItemIsFocusable)

        self.timer = QTimer()
        self.timer.timeout.connect(self.on_timeout)
        self.timer.start(10)
        self.i = 0

    def CheckMonster(self):
        for monster in self.game.monsters.monsters.list:
            if self.collidesWithItem(monster) and not monster.monster.is_dead:
                monster.damage()
                if monster.monster.life == 0:
                    self.game.score.add_count(monster.monster.count_for_kill)
                    self.player.killings += 1
                    monster.monster.is_dead = True
                    monster.hide()
                    if self.player.killings == self.game.monsters.size*3:
                        self.game.Win("YOU WIN")
                self.RemoveProjectile()

    def CheckBarrier(self):
        for barrier in self.game.barriers.barriers_list:
            if self.collidesWithItem(barrier):
                if not barrier.barrier.is_dead:
                    self.RemoveProjectile()
                    barrier.barrier_damage()

    def RemoveProjectile(self):
        self.player.shots += 1
        self.shot.is_dead = True
        self.setPos(0, 0)
        self.hide()

    def Move(self):
        self.shot.move()
        self.setPos(self.shot.x, self.shot.y)

    def on_timeout(self):
        if not self.shot.is_dead:
            self.CheckBarrier()
            self.CheckMonster()
            if self.shot.check_window():
                self.RemoveProjectile()
            self.Move()
