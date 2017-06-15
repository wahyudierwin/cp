#include <bits/stdc++.h>

using namespace std;

int t,n;

string solve(int nn)
{
	int dua=0, tiga=0, lima=0, tujuh=0;
	if (nn%2==0)
	{
		while (nn%2==0)
		{
			dua++;
			nn = nn/2;
		}
	}
	if (nn%3==0)
	{
		while (nn%3==0)
		{
			tiga++;
			nn = nn/3;
		}
	}
	if (nn%5==0)
	{
		while (nn%5==0)
		{
			lima++;
			nn = nn/5;
		}
	}
	if (nn%7==0)
	{
		while (nn%7==0)
		{
			tujuh++;
			nn = nn/7;
		}
	}

	if (nn>1) return "-1";

	int a[10];
	a[9] = tiga/2;
	tiga = tiga%2;

	a[8] = dua/3;
	dua = dua%3;

	a[7] = tujuh;
	a[6] = min(dua, tiga);
	dua -= a[6];
	tiga -= a[6];

	a[5] = lima;
	a[4] = dua/2;
	dua = dua%2;

	a[3] = tiga;
	a[2] = dua;

	string ans = "";
	for (int i=9 ; i>=2 ; i--)
	{
		char c = '0' + i;
		for (int j=0 ; j<a[i] ; j++)
		{
			ans = c + ans;
		}
	}
	return ans;
}

int main()
{
	scanf("%d", &t);
	while (t--)
	{
		scanf("%d", &n);
		if (n == 0) printf("10\n");
		else if (n < 10) printf("%d\n", n);
		else
		{
			string ans = solve(n);
			printf("%s\n", ans.c_str());
		}
	}
}