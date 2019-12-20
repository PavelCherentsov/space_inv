from math import cos, sin, radians


class ShotPlayer:
    def __init__(self, x, y, angle, width, height, window_width,
                 window_height):
        self.x = x
        self.y = y
        self.center_x = self.start_x = x + width / 2
        self.center_y = self.start_y = y + height / 2
        self.angle = angle
        self.width = width
        self.height = height
        self.is_dead = False
        self.window_width = window_width
        self.window_height = window_height

    def move(self):
        self.x -= 5 * cos(radians(self.angle + 90))
        self.y -= 5 * sin(radians(self.angle + 90))
        self.center_y -= 5 * sin(radians(self.angle + 90))
        self.center_x -= 5 * cos(radians(self.angle + 90))

    def check_monster(self, monsters):
        if not self.is_dead:
            for monster in monsters:
                if not monster.is_dead:
                    if self.center_x > monster.x \
                            and self.center_x < monster.x + monster.width \
                            and self.center_y > monster.y \
                            and self.center_y < monster.y + monster.height:
                        monster.damage()
                        self.is_dead = True

    def check_barrier(self, barriers):
        if not self.is_dead:
            for barrier in barriers:
                if self.center_x > barrier.x \
                        and self.center_x < barrier.x + barrier.width \
                        and self.center_y > barrier.y \
                        and self.center_y < barrier.y + barrier.height:
                    if not barrier.is_dead:
                        barrier.barrier_damage()
                        self.is_dead = True

    def check_window(self):
        return self.center_x < 0 or \
               self.center_x > self.window_width or \
               self.center_y < 0
