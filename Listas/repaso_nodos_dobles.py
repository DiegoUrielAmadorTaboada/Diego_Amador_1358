class NodoDoble:
    def __init__(self,value,siguiente,previo):
        self.data = value
        self.next = siguiente
        self.prev= previo

def main():
    head = NodoDoble(None,None,None)
    tail = NodoDoble(None,None,None)
    head.next = tail
    tail.prev = head
    nuevo = NodoDoble(6,tail,head)
    head.next = nuevo
    tail.prev = nuevo

main()
