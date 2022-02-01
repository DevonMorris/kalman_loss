import numpy as np
import numpy.linalg as la
import pandas as pd
from matplotlib import pyplot as plt

# Global vars because IDGAF
Q = np.matrix([
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 0.1**2, 0.0, 0.0],
    [0.0, 0.0, 0.1**2, 0.0],
    [0.0, 0.0, 0.0, 10**2]])
M = np.matrix([
    [150**2, 0.0],
    [0.0, 50**2]])
R = np.matrix([0.1**2])

def state_transition(x : np.matrix, u : np.matrix) -> np.matrix:
    return np.matrix([[x[0,0] + x[1,0]],
                     [x[2,0] * (u[0,0] - u[1,0] - x[3,0]) / 1000],
                     [x[2,0]],
                     [x[3,0]]])

def state_transition_jac(x : np.matrix, u : np.matrix) -> np.matrix:
    return np.matrix([
        [1.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, (u[0,0] - u[1,0] - x[3,0]) / 1000, -x[2,0] / 1000],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0]])

def state_input_jac(x : np.matrix, u : np.matrix) -> np.matrix:
    return np.matrix([
        [0.0, 0.0],
        [x[2,0] / 1000, -x[2,0]/1000],
        [0.0, 0.0],
        [0.0, 0.0]])

def measure(x):
    return np.matrix([[x[0,0]]])

def state_measurement_jac(x : np.matrix) -> np.matrix:
    return np.matrix([1.0, 0.0, 0.0, 0.0])

def predict(x : np.matrix, u : np.matrix, P : np.matrix) -> np.matrix:
    xp = state_transition(x,u)
    A = state_transition_jac(x,u)
    B = state_input_jac(x,u)

    Pp = A * P * A.T + B * M * B.T + Q
    return xp, Pp

def update(x : np.matrix, z : np.matrix, P : np.matrix) -> (np.matrix, np.matrix):
    zp = measure(x)
    e = z - zp
    C = state_measurement_jac(x)
    S = C * P * C.T + R
    K = P * C.T * la.inv(S)

    xc = x + K*e
    Pc = (np.matrix(np.eye(4)) - K * C) * P
    return xc, Pc

def predict_update(x : np.matrix, u : np.matrix, z : np.matrix, P : np.matrix) -> (np.matrix, np.matrix):
    xp, Pp = predict(x,u,P)
    xc, Pc = update(xp, z, Pp)
    return xc, Pc

if __name__ == "__main__":
    pass
