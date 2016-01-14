# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 09:44:39 2016

@author: toffo
Simple python based plotting program
"""
import numpy as np
import matplotlib.pyplot as plt
def f1(x):
    """
    this is where documentation goes
    """
    return np.exp(-x/4)*np.sin(x)

def fwithoutsin(x):
    return np.exp(-x/4)

def f3(x):
    return np.exp(-x)*np.sin(x)**2


x = np.linspace(0,20,100) # create an array theta
x2 = np.linspace(2,20,10)
#plt.figure(1) # open up a figure window
#plt.clf() # clear the window
# now plot

plt.subplot(221)
plt.plot(x,f1(x))
plt.ylabel(r'$f(x)$')
plt.title('$f(x)=exp(-x/4)*sin(x)$')
plt.grid(True)
plt.xlabel('x')

plt.subplot(222)
plt.plot(x,f1(x))
plt.plot(x2,f1(x2),'o')   #I don't know how to make circle bigger
plt.plot(x,np.exp(-x/4))
plt.ylabel('f(x)')
plt.title('$f(x)=exp(-x/4)*sin(x)$')
plt.grid(True)
plt.xlabel('x')



ax =plt.subplot(223)
ax.xaxis.set_ticks(np.arange(0,20,5))
#ax.yaxis.set_ticks([10**-10,10**0])
plt.grid(True)
plt.plot(x,f3(x),'.')
plt.yscale('log')
plt.xlabel('x')
plt.title('$f(x)=exp(-x)*\sin(x)^2$')


x4 = np.linspace(0,20,1000)
ax = plt.subplot(224,polar=True)
plt.plot(x4,np.sin(6*x4+4.8))
ax.yaxis.set_ticks([0,0.5,1])

# plt.grid(False)
plt.show() # shows the plot window



# fig,axs = plt.subplots(2,2)
#
# ax = axs[0,0]
# ax.plot(x,f1(x))
#
# #ax.set_xlabel(r'$\theta$') #x label
# ax.set_xlabel('x')
# ax.set_ylabel('f(x)') # y label use latex for greek symbols
# ax.set_title('f(x)=exp(-x/4)*sin(x)')
#
#
# ax = axs[0,1]
# ax.plot(x,f1(x))
# ax.plot(x2,f1(x2),'o')
# ax.plot(x,fwithoutsin(x))
# #ax.set_xlabel(r'$\theta$') #x label
# ax.set_xlabel('x')
# ax.set_ylabel('f(x)') # y label use latex for greek symbols
# ax.set_title('f(x)=exp(-x/4)*sin(x)')
#
#
# ax = axs[1,0]
# ax.plot(x,f3(x))
# #ax.set_xlabel(r'$\theta$') #x label
# ax.set_xlabel('x')
# ax.set_ylabel('f(x)') # y label use latex for greek symbols
# ax.set_title(r'$f(x)=exp(-x)*sin(x)^2$')
#
# plt.subplot(224)
# plt.polar(x,np.sin(x))