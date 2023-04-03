import numpy as np

C = 4
A = np.random.random((4, C))
B = np.random.random((C, 1))
print(f"A is : \n\n {A}\n\n")
print(f"B is : \n\n {B}\n\n")

ans = np.linalg.lstsq(A, B, rcond=None)[0]

print(f"approximate solution : \n\n {ans}\n\n")

print(f"approximate B : \n\n{A@ans}")
