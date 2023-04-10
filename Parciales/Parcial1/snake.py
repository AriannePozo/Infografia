import arcade


class Snake:
    def __init__(self, center_x, center_y, width, height, color=arcade.color.DEEP_SKY_BLUE):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.color = color
        self.movement = 120

    def draw(self):
        arcade.draw_rectangle_filled(
            self.center_x, self.center_y, self.width, self.height, self.color, 0)
