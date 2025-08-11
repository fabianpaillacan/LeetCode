# Add Binary
# Given two binary strings a and b, return their sum as a binary string.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        suma = (int(a,2))+ (int(b,2)) # Convertir a decimal, entero y luego sumar
        return bin(suma)[2:] # Convertir a binario y quitar el prefijo '0b' con el [2:]