'''
LISTAS

Una lista es una estructura de datos que contiene una secuencia de elementos de cierto tipo,
las listas NO SON ARREGLOS, ya que las listas no tiene un tamaño fijo un arreglo si; esta
caracteristica las hace flexibles y muy atractivas para diferentes soluciones de desarrollo.

Para mantener esta flexibilidad de crecimiento es necesario implementar una Llista enlazada, la cual
permite instanciar elementos en memoria de forma no secuencialy recalco en memoria, de forma logica si
lo debe de ser.

LISTA ENLAZADA

Una lista enlazada Es una coleccion de objetos llamados nodos el cual cada uno de ellos contiene un campo interno
que apunta al siguiente incremento, lo cual permitira realizar un recorrido transversal por la estructura
'''

class Nodo:
    def __init__(self,value, siguiente=None):
        self.data = value
        self.next = siguiente


class LinkedList:

    def __init__(self):
        self.head=None #solamente se requiere una sola variable para referenciar al elemento 


    def is_empty(self):
        return self.head ==None

    def tall(self):
        curNode= self.head
        while curNode.next != None:
            curNone = curNone.next
        return curNone

    def append(self,valuecurNode= self.head
        while curNode.next != None:
            curNone = curNone.next
        curNode.next= Nodo(value)#su proxima referencia sera el valor introducido'''
        self.tall().next=Nodo(value)

    def prepend(self,value):
        self.head=Nodo(value,head)

    
        

        
        
        















