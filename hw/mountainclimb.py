#思路:基底以老師的程式碼並結合hillClimbing2的程式碼 用爬山慢慢找出新解 若新解更優則將解改為新解

import matplotlib.pyplot as plt
import numpy as np
import random

# x = np.array([0, 1, 2, 3, 4], dtype=np.float32)
# y = np.array([2, 3, 4, 5, 6], dtype=np.float32)
x = np.array([0, 1, 2, 3, 4], dtype=np.float32)
y = np.array([1.9, 3.1, 3.9, 5.0, 6.2], dtype=np.float32)

def predict(a, xt):
	return a[0]+a[1]*xt

def MSE(a, x, y):
	total = 0
	for i in range(len(x)):
		total += (y[i]-predict(a,x[i]))**2
	return total

def loss(p):
	return MSE(p, x, y)



#此段參照hillClimbing2之程式碼修改
def optimize(a):
    round=1000
    Time=0
    while (Time<round):
        p1 = random.uniform(-0.1,0.1)
        p2 = random.uniform(-0.1,0.1)
        new_a = [a[0]+p1,a[1]+p2]
        if loss(a)>loss(new_a): 
            a=new_a
        else:
            Time+=1
    return a


p = optimize([0,0])



# Plot the graph
y_predicted = list(map(lambda t: p[0]+p[1]*t, x))
print('y_predicted=', y_predicted)
plt.plot(x, y, 'ro', label='Original data')
plt.plot(x, y_predicted, label='Fitted line')
plt.legend()
plt.show()

