def solve(paths, points):
	# add point END where END_i END 0 and END 0
	points.append(['END', 0])
	gifts = {point[0]:point[1] for point in points}

	for point in points:
		if (len(point[0]) > 3) & (point[0][:3] == 'END'):
			paths.append([point[0], 'END', 0])

	# create adjacency list
	adj_list = {point[0]: [] for point in points}
	current_gift = {point[0]: -1 for point in points}
	current_path = {point[0]: [] for point in points}

	# assume it's only one way
	for path in paths:
		adj_list[path[0]].append([path[1], path[2]])

	# do BFS
	queue = []

	queue.append(["START", ["START"], 0])
	while (len(queue) > 0):
		s = queue.pop(0)
		# print(s)
		cur_point = s[0]
		cur_path = s[1]
		cur_gift = s[2]

		for point in adj_list[cur_point]:
			next_point = point[0]
			cost = point[1]

			# if next gift is greater than current gitf, update and add to queue
			next_gift = cur_gift + gifts[next_point] - cost
			if next_gift > current_gift[next_point]:
				current_gift[next_point] = next_gift
				current_path[next_point] = [point for point in cur_path] + [next_point]
				queue.append([next_point, current_path[next_point], current_gift[next_point]])


	return current_gift["END"], current_path["END"][:-1]


def main():
	n_path = int(input())
	paths = []

	for _ in range(n_path):
		first_point, second_point, cost = input().split()
		paths.append([first_point, second_point, int(cost)])

	n_point = int(input())
	points = []

	for _ in range(n_point):
		point, gift = input().split()
		points.append([point, int(gift)])

	total_gift, order = solve(paths, points)

	print(total_gift, ",".join(order))


if __name__ == "__main__":
	main()