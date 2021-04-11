#This code implements Bernstein-Vazirani algorithm and
#follows the tutorial found here: https://qiskit.org/textbook/ch-algorithms/bernstein-vazirani.html
from flask import Flask
app = Flask(__name__)

import QiskitWorker

@app.route('/', methods = ['GET'])
def qiskitFetcher():
        QiskitWorker('000')