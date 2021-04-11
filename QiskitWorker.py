
class QiskitWorkout():
   def __init__(self, message):
        self.message = message

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()
        
    def run(self):
        note = self.message
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
