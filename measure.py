import numpy as np
from scipy import signal

class Static_object:
    def __init__(self, cycles, samples_number):
        self.t = np.linspace(0, cycles*2*np.pi, samples_number)
        self.u = np.random.rand(samples_number)

    def set_parameters(self, parameters):
        self.parameters = np.array(parameters)

    def transform(self):
        self.v = np.zeros_like(self.u)

        #set first two values manually, because u[k-1] and/or u[k-2] are not defined (equal zero)
        self.v[0] = self.u[0] * self.parameters[0]
        self.v[1] = self.u[1] * self.parameters[1] + self.u[0] * self.parameters[0]
        
        for i in range(2, len(self.u)):
            #replace it with numpy dot function
            self.v[i] = np.dot(self.parameters, self.u[i-2:i+1])
        
    
    def noise(self, noise_amplitude = 0.1, offset = 0):
        self.y = np.zeros_like(self.v)

        self.noise = np.random.rand(len(self.v)) * noise_amplitude + offset
        self.y = self.v + self.noise

    def matrix_multiply(self, *args):
        result = 1
        for matrix in args:
            result = np.dot(result, matrix)

        return result
    
    def LSM(self): #least squares method
        P = np.array([
            [100, 0, 0],
            [0, 100, 0],
            [0, 0, 100]
        ])


        b = np.array([0,0,0])[np.newaxis]
        b = b.T
            
        for i in range(2, len(self.u)):
            f = np.array(self.u[i-2:i+1])[np.newaxis]
            f = f.T

            nominator = self.matrix_multiply(P, f, f.T, P)
            denominator = 1 + self.matrix_multiply(f.T, P, f)

            P = P - nominator/denominator
            Pf = self.matrix_multiply(P, f)
            fTb = self.matrix_multiply(f.T, b)
            b = b + Pf * (self.y[i]-fTb)

        return b
