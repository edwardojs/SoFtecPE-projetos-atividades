def par_ou_impar():
    try:
        numero = int(input("Digite um número inteiro: "))
        if numero % 2 == 0:
            print(f"O número {numero} é PAR.")
        else:
            print(f"O número {numero} é ÍMPAR.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

if __name__ == "__main__":
    par_ou_impar()