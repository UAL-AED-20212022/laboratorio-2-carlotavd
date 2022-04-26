from models.LinkedList import LinkedList

def main():
    lista_ligada = LinkedList()
    while True:
        try:
            comandos = input().split(" ")
        except EOFError:
            return

        #Registar o país no inicio da lista.
        if comandos[0] == "RPI":
            RPI(comandos[1], lista_ligada)

        #Registar o país no fim da lista.
        elif comandos[0] == "RPF":
            RPF(comandos[1], lista_ligada)

        #Registar o país depois de outro elemento da registado.
        elif comandos[0] == "RPDE":
            RPDE(comandos[2], comandos[1], lista_ligada)

        #Registar o país antes de outro elemento da registado.
        elif comandos[0] == "RPAE":
            RPAE(comandos[2], comandos[1], lista_ligada)

        #Registar o país num determinado indice.
        elif comandos[0] == "RPII":
            RPII(int(comandos[2]), comandos[1], lista_ligada)

        #Verificar o número de elementos da lista.
        elif comandos[0] == "VNE":
            VNE(lista_ligada)

        #Verificar se um país se encontra na lista.
        elif comandos[0] == "VP":
            VP(comandos[1], lista_ligada)

        #Eliminar o primeiro elemento da lista.
        elif comandos[0] == "EPE":
            EPE(lista_ligada)

        #Eliminar o último elemento da lista.
        elif comandos[0] == "EUE":
            EUE(lista_ligada)

        ##Eliminar um determiado país da lista.
        elif comandos[0] == "EP":
            EP(comandos[1], lista_ligada)


#Esta função serve para o país que for introduzido pelo utilizador seja inserido no inicio da lista.
def RPI(pais_novo, lista_ligada):
    lista_ligada.insert_at_start(pais_novo)
    lista_ligada.traverse_list()

#Esta função serve para o país que for introduzido pelo utilizador seja inserido no fim da lista.
def RPF(pais_novo, lista_ligada):
    lista_ligada.insert_at_end(pais_novo)
    lista_ligada.traverse_list()

#Esta função serve para o novo país introduzido pelo utilizador seja inserido depois do país já registado e indicado pelo utilizador.  
def RPDE(pais_registado, pais_novo, lista_ligada):
    lista_ligada.insert_after_item(pais_registado, pais_novo)
    lista_ligada.traverse_list()

#Esta função serve para o novo país introduzido pelo utilizador seja inserido antes do país já registado e indicado pelo utilizador.
def RPAE(pais_registado, pais_novo, lista_ligada):
    lista_ligada.insert_before_item(pais_registado, pais_novo)
    lista_ligada.traverse_list()

#Esta função serve para o novo país introduzido pelo utilizador seja inserido no indice indicado pelo mesmo.
def RPII(indice, pais_novo, lista_ligada):
    lista_ligada.insert_at_index(int(indice), pais_novo)
    lista_ligada.traverse_list()

#Esta função serve para retornar o número de elementos presentes na lista.
def VNE(lista_ligada):
    print(f"O número de elementos são {lista_ligada.get_count()}.")

#Esta função serve para verificar se um determinado País se encontra na lista. 
def VP(nome_pais, lista_ligada):
    if lista_ligada.search_item(nome_pais):
        print(f"O país {nome_pais} encontra-se na lista.")
    else:
        print(f"O país {nome_pais} não se encontra na lista.")

#Esta função serve para eliminar o primeiro elemento da lista.
def EPE(lista_ligada):
    l = lista_ligada.start_node.item
    lista_ligada.delete_at_start()
    print(f"O país {l} foi eliminado da lista.")

#Esta função serve para eliminar o último elemento da lista.
def EUE(lista_ligada):
    l = lista_ligada.get_last_node()
    lista_ligada.delete_at_end()
    print(f"O país {l} foi eliminado da lista.")

#Esta função serve para eliminar um determinado país da lista.
def EP(nome_pais, lista_ligada):
    if lista_ligada.search_item(nome_pais) == True:
        lista_ligada.delete_element_by_value(nome_pais)
        print(f"O país {nome_pais} foi eliminado da lista.")
    else:
        print(f"O país {nome_pais} não se encontra na lista.")

