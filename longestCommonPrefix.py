strs = ["flower","flow","flight"]

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
   
        if not strs:  # Si la lista está vacía
            print("No hay palabras para comparar")
            output = ""
        else:
            firstWord = strs[0]
            output = ""
            
            for letra in firstWord:
                isAll = True
                for palabra in strs[1:]:
                    if letra not in palabra:
                        isAll = False
                        break
                if isAll:
                    output += letra
                else:
                    break  
        return output