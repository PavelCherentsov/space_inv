from PyQt5.QtWidgets import QGraphicsScene, QGraphicsTextItem
from PyQt5.QtGui import QPixmap, QPainter, QColor, QFont
from PyQt5.QtCore import Qt


class StartWindow(QGraphicsScene):
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

        self.size = 200
        self.head = QGraphicsTextItem("Space Invaders")
        self.head.setFont(QFont("Space Invaders", self.size))
        self.set_size(self.window_width - 400)
        indent = self.head.document().size().width() / 2
        self.x = self.window_width / 2 - indent
        self.y = self.window_height / 4
        self.head.setDefaultTextColor(QColor(255, 255, 255))
        self.head.setPos(self.x, self.y)

        self.addItem(self.head)

        self.size = 200
        self.y += self.head.document().size().height()
        self.head = QGraphicsTextItem("Press any key to start the game")
        self.head.setFont(QFont("Space Invaders", self.size))
        self.set_size(self.window_width / 2)
        indent = self.head.document().size().width() / 2
        self.x = self.window_width / 2 - indent
        self.head.setDefaultTextColor(QColor(255, 255, 255))
        self.head.setPos(self.x, self.y)

        self.addItem(self.head)

        self.size = 200
        self.y += self.head.document().size().height()
        self.head = QGraphicsTextItem("\nLeft / Right Arrows - Move Player")
        self.head.setFont(QFont("Space Invaders", self.size))
        self.set_size(self.window_width / 3)
        indent = self.head.document().size().width() / 2
        self.x = self.window_width / 2 - indent
        self.head.setDefaultTextColor(QColor(255, 255, 255))
        self.head.setPos(self.x, self.y)

        self.addItem(self.head)

        self.y += self.head.document().size().height()
        self.head = QGraphicsTextItem("Space - Shoot")
        self.head.setFont(QFont("Space Invaders", self.size))
        self.doc = self.head.document()
        self.set_size(self.window_width / 3)
        indent = self.head.document().size().width() / 2
        self.x = self.window_width / 2 - indent
        self.head.setDefaultTextColor(QColor(255, 255, 255))
        self.head.setPos(self.x, self.y)

        self.addItem(self.head)

        self.y += self.head.document().size().height()
        self.head = QGraphicsTextItem("R - Restart game")
        self.head.setFont(QFont("Space Invaders", self.size))
        self.doc = self.head.document()
        indent = self.head.document().size().width() / 2
        self.set_size(self.window_width / 3)
        self.x = self.window_width / 2 - indent
        self.head.setDefaultTextColor(QColor(255, 255, 255))
        self.head.setPos(self.x, self.y)

        self.addItem(self.head)

    def set_size(self, default):
        default_size = default
        while self.head.document().size().width() > default_size:
            self.size -= 1
            self.head.setFont(QFont("Space Invaders", self.size))

    def keyPressEvent(self, e):
            self.window.restart(False)
