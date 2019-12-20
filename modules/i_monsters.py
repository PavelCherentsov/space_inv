from modules.i_moster_shots import ProjectileMonster
from modules.i_monster import MonsterQt
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QGraphicsItemGroup
from PyQt5.QtGui import QPixmap
from modules.monsters import Monsters


class MonstersQt(QGraphicsItemGroup):
    def __init__(self, game):
        super().__init__()
        self.monsters = Monsters(game.window_width, game.window_height)
        self.width = QPixmap("./images/enemy1_1.png").width()
        self.game = game
        self.size = self.set_size()
        for i in range(self.size):
            self.monsters.list.append(MonsterQt(game,
                                                100 + 30 * (2 * i + 1),
                                                100 + self.width / 2,
                                                "./images/enemy1_1.png",
                                                "./images/enemy1_2.png",
                                                2,
                                                "./images/enemy1_1_1hp.png",
                                                "./images/enemy1_2_1hp.png"))
            self.addToGroup(self.monsters.list[i])
        for i in range(self.size):
            self.monsters.list.append(MonsterQt(game,
                                                100 + 30 * (2 * i + 1),
                                                170 + self.width / 2,
                                                "./images/enemy2_1.png",
                                                "./images/enemy2_2.png",
                                                1,
                                                "./images/enemy2_1.png",
                                                "./images/enemy2_2.png"))
            self.addToGroup(self.monsters.list[i + self.size])
        for i in range(self.size):
            self.monsters.list.append(MonsterQt(game,
                                                100 + 30 * (2 * i + 1),
                                                230 + self.width / 2,
                                                "./images/enemy3_1.png",
                                                "./images/enemy3_2.png",
                                                1,
                                                "./images/enemy3_1.png",
                                                "./images/enemy3_2.png"))
            self.addToGroup(self.monsters.list[i + 2*self.size])
        self.game = game

        self.monsters.list.reverse()

        self.timer = QTimer()
        self.timer.timeout.connect(self.on_timeout)
        self.timer.start(500)

    def set_size(self):
        return (self.game.window_width // 2 - 200) // self.width

    def move(self):
        self.monsters.move()
        for monster in self.monsters.list:
            monster.move()

    def shot(self, monster):
        projectile = ProjectileMonster(monster, self.game)
        self.game.addItem(projectile)

    def on_timeout(self):
        if not self.game.player.player.is_dead:
            monster = self.monsters.find_player(self.game.player.player)
            if monster is not None:
                self.shot(monster)
        self.move()
