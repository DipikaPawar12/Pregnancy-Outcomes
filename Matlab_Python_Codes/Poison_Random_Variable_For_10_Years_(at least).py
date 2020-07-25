import matplotlib.pyplot as plt
import scipy.special
import math
t=111
r=5
m=15
ro=0.01
v=0
w = 5
n=t-((r-1)*(m-1))- (v*(w-1))
tot=0
nt = n*ro
xip =[]
xip.append(0);
for r in range(1,5):
    n=t-((r-1)*(m-1))- (v*(w-1))
    nt = n*ro
    tot = 0
    for i in range(r,n):    
        tot =tot+ math.exp(-nt)*(pow(nt,i)/math.factorial(i))
    xip.append(tot)
xip[0]=1-xip[1]
print(xip)
plt.title('Poison Random Variable For 10 Years (at least)')
plt.plot(xip,'ro')
plt.plot(xip)
plt.grid()
plt.xlabel('Number Of Birth')
plt.ylabel('Probability of Nth Birth')
plt.show()