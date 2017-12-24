from __future__ import division
import numpy as np
import pylab as pl
import random
import math



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