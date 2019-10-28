'''
Lista Doblemente Ligadas

ADT Lista Doblemente Ligada

ListaDoblementeEnlazada()
get_size()
insert(value)
find_from_head(value)--encontar el nodo
find_from_tail(value)--hacer el nuevo nodo
remove_from_head(value)
remove_from_tail(value)
insert_between(value,predecesor,sucesor)
transversal()
reverse_transversal()

'''


class NodoDoble:
    def __init__(self, value,siguiente,previo):
        self.data= value
        self.next=siguiente
        self.prev=previo


class ListaDoblementeEnlazada:
    def __init__(self):    
        self.__head = NodoDoble(None,None,None)
        self.__tail = NodoDoble(None,None,None)
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
        self.__size = 0

    def get_size(self):
        return self.__size

    def insert(self,value):
        """inserta al final"""
        if self.__size == 0:
            nuevo = NodoDoble(value, self.__tail, self.__head)
            self.__head.next = nuevo
            self.__tail.prev = nuevo
        else:
            nuevo= NodoDoble(value,self.__tail, self.__tail.prev)
            self.__tail.prev.next = nuevo
            self.__tail.prev = nuevo


        self.__size += 1

    def transversal(self):
        curr_Node = self.__head
        while curr_Node.next != None:
            print(curr_Node.data,"->", end="")
            curr_Node=curr_Node.next
        print("")

    def reverse_transversal(self):
        curr_Node = self.__tail
        while curr_Node.prev != None:
            print(curr_Node.data,"->", end="")
            curr_Node=curr_Node.prev
        print("")

    def find_from_head(self, value):
        curr_Node = self.__head
        while curr_Node.data != value:
            curr_Node = curr_Node.next

        if curr_Node.data == value:
            encontrado = curr_Node
        return encontrado

    
    def find_from_tail(self,value):
        curr_Node = self.__tail
        while curr_Node.data != value:
            curr_Node = curr_Node.prev

        if curr_Node.data == value:
            encontrado = curr_Node
        return encontrado

         
    def remove_from_head(self,value):
        remover=0
        curr_Node = self.__head
        while curr_Node.data != value:
            curr_Node = curr_Node.next
            
        if curr_Node.data == value:
            curr_Node.head = curr_Node.next 
            curr_Node.head.prev = None
            
            print(curr_Node,"->",end="")
        else:
            
            curr_Node.tail = curr_Node.tail.prev
            curr_Node.tail.next = None
        
        print(curr_Node.head,"->",end="")
        
        
        #remover +=1
            
            

        
    #def remove_from_tail(value):

        
    #def insert_between(value,predecesor,sucesor):

   

        










        
