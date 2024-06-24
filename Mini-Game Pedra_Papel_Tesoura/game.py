import random

def game(escolha_usuario):
    opcoes=['pedra','papel','tesoura']
    escolha_computador=random.choice(opcoes)

    print("voce escolheu: ",escolha_usuario)
    print("O computador escolheu: ",escolha_computador)

    if escolha_usuario==escolha_computador:
        print("Empate!")

    elif(escolha_usuario=='pedra' and escolha_computador=='tesoura') or (escolha_usuario=='papel' and escolha_computador=='pedra') or (escolha_usuario=='tesoura' and escolha_computador=='papel'):
        print("Vencedor: Usuario!")
    
    else:
        print("Vencedor: Computador!")

print("\nEscolha uma das opcões: pedra, papel ou tesoura.")

escolha_usuario=input("Digite sua opção: ").lower()

if escolha_usuario in['pedra','papel','tesoura']:
    game(escolha_usuario)

else:
    print("escolha invalida. Por favor, escolha entre as tres opções apresentadas")