#binomial Random Variable For 10 Years (at least)
import matplotlib.pyplot as plt
import scipy.special
t=111
r=5
m=15
ro=0.01
v=0
w=5
n=t-((r-1)*(m-1))- (v*(w-1))
tot=0
xi=[]
pt_tot=[]
pt_tot.append(0.3277)
age=35
if age<25 and age >18:
    age_factor=0.96
elif age>=25 and age<35:
    age_factor=0.86
elif age>=35 and age<40:
    age_factor=0.78
elif age>=40 and age<45:
    age_factor=0.15
elif age>=45:
    age_factor=0.035
    
for r in range(1,6):
    tot=0
    n=t-((r-1)*(m-1))- (v*(w-1))
    for i in range(r,n):        
        tot=tot+scipy.special.binom(n,i)*pow(ro,i)*pow(1-ro,n-i)
        xi.append(tot)        
    pt_tot.append(tot*age_factor)
pt_tot[0]=1-pt_tot[1];
plt.plot(pt_tot)

plt.title('Binomial Random Variable with age factor For 10 Years (at least)')
plt.plot(pt_tot,'ro')
plt.grid()
plt.xlabel('Number Of Birth')
plt.ylabel('Probability of Nth Birth')
plt.ylabel('with Probability of Nth Birth')
plt.show()
print('Period of 10 years (With Age Factor)')
print('With Fetal Mortality 0%, probability of')
for i in range(0,len(pt_tot)):
    print('At least ',i,' Birth ', pt_tot[i])
    