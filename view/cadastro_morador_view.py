import os
from typing import Morador

class CadastrarMoradorView:
    def cadastrar_morador_view(self):
        print("Cadastrar Morador")
        nomemorador = input("Nome: ")
        cpfmorador = input("CPF: ")
        emailmorador = input("Email: ")
        senhamorador = input("Senha: ")
        telefonemorador = input("Telefone: ")
        return nomemorador, cpfmorador, emailmorador, senhamorador, telefonemorador