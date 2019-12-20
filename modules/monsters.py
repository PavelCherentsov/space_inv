from math import inf, fabs


class Monsters:
    def __init__(self, window_width, window_height):
        self. list = []
        self.go_right = True
        self.window_width = window_width
        self.window_height = window_height

    def check_right_border(self):
        go_down = False
        not_go_down = False
        for monster in self.list:
            if not monster.monster.is_dead:
                if monster.monster.x + \
                        monster.monster.width + \
                        monster.monster.step > \
                        self.window_width - 100:
                    if monster.monster.y + \
                            monster.monster.height < \
                            self.window_height / 3:
                        go_down = True
                    else:
                        not_go_down = True
        return go_down, not_go_down

    def check_left_border(self):
        go_down = False
        not_go_down = False
        for monster in self.list:
            if not monster.monster.is_dead:
                if monster.monster.x - monster.monster.step < 100:
                    if monster.monster.y + \
                            monster.monster.height < \
                            self.window_height / 3:
                        go_down = True
                    else:
                        not_go_down = True
        return go_down, not_go_down

    def find_player(self, player):
        r = inf
        m = None
        for monster in self.list:
            if not monster.monster.is_dead:
                if fabs(monster.monster.center_x - player.center_x) < r:
                    r = fabs(monster.monster.center_x - player.center_x)
                    m = monster
        return m

    def move_down(self):
        for monster in self.list:
            monster.go_down()

    def move(self):
        if self.go_right:
            go_down = self.check_right_border()[0]
            not_go_down = self.check_right_border()[1]
            if go_down:
                self.move_down()
                self.go_right = False
            elif not_go_down:
                for monster in self.list:
                    monster.monster.go_right = False
                self.go_right = False
        else:
            go_down = self.check_left_border()[0]
            not_go_down = self.check_left_border()[1]
            if go_down:
                self.move_down()
                self.go_right = True
            elif not_go_down:
                for monster in self.list:
                    monster.monster.go_right = True
                self.go_right = True
