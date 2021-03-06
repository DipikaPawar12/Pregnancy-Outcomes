#binomial Random Variable For 10 Years (at least)
import matplotlib.pyplot as plt
import scipy.special
t=111
r=5
m=15
ro=0.01
n=t-((r-1)*(m-1))
tot=0
xi=[]
pt_tot=[]
pt_tot.append(0.3277)
for r in range(1,5):
    tot=0
    n=t-((r-1)*(m-1))
    for i in range(r,n):        
        tot=tot+scipy.special.binom(n,i)*pow(ro,i)*pow(1-ro,n-i)
        xi.append(tot)        
    print(tot)
    pt_tot.append(tot)
plt.plot(pt_tot)
plt.title('Binomial Random Variable For 10 Years (at least)')
plt.plot(pt_tot,'ro')
plt.grid()
plt.xlabel('Number Of Birth')
plt.ylabel('Probability of Nth Birth')
plt.show()    