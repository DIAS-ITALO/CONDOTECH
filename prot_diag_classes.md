#Protótipo de Diagrama de Classes

MORADOR:
- id: int
- nome: string
- cpf: string
- email: string
- numero_telefone: int 
- senha: string
+CadastrarMorador
+LogarMorador
+CadastrarReserva
+MostrarReservas
+ExcluirReserva
+AlterarReserva

GESTOR:
- id: int
- nome: string
- cpnj: string
- email: string
- numero_telefone: int
- senha:string
+LogarGestor
+MostrarReserva
+ExcluirReserva
+AlterarReserva
+CadastrarReserva


RESERVA:
- id: int
- idmorador: int
- dia: date
- horario_inicio: date
- horario_fim: date
+RegistrarReserva