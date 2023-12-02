import numpy as np
from scipy import signal

class Static_object:
    def __init__(self, cycles, original_samples_number):
        self.t = np.linspace(0, cycles*2*np.pi, original_samples_number)
        self.original_y = signal.sawtooth(self.original_t, 0.5) 

        