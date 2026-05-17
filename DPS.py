import numpy as np


n = 10


# Bits generados por Alice
alice_bits = np.random.randint(2, size=n)


# Fases asociadas
phases = []


for bit in alice_bits:
    if bit == 0:
        phases.append(0)
    else:
        phases.append(np.pi)


# Comparación de diferencias de fase
detected_bits = []


for i in range(1, n):
    delta_phase = phases[i] - phases[i - 1]

    if delta_phase == 0:
        detected_bits.append(0)
    else:
        detected_bits.append(1)


print("Bits de Alice:", alice_bits.tolist())
print("Bits detectados:", detected_bits)
