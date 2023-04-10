import arcade


class Food:
    def __init__(self, center_x, center_y, radius, color=arcade.color.RED_DEVIL):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(
            self.center_x, self.center_y, self.radius, self.color, 0, - 1)
