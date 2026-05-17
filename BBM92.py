from qiskit import QuantumCircuit, Aer, execute
import numpy as np

shots = 100

backend = Aer.get_backend('qasm_simulator')

# Generación aleatoria de bases (0: Z, 1: X)
alice_bases = np.random.randint(2, size=shots)
bob_bases = np.random.randint(2, size=shots)

results_data = []

for i in range(shots):
    qc = QuantumCircuit(2, 2)
    
    # Crear estado de Bell
    qc.h(0)
    qc.cx(0, 1)
    
    # Base de Alice
    if alice_bases[i] == 1:
        qc.h(0)
    
    # Base de Bob
    if bob_bases[i] == 1:
        qc.h(1)
    
    qc.measure([0, 1], [0, 1])
    
    job = execute(qc, backend, shots=1)
    result = job.result()
    counts = result.get_counts()
    outcome = list(counts.keys())[0]
    
    # Qiskit devuelve bits en orden inverso
    a_bit = int(outcome[1])
    b_bit = int(outcome[0])
    
    results_data.append((alice_bases[i], bob_bases[i], a_bit, b_bit))

# Sifting
key_alice = []
key_bob = []

for a_basis, b_basis, a_bit, b_bit in results_data:
    if a_basis == b_basis:
        key_alice.append(a_bit)
        key_bob.append(b_bit)

# Cálculo de QBER
errors = sum(1 for a, b in zip(key_alice, key_bob) if a != b)
qber = errors / len(key_alice) if len(key_alice) > 0 else 0

print("Clave de Alice:", key_alice[:20])
print("Clave de Bob:", key_bob[:20])
print("QBER:", qber)
