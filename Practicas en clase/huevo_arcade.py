import arcade

# Define las dimensiones de la ventana
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Definimos los colores que se utilizarán para dibujar
color_fondo = arcade.color.LIGHT_BROWN
color_clara = arcade.color.WHITE
color_centro = arcade.color.YELLOW
color_sarten = arcade.color.GRAY
color_borde = arcade.color.LIGHT_GRAY

# Definimos la posición y tamaño de la yema del huevo
x_centro = 300
y_centro = 300
radio_centro = 40

# Definimos la posición y tamaño de la clara del huevo
x_clara = x_centro
y_clara = y_centro
ancho_clara = 100
alto_clara = 100

# Definimos la posición y tamaño del sarten
x_sarten = x_centro
y_sarten = y_centro
radio_sarten = 200

# Definimos la posición y tamaño del borde del sarten
x_borde = x_centro
y_borde = y_centro
radio_borde = 250

# Definimos la función encargada de dibujar en la ventana


def dibujar():
    arcade.start_render()

    # Dibujamos el borde de la sarten
    arcade.draw_circle_filled(
        x_borde,
        y_borde,
        radio_borde,
        color_borde
    )

    # Dibujamos la sarten
    arcade.draw_circle_filled(
        x_sarten,
        y_sarten,
        radio_sarten,
        color_sarten
    )

    # Dibuja la clara del huevo
    arcade.draw_ellipse_filled(
        x_clara - ancho_clara/2,
        y_clara,
        ancho_clara,
        alto_clara,
        color_clara
    )

    arcade.draw_ellipse_filled(
        x_clara + ancho_clara/2,
        y_clara,
        ancho_clara,
        alto_clara,
        color_clara
    )

    arcade.draw_ellipse_filled(
        x_clara,
        y_clara - alto_clara/2,
        alto_clara,
        ancho_clara,
        color_clara
    )

    arcade.draw_ellipse_filled(
        x_clara,
        y_clara + alto_clara/2,
        alto_clara,
        ancho_clara,
        color_clara
    )

    # Dibuja la yema del huevo
    arcade.draw_circle_filled(
        x_centro,
        y_centro,
        radio_centro,
        color_centro
    )

    arcade.finish_render()


# Crea la ventana y corre la aplicación
ventana = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Huevo Frito")
ventana.background_color = color_fondo
ventana.on_draw = dibujar
arcade.run()
