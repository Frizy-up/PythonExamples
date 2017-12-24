from __future__ import division
import numpy as np
import pylab as pl
import random
import math


'''
# plot sigmoid function
x = np.arange(-10,10,0.001)
# sigmoid = [i*i for i in x]
sigmoid = 1. / ( 1 + np.exp(-x) )
den = pow((1 + np.exp(-x)),2)
sigmoidDer = np.exp(-x) / ( den  )

fig = pl.figure()
pl.grid(True)
pl.xlim(-10, 10)
pl.ylim(-1, 1)
# pl.title('Sigmoid')
pl.plot(x, sigmoid, 'r-', label='Sigmoid function')
pl.plot(x, sigmoidDer, 'b--', label='Derivative of sigmoid function')
pl.legend()
# pl.xlabel('')
# pl.ylabel(u"sf")
pl.show()
fig.savefig('sigmoid.png')

'''
# plot tanh function
x = np.arange(-10,10,0.001)
# sigmoid = [i*i for i in x]
tanh = (np.exp(x) - np.exp(-x)) / ( np.exp(x) + np.exp(-x) )
tanhDer = 1 - pow(tanh,2)

fig = pl.figure()
pl.grid(True)
pl.xlim(-10, 10)
pl.ylim(-1, 1)
# pl.title('Sigmoid')
pl.plot(x, tanh, 'r-', label='tanh function')
pl.plot(x, tanhDer, 'b--', label='Derivative of tanh function')
pl.legend()
# pl.xlabel('')
# pl.ylabel(u"sf")
pl.show()
fig.savefig('tanh.png')