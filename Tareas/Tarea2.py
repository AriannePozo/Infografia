import random
import time


class Personaje:
    # se encarga de inicializar los atributos con los valores que recibe como parámetros
    def __init__(self, nombre, vitalidad):
        self.nombre = nombre
        self.vitalidad = vitalidad

    # imprime un mensaje de saludo con el nombre del personaje.
    def saludo(self):
        print(f"Hola, mi nombre es {self.nombre}")

    def esta_vivo(self):  # si la vitalidad es mayor a cero el personaje se encuentra con vida
        return self.vitalidad > 0

# 2. Agregar lógica de contraataque del jugador. y # 3. Agregar posibilidad de daño crítico en contra ataque del jugador.


class Jugador(Personaje):  # Este hereda de la clase personaje
    def __init__(self, nombre, vitalidad, habilidades):
        super().__init__(nombre, vitalidad)
        self.habilidades = habilidades

    def recibir_daño(self, daño):  # Se restara puntos de vitalidad cuando reciba daño
        self.vitalidad -= daño

    def listar_habilidades(self):  # lista de habilidades del jugador
        for h in self.habilidades:
            print(f"Puedo {h}")

    # tiene una probabilidad de activarse (30%) cada vez que el enemigo ataca al jugador.
    def contraatacar(self, enemigo):
        if random.random() < 0.5:
            danio = self.vitalidad // 2
            if random.random() < 0.1:
                # Si se activa, el jugador hace un ataque con daño crítico que resta el doble de daño al enemigo.
                danio *= 2
                print(
                    f"{self.nombre} hizo un contraataque CRÍTICO al enemigo {enemigo.nombre} con daño: {danio}")
            else:
                print(
                    f"{self.nombre} hizo un contraataque al enemigo {enemigo.nombre} con daño: {danio}")
            enemigo.recibir_daño(danio)
        else:
            print(f"{self.nombre} no logró hacer un contraataque.")

# 1. Agregar logica de daño aleatorio al enemigo.


class Enemigo(Personaje):
    def __init__(self, nombre, vitalidad, ataque):
        super().__init__(nombre, vitalidad)
        self.ataque = ataque

    def recibir_daño(self, daño):
        self.vitalidad -= daño

    def atacar_jugador(self, jugador):
        print(
            f"Enemigo {self.nombre} está atacando al jugador {jugador.nombre}")
        if random.random() < 0.7:  # Si el número es menor a 0.7 (es decir, hay un 70% de probabilidad de que el enemigo ataque), se procede a calcular el daño del ataque.
            # La suma del ataque del enemigo y un número aleatorio entre -2 y 2, que simula la variabilidad del daño.
            danio = self.ataque + random.randint(-2, 2)
            if danio <= 0:
                print(f"¡{self.nombre} falló su ataque!")
            else:
                print(
                    f"{self.nombre} atacó al jugador {jugador.nombre} con daño: {danio}")
                jugador.recibir_daño(danio)
                jugador.contraatacar(self)
        else:
            print(f"{self.nombre} no logró atacar al jugador {jugador.nombre}.")


jugador = Jugador("Juan", 100, ["atacar", "volar", "esquivar"])
jugador.listar_habilidades()
jugador.saludo()

enemigo = Enemigo("Raul", 50, 10)

# El ciclo while se repite hasta que uno de los personajes muera.
while jugador.esta_vivo() and enemigo.esta_vivo():
    enemigo.atacar_jugador(jugador)
    print(f"Vitalidad {jugador.nombre}: {jugador.vitalidad}")
    if jugador.esta_vivo():
        time.sleep(2)

if not jugador.esta_vivo():
    print(f"El jugador {jugador.nombre} ha muerto.")
else:
    print(
        f"¡El jugador {jugador.nombre} ha vencido al enemigo {enemigo.nombre}!")


# EJERCICIO:
# Modificar este programa para agregar las siguientes caracteristicas:
