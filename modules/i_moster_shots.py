from PyQt5.QtWidgets import QGraphicsPixmapItem, QGraphicsItem
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from modules.monster_shots import ShotMonster


class ProjectileMonster(QGraphicsPixmapItem):
    def __init__(self, monster, game):
        self.image = QPixmap("./images/enemylaser.png")
        super().__init__(self.image)
        self.monster = monster
        self.game = game
        self.shot = \
            ShotMonster(monster.monster.x + monster.image1.width() / 2,
                        monster.monster.y + monster.image1.height() / 2,
                        monster.image1.width(),
                        monster.image1.height(),
                        game.window_width,
                        game.window_height)
        self.setPos(self.shot.x, self.shot.y)
        self.setFlag(QGraphicsItem.ItemIsFocusable)

        self.timer = QTimer()
        self.timer.timeout.connect(self.on_timeout)
        self.timer.start(10)

    def check_player(self):
        if self.collidesWithItem(self.game.player):
            self.game.player.Kill()
            self.remove_monster_shot()

    def check_barrier(self):
        if not self.shot.is_dead:
            for barrier in self.game.barriers.barriers_list:
                if not barrier.barrier.is_dead:
                    if self.collidesWithItem(barrier):
                        self.remove_monster_shot()
                        barrier.barrier_damage()

    def remove_monster_shot(self):
        self.shot.is_dead = True
        self.setPos(-100, -100)
        self.hide()

    def move(self):
        self.shot.y += 5
        self.moveBy(0, 5)

    def on_timeout(self):
        if not self.shot.is_dead:
            self.check_player()
            self.check_barrier()
            if self.shot.y > self.game.window_height-100:
                self.remove_monster_shot()
            self.move()
