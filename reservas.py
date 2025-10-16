from clientes import Cliente
from quartos import Quarto
from datetime import date

def reservar(cliente: Cliente, quarto: Quarto, entrada: date, saida):
    data = entrada
    while data < saida:
        if not quarto.esta_disponivel(data):
            return f"Quarto {quarto.nome} indisponível  na data {data}"
        data += timedelta(day=1)

    quarto.nova_marcacao(entrada, saida)
    return f"Reserva efetuada com sucesso.\n{quarto.nome}: {cliente.nome} de {entrada} a {saida}"