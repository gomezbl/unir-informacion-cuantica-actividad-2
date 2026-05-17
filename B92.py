from qiskit import QuantumCircuit, Aer, execute
import numpy as np

n = 10

# bits de Alice
alice_bits = np.random.randint(2, size=n)

circuits = []

for i in range(n):
    qc = QuantumCircuit(1, 1)
    
    # Codificación de Alice
    if alice_bits[i] == 1:
        qc.h(0)  # |+>
    # si es 0, estado |0>
    
    # Medida de Bob
    # elegimos aleatoriamente qué estado queremos detectar
    measurement_choice = np.random.randint(2)
    
    if measurement_choice == 0:
        # medir proyector asociado a |1>
        qc.measure(0, 0)
    else:
        # cambiar a base X para detectar |-> 
        qc.h(0)
        qc.measure(0, 0)
    
    circuits.append((qc, measurement_choice))

backend = Aer.get_backend('qasm_simulator')
results = execute([c[0] for c in circuits], backend, shots=1).result()

bob_results = []
conclusive = []

for i, (qc, choice) in enumerate(circuits):
    counts = results.get_counts(qc)
    bit = int(list(counts.keys())[0])
    
    if choice == 0 and bit == 1:
        bob_results.append(1)
        conclusive.append(True)
    elif choice == 1 and bit == 1:
        bob_results.append(0)
        conclusive.append(True)
    else:
        bob_results.append(None)
        conclusive.append(False)

# Filtrado (sólo eventos concluyentes)
key_alice = []
key_bob = []

for i in range(n):
    if conclusivekey_alice.append(alice_bits[i])
        key_bob.append(bob_results[i])

print("Clave de Alice:", key_alice)
print("Clave de Bob:", key_bob)
