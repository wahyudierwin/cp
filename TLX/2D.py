def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a%b)


def lcm(a, b):
	return a * int(b // gcd(a,b))


def main():
	# print(primes)
	t = int(input())
	res = 1
	for _ in range(t):
		k = int(input())
		res = lcm(res, k)
	print(res)


if __name__ == "__main__":
	main()