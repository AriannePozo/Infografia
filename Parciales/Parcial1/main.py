import arcade
import random
from food import Food
from snake import Snake

# definicion de constantes
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Snake"
SCALING = 0.5


class TransformWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.FOREST_GREEN)
        self.last_key = arcade.key.UP  # Para que inicie moviendose hacia arriba
        self.sprites = None
        self.snake = None
        self.snake_tail = None
        self.segments_tail = [(0, 0)]

    def setup(self):
        self.sprites = arcade.SpriteList()
        self.snake_tail = arcade.SpriteList()

        self.new_food()

        self.snake = Snake("sprites/snake2.png", 0.055, 20, 20)

        self.sprites.append(self.snake)

    def on_draw(self):
        arcade.start_render()
        self.sprites.draw()

        # Dibujar lineas
        for v_l in range(0, SCREEN_WIDTH, 20):
            arcade.draw_line(
                v_l,
                0,
                v_l,
                SCREEN_HEIGHT,
                arcade.color.BEIGE
            )
        for h_l in range(0, SCREEN_HEIGHT, 20):
            arcade.draw_line(
                0,
                h_l,
                SCREEN_WIDTH,
                h_l,
                arcade.color.BEIGE
            )

        arcade.finish_render()

    def update(self, delta_time):

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

        self.snake_eat()

        self.snake.wall_collision(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.actualizar_cola()
        self.segments_tail[0] = (
            self.snake.center_x, self.snake.center_y)
        print(f"{self.segments_tail[0]}")

        self.sprites.update()

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

    def snake_eat(self):
        if self.snake.eat_food(self.food):
            self.snake_new_segment(-10, -10)
            self.segments_tail.append((-10, -10))
            self.food.remove_from_sprite_lists()
            self.new_food()

    def snake_new_segment(self, center_x, center_y):
        tail = Snake("sprites/snake2.png", 0.055, center_x, center_y)
        self.snake_tail.append(tail)
        self.sprites.append(tail)

    def new_food(self):
        numero_aleatorio_x = random.randrange(10, 491, 20)
        numero_aleatorio_y = random.randrange(10, 691, 20)

        self.food = Food("sprites/apple.png", 0.045,
                         numero_aleatorio_x, numero_aleatorio_y)
        self.sprites.append(self.food)

    def actualizar_cola(self):
        if len(self.segments_tail) > 1:
            for i in range(len(self.segments_tail) - 1, 0, -1):
                tail = self.snake_tail[i]
                prev_tail = self.snake_tail[i - 1]
                dx = tail.center_x - prev_tail.center_x
                dy = tail.center_y - prev_tail.center_y
                if dx > 0:
                    tail.center_x = prev_tail.center_x + 10
                elif dx < 0:
                    tail.center_x = prev_tail.center_x - 10
                elif dy > 0:
                    tail.center_y = prev_tail.center_y + 10
                elif dy < 0:
                    tail.center_y = prev_tail.center_y - 10
                self.segments_tail[i] = (tail.center_x, tail.center_y)

    def score(self):
        ...


def main():
    app = TransformWindow()
    app.setup()
    arcade.run()


if __name__ == "__main__":
    main()
