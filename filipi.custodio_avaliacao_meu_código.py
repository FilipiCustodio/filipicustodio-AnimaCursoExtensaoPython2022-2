print("Olá caro colaborador, seja bem vindo ao meu código, aqui você consegue calcular o valor do seu reajuste salárial")

nome = input("Digite seu nome: ")

print(nome + ", qual o valor do seu salario?")

salario = float(input())

print("Qual sera o aumento salarial?")

porcentagem = float(input())

aumento = salario*porcentagem/100
salarioFinal = salario + aumento

print(nome + ", o valor do seu aumento será R$%.2f" % aumento)

print(nome + ", o valor do seu salario final será R$%.2f" % salarioFinal) 

print(nome + " Muito Obrigado por utilizar o nosso programa")

input()


