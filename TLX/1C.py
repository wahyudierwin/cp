def match(data, pattern):
	if pattern == "*":
		return True
	elif pattern[0] == '*':
		sub = pattern[1:len(pattern)]
		if (len(data) >= len(sub)) & (data[-len(sub):len(data)] == sub):
			return True
	elif pattern[-1] == '*':
		sub = pattern[0:-1]
		if (len(data) >= len(sub)) & (data[0:len(sub)] == sub):
			return True
	else:
		splitted = pattern.split('*')
		front_pattern = splitted[0]
		back_pattern = splitted[1]
		if (len(data) >= len(front_pattern) + len(back_pattern)) & (data[0:len(front_pattern)] == front_pattern) & (data[-len(back_pattern):len(data)] == back_pattern):
			return True
	return False


p = input()
n = int(input())

for _ in range(n):
	data = input()
	if match(data, p):
		print(data)
	else:
		pass