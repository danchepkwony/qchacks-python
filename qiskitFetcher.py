#This code implements Bernstein-Vazirani algorithm and
#follows the tutorial found here: https://qiskit.org/textbook/ch-algorithms/bernstein-vazirani.html
from flask import Flask
app = Flask(__name__)

import QiskitWorker
from qiskit import *
from qiskit.providers.ibmq import least_busy
    
IBMQ.save_account('daffffa40c20d3f39cbcd68720561cec5e7cffa25c8f863423ffbf18e3c79b8fa07253d502fa37210e4177c176a282d56e54ba665541c2f272ac07eca13580b8')
provider = IBMQ.load_account()
backend = provider.get_backend('ibmq_qasm_simulator')

@app.route('/', methods = ['GET'])
def qiskitFetcher():
        QiskitWorker('000')