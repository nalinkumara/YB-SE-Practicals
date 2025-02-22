from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
import math
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
## Uncomment the next line to see diagrams when running in a notebook
#%matplotlib inline

## Example 3-2: Entangled Qubits
# Set up the program
a = QuantumRegister(1, name='a')
b = QuantumRegister(1, name='b')
a_c = ClassicalRegister(1, name='ac')
b_c = ClassicalRegister(1, name='bc')
qc = QuantumCircuit(a, b, a_c, b_c)

qc.h(a)              # put a into a superposition of 0 and 1
qc.cx(a, b)        # entangle a and b
qc.measure(a, a_c)
qc.measure(b, b_c)

print(qc)

# Choose the qasm_simulator backend
simulator = AerSimulator(method='statevector')

# Simulate the circuit
job = simulator.run(qc, shots=10000)

# Get the result
result = job.result()

# Print the counts
print(result.get_counts(qc))

# Visualize the circuit
print(qc)
#qc.draw(output='mpl').show()

# Visualize the measurement outcomes
plot_histogram(result.get_counts(qc))