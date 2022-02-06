import random

print("*********************************")
print("Bem-vindo ao Jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)
total_de_chutes = 3

print(numero_secreto)

for rodada in range(1, total_de_chutes + 1):
    print("Tentativa {} de {}".format(rodada, total_de_chutes))
    chute = int(input("Digite um número entre 1 e 100: "))
    print("Você digitou: ", chute)

    if(chute < 1 or chute >100):
        print("Você deve digitar um número entre 1 e 100!")
        continue
    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou!")
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior que o número secreto!")
        elif(menor):
            print("Você errou! O seu chute foi menor que o número secreto!")


print("Fim do Jogo!")


