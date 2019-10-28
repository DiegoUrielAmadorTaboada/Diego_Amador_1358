from listas_doblementeenlazadas import ListaDoblementeEnlazada


def main():
    ldl = ListaDoblementeEnlazada()
    print(f" Tamaño = {ldl.get_size()}")
    ldl.insert(10)
    ldl.insert(20)
    ldl.insert(30)
    ldl.insert(40)

    ldl.insert(50)
    ldl.transversal()
    ldl.reverse_transversal()
    ldl.find_from_head(10)
    ldl.find_from_tail(30)
    ldl.remove_from_head(30)
    

main()

    
