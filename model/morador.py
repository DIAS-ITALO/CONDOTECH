""" from reserva import Reserva """

class Morador:
    def __init__(self, name, cpf, email, keyword, number_phone):
        self.nome = name
        self.cpf = cpf
        self.email = email
        self.keyword = keyword
        self.number_phone = number_phone
        
    def criar_reserva(self, dia, init_time, time_over):
        self.dia = dia 
        self.init_time = init_time
        self.time_over = time_over
        print(self.nome, "sua reserva foi registrada para ", dia, "com início em ", init_time,"h e finalização em", time_over,"h")
        
morador1 = Morador("Ana", 38641808809, "aninha@gmail.com", "ana123456", 17995651010)


morador1.criar_reserva(12, 12:00, 14:00)