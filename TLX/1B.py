def is_all_one(row):
	for c in row:
		if c != '1':
			return False
	return True

def set_zero(row):
	result = ""
	for _ in range(len(row)):
		result = result + '0'
	return result

def is_same(tetris1, tetris2):
	for i in range(len(tetris1)):
		if tetris1[i] != tetris2:
			return False
	return True

def runtuh(tetris):
	for i in range(len(tetris)):
		if is_all_one(tetris[i]):
			tetris[i] = set_zero(tetris[i])

	return tetris


def main():
	n, m = map(lambda x: int(x), input().split())
	
	data = []
	for _ in range(n):
		row = input()
		data.append(row)

	result = runtuh(data)
	for row in data:
		print(row)

if __name__ == "__main__":
	main()