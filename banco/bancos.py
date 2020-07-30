class Bancos:
    def __init__(self):
        self.agencias = [1111, 2222, 3333]
        self.clientes = []
        self.contas = []

    def inserir_clientes(self,clientes):
        self.clientes.append(clientes)

    def inserir_conta(self, conta):
        self.contas.append(conta)

    def autenticar(self, cliente):
        if cliente not in self.clientes:
            return None
        if cliente.conta not in self.contas:
            return False

        if cliente.conta.agecia not in self.agencias:
            return False

        return True
