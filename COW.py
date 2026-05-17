"""
El siguiente ejemplo muestra una representación simplificada del protocolo Coherent One-Way utilizando secuencias binarias para modelar la presencia y ausencia de pulsos coherentes.
Se muestra únicamente una simulación conceptual del protocolo COW. No incluye interferómetros reales, estados coherentes físicos ni modelos completos de transmisión óptica.
"""

import numpy as np

n = 10

# Bits generados por Alice
alice_bits = np.random.randint(2, size=n)

# Codificación de pulsos
pulse_sequence = []

for bit in alice_bits:
    if bit == 0:
        pulse_sequence.append([1, 0])

    else:
        pulse_sequence.append([0, 1])


# Detección simplificada de Bob
bob_results = []

for pulse_pair in pulse_sequence:

    if pulse_pair == [1, 0]:
        bob_results.append(0)

    else:
        bob_results.append(1)

print("Bits de Alice:", alice_bits.tolist())
print("Bits detectados:", bob_results)
