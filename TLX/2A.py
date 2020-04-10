def convert(item):
	if item[1] == 1:
		return str(item[0])
	else:
		return f'{str(item[0])}^{str(item[1])}'

def main():
	n = int(input())

	fp = []

	pembagi = 2
	while n>1:
		pangkat = 0
		while n%pembagi == 0:
			pangkat = pangkat + 1
			n = n/pembagi
		if pangkat > 0:
			fp.append([pembagi, pangkat])
		# print(pembagi, pangkat)
		pembagi = pembagi + 1
		
	# print(fp)
	result = ' x '.join( map( lambda x: convert(x), fp) )
	print(result)



	

if __name__ == "__main__":
	main()