# Importamos paquetes
import arcade
import math

# Definición de constantes
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Hola Arcade"

# Definición de la función para dibujar una estrella


def draw_star(center_x, center_y, radius, color):
    # Definir los puntos de la estrella
    angle = - math.pi / 2
    angle_step = 2 * math.pi / 5
    # Contendrá las coordenadas de los puntos que forman la estrella.
    points = []
    for i in range(5):
        # Calculamos las coordenadas x e y del punto actual utilizando la fórmula matemática para un círculo:
        x = center_x + radius * math.cos(angle)
        # x = rcos(angulo) , y = rsin(angulo); donde r es el radio de la estrella y angulo es el ángulo actual
        y = center_y + radius * math.sin(angle)
        points.append((x, y))
        # Avanzamos el ángulo, en la mitad del ángulo para calcular el punto intermedio
        angle += angle_step / 2
        x = center_x + radius / 2 * math.cos(angle)
        y = center_y + radius / 2 * math.sin(angle)
        points.append((x, y))
        angle += angle_step / 2

    # Dibujar la estrella
    arcade.draw_polygon_filled(points, color)

# Definición de la clase ventana


class Hola(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.SEA_BLUE)

    def on_draw(self):
        # Iniciar renderizado
        arcade.start_render()

        # Dibujar la estrella
        draw_star(SCREEN_WIDTH / 2, SCREEN_HEIGHT /
                  2, 100, arcade.color.YELLOW)


# Entrypoint
if __name__ == "__main__":
    app = Hola()
    arcade.run()
