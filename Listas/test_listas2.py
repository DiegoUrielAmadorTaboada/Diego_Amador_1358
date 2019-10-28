
from listas_enlazadas import Nodo

def main():
    head = Nodo(10)
    head.next=Nodo(20,Nodo(30))
    head=Nodo(5,head)



    aux = head
    while(aux.next!= None):
        print("->",aux.data, end="")
        aux=aux.next
    print("->",aux.data, end="")

main()
