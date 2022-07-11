import numpy as np
import matplotlib.pyplot as plt

def pdf(x):
    mean = np.mean(x)
    std = np.std(x)
    y_out = 1/(std * np.sqrt(2 * np.pi)) * np.exp( - (x - mean)**2 / (2 * std**2))
    return y_out



x = np.arange(-2, 2, 0.1)


y = pdf(x)

plt.style.use('seaborn')
plt.figure(figsize = (6, 6))
plt.plot(x, y, color = 'purple',
         linestyle = 'dashed')

plt.scatter( x, y, marker = 'x', s = 25, color = 'orange')
plt.show()