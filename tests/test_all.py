import unittest
from math import inf, fabs
import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))

from modules.player import Player
from modules.vector import Vector
from modules.player_shots import ShotPlayer
from modules.monster import Monster
from modules.barrier import Barrier
from modules.monster_shots import ShotMonster


class GameTest(unittest.TestCase):

    def test_PositionPlayer(self):
        window_width = 1000
        window_height = 1000
        player = Player(window_width / 2, window_height - 100 - 20 / 2, 20, 20,
                        window_width, window_height)
        self.assertEqual(player.angle, 0)
        self.assertEqual(player.life, 10)
        self.assertEqual(player.killings, 0)

    def test_PositionPlayerMoveLeft(self):
        window_width = 1000
        window_height = 1000
        player = Player(window_width / 2, window_height - 100 - 20 / 2, 20, 20,
                        window_width, window_height)
        for i in range(10000):
            player.move_left()
        self.assertEqual(player.center_x, 100 + player.width / 2)
        self.assertEqual(player.center_y, player.ellipse(player.center_x))
        self.assertEqual(inf, player.ellipse_diff(player.center_x))

    def test_PositionPlayerMoveRight(self):
        window_width = 1000
        window_height = 1000
        player = Player(window_width / 2, window_height - 100 - 20 / 2, 20, 20,
                        window_width, window_height)
        for i in range(10000):
            player.move_right()
        self.assertEqual(player.center_x,
                         window_width - 100 + player.width / 2)
        self.assertEqual(player.center_y, player.ellipse(player.center_x))
        self.assertEqual(-inf, player.ellipse_diff(player.center_x))

    def test_StatePlayerDeath(self):
        window_width = 1000
        window_height = 1000
        player = Player(window_width / 2, window_height - 100 - 20 / 2, 20, 20,
                        window_width, window_height)
        life = player.life
        player.death()
        self.assertEqual(player.life, life - 1)
        player.death()
        self.assertEqual(player.life, life - 2)
        player.death()
        self.assertEqual(player.life, life - 3)

    def test_StatePlayerA(self):
        window_width = 1000
        window_height = 1000
        player = Player(window_width / 2, window_height - 100 - 20 / 2, 20, 20,
                        window_width, window_height)
        a = player.get_acceleration()
        self.assertEqual(a.y, 0)
        self.assertLessEqual(fabs(a.x-0.1), 1)

    def test_StatePlayerSet(self):
        window_width = 1000
        window_height = 1000
        player = Player(window_width / 2, window_height - 100 - 20 / 2, 20, 20,
                        window_width, window_height)
        player.set_x(500)
        self.assertEqual(player.x, 500)
        self.assertEqual(player.center_x, 500 + player.width / 2)
        player.set_center_x(500)
        self.assertEqual(player.center_x, 500)
        self.assertEqual(player.x, 500 - player.width / 2)
        player.set_y(500)
        self.assertEqual(player.y, 500)
        self.assertEqual(player.center_y, 500 + player.height / 2)
        player.set_center_y(500)
        self.assertEqual(player.center_y, 500)
        self.assertEqual(player.y, 500 - player.height / 2)
        player.convert_to_left(500, 500)
        self.assertEqual(player.x, 500 - player.width / 2)
        self.assertEqual(player.y, 500 - player.height / 2)
        player.convert_to_center(500, 500)
        self.assertEqual(player.center_x, 500)
        self.assertEqual(player.center_y, 500)

    def test_StatePlayerDiffEllipse(self):
        window_width = 1000
        window_height = 1000
        player = Player(window_width / 2, window_height - 100 - 20 / 2, 20, 20,
                        window_width, window_height)
        player.set_center_x(500)
        player.set_center_y(player.ellipse(player.center_x))
        player.get_angle()
        self.assertEqual(player.angle, player.ellipse_diff(player.center_x))

    def test_StatePlayerDiffEllipse(self):
        window_width = 1000
        window_height = 1000
        player = Player(window_width / 2, window_height - 100 - 20 / 2, 20, 20,
                        window_width, window_height)
        for i in range(10000):
            player.move_left()
        player.V = 1000
        a = Vector(100000, 10000)
        player.check_inf(a)
        self.assertEqual(player.V, 0)

    def test_StatePlayerShot(self):
        window_width = 1000
        window_height = 1000
        player = Player(window_width / 2, window_height - 100 - 20 / 2, 20, 20,
                        window_width, window_height)
        self.assertEqual(player.shot(), True)
        self.assertEqual(player.shots, 2)
        player.shot()
        self.assertEqual(player.shots, 1)
        player.shot()
        self.assertEqual(player.shots, 0)
        self.assertEqual(player.shot(), False)

    def test_StatePlayerShotMove(self):
        window_width = 1000
        window_height = 1000
        player = Player(window_width / 2, window_height - 100 - 20 / 2, 20, 20,
                        window_width, window_height)
        player.set_center_x(500)
        player.set_center_y(900)
        shot = ShotPlayer(player.center_x - 2, player.center_y - 2, 0, 4, 4,
                          window_width, window_height)
        for i in range(10):
            shot.move()
        self.assertEqual(shot.center_x, player.center_x)
        self.assertEqual(shot.center_y, player.center_y - 5 * 10)
        self.assertEqual(shot.check_window(), False)
        for i in range(10000):
            shot.move()
        self.assertEqual(shot.check_window(), True)

    def test_StateMonster1(self):
        window_width = 1000
        window_height = 1000
        player = Player(window_width / 2, window_height - 100 - 20 / 2, 20, 20,
                        window_width, window_height)
        player.set_center_x(500)
        player.set_center_y(900)
        shot = ShotPlayer(player.center_x - 2, player.center_y - 2, 0, 4, 4,
                          window_width, window_height)
        m1 = Monster(500, 500, 20, 20, 2, window_width, window_height)
        for i in range(1000):
            shot.check_monster([m1])
            shot.move()
        self.assertEqual(m1.life, 1)

    def test_StateMonster2(self):
        window_width = 1000
        window_height = 1000
        m1 = Monster(500 - 10, 500 - 10, 20, 20, 2,
                     window_width, window_height)
        self.assertEqual(m1.center_x, 500)
        m1.move_left()
        self.assertEqual(m1.center_x, 500 - m1.step)
        m1.move_right()
        self.assertEqual(m1.center_x, 500)

    def test_StateMonster3(self):
        window_width = 1000
        window_height = 1000
        m1 = Monster(500 - 10, 500 - 10, 20, 20, 2,
                     window_width, window_height)
        m1.move_down()
        self.assertEqual(m1.center_x, 500)
        self.assertEqual(m1.center_y, 550)
        self.assertEqual(m1.go_right, False)

    def test_StateMonster4(self):
        window_width = 1000
        window_height = 1000
        m1 = Monster(500 - 10, 500 - 10, 20, 20, 3,
                     window_width, window_height)
        m1.damage()
        self.assertEqual(m1.life, 2)
        m1.damage()
        self.assertEqual(m1.life, 1)
        m1.damage()
        self.assertEqual(m1.life, 0)
        self.assertEqual(m1.is_dead, True)

    def test_StateMonster5(self):
        window_width = 1000
        window_height = 1000
        player = Player(window_width / 2, window_height - 100 - 20 / 2, 20, 20,
                        window_width, window_height)
        m1 = Monster(500 - 10, 500 - 10, 20, 20, 3,
                     window_width, window_height)
        shot = ShotMonster(m1.center_x, m1.center_y, 6, 6,
                           window_width, window_height)
        for i in range(1000):
            shot.check_player(player)
            shot.move()
        self.assertEqual(player.life, 9)

    def test_StateMonster6(self):
        window_width = 1000
        window_height = 1000
        b = Barrier(window_width / 2, window_height - 100 - 20 / 2, 20, 20,
                    window_width, window_height)
        m1 = Monster(500, 500, 20, 20, 3, window_width, window_height)
        shot = ShotMonster(m1.center_x, m1.center_y, 6, 6,
                           window_width, window_height)
        for i in range(1000):
            shot.check_barrier([b])
            shot.move()
        self.assertEqual(b.life, 2)

    def test_StateMonster7(self):
        window_width = 1000
        window_height = 1000
        m1 = Monster(500, 500, 20, 20, 3, window_width, window_height)
        shot = ShotMonster(m1.center_x, m1.center_y, 6, 6,
                           window_width, window_height)
        self.assertEqual(shot.check_window(), False)
        for i in range(1000):
            shot.move()
        self.assertEqual(shot.check_window(), True)

    def test_Barrier(self):
        window_width = 1000
        window_height = 1000
        player = Player(window_width / 2, window_height - 100 - 20 / 2, 20, 20,
                        window_width, window_height)
        player.set_center_x(500)
        player.set_center_y(900)
        shot = ShotPlayer(player.center_x - 2, player.center_y - 2, 0, 4, 4,
                          window_width, window_height)
        b = Barrier(500 - 5, 100, 10, 10, window_width, window_height)
        for i in range(1000):
            shot.check_barrier([b])
            shot.move()
        self.assertEqual(b.life, 2)
        shot = ShotPlayer(player.center_x - 2, player.center_y - 2, 0, 4, 4,
                          window_width, window_height)
        for i in range(1000):
            shot.check_barrier([b])
            shot.move()
        self.assertEqual(b.life, 1)
        shot = ShotPlayer(player.center_x - 2, player.center_y - 2, 0, 4, 4,
                          window_width, window_height)
        for i in range(1000):
            shot.check_barrier([b])
            shot.move()
        self.assertEqual(b.life, 0)
        self.assertEqual(b.is_dead, True)

    def test_BarrierUpdate(self):
        window_width = 1000
        window_height = 1000
        player = Player(window_width / 2, window_height - 100 - 20 / 2, 20, 20,
                        window_width, window_height)
        player.set_center_x(500)
        player.set_center_y(900)

        b = Barrier(500-5, 100, 10, 10, window_width, window_height)

        for i in range(1000):
            b.chance_update()
        self.assertGreaterEqual(b.life, 3)
        life = b.life
        b.barrier_update()
        self.assertEqual(life+1, b.life)


if __name__ == '__main__':
    unittest.main()
