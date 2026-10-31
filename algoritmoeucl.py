def eucl(a,b):
	r= a % b
	while r != 0:
		a=b
		b=r
		r= a%b
	return print("El MCD es:", b)

