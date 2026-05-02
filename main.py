import numpy as np

def matritsa_kopaytma_invers(matritsa):
    # Matritsa ko'paytmasini hisoblash
    kopaytma = np.linalg.matrix_power(matritsa, 2)
    
    # Matritsa inversini hisoblash
    invers = np.linalg.inv(matritsa)
    
    return kopaytma, invers

# Misol uchun matritsa
matritsa = np.array([[1, 2], [3, 4]])

# Matritsa ko'paytmasi va inversini hisoblash
kopaytma, invers = matritsa_kopaytma_invers(matritsa)

print("Matritsa ko'paytmasi:")
print(kopaytma)
print("\nMatritsa inversi:")
print(invers)
