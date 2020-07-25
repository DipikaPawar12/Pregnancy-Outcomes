import matplotlib.pyplot as plt
import scipy.special
xi=[0.3277, 0.6723, 0.2531, 0.0509, 0.0052, 0.0002]
plt.plot(xi)
plt.title('Binomial Random Variable For 10 Years (at least)')
plt.plot(xi,'ro')
plt.grid()
plt.xlabel('Number Of Birth')
plt.ylabel('Probability of Nth Birth')
plt.show()    