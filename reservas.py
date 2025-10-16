from datetime import date, timedelta


from clientes import Cliente
from quartos import Quarto


class Reserva:
    def __init__(self, cliente: Cliente, quarto: Quarto, checkin: date, checkout: date):
        self.cliente = cliente
        self.quarto = quarto
        self.checkin = checkin
        self.checkout = checkout


reservas = []


def quarto_disponivel(quarto: Quarto, entrada: date, saida: date):
    """Verifica se o quarto está disponível entre duas datas [entrada, saida)."""
    for r in reservas:
        if r.quarto is quarto:
            # sobreposição se intervalos se intersectarem: [a,b) e [c,d)
            if not (saida <= r.checkin or entrada >= r.checkout):
                return False
    return True


def reservar(cliente: Cliente, quarto: Quarto, entrada: date, saida: date):
    """Cria uma reserva se o quarto estiver disponível em todo o intervalo."""
    if entrada >= saida:
        return "Intervalo de datas inválido (entrada deve ser menor que saída)."

    if not quarto_disponivel(quarto, entrada, saida):
        return f"Quarto {quarto.nome} indisponível entre {entrada} e {saida}"

    reservas.append(Reserva(cliente=cliente, quarto=quarto, checkin=entrada, checkout=saida))
    return f"Reserva efetuada com sucesso.\n{quarto.nome}: {cliente.nome} de {entrada} a {saida}"


def listar_reservas():
    if not reservas:
        return "(Sem reservas)"
    linhas = []
    for i, r in enumerate(reservas):
        linhas.append(f"{i} - {r.quarto.nome}: {r.cliente.nome} de {r.checkin} a {r.checkout}")
    return "\n".join(linhas)


def cancelar_reserva(indice: int):
    if 0 <= indice < len(reservas):
        r = reservas.pop(indice)
        return f"Reserva cancelada: {r.quarto.nome} - {r.cliente.nome} de {r.checkin} a {r.checkout}"
    return None