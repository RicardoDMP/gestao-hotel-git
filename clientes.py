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
    


def adicionar_cliente(clientes: list, cliente: Cliente):
    """Adiciona um cliente à lista de clientes"""

    clientes.append(cliente)
    return cliente

def eliminar_cliente(clientes: list, cliente: Cliente):
    """Elimina um cliente da lista de clientes"""

    if cliente in clientes:
        clientes.remove(cliente)
        return f"Cliente {cliente} eliminado com sucesso"
    

def listar_clientes(clientes: list):
    """Retorna todos os clientes em formato legível com índice."""
    return "\n".join(f"{i} - {c}" for i, c in enumerate(clientes))