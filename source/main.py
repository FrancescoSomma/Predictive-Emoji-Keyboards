from source import utils as ut
from source import train as tr
import pickle

try:
    modello = ut.carica_modello()

except FileNotFoundError:
    print('File non trovato')
