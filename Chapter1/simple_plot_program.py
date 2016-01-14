# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 09:44:39 2016

@author: toffo
Simple python based plotting program
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi,2*np.pi,51) # create an array x

plt.figure(1) # open up a figure window
plt.clf() # clear the window
# now plot
plt.plot(x,np.sin(x))
plt.xlabel('x') #x label
plt.ylabel('sin(x)') # y label 
plt.show() # shows the plot window