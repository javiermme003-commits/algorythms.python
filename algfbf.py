
atomos = {"p","q","r"}

def es_atomo(A):
  return A in atomos

def es_fbf(A):
  if es_atomo(A):
    return True
  elif A != "" and A[0] == "¬":
    return es_fbf(A[1:])
  elif A != "" and A[0] == "(" and A[-1] == ")":
    contador = 0
    for i, caracter in enumerate(A):
      if caracter == "(":
        contador = contador + 1
      elif caracter == ")":
          contador = contador - 1
      elif contador == 1 and caracter in {"-", "o","&", "~"}:
        posición = i
        P=A[1:posición] 
        Q=A[posición+1:-1]
        return es_fbf(P) and es_fbf(Q)
    return False
  else:
     return False
  
