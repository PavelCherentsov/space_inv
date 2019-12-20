from PyQt5.QtWidgets import QGraphicsView, QApplication
from PyQt5.QtGui import QIcon, QFontDatabase
from PyQt5.QtMultimedia import QSound
from PyQt5.QtCore import QCoreApplication
import sys
from modules.i_game import Game
from modules.i_start_window import StartWindow


class MainWindow(QGraphicsView):
    def __init__(self, width, height):
        super().__init__()

        self.window_width = width
        self.window_height = height

        self.setWindowTitle("Space invaders")
        self.resize(self.window_width, self.window_height)

        self.move(200, 0)

        self.setWindowIcon(QIcon("./images/ship.png"))
        self.setFixedSize(width, height)

        QFontDatabase.addApplicationFont('./fonts/space_invaders.ttf')

        self.game = StartWindow(self)
        self.setScene(self.game)

        self.show()

    def restart(self, start=True):
        self.game.clear()
        if start:
            sound_restart()
        self.game = Game(self)
        self.setScene(self.game)


def main():
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    rect = screen.availableGeometry()
    print(rect.width() - 400, rect.height())
    MainWindow(rect.width() - 400, rect.height())
    sys.exit(app.exec_())


def sound_restart():
    """
    sound.stop()
    sound.play()
    """


if __name__ == '__main__':
    if len(sys.argv) > 1:
            print('\nДля запуска приложения "Space Invaders" ')
            print('введите: `py space_inv.py` ')
    else:
        sound = QSound('./sound/back.wav')
        sound.setLoops(QSound.Infinite)
        #sound.play()
        main()
