import numpy as np
import matplotlib.pyplot as plt
csfont = {'fontname':'Times New Roman'}

t = np.linspace(-2, 2, 101) #Generate points
polynomial = 4 * t**3 - 4 * t #Define the polynomial, as presented in the instruction.

#Generating the 'noise' points:
np.random.seed(998)  # This seed's great for a standard visualization, not too close to the original polynomial.
randomVar = np.random.normal(0, 5, 101)
y = 4 * t**3 - 4 * t + randomVar

#Fitting with a Cubic Polynomial (internal Vandermonde)
fittedCubic = np.polyfit(t, y, 3) #Polyfit also provides a Vandermonde matrix, saving a step.

#Side-by-side Visualization for the cubic polynomial:
plt.scatter(t, y, label='Random distribution (w/ "Noise")', color='cornflowerblue')
plt.plot(t, np.polyval(fittedCubic, t), color='red', label='Fitted Cubic Polynomial')
plt.plot(t, polynomial, linestyle='dashdot', color='green', label='Original Polynomial p(t)')

plt.title('Cubic polynomial fit to data w/ noise.', **csfont)
plt.legend()
plt.show()

#Generating and visualizing the quadratic/linear polynomials:
#1 - Quadratic:
fittedQuadratic = np.polyfit(t, y, 2)
plt.scatter(t, y, label='Random distribution (w/ "Noise")', color='cornflowerblue')
plt.plot(t, np.polyval(fittedQuadratic, t), color='darkorange', label='Fitted Quatradic Polynomial')

plt.title('Quadratic polynomial fit to data w/ noise.', **csfont)
plt.legend()
plt.show()

#2 - Linear:
fittedLinear = np.polyfit(t, y, 1)
plt.scatter(t, y, label='Random distribution (w/ "Noise")', color='cornflowerblue')
plt.plot(t, np.polyval(fittedLinear, t), color='goldenrod', label='Fitted Linear Polynomial')

plt.title('Linear polynomial fit to data w/ noise.', **csfont)
plt.legend()
plt.show()

#It seems that the linear polynomial is far more similar to the quadratic polynomial than expected. 






