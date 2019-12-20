from PyQt5.QtWidgets import QGraphicsPixmapItem, QGraphicsItem
from PyQt5.QtGui import QPixmap
from modules.monster import Monster


class MonsterQt(QGraphicsPixmapItem):
    def __init__(self, game, x, y, image1, image2,
                 life, image_damage1, image_damage2):

        super().__init__(QPixmap(image1))

        self.image1 = QPixmap(image1)
        self.image2 = QPixmap(image2)

        self.image_damage1 = QPixmap(image_damage1)
        self.image_damage2 = QPixmap(image_damage2)

        self.monster = Monster(x, y,
                               self.image1.width(), self.image1.height(),
                               life,
                               game.window_width, game.window_height)

        self.setPos(self.monster.x, self.monster.y)

        self.setFlag(QGraphicsItem.ItemIsFocusable)

    def go_down(self):
        self.moveBy(0, 50)
        self.monster.move_down()

    def damage(self):
        if not self.monster.is_dead:
            self.monster.damage()
            self.image1 = self.image_damage1
            self.image2 = self.image_damage2
            if self.monster.life == 0:
                self.hide()

    def move(self):
        self.setPixmap(self.image2)
        self.image1, self.image2 = self.image2, self.image1
        if self.monster.go_right:
            self.moveBy(15, 0)
            self.monster.move_right()
        else:
            self.moveBy(-15, 0)
            self.monster.move_left()
