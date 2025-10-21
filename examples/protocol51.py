"""
Protocol 5.1 Implementation
MEGL Semigroups in Cryprography
"""

import numpy as np

# Alice's private key
def p_a(t: np.array):
    return np.maximum(np.identity(3), t)

def q_a(t: np.array):
    return np.identity(3)

# Bob's private key
def p_b(t: np.array):
    return np.maximum(np.identity(3), np.linalg.matrix_power(t, 2))

def q_b(t: np.array):
    return np.maximum(np.identity(3), t)

# Public parameters
M_1 = np.array([[0, 1, 0],
               [0, 0, 1],
               [1, 0, 0]])

M_2 = np.array([[0, 1, 0],
               [1, 0, 0],
               [0, 0, 1]])

S = np.array([[1, 0, 0],
             [0, 0, 1],
             [0, 0, 0]])

# Alice and Bob's public key
a_pub = p_a(M_1) @ S @ q_a(M_2)
b_pub = p_b(M_1) @ S @ q_b(M_2)

# Alice and Bob compute the common secret key
common_secret_a = p_a(M_1) @ b_pub @ q_a(M_2)
common_secret_b = p_b(M_1) @ a_pub @ q_b(M_2)

print("[PUBLIC PARAMETERS]")
print("[M_1] \n", M_1)
print("[M_2] \n", M_2)
print("[S] \n", S, "\n")

print("[ALICE PUBLIC KEY]")
print(a_pub)

print("[BOB PUBLIC KEY]")
print(b_pub, "\n")

print("[ALICE COMMON SECRET]")
print(common_secret_a)

print("[BOB COMMON SECRET]")
print(common_secret_b)
# Addition: a V b = max(a, b)
# Multiplication: a Λ b = min(a, b)