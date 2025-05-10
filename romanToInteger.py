class Solution:
    def romanToInt(self, s: str) -> int:
        diccionario = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        result = 0

        for i in s:
            if i in diccionario:
                result = result + diccionario[i]
        
        return result 
    # me falta saber cuando hay IV y esos tipos de casos