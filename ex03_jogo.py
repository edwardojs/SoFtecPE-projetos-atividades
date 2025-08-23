import random

def pedra_papel_tesoura():
    opcoes = ["pedra", "papel", "tesoura"]
    usuario = input("Escolha: pedra, papel ou tesoura: ").lower()

    if usuario not in opcoes:
        print("Opção inválida!")
        return

    computador = random.choice(opcoes)
    print(f"Você escolheu: {usuario}")
    print(f"O computador escolheu: {computador}")

    if usuario == computador:
        print("Empate!")
    elif (usuario == "pedra" and computador == "tesoura") or \
         (usuario == "tesoura" and computador == "papel") or \
         (usuario == "papel" and computador == "pedra"):
        print("Você venceu!")
    else:
        print("O computador venceu!")

if __name__ == "__main__":
    pedra_papel_tesoura()