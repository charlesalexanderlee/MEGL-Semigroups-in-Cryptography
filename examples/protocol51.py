"""
Protocol 5.1 Implementation
MEGL Semigroups in Cryprography
"""

import numpy as np

def boolean_matmul(A, B):
    """
    Perform Boolean matrix multiplication:
    (A ⊙ B)[i,j] = OR_k (A[i,k] AND B[k,j])
    """
    # Ensure boolean dtype
    A = np.array(A, dtype=bool)
    B = np.array(B, dtype=bool)
    
    # Use broadcasting to compute all (A[i,k] AND B[k,j]) pairs
    # (m x n) @ (n x p)  ->  result shape (m, p)
    result = np.any(A[:, :, None] & B[None, :, :], axis=1)

    return result.astype(int)
    
# Alice's private key
def p_a(t: np.array):
    return np.maximum(np.identity(3, dtype=int), t)

def q_a(t: np.array):
    return np.identity(3, dtype=int)

# Bob's private key
def p_b(t: np.array):
    t_squared = boolean_matmul(t, t)
    return np.maximum(t, t_squared)

def q_b(t: np.array):
    t_squared = boolean_matmul(t, t)  
    return np.maximum(np.identity(3, dtype=int), np.maximum(t, t_squared))

# Public parameters
M_1 = np.array([[0, 1, 0],
               [0, 1, 1],
               [1, 0, 0]])

M_2 = np.array([[0, 1, 0],
               [1, 0, 0],
               [0, 0, 1]])

S = np.array([[1, 0, 0],
             [0, 0, 1],
             [0, 0, 0]])

# Alice and Bob's public key
a_pub = boolean_matmul(p_a(M_1), boolean_matmul(S, q_a(M_2)))
b_pub = boolean_matmul(p_b(M_1), boolean_matmul(S, q_b(M_2)))

# Alice and Bob compute the common secret key
common_secret_a = boolean_matmul(p_a(M_1), boolean_matmul(b_pub, q_a(M_2)))
common_secret_b = boolean_matmul(p_b(M_1), boolean_matmul(a_pub, q_b(M_2)))

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
