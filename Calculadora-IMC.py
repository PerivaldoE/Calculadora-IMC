def calculo_imc(peso, altura):
    imc = peso / (altura * altura)
    if imc < 16 :
        categoria = "Abaixo do peso(Grau I)"
    elif 16 <= imc < 16.99:
        categoria = "Abaixo do peso(Grau II)"
    elif 17 <= imc < 18.49:
        categoria = "Abaixo do peso(Grau III)"
    elif 18.50 <= imc < 24.99:
        categoria = "Peso adequado"
    elif 25 <= imc < 29.99:
        categoria = "Sobrepeso"
    elif 30<= imc < 34.99:
        categoria = "Obesidade (Grau I)"
    elif 35<= imc < 39.99:
        categoria = "Obesidade (Grau II)"
    else:
        categoria = "Obesidade (Grau III)"

    return imc, categoria

def main ():
    print("Cálculando Índice de Massa Corporal (IMC)")
    
    peso=float(input("Digite deu peso em KG:  "))
    altura=float(input("Digite sua altura:  "))

    imc, categoria = calculo_imc(peso, altura)

    print(f"\nSeu IMC é: {imc:.2f}")
    print(f"Categoria: {categoria}")

if __name__ == "__main__":
    main()