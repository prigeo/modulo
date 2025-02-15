from datetime import date

# função menu
def exibir_menu():
    meses = ('Janeiro', "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", 'Dezembro')
    dia = date.today().day
    mes = date.today().month
    ano = date.today().year
    print(f'\n{dia} de {meses[mes-1]} de {ano}.\n')
    print('1 - Calcular quadrilátero')
    print('2 - Calcular circulo')
    print('3 - Calcular triângulo')
    print('4 - Calcular trapézio')
    print('5 - Sair do programa')


# função que calcular quadrilatero
def calcular_quadrilateros(b,h):
    a = b*h
    return a

# função da circunferência
def calcular_circulo(r):
    a = 3.14*r**2
    return a

# Função do triângulo
def calcular_triangulo(b,h):
    a = (b*h)/2
    return a

# Função do trapézio
def calcular_trapezio(b_menor, b_maior, h):
    a = ((b_menor+b_maior)*h)/2
    return a
