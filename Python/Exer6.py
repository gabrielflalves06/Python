
Peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))


IMC = Peso/ (altura*altura)


if IMC < 18.5:
    print(f'Seu IMC é de {IMC:.1f}, Você está Abaixo do peso')
elif IMC > 18.5 and IMC < 25:
    print(f'Seu IMC é de {IMC:.1f}, Você está no peso ideal')
elif IMC > 25 and IMC < 30:
    print(f'Seu IMC é de {IMC:.1f}, Você está no Sobrepeso')
else:
    print(f'Seu IMC é de {IMC:.1f}, Você está na Obesidade')