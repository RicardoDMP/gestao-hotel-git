from clientes import Cliente, adicionar_cliente, eliminar_cliente, listar_clientes
from quartos import Quarto
from reservas import reservar
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

operacao = 0

print("Bem vindo ao sistema de gestão de reservas!\n")

while operacao != 3:
    operacao = menu_principal()
    match operacao:
        case 1:
            print("\n---------- LISTA DE CLIENTES ----------")
            print(listar_clientes(clientes))

            operacao1 = menu_gestao_clientes()

            match operacao1:
                case 1:
                    cliente = int(input("Insira o ID do cliente: "))
                    print(f"Cliente selecionado: {clientes[cliente]}")
                    email = input("Insira o novo email: ")
                    clientes[cliente].atualizar_email(email)
                case 2:
                    cliente = int(input("Insira o ID do cliente: "))
                    print(f"Cliente selecionado: {clientes[cliente]}")
                    telefone = input("Insira o novo contacto: ")
                    clientes[cliente].atualizar_telefone(telefone)       
                case 3:
                    nome = input("Insira o nome do cliente: ")
                    email = input("\nInsira o email do cliente: ")      
                    telefone = input("\nInsira o telefone do cliente: ") 
                    novo_cliente = Cliente(nome, email, telefone)  
                    adicionar_cliente(clientes, novo_cliente)
                    print(f"\nCliente {novo_cliente} adicionado com sucesso!")
                case 4:
                    cliente = clientes[int(input("Insira o ID do cliente a eliminar: "))]
                    eliminar_cliente(clientes, cliente)
                    print(f"\nCliente {cliente} eliminado com sucesso!")
                case 5:
                    break
                case _:
                    print("Opção não permitida")

        case 2:
            print("Gestão de reservas ainda não implementada.")
        case 3:
            print("A sair...")
        case _:
            print("Opção não permitida")