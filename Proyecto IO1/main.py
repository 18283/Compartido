from simplex import Simplex
from fractions import Fraction

    # Ejemplo de configuración del problema
numerosDeVariables = 6
funcioncObjetivo = ('max', '1/25x_1 + 1/20x_2 + 3/50x_3 + 1/20x_4 + 1/20x_5 + 1/25x_6')
restricciones = ['1x_1 + 1x_2 + 1x_3 + 1x_4 + 1x_5 + 1x_6 = 10', '1x_1 >= 1', '1x_2 >= 1', '1x_3 >= 1', '1x_4 >= 1', '1x_5 >= 1',
                  '1x_6 >= 1', '1x_1 <= 3', '1x_2 <= 3', '1x_3 <= 3', '1x_4 <= 3', '1x_5 <= 3', '1x_6 <= 3']
    
    # Intenta crear y resolver el problema
try:
    lp_system = Simplex(numerosDeVariables, restricciones, funcioncObjetivo)
    print("soluciones", lp_system.solution)
    print("La solucion optima es Z=", lp_system.optimize_val)
except ValueError as e:
    print("Error:", e)