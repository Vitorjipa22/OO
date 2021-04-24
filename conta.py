
class Conta:
    def __init__(self,numero,titular,saldo,limite):
        print(f"construindo o objeto {self}")
        self.numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def __pode_sacar(self,valor_saque):
        valor_disponivel = self.__saldo + self.__limite
        return (valor_saque <= valor_disponivel)

    def extrato(self):
        print(f"titular: {self.__titular} \nSaldo : {self.__saldo}")

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("Saldo indisponivel")

    def transfere(self,destino,valor):
        destino.deposita(valor)
        self.saca(valor)

    @property
    def titular(self):
        return self.__tilular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @titular.setter
    def titular(self,titular):
        self.__titular = titular

    @saldo.setter
    def titular(self, saldo):
        self.__titular = saldo

    @limite.setter
    def limite(self, limite):
        self.__titular = limite

    @staticmethod
    def codigo_banco():
        return {"BB": "001", "CAIXA" : "104", "BRADESCO" : "237" }
