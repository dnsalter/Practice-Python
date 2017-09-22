def main():
	a = b = c = 1
	n = eval(input("Input an integer: "))
	for i in range(n):
		c = a + b
		a = b
		b = c
	print(a)
main()