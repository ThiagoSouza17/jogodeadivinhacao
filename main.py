print("*********************************")
print("Bem-vindo ao Jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_chutes = 3
rodada = 1

while(rodada <= total_de_chutes):
    print("Tentativa {} de {}".format(rodada, total_de_chutes))
    chute = int(input("Digite o seu número: "))
    print("Você digitou: ", chute)

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou!")
    else:
        if(maior):
            print("Você errou! O seu chute foi maior que o número secreto!")
        elif(menor):
            print("Você errou! O seu chute foi menor que o número secreto!")
    rodada = rodada + 1

print("Fim do Jogo!")


