from cuentaBancaria import CuentaBancaria

class Usuario:
    def __init__(self, name="n/a", numero_de_cuentas=1, tasa_interés=0.01):
        self.name = name
        self.cuenta = []
        self.numero_de_cuentas = numero_de_cuentas
        for i in range(0, self.numero_de_cuentas):
            self.cuenta.append(CuentaBancaria(tasa_interés, balance=0))

    def hacer_depósito(self, amount=0, n=1):
        self.cuenta[n-1].depósito(amount)
        return self
    
    def hacer_retiro(self, amount=0, n=1):
        self.cuenta[n-1].retiro(amount)
        return self

    def mostrar_balance_usuario(self):
        valor = "User: " + self.name
        for i in range(0, self.numero_de_cuentas):
            valor = valor + ", Balance " + str(i+1) + ": " + str(self.cuenta[i].balance)
        print(valor)
        print(" ")
        return self
    
    def transferir_dinero(self, amount=0, n1=1, name="n/a", n2=1):
        self.cuenta[n1-1].retiro(amount)
        name.cuenta[n2-1].depósito(amount)
        return self
    
    def generar_interes(self, n=1):
        self.cuenta[n-1].interes()
        return self