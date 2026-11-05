
def codificar(m,n):
	resultado = ((m+n)*(m+n+1))//2+m
	return resultado

def fst(k):
	j=0
	while k>(j*(j+1))//2+j: 
		j=j+1
	m=k-(j*(j+1))//2
	return m

def snd(k):
	j=0
	while k>(j*(j+1))//2+j:
		j=j+1
	n=j-fst(k)
	return n

def decodificar(k):
	valor1=fst(k)
	valor2=snd(k)
	return valor1, valor2

def dib_zigzag1(diagonales):
	ancho = len(str(diagonales-1))

	for j in range(diagonales):
		for m in range(j+1):
			n=j-m
			print(f"({m:>{ancho}},{n:>{ancho}})", end="")
		print()

def dib_zigzag2(diagonales):
	ancho= len(str(diagonales-1))
	for j in range(diagonales):
		print(" " * (3*(diagonales-j)), end="")

		for m in range(j+1):
			n=j-m
			print(f"({m:>{ancho}},{n:>{ancho}})", end="")
		print()
