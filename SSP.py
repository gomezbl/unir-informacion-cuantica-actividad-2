"""
El siguiente ejemplo muestra una implementación simplificada inspirada en el protocolo Six-state.
Se incluyen las tres bases posibles utilizadas durante la transmisión y medición de los qubits.
Se muestra únicamente una simulación conceptual del protocolo Six-state. No incluye procesos completos de corrección de errores, amplificación de privacidad ni modelos avanzados de ataque.
"""

from qiskit import QuantumCircuit, Aer, execute
import numpy as np

n = 10

# Bits y bases de Alice
alice_bits = np.random.randint(2, size=n)
alice_bases = np.random.randint(3, size=n)

# Bases de Bob
bob_bases = np.random.randint(3, size=n)

circuits = []

for i in range(n):
    qc = QuantumCircuit(1, 1)

    # Preparación del bit
    if alice_bits[i] == 1:
        qc.x(0)

    # Base X
    if alice_bases[i] == 1:
        qc.h(0)

    # Base Y
    elif alice_bases[i] == 2:
        qc.sdg(0)
        qc.h(0)

    # Medición de Bob
    if bob_bases[i] == 1:
        qc.h(0)

    elif bob_bases[i] == 2:
        qc.h(0)
        qc.s(0)

    qc.measure(0, 0)
    circuits.append(qc)

backend = Aer.get_backend('qasm_simulator')
results = execute(circuits, backend, shots=1).result()

bob_results = []

for qc in circuits:
    counts = results.get_counts(qc)
    measured_bit = int(list(counts.keys())[0])
    bob_results.append(measured_bit)

key_alice = []
key_bob = []

for i in range(n):
    if alice_bases[i] == bob_bases[i]:
        key_alice.append(alice_bits[i])
        key_bob.append(bob_results[i])

print("Clave de Alice:", key_alice)
print("Clave de Bob:", key_bob)
