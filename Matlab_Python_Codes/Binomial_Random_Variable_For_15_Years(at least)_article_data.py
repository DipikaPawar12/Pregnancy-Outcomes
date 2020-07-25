import matplotlib.pyplot as plt
import scipy.special
xi=[0.1793, 0.8207, 0.4662, 0.1731, 0.0412, 0.0062, 0.0006]
plt.plot(xi)
plt.title('Binomial Random Variable For 15 Years (at least)')
plt.plot(xi,'ro')
plt.grid()
plt.xlabel('Number Of Birth')
plt.ylabel('Probability of Nth Birth')
plt.show()    