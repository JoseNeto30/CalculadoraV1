# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso.
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")
try:
    num1 = float(input('Insira o primeiro número: '))
    num2 = float(input('Insira o segundo número: '))
    # Removendo espaços extras
    operacao = input('Selecione uma operação (+, -, *, /):').strip()
except ValueError:
    print("Por favor, insira números válidos.")
    exit()

# Execução da operação escolhida
if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Não é possível dividir por zero.")
        exit()
else:
    print('Operação inválida.')
    exit()

    # Exibição do resultado formatado
print('O resultado é: {:.2f}'.format(resultado))
