from listas_enlazadas import Nodo

def main():
    a = Nodo(10)
    b = Nodo(20)
    c = Nodo(30)
    d = Nodo(40)
    print(c.data)# --> nodo separado
    a.next=b # --> a deja de ser none y ahora sera b
    b.next=c
    c.next=d
    d.next = Nodo(50)

    #¿Como acceder al valor de b por medio del nodo A?????
    print(a.next.data)#a.next # --> esto es equivalente a 'b'
    print(a.next.next.next.data) # ---> accediendo desda al d

    contador = 0
    tmp = a.next
    contador += 1
    while tmp !=None:
        #a.next= d.next
        contador +=1
        tmp = tmp.next
    print(contador)
        

main()
