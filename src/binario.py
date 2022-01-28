def esBinario(strbinario):
    var = 1
    for digito in strbinario:
        if digito != '0' and digito != '1':
            var = 0
    if (var == 0):
        return False
    else:
        return True

def binarioDecimal(strbinario):
    if esBinario(strbinario) == True:
        return(int(strbinario, 2))
    else:
        return("El número no es binario")
    
        
print(esBinario("1001"))

print(esBinario("Hola"))

print(binarioDecimal("111"))

print(binarioDecimal("Hola"))
