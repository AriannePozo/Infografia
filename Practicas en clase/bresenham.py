def get_line(x0, y0, x1, y1):
    points = []  # lista para almacenar puntos generados
    # 1er paso: dx, dy
    # utilizar el valor absoluto para asegurar valores positivos
    dx = abs(x1 - x0)
    # utilizar el valor absoluto para asegurar valores positivos
    dy = abs(y1 - y0)
    # variables para iterar xk, yk
    xk = x0
    yk = y0
    x_inc = 1 if x1 > x0 else -1  # determinar la dirección de incremento en x
    y_inc = 1 if y1 > y0 else -1  # determinar la dirección de incremento en y

    # 2do paso: parametro de decision Pk
    Pk = 2 * dy - dx

    # 3er paso: iterar hasta el punto final:
    while xk != x1 or yk != y1:  # cambiar la condición para llegar al punto final exacto
        # agregar punto a la lista
        points.append((xk, yk))
        # decido en base a Pk si x e y incrementan o no
        if Pk < 0:
            Pk += 2 * dy
        else:
            Pk += 2 * dy - 2 * dx
            yk += y_inc
        xk += x_inc

    # agregar el punto final a la lista
    points.append((x1, y1))

    return points


if __name__ == "__main__":
    print(get_line(0, 3, 6, 5))
