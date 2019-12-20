from PyQt5.QtWidgets import QGraphicsItemGroup
from PyQt5.QtGui import QPixmap
from modules.i_barrier import BarrierQt


class Barriers(QGraphicsItemGroup):
    def __init__(self, game):
        super().__init__()

        self.window_width = game.window_width
        self.window_height = game.window_height

        self.image1 = QPixmap("./images/barrier1.png")

        self.width = self.image1.width()
        self.height = self.image1.height()

        self.barriers_list = []

        k = self.set_size() + 1
        start_x = self.window_width / k - self.width * 5 + self.width / 2

        for j in range(k-1):
            for i in range(30):
                self.barriers_list.append(
                    BarrierQt(game,
                              start_x + j * self.window_width / k
                              + 21 * ((i % 10) - 1),
                              2 * game.height() / 3 - 21 * 1.5
                              + 21 * (i // 10)))
                self.addToGroup(self.barriers_list[i + 30 * j])

    def set_size(self):
        return self.window_width // (self.width*20)
