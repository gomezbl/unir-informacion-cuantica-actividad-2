from qiskit import QuantumCircuit, Aer, execute
import numpy as np


n = 10


# Bits y bases de Alice
alice_bits = np.random.randint(2, size=n)
alice_bases = np.random.randint(2, size=n)


# Bases de Bob
bob_bases = np.random.randint(2, size=n)


circuits = []


for i in range(n):
    qc = QuantumCircuit(1, 1)

    # Preparación del bit
    if alice_bits[i] == 1:
        qc.x(0)

    # Cambio a base X
    if alice_bases[i] == 1:
        qc.h(0)

    # Medición de Bob
    if bob_bases[i] == 1:
        qc.h(0)

    qc.measure(0, 0)
    circuits.append(qc)


backend = Aer.get_backend('qasm_simulator')
results = execute(circuits, backend, shots=1).result()


bob_results = []


for qc in circuits:
    counts = results.get_counts(qc)
    measured_bit = int(list(counts.keys())[0])
    bob_results.append(measured_bit)


# Reconciliación simplificada tipo SARG04
# Alice anuncia pares de estados no ortogonales.
# Bob conserva solo los casos en los que su resultado
# permite descartar uno de los dos estados anunciados.

key_alice = []
key_bob = []


for i in range(n):

    # Estado enviado por Alice:
    # 0 -> |0>, 1 -> |1>, 2 -> |+>, 3 -> |->
    sent_state = alice_bits[i] + 2 * alice_bases[i]

    # Pares posibles anunciados por Alice.
    # Cada par contiene el estado enviado y otro estado no ortogonal.
    possible_pairs = {
        0: [(0, 2), (0, 3)],
        1: [(1, 2), (1, 3)],
        2: [(2, 0), (2, 1)],
        3: [(3, 0), (3, 1)]
    }

    announced_pair = possible_pairs[sent_state][np.random.randint(2)]

    # Resultado medido por Bob, traducido al estado compatible
    if bob_bases[i] == 0:
        measured_state = bob_results[i]
    else:
        measured_state = 2 + bob_results[i]

    # Estado ortogonal al resultado de Bob
    orthogonal_state = {
        0: 1,
        1: 0,
        2: 3,
        3: 2
    }[measured_state]

    # Bob puede descartar uno de los estados anunciados
    if orthogonal_state in announced_pair:
        inferred_state = announced_pair[0]

        if inferred_state == orthogonal_state:
            inferred_state = announced_pair[1]

        inferred_bit = inferred_state % 2

        key_alice.append(alice_bits[i])
        key_bob.append(inferred_bit)


print("Clave de Alice:", key_alice)
print("Clave de Bob:", key_bob)
