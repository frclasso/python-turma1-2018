'''Exercício 8.3 - Escreva uma função que receba o lado (1) de um quadrado e
retorne sua área (A = lado2​ ​).
Valores esperados:
area_quadrado(4) == 16
area_quadrado(9) == 81'''


def area_quadrado(lado):
    return lado ** 2


def main():
    print(f'Area do quadrado(4) eh: {area_quadrado(4)}')
    print(f'Area do quadrado(9) eh: {area_quadrado(9)}')


if __name__=="__main__":main()

