def codificar(m,n):
	resultado =2**m * (2*n +1)
	return resultado

def fst(k):
	contador = 0
	while k % 2 == 0:
		k=k//2
		contador=contador+1
	return contador

def snd(k):
	while k % 2 == 0:
		k=k//2
	resultado=(k-1)//2
	return resultado

def decodificar(k):
	valor1 = fst(k)
	valor2 = snd(k)
	return valor1, valor2

