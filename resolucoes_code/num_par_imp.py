# Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. Uma dica é: Utilize condicionais para realizar a verificação e, se possível, faça uso do Github Copilot(ou outra IA) para otimizar a estrutura do código.

numero = int(input("Digite um numero inteiro: "))

if numero % 2 == 0:
    print("O número {numero} é par.")
else:
    print("O número {numero} é ímpar.")