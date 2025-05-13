#no me esta funcionando el test, con un arreglo de flower, flower, flower
#solo me imprime fff, y no flower

strs = ["flower", "flow", "flight"]

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:  
            return ""

        if all(s == strs[0] for s in strs):
            if strs[0]: 
                return strs[0][0] * len(strs)
            else:
                return ""

        # Caso general: encontrar el prefijo común
        output = ""
        for i in range(len(strs[0])):
            current_char = strs[0][i]
            for word in strs[1:]:
                if i >= len(word) or word[i] != current_char:
                    return output
            output += current_char
        return output
