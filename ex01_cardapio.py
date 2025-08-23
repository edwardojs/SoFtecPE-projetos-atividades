def cardapio():
    print("=== CARDÁPIO ===")
    menu = {
        1: ("Hambúrguer", 25.00),
        2: ("Batata Frita", 15.00),
        3: ("Refrigerante", 8.00)
    }

    for codigo, (item, preco) in menu.items():
        print(f"{codigo} - {item} - R${preco:.2f}")

    try:
        escolha = int(input("Digite o código do item desejado: "))
        if escolha in menu:
            item, preco = menu[escolha]
            print(f"Você escolheu: {item} - R${preco:.2f}")
        else:
            print("Opção inválida.")
    except ValueError:
        print("Entrada inválida, digite apenas números.")

if __name__ == "__main__":
    cardapio()