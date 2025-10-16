class Quarto:
    def __init__(self, nome):
        self.nome = nome
        self.marcacoes = []  # list of dicts: {"checkin": date, "checkout": date}

    def nova_marcacao(self, checkin, checkout):
        """Adiciona uma nova reserva, represented as a date range."""
        self.marcacoes.append({"checkin": checkin, "checkout": checkout})

    def esta_disponivel(self, data):
        """Verifica se o quarto está disponível numa data."""
        for reserva in self.marcacoes:
            if reserva["checkin"] <= data < reserva["checkout"]:
                return False
        return True