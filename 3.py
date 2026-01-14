import numpy as np
r = int(input("Rows of A: "))
c = int(input("Columns of A: "))
print("Enter elements of A:")
A = np.array([list(map(int, input().split())) for _ in range(r)])
print("Enter elements of B:")
B = np.array([list(map(int, input().split())) for _ in range(r)])
print("\nMatrix A - Matrix B =\n", A -B)