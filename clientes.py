class Cliente:
    """
    Classe que representa um cliente do hotel.
    """

    def __init__(self, id_cliente, nome, email, telefone):
        self.id_cliente = id_cliente
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
        return f"Cliente #{self.id_cliente}: {self.nome} ({self.email}, {self.telefone})"