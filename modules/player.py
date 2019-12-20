from math import sqrt, atan, pi, cos, sin, inf
from modules.vector import Vector


class Constants:
    def __init__(self):
        self.Mu = 0.5
        self.G = 5.8
        self.M = 1
        self.F = 0.01


class Player:
    def __init__(self, center_x, center_y, width, height,
                 window_width, window_height):
        self.width = width
        self.height = height
        self.center_x = center_x
        self.center_y = center_y
        self.x = self.start_x = self.center_x - self.width / 2
        self.y = self.start_y = self.center_y - self.height / 2
        self.angle = 0
        self.life = 10
        self.killings = 0
        self.shots = 3
        self.step = 1
        self.V = 0
        self.f = 0
        self.f_old = 0
        self.is_dead = False
        self.constants = Constants()
        self.window_width = window_width
        self.window_height = window_height

    def move_left(self):
        if self.x - self.step >= 100:
            self.set_center_x(self.center_x - self. step)
            self.set_center_y(self.ellipse(self.center_x))
            self.get_angle()

    def move_right(self):
        if self.x + self.step <= self.window_width - 100:
            self.set_center_x(self.center_x + self.step)
            self.set_center_y(self.ellipse(self.center_x))
            self.get_angle()

    def death(self):
        self.set_x(self.start_x)
        self.set_y(self.start_y)
        self.life -= 1
        self.V = 0
        if self.life == 0:
            self.is_dead = True

    def get_angle(self):
        self.angle = atan(self.ellipse_diff(self.center_x)) * 180 / pi

    def shot(self):
        if self.shots != 0:
            self.shots -= 1
            return True
        return False

    def set_x(self, x):
        self.x = x
        self.center_x = x + self.width / 2

    def set_center_x(self, x):
        self.center_x = x
        self.x = x - self.width / 2

    def set_y(self, y):
        self.y = y
        self.center_y = y + self.height / 2

    def set_center_y(self, y):
        self.center_y = y
        self.y = y - self.height / 2

    def convert_to_left(self, x, y):
        return (x - self.width / 2,
                y - self.height / 2)

    def convert_to_center(self, x, y):
        return (x + self.width / 2,
                y + self.height / 2)

    def ellipse_diff(self, x):
        a = self.window_width / 2 - 100 - self.width / 2
        b = (self.window_height - 200) / 3 - self.height / 2
        x0 = self.window_width / 2
        if a * a - (x - x0) * (x - x0) <= 0 and x < self.window_width / 2:
            return inf
        if a * a - (x - x0) * (x - x0) <= 0 and x > self.window_width / 2:
            return -inf
        return -b * (x-x0) / (sqrt(a * a - (x - x0) * (x - x0)) * a)

    def ellipse(self, x):
        a = self.window_width / 2 - 100 - self.width / 2
        b = (self.window_height - 200) / 3 - self.height / 2
        x0 = self.window_width / 2
        y0 = (2*(self.window_height-200)) / 3 + 100
        if a*a - (x-x0)*(x-x0) <= 0:
            return y0
        return y0 + b/a * sqrt(a*a - (x-x0)*(x-x0))

    def get_acceleration(self):
        alpha = atan(self.ellipse_diff(self.center_x))
        f = Vector(-self.f * cos(pi - alpha),
                   self.f * sin(pi - alpha))
        N = Vector(self.constants.M * self.constants.G
                   * cos(pi - alpha) * cos(alpha - pi / 2),
                   self.constants.M * self.constants.G
                   * cos(pi - alpha) * sin(alpha - pi / 2))
        if self.V > 0:
            Mu_N = Vector(self.constants.Mu * self.constants.M
                          * cos(pi - alpha) * cos(pi - alpha),
                          self.constants.Mu * self.constants.M
                          * cos(pi - alpha) * sin(pi - alpha))
        else:
            Mu_N = Vector(self.constants.Mu * self.constants.M
                          * cos(pi - alpha) * cos(pi - alpha),
                          self.constants.Mu * self.constants.M
                          * cos(pi - alpha) * sin(pi - alpha)) * -1
        mg = Vector(0, -self.constants.M * self.constants.G)
        return (f + N + Mu_N + mg) * -self.constants.M

    def set_movement(self, a):
        self.V += a.x
        self.set_center_x(self.center_x + self.V + a.x / 2)

    def check_inf(self, a):
        if self.ellipse_diff(self.center_x) == inf or \
                self.ellipse_diff(self.center_x) == -inf:
            self.set_center_x(self.center_x - self.V - a.x / 2)
            self.V = 0
        self.set_center_y(self.ellipse(self.center_x))
