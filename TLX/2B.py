def gcd(a, b):
	if b==0:
		return int(a)
	else:
		return int(gcd(b, a%b))


def main():
	a,b = input().split()
	c,d = input().split()

	a = int(a)
	b = int(b)
	c = int(c)
	d = int(d)

	# a/b + c/d = (a*d + c*b)/(b*d) but hitung KPK(b,d), bukan asal b*d
	gcd_bd = gcd(b,d)
	kpk_bd = b*int(d//gcd_bd)

	# print(gcd_bd, kpk_bd)

	pembilang = a*int(d//gcd_bd) + c*int(b//gcd_bd)
	pembagi = kpk_bd

	# print(a*int(d/gcd_bd), c*int(b/gcd_bd))
	# print(pembilang, pembagi)

	gcd_res = gcd(pembilang, pembagi)

	# print(int(pembilang//gcd_res))

	print(int(pembilang//gcd_res), int(pembagi//gcd_res))



if __name__ == "__main__":
	main()