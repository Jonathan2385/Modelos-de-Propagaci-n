
"""
Created on Wed Jan  3 07:31:55 2024

@author: Jonathan
"""

import math
#esta biblioteca nos permite el calculo mátematico de numero reales y decimales
def okumura_hata(frequency, distance, h_b, h_m, area_type):
    #En esta parte se explica el funcionamiento del programa, los dattos que va a pedir y la solución que nos dará
    #en este caso la solución sería la pérdida de propagación en el modelo deseado, escogiendo de las 4 opciones 
    """
    Calcula la pérdida de propagación según el modelo de Okumura-Hata.

    Parámetros:
    - frequency: Frecuencia de la señal en MHz.
    - distance: Distancia entre la estación base y el receptor en kilómetros.
    - h_b: Altura de la estación base en metros.
    - h_m: Altura del receptor en metros.
    - area_type: Tipo de área (ciudad pequeña, grande, suburbana, rural).

    Devuelve:
    - Pérdida de propagación en dB.
    """
    # Constantes del modelo Okumura-Hata
    if area_type == 'ciudad_pequena':
        #Formula del modelo para una ciudad pequeña 
        a_hm = 3.2 * (math.log10(11.75 * h_m)) ** 2 - 4.97
        C = 0
    elif area_type == 'ciudad_grande':
        #Formula del modelo para una ciudad grande 
        a_hm = 3.2 * (math.log10(11.75 * h_m)) ** 2 - 4.97
        C = 3
    elif area_type == 'suburbana':
        #Formula del modelo para una ciudad suburbana (un poco alejada de la zona urbana )
        a_hm = 3.2 * (math.log10(11.75 * h_m)) ** 2 - 4.97
        C = 6
    elif area_type == 'rural':
        #Formula de la zona rural
        a_hm = 3.2 * (math.log10(11.75 * h_m)) ** 2 - 4.97
        C = 9

    # Cálculo de la pérdida de propagación
    #Formula general de la formula de propagación en el espaio libre 
    loss = 69.55 + 26.16 * math.log10(frequency) - 13.82 * math.log10(h_b) - a_hm + \
           (44.9 - 6.55 * math.log10(h_b)) * math.log10(distance) + C

    return loss
def free_space_path_loss_with_exponent(frequency, distance, exponent):
    #Funcionamiento delmprograma con las variables ingresadas
    """
    Calcula la pérdida de propagación en el espacio libre con un exponente adicional.

    Parámetros:
    - frequency: Frecuencia de la señal en Hz.
    - distance: Distancia entre la estación base y el receptor en metros (específicamente en metros)
    - exponent: Exponente de pérdida de trayectoria en sistemas prácticos.

    Devuelve:
    - Pérdida de propagación en dB.
    """
    speed_of_light = 3 * 10**8  # Velocidad de la luz en el vacío en metros por segundo

    loss = 20 * math.log10(distance*10**3) + 20 * math.log10(frequency*10**6) + \
           20 * math.log10(4 * math.pi / speed_of_light) + 20 * math.log10(exponent)

    return loss
#En esta parte se imprimirá la entrada de valores 
frequency = float(input("Ingrese la frecuencia en MHz: "))
distance = float(input("Ingrese la distancia en kilómetros: "))
h_b = float(input("Ingrese la altura de la estación base en metros: "))
h_m = float(input("Ingrese la altura del receptor en metros: "))
exponent = float(input("Ingrese el exponente de pérdida de trayectoria: "))
area_type = input("Ingrese el tipo de área (ciudad_pequena, ciudad_grande, suburbana, rural): ")

loss = okumura_hata(frequency, distance, h_b, h_m, area_type)
#Se imprimirá la pérdida en el área establecida con los vaores dados.
print(f"Pérdida de propagación: {loss:.2f} dB")

# Calcular la pérdida de propagación en el espacio libre con el exponente adicional
loss_space_free_with_exponent = free_space_path_loss_with_exponent(frequency, distance, exponent)
print(f"Pérdida de propagación en el espacio libre con exponente: {loss_space_free_with_exponent:.2f} dB")
