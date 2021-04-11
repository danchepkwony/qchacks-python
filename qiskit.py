#This code implements Bernstein-Vazirani algorithm and
#follows the tutorial found here: https://qiskit.org/textbook/ch-algorithms/bernstein-vazirani.html

import qiskit
from qiskit import *
from qiskit.providers.ibmq import least_busy

IBMQ.save_account('daffffa40c20d3f39cbcd68720561cec5e7cffa25c8f863423ffbf18e3c79b8fa07253d502fa37210e4177c176a282d56e54ba665541c2f272ac07eca13580b8')
provider = IBMQ.get_provider(hub='ibm-q')
backend = least_busy(provider.backends(filters=lambda x: x.configuration().n_qubits <= 5 and
                                   x.configuration().n_qubits >= 2 and
                                   not x.configuration().simulator and x.status().operational==True))

def quantumMusic(note):
    circuit = QuantumCircuit(4, 3)
    circuit.h(3)
    circuit.z(3)
    
    for i in range(3):
        circuit.h(i)
        
    circuit.barrier()
    
    note = note[::-1]
    for q in range(3):
        if note[q] == '0':
            circuit.i(q)
        else:
            circuit.cx(q, 3)
            
    circuit.barrier()
        
    for i in range(3):
        circuit.h(i)
    
    for i in range(3):
        circuit.measure(i, i)
    
    result = execute(circuit, backend = backend, shots = 1000).result().get_counts()
    return result