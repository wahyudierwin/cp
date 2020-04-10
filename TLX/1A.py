t = int(input())

for _ in range(t):
	n, m = map(lambda x: int(x), input().split(" "))
	user = input()
	data = []
	for t in range(n):
		inp = input().split(" ")
		data.append([inp[0], int(inp[1]), int(inp[2]), int(inp[3])])

	data.sort(key=lambda x: (-x[3], -x[2], -x[1]))
	user_passing = [temp[0] for temp in data[:m]]
	# print(user_passing)

	if user in user_passing:
		print("YA")
	else:
		print("TIDAK")
