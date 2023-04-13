import arcade


class Snake(arcade.Sprite):
    def __init__(self, image, scale, center_x, center_y):
        super().__init__(image, scale, center_x=center_x, center_y=center_y)

        self.movement = 120

    def eat_food(self, food):
        if self.collides_with_sprite(food):
            return True
        return False

    def wall_collision(self, width, height):
        if self.center_x <= 0 or self.center_x >= width or self.center_y <= 0 or self.center_y >= height:
            print("snake muere pared")

    def update(self):
        ...
