import numpy as np
import matplotlib.pyplot as plt
N=100000


Theta1 = []
Theta2=[]
for i in range (0, N):
    theta1 = np.random.randn()*2*np.pi
    theta2 = np.random.randn()*2*np.pi
    P1=np.array([np.cos(theta1), np.sin(theta1)])*4
    P2=P1 + np.array([np.cos(theta2-theta1), np.sin(theta2-theta1)])*2*np.sqrt(2)
    if P2[1]>=0:
        if P1[1]>=0:
            Theta1.append(theta1)
            Theta2.append(theta2)

plt.figure()
plt.scatter(Theta1, Theta2, s=1)
plt.xlabel('Theta1')
plt.ylabel('Theta2')
plt.title('Valid Configurations of Theta1 and Theta2')
plt.show()