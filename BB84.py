from qiskit import QuantumCircuit, Aer, execute
import numpy as np

n = 10  # número de qubits

# Generación aleatoria
alice_bits = np.random.randint(2, size=n)
alice_bases = np.random.randint(2, size=n)
bob_bases = np.random.randint(2, size=n)

circuits = []

# Codificación de Alice
for i in range(n):
    qc = QuantumCircuit(1, 1)
    
    # Preparar bit
    if alice_bits[i] == 1:
        qc.x(0)
    
    # Cambiar base si es necesario
    if alice_bases[i] == 1:
        qc.h(0)
    
    # Medición en base de Bob
    if bob_bases[i] == 1:
        qc.h(0)
    
    qc.measure(0, 0)
    circuits.append(qc)

# Simulación
backend = Aer.get_backend('qasm_simulator')
results = execute(circuits, backend, shots=1).result()

bob_results = []
for i in range(n):
    counts = results.get_counts(circuits[i])
    measured_bit = int(list(counts.keys())[0])
    bob_results.append(measured_bit)

# Sifting
sifted_key_alice = []
sifted_key_bob = []

for i in range(n):
    if alice_bases[i] == bob_basessifted_key_alice.append(alice_bits[i])
        sifted_key_bob.append(bob_results[i])

print("Clave de Alice:", sifted_key_alice)
print("Clave de Bob:", sifted_key_bob)
