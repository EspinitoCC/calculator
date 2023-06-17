while True:
print('-----Menu Calculadora-----')
print('Comandos: ')
print('1 = Somar')
print('2 = Subtrair')
print('3 = Multiplicar')
print('4 = Dividir')
print('--------------------------')
comando = int(input('Digite seu comando: '))
n2 = float(input('Digite seu primeiro numero: '))
n1 = float(input('Digite seu segundo numero: '))
if comando == 1:
print(f'O resultado é: {n1 + n2}')
elif comando == 2:
print(f'O resultado é: {n1-n2}')
elif comando == 3:
print(f'O resultado é: {n1*n2}')
elif comando == 4:
print(f"O resultado é: {n1%n2}")
elif comando == 0:
break
else: print('Este comando é invalido')
