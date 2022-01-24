lista = [6,14,11,3,2,1,15,19]

def ordenarLista(lista):
    return(sorted(lista))

def ordenarListaRev(lista):
    return(sorted(lista, reverse=True))

def estaEnRango(valor,minimo,maximo):
    if valor >= minimo and valor <= maximo:
        return("Está en rango")
    else:
        return("No está en rango")

def estaEnLista(valor, lista):
    boolean = 0
    for digito in lista:
        if valor == digito:
            boolean = boolean + 1
    if boolean > 0:
        return("Está en la lista")
    else:
        return("No está en la lista")
        
print(ordenarLista(lista))

print(ordenarListaRev(lista))

print(estaEnRango(10,1,15))

print(estaEnRango(10,1,9))

print(estaEnLista(10,lista))

print(estaEnLista(11,lista))