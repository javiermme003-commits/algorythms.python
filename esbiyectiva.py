#Dominio y codominio ejemplo#

dom = [1,2,3,4]

codom = ["a","b","c"]

imag = ["a", "b", "b", "c"]

#Definición de la función#

def es_sobreyectiva(imag, codom):
    for elem in codom:
        if elem not in imag:
            return False
    return True

def es_inyectiva(imagenes):
    for i in range(len(imagenes)):
        for j in range(i+1, len(imagenes)):
            if imagenes[i]==imagenes[j]:
                return False
    return True

def es_biyectiva(imag,codom):
    if es_inyectiva(imag)==False:
       return False
    elif es_sobreyectiva(imag, codom)==False:
        return False
    else:
        return True
