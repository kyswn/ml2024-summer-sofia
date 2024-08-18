import numpy as np
from sklearn.neighbors import KNeighborsRegressor

n = int(input("Please input positive integer N\n"))
k = int(input("Please input integer k\n"))
if(k>n):
    print("k has to be smaller or equal to n")
else:
    x = np.zeros((n,1))
    y = np.zeros(n)
    for i in range(n):
        x[i,0] = float(input("Please input x\n"))
        y[i] = float(input("Please input y\n"))
    variance = np.var(y)
    print("Variance of labels is: "+ str(variance))
    neigh = KNeighborsRegressor(n_neighbors=k)
    neigh.fit(x,y)
    test_x = np.zeros((1,1))
    test_x[0,0] = float(input("please input x\n"))
    print(neigh.predict(test_x))
