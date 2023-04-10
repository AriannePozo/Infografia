import arcade
import random
from food import Food
from snake import Snake

# definicion de constantes
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Snake"


class TransformWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.FOREST_GREEN)
        self.last_key = arcade.key.UP
        self.food = None
        self.snake = None

    def setup(self):
        numero_aleatorio_x = random.randrange(10, 491, 20)
        print(numero_aleatorio_x)
        numero_aleatorio_y = random.randrange(10, 691, 20)
        print(numero_aleatorio_y)
        self.food = Food(numero_aleatorio_x, numero_aleatorio_y, 10)

        self.snake = Snake(10, 10, 20, 20)

    def on_draw(self):
        arcade.start_render()
        for v_l in range(0, SCREEN_WIDTH, 20):
            arcade.draw_line(
                v_l,
                0,
                v_l,
                SCREEN_HEIGHT,
                arcade.color.DARK_GRAY
            )

        for h_l in range(0, SCREEN_HEIGHT, 20):
            arcade.draw_line(
                0,
                h_l,
                SCREEN_WIDTH,
                h_l,
                arcade.color.LIGHT_GRAY
            )

        self.food.draw()
        self.snake.draw()
        arcade.finish_render()

    def update(self, delta_time):
        self.snake_wall_collision()

        if arcade.key.UP == self.last_key:
            if self.snake.center_x % 20 != 10:
                self.snake.center_x += (10-self.snake.center_x % 20)
            self.snake.center_y += self.snake.movement * delta_time
        elif arcade.key.DOWN == self.last_key:
            if self.snake.center_x % 20 != 10:
                self.snake.center_x += (10-self.snake.center_x % 20)
            self.snake.center_y -= self.snake.movement * delta_time
        elif arcade.key.LEFT == self.last_key:
            if self.snake.center_y % 20 != 10:
                self.snake.center_y += (10-self.snake.center_y % 20)
            self.snake.center_x -= self.snake.movement * delta_time
        elif arcade.key.RIGHT == self.last_key:
            if self.snake.center_y % 20 != 10:
                self.snake.center_y += (10-self.snake.center_y % 20)
            self.snake.center_x += self.snake.movement * delta_time

    def on_key_press(self, key, modifiers):
        if self.last_key == arcade.key.UP and key == arcade.key.DOWN:
            self.last_key = arcade.key.UP
        elif self.last_key == arcade.key.DOWN and key == arcade.key.UP:
            self.last_key = arcade.key.DOWN
        elif self.last_key == arcade.key.LEFT and key == arcade.key.RIGHT:
            self.last_key = arcade.key.LEFT
        elif self.last_key == arcade.key.RIGHT and key == arcade.key.LEFT:
            self.last_key = arcade.key.RIGHT
        else:
            self.last_key = key

    def snake_wall_collision(self):
        if self.snake.center_x <= 0:
            print("snake muere izq")

        if self.snake.center_x >= SCREEN_WIDTH:
            print("snake muere der")

        if self.snake.center_y <= 0:
            print("snake muere abj")

        if self.snake.center_y >= SCREEN_HEIGHT:
            print("snake muere arr")

    def snake_tail_collision(self):
        ...

    def snake_eat_food(self):
        ...

    def snake_grow_tail(self):
        ...

    def score(self):
        ...


def main():

    app = TransformWindow()
    app.setup()
    arcade.run()


if __name__ == "__main__":
    main()
