class Cliente:
    """
    Classe que representa um cliente do hotel.
    """

    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def atualizar_email(self, novo_email):
        """Atualiza o email do cliente."""
        self.email = novo_email

    def atualizar_telefone(self, novo_telefone):
        """Atualiza o número de telefone do cliente."""
        self.telefone = novo_telefone

    def __str__(self):
        """Retorna uma representação legível do cliente."""
        return f"Cliente: {self.nome} ({self.email}, {self.telefone})"
    
clientes = [
    Cliente("Ricardo ABCD", "email@email.pt", "919191919"),
    Cliente("Daniel ABCD", "email1@email.pt", "911191919"),
    Cliente("Andreia DCBA", "email21@email.pt", "911181919"),
    Cliente("Manuela CBDA", "email13@email.pt", "911191919"),
    Cliente("Zé DACB", "email221@email.pt", "911591919"),
    Cliente("Joaquina ABCD", "email1@email.pt", "913791919"),
    Cliente("Maria ABCD", "email112@email.pt", "914491919")
]

def adicionar_cliente(cliente: Cliente):
    """Adiciona um cliente à lista de clientes"""

    clientes.append(cliente)
    return cliente

def eliminar_cliente(cliente: Cliente):
    """Elimina um cliente da lista de clientes"""

    for c in clientes:
        if c == cliente:
            clientes.remove(c)
            return f"Cliente {c} eliminado com sucesso"
    

def listar_clientes():
    """Lista todos os clientes"""

    for c in clientes:
        print(c)
