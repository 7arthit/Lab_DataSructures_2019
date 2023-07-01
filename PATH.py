import numpy as np
N = 4 #จำนวนโหนด
def multiply(a, b, res) :
	mul = np.zeros((N,N));
	for i in range(N) :
		for j in range(N) :
			mul[i][j] = 0;
			for k in range(N) :
				mul[i][j] += a[i][k] * b[k][j];
	for i in range(N) :
		for j in range(N) :
			res[i][j] = mul[i][j];
def power(G, res, n) :
	if (n == 1) :
		for i in range(N) :
			for j in range(N) :
				res[i][j] = G[i][j];
		return;
	power(G, res, n // 2);
	multiply(res, res, res);
	if (n % 2 != 0) :
		multiply(res, G, res);
if __name__ == "__main__" :
	G = [
		[ 0, 0, 0 ,1 ,1],
		[ 1, 0, 1 ,1 ,0],
		[ 1, 0, 0 ,1 ,0],
		[ 0, 0, 0 ,0 ,0],
        [ 0, 0, 1 ,0 ,0]
		];
	k = 4; #รอบ AxA
	res = np.zeros((N,N));
	power(G, res, k);
	for i in range(N) :
		for j in range(N) :
			print(res[i][j],end = " ");
		print()