# Programa para medición de tiempo de suma de datos con el metodo for, con el metodo sum de python y con numpy
import time
import numpy as np

# Metodo FOR
start = time.time() # Timpo en este momento en segundos
resultado = 0

for i in range(50000000):
    resultado += i

print(f'Resultado de la suma (FOR): {resultado}')
print(f'Tiempo ejecutado: {time.time() - start}\n')

# Metodo Sum de python
start = time.time()
resultado = sum(range(50000000))

print(f'Resultado de la suma (SUM): {resultado}')
print(f'Tiempo ejecutado: {time.time() - start}\n') # Resultado notablemente mejor que el FOR por 1 segundo

# Usando Numpy

start = time.time()
resultado = np.sum(np.arange(50000000, dtype='int64')) # Permite que tenga mas espacio en memoria para guardar el resultado

print(f'Resultado de la suma (Numpy): {resultado}')
print(f'Tiempo ejecutado: {time.time() - start}') # Tiempo de ejecución menor al FOR por 2.5 segundos y al SUM de python por 0.9 segundos
