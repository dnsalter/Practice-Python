a = 1
b = 1
c = 0
x = 0

while c <= 4000000:
	c = a + b
	a = b
	b = c
	if not(b%2):
		x+=b
		
print(x)