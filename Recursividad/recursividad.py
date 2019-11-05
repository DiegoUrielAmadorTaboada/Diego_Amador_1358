
def suma_lista(lista):
    #caso base
    if len(lista)==1:
        return lista[0]
    else:
        actual=lista.pop()
        return actual + suma_lista(lista)

def factorial(n):
    if n==1:
        return 1
    else:
        return n* factorial(n-1)

def main():
    lista=[3,5,2,1]
    print(f'Lista = {lista}')
    print(f'\nLa suma de los elementos{lista} es {suma_lista(lista)}')
    print("\nFactorial con recursividad")
    n=int(input("\nIngresa un valor entero: "))
    print(f'\nLa suma de {n}! factorial es {factorial(n)}')

main()
