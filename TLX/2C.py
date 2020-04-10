primes = []

def sieve():
	flag = [False for x in range(1000001)]
	for i in range(2, 1000001):
		if not flag[i]:
			primes.append(i)
			j = 1
			while i*j <= 1000000:
				flag[i*j] = True
				j = j+1



def main():
	sieve()
	# print(primes)
	t = int(input())
	for _ in range(t):
		k = int(input())
		print(primes[k-1])


if __name__ == "__main__":
	main()