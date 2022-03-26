times = ('Palmeiras', 'Santos', 'Flamengo', 'Internacional',
         'Atlético-PR', 'Botafogo', 'Corinthians', 'Grêmio',
         'Bahia', 'São Paulo', 'Vasco da Gama', 'Fluminense')

menu = int(input('''
[ 1 ] Imprimir toda a lista de times.
[ 2 ] Imprimir os 5 primeiros colocados.
Sua Opção: '''))

if menu == 1:
    for time in range(0, 11):
        print(f'{time+1}º {times[time]}')
elif menu == 2:
    for time in range(0, 5):
        print(f'{time + 1}º {times[time]}')
else:
    print('Opção Inválida.')