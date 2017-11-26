import numpy as np

################################## Parametros ##################################

# Maximo Camion
MAX_CAMION = 1000

# Variables de peso
M = 1
N = 1

##################################### Data #####################################

# Declaro los bancos. Considero 'O' como el inicial
# Central                  O
# Banco Portenio            A   
# Banco Del Plata          B
# Banco De Los Andres      C
# Banco Plural             D
# Banco Del Norte          E
# Banco Pampeano           F
# Banco Cooperativo        G
# Banco Sol                H
# Banco Republica          I
# Banco Vientos del Sur    J

BANCOS = ['O', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

MONTO = {'O': 0, 'A': -44036, 'B': -9025, 'C': 34580, 'D': -46829, 'E': -16677, 'F': 37619, 'G': 48998, 'H': 42037, 'I': -5090, 'J':-33475}

POS = {'O':0, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,'G': 7, 'H': 8, 'I': 9, 'J': 10}

DIST = np.matrix('0, 4, 8, 4, 1, 4, 4, 7, 2, 1, 6;4, 0, 4, 4, 8, 7, 4, 9, 7, 5, 9;8, 4, 0, 1, 9, 3, 8, 4, 5, 1, 6;4, 4, 1, 0, 5, 3, 3, 4, 4, 6, 1;1, 8, 9, 5, 0, 8, 2, 1, 6, 3, 1;4, 7, 3, 3, 8, 0, 6, 8, 7, 2, 8;4, 4, 8, 3, 2, 6, 0, 1, 1, 6, 8;7, 9, 4, 4, 1, 8, 1, 0, 7, 2, 4;2, 7, 5, 4, 6, 7, 1, 7, 0, 5, 3;1, 5, 1, 6, 3, 2, 6, 2, 5, 0, 6;6, 9, 6, 1, 1, 8, 8, 4, 3, 6, 0')

print(DIST)

