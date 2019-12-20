class Monster:
    def __init__(self, x, y, width, height, life, window_width, window_height):
        self.center_x = self.start_x = x
        self.center_y = self.start_y = y
        self.x = x - width / 2
        self.y = y - height / 2
        self.center_x = self.start_x = x + width / 2
        self.center_y = self.start_y = y + height / 2
        self.width = width
        self.height = height
        self.life = life
        self.step = 15
        self.count_for_kill = life * 10
        self.is_dead = False
        self.go_right = True
        self.window_width = window_width
        self.window_height = window_height

    def move_left(self):
        self.x -= self.step
        self.center_x -= self.step

    def move_right(self):
        self.x += self.step
        self.center_x += self.step

    def move_down(self):
        self.y += 50
        self.go_right = not self.go_right
        self.center_y += 50

    def damage(self):
        self.life -= 1
        if self.life == 0:
            self.is_dead = True
