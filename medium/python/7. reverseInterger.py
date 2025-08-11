class Solution:
    def retornar(self):
        return 0

    def comprobacion(self, numero):
        return numero if -2**31 <= numero <= 2**31 - 1 else self.retornar()

    def reverse(self, x: int) -> int:
        signo = -1 if x < 0 else 1
        res = list(map(int, str(abs(x))))
        res.reverse()
        numero = int("".join(map(str, res))) * signo
        return self.comprobacion(numero)