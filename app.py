from clientes import Cliente, adicionar_cliente, eliminar_cliente, listar_clientes
from quartos import Quarto
from reservas import reservar, listar_reservas, cancelar_reserva, reservas
from datetime import date

clientes = [
    Cliente("Ricardo ABCD", "email@email.pt", "919191919"),
    Cliente("Daniel ABCD", "email1@email.pt", "911191919"),
    Cliente("Andreia DCBA", "email21@email.pt", "911181919"),
    Cliente("Manuela CBDA", "email13@email.pt", "911191919"),
    Cliente("Zé DACB", "email221@email.pt", "911591919"),
    Cliente("Joaquina ABCD", "email1@email.pt", "913791919"),
    Cliente("Maria ABCD", "email112@email.pt", "914491919")
]

quartos = [
    Quarto("Quarto 1"),
    Quarto("Quarto 2"),
    Quarto("Quarto 3"),
    Quarto("Quarto 4"),
]

reservar(clientes[0], quartos[0], date(2025, 10, 20), date(2025, 10, 25))
reservar(clientes[1], quartos[1], date(2025, 10, 18), date(2025, 10, 22))
reservar(clientes[2], quartos[2], date(2025, 10, 15), date(2025, 10, 17))


def menu_principal():
    return int(input("1. Gestão de clientes\n" \
        "2. Gestão de reservas\n"
        "3. Sair\n" \
        "\nSelecione a opção pretendida: "))

def menu_gestao_clientes():
    return int(input("\nOpções disponíveis:\n" \
            "1. Atualizar email do cliente\n" \
            "2. Atualizar o contacto telefónico do cliente\n" \
            "3. Adicionar cliente\n" \
            "4. Eliminar cliente\n" \
            "5. Voltar atrás\n" \
            "\nSelecione a opção pretendida: "))

def menu_gestao_reservas():
    return int(input("\nOpções disponíveis:\n" \
            "1. Efetuar reserva\n" \
            "2. Cancelar reserva\n" \
            "3. Listar reservas\n" \
            "4. Voltar atrás\n" \
            "\nSelecione a opção pretendida: "))

operacao = 0

print("Bem vindo ao sistema de gestão de reservas!\n")

print("Reservas atuais:")
print(listar_reservas())
print()

while operacao != 3:
    operacao = menu_principal()
    match operacao:
        case 1:
            print("\n---------- LISTA DE CLIENTES ----------")
            print(listar_clientes(clientes))

            operacao1 = menu_gestao_clientes()

            match operacao1:
                case 1:
                    print("\n---------- Atualizar Email ----------")
                    cliente = int(input("Insira o ID do cliente: "))
                    print(f"Cliente selecionado: {clientes[cliente]}")
                    email = input("Insira o novo email: ")
                    clientes[cliente].atualizar_email(email)
                case 2:
                    print("\n---------- Atualizar Contacto Telefónico ----------")
                    cliente = int(input("Insira o ID do cliente: "))
                    print(f"Cliente selecionado: {clientes[cliente]}")
                    telefone = input("Insira o novo contacto: ")
                    clientes[cliente].atualizar_telefone(telefone)       
                case 3:
                    print("\n---------- Adicionar Cliente ----------")
                    nome = input("Insira o nome do cliente: ")
                    email = input("\nInsira o email do cliente: ")      
                    telefone = input("\nInsira o telefone do cliente: ") 
                    novo_cliente = Cliente(nome, email, telefone)  
                    adicionar_cliente(clientes, novo_cliente)
                    print(f"\nCliente {novo_cliente} adicionado com sucesso!")
                case 4:
                    print("\n---------- Eliminar Cliente ----------")
                    cliente = clientes[int(input("Insira o ID do cliente a eliminar: "))]
                    eliminar_cliente(clientes, cliente)
                    print(f"\nCliente {cliente} eliminado com sucesso!")
                case 5:
                    continue
                case _:
                    print("Opção não permitida")

        case 2:
            print("\n---------- GESTÃO DE RESERVAS ----------")

            operacao2 = menu_gestao_reservas()

            match operacao2:
                case 1:
                    print("\n---------- LISTA DE CLIENTES ----------")
                    print(listar_clientes(clientes))
                    cliente = clientes[int(input("Insira o ID do cliente: "))]
                    print(f"Cliente selecionado: {cliente}")
                    print("\n---------- LISTA DE QUARTOS ----------")
                    for i, q in enumerate(quartos, start=1):
                        reservas_quarto = [r for r in reservas if r.quarto is q]
                        info_res = ", ".join([f"{r.checkin}->{r.checkout}" for r in reservas_quarto]) or "Sem marcações"
                        print(f"{i} - {q.nome} - Marcações: {info_res}")
                    quarto = quartos[int(input("Insira o ID do quarto: "))-1]
                    print(f"Quarto selecionado: {quarto.nome}")
                    entrada = date.fromisoformat(input("Insira a data de entrada (YYYY-MM-DD): "))
                    saida = date.fromisoformat(input("Insira a data de saída (YYYY-MM-DD): "))
                    reserva = reservar(cliente, quarto, entrada, saida)
                    print(reserva)
                case 2:
                    print("\n---------- CANCELAR RESERVA ----------")
                    print(listar_reservas())
                    idx = int(input("Insira o ID da reserva a cancelar: "))
                    msg = cancelar_reserva(idx)
                    if msg:
                        print(msg)
                    else:
                        print("Índice inválido.")
                case 3:
                    print("\n---------- LISTAR RESERVAS ----------")
                    print(listar_reservas())
                    print()
                case 4:
                    continue

        case 3:
            print("A sair...")
        case _:
            print("Opção não permitida")