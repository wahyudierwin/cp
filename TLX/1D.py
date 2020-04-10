a = input()
b = input()

bisa = False
for i in range(len(a)):
	temp = a[0:i] + a[i+1:len(a)]
	# print(temp)
	if temp == b: bisa = True

if bisa:
	print("Tentu saja bisa!")
else:
	print("Wah, tidak bisa :(")
