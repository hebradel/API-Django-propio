salir=False
cuenta=500
print('#####################\n# Cajero automatico #\n#####################\n')

while not salir:
    print(' 1.Depositar\n 2.Retirar\n 3.Saldo \n 4.Salir')
    num=int(input(' Opcion: '))
    if num==1:
        cuenta+=int(input('\nIngrese monto: '))
        print(f'Saldo: {cuenta}\n')
    if num==2:
        monto=int(input('\nIngrese monto: '))
        if cuenta<monto:
            print(f'Saldo insuficiente, saldo actual: {cuenta}\n')
        else:
            cuenta-= monto
            print(f'Saldo: {cuenta}\n')
    if num==3:
        print(f'\nSu Saldo es: {cuenta}\n')
    if num==4:
        print('\nSaliendo del cajero automatico.....')
        salir=True