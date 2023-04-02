# Creamos personaje
Arquera = 120

# Creamos funcion de daño recibido
def ataque_recibido(vida_personaje, ataque):
        salud = vida_personaje - ataque

        if (salud > 0):
            print(f"Tu personaje a recibido daño del enemigo: -{ataque}HP")
            print(f"Salud restante: {salud}HP")
        else:
            print("Has muerto...")
        

# EJECUCIÓN

ataque_recibido(Arquera,10);
ataque_recibido(Arquera,120)