import numpy as np
r = int(input("Rows of A: "))
c = int(input("Columns of A: "))
print("Enter elements of A:")
A = np.array([list(map(int, input().split())) for _ in range(r)])
print("\nTranspose of Matrix A =\n", A.T)
