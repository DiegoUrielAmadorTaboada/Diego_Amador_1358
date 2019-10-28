class Nodo:

    def __init__(self,value,siguiente=None):

        self.data = value
        self.next = siguiente

def main():
    head = Nodo(6,None)
    head.next = Nodo(12,None)
    head.next.next = Nodo(18,None)
    head.next.next.next = Nodo(24,Nodo(30,None))
    print(f"Primer Nodo = {head.data}")
    print(f"Segundo Nodo = {head.next.data}")
    print(f"Tercer Nodo = {head.next.next.data}")
    print(f"Cuarto Nodo = {head.next.next.next.data}")
    print(f"Quinto Nodo = {head.next.next.next.next.data}")

    contador = 0
    tmp = head.next
    contador += 1
    while tmp != None:
        
        print(tmp.data,"/",end="")
        contador +=1
        tmp = tmp.next
        
main()
