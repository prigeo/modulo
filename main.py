# Importar o módulo
import os
from modulo import *

# Programa princial
if __name__ == '__main__':
    while True:
        exibir_menu()
        opcao = input('Opção desejada: ')
        os.system('cls')

        match opcao:
            case '1':
                b = int(input('Base do quadrilátero: '))
                h = int(input('Altura do quadriláterp: '))
                print(f'Área: {calcular_quadrilateros(b,h)}')
                continue
            case '2':
                r = int(input('Raio do círculo: '))
                print(f'Área: {calcular_circulo(r)}')
                continue
            case '3':
                b = int(input('Base do triãngulo:  '))
                h = int(input('Altura do triângulo: '))
                print(f'Área: {calcular_triangulo(b,h)}')
                continue
            case '4':
                b_menor = int(input('Base menor: '))
                b_maior = int(input('Base maior: '))
                h = int(input('Altura do trapézio: '))
                continue
            case '5':
                break