from qiskit import QuantumCircuit, Aer, execute
import numpy as np

shots = 1024

# Crear circuito para estado de Bell
def create_bell_pair():
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    return qc

# Aplicar medición en diferentes bases
def measure_in_basis(qc, qubit, basis):
    if basis == 1:
        qc.h(qubit)
    return qc

# Bases de medición (0: Z, 1: X)
alice_bases = np.random.randint(2, size=shots)
bob_bases = np.random.randint(2, size=shots)

results_list = []

backend = Aer.get_backend('qasm_simulator')

for i in range(shots):
    qc = create_bell_pair()
    
    # Aplicar bases
    qc = measure_in_basis(qc, 0, alice_bases[i])
    qc = measure_in_basis(qc, 1, bob_bases[i])
    
    qc.measure([0,1], [0,1])
    
    result = execute(qc, backend, shots=1).result()
    counts = result.get_counts()
    outcome = list(counts.keys())[0]
    
    results_list.append((alice_bases[i], bob_bases[i], outcome))

# Filtrado para clave (bases iguales)
key_alice = []
key_bob = []

for a_basis, b_basis, outcome in results_list:
    if a_basis == b_basis:
        a_bit = int(outcome[1])  # orden invertido en qiskit
        b_bit = int(outcome[0])
        key_alice.append(a_bit)
        key_bob.append(b_bit)

print("Clave de Alice:", key_alice[:20])
print("Clave de Bob:", key_bob[:20])
