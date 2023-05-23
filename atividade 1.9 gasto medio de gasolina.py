nome = input("Qual é o seu nome?")

gasto = input("{}, digite o tempo gasto na viagem (em horas): ".format(nome))

velocidade = input('{}, digite agora a velocidade média praticado na viagem: '.format(nome))

consumo = float(velocidade/12)

print("Foram gastos ", consumo, " litros de combustível.")
