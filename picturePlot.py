from __future__ import division
import numpy as np
import pylab as pl
import random
import math
import matplotlib.pyplot as plt
import matplotlib as mpl


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

'''

'''
# plot ReLU function
x = np.arange(-10,10,0.001)
# sigmoid = [i*i for i in x]
relu = np.where(x<0,0,x)
reluDer = np.where(x<0,0,1)

fig = pl.figure()
pl.grid(True)
pl.xlim(-2, 2)
pl.ylim(-2, 2)

pl.spines['top'].set_color('none')

# pl.title('Sigmoid')
pl.plot(x, relu, 'r-', label='ReLU function')
pl.plot(x, reluDer, 'b--', label='Derivative of ReLU function')
pl.legend()
# pl.xlabel('')
# pl.ylabel(u"sf")
pl.show()
fig.savefig('relu.png')
'''


'''
mpl.rcParams['axes.unicode_minus']=False

fig = plt.figure(figsize=(6,4))
ax = fig.add_subplot(111)

x = np.arange(-10, 10)
y = np.where(x<0,0,x)

plt.xlim(-11,11)
plt.ylim(-11,11)

ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.set_xticks([-10,-5,0,5,10])
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
ax.set_yticks([-10,-5,5,10])

plt.plot(x,y,label="ReLU",color = "red")
plt.legend()
plt.show()
fig.savefig('relu.png')

'''

'''
# plot leak ReLU function
mpl.rcParams['axes.unicode_minus']=False

fig = plt.figure(figsize=(6,4))
ax = fig.add_subplot(111)

x = np.arange(-10, 10)
y = np.where(x<0,0.2*x,x)

plt.xlim(-11,11)
plt.ylim(-11,11)

ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.set_xticks([-10,-5,0,5,10])
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
ax.set_yticks([-10,-5,5,10])

plt.plot(x,y,label="Leak ReLU",color = "red")
plt.legend()
plt.show()
fig.savefig('leakRelu.png')

'''



# plot ELU function
mpl.rcParams['axes.unicode_minus']=False

fig = plt.figure(figsize=(6,4))
ax = fig.add_subplot(111)

x = np.arange(-10, 10)
y = np.where(x<0,1*(np.exp(x)-1),x)

plt.xlim(-11,11)
plt.ylim(-11,11)

ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.set_xticks([-10,-5,0,5,10])
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
ax.set_yticks([-10,-5,5,10])

plt.plot(x,y,label="ELU",color = "red")
plt.legend()
plt.show()
fig.savefig('ELU.png')