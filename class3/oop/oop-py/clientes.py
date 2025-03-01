class Cliente(abc):
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo
    
    def retirar(self, monto):
        self.saldo -= monto
    
    def depositar(self, monto):
        self.saldo += monto

    @abstractmethod
    def crear_cuenta(self, nombre, salgo, extra):
        pass

class UnderAgeClient(Client):
    
    def retirar(self, monto):
        raise Exception("No puedes retirar dinero si eres menor de edad")
    
    def crear_cuenta(self, nombre, saldo, extra):
        super().__init__(nombre, saldo)
        self.acudiente = extra.acudiente
    

class InternationalClient(Client):

    def retirar(self,monto):
        self.saldo -= monto * 1.2
        # Depositar el 20% adicional en la cuenta del banco

