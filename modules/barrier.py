from random import randint


class Barrier:
    def __init__(self, x, y, width, height, window_width, window_height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.life = 3
        self.is_dead = False
        self.window_width = window_width
        self.window_height = window_height

    def barrier_damage(self):
        if not self.is_dead:
            self.life -= 1
            if self.life == 0:
                self.is_dead = True

    def barrier_update(self):
        self.life += 1

    def chance_update(self):
        if randint(0, 100) % 20 == 0:
            self.barrier_update()
            return True
        return False
