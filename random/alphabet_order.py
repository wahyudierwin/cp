def get_minimum(a, b):
	if a<b:
		return a
	else:
		return b


def DFS(point, order, flag, adj_list):
	flag[point] = True

	for next_point in adj_list[point]:
		if not flag[next_point]:
			DFS(next_point, order, flag, adj_list)

	order.insert(0, point) # put in front


def solve(words):
	pairs = []
	for i in range(len(words)):
		for j in range(i+1, len(words)):
			word1 = words[i]
			word2 = words[j]
			idx = -1
			for k in range(get_minimum(len(word1), len(word2))):
				if word1[k] != word2[k]:
					idx = k
					break

			if idx != -1:
				pair = [word1[idx], word2[idx]]
				if (pair[0] != pair[1]) & (pair not in pairs):
					pairs.append(pair)

	# print(pairs)

	# create graph, then do topological sort, with vertex is all alphabet in words
	points = list(set("".join(words)))
	adj_list = {point: [] for point in points}
	flag = {point: False for point in points}

	for pair in pairs:
		adj_list[pair[0]].append(pair[1])

	# do DFS for topological sort
	order = []
	for point in points:
		if not flag[point]:
			DFS(point, order, flag, adj_list)

	# print(order)
	return order


def main():
	# print(primes)
	t = int(input())
	words = []

	for _ in range(t):
		word = input()
		words.append(word)

	order = solve(words)

	result = "".join(order)
	print(result)


if __name__ == "__main__":
	main()