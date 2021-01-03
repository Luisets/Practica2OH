import benchmarks.functions as functions
import group06.EA as ea
import group06.Genome as genome
import math

# def fitness(arr):
#     ob_x = 5
#     ob_y = 7
#     g = 9.8
#     m = 1000
#     Ec_kg = 3000000
#     gr_powder = arr[0] * 100
#     angle = arr[1] * 90
#     Ec = (Ec_kg * gr_powder)/m
#     sqr_V0 = (2 * Ec) / m
#     x_max = (sqr_V0 * math.sin(math.radians(2 * angle))) / g
#     # return math.sin(math.radians(180))

#     return -x_max
#     # return Ec, sqr_V0
#     pass


def dist(p1, p2):
    return math.sqrt(math.pow(p1[0] - p2[0],2) + math.pow(p1[1] - p2[1], 2))

def fitness(arr):
    # coordenadas del objetivo
    p1 = (4, 9)
    # gravedad para la simulacion
    g = 9.8
    # masa de la bala de cañon
    m = 1000
    # energia cinetica por cada Kg de polvora
    Ec_kg = 3000000
    # gramos de polvora que disponemos
    gr_powder = arr[0] * 100
    # angulo vertical del cañon para disparar
    angle_xz_y = arr[1] * 90
    # rotacion del cañon
    angle_x_z = arr[2] * 360
    # calculamos la energia cinetica que se generaria con determinada cantidad de polvora
    Ec = (Ec_kg * gr_powder)/1000
    sqr_V0 = (2 * Ec) / m
    # calculamos la distancia maxima que recorreria la bala
    recorrido = (sqr_V0 * math.sin(math.radians(2 * angle_xz_y))) / g
    x = math.sin(math.radians(angle_x_z)) * recorrido
    z = math.cos(math.radians(angle_x_z)) * recorrido
    p2 = (x, z)
    # return(x, z)
    return dist(p1, p2)

def main():
    mybounds = [(0, 1),(0, 1), (0, 1)]
    myea = ea.EA(fitness, mybounds, 50)
    myea.run(10000)
    sol = myea.best()
    print(sol.solution)
    print(sol.fitnes)
    print(fitness([0.1942986  ,0.31047878 ,0.06656247]))
    pass

# [0.1942986  0.31047878 0.06656247]
# 3.619537178399673e-07





if __name__ == "__main__":
    main()
    pass
