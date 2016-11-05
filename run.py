import numpy as np
import matplotlib.pyplot as plt
import math

plt.close('all')

def alpha(ai, bi,u,u0):
	return 1./ai - bi/2./math.pi * math.log(u/u0)

b1 = 4.1
b2 = -19./6.
b3 = -7.

x = np.arange(2,18.2,.1)
xlab = range(2,17,2)
y1,y2,y3 = [],[],[]
labels = []
a1 = 0.016946
a2 = 0.033812
a3 = 0.1176
for xi in x:
	y1.append(alpha(a1,b1,10**xi,10**2))
	y2.append(alpha(a2,b2,10**xi,10**2))
	y3.append(alpha(a3,b3,10**xi,10**2))
for xi in xlab:
	string = r"$10^{" + (str) (xi) + r"}$"
	labels.append(string)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,y1,label = r'$\alpha^{-1}_1$')
ax.plot(x,y2,label = r'$\alpha^{-1}_2$')
ax.plot(x,y3,label = r'$\alpha^{-1}_3$')
ax.annotate(r'$\alpha^{-1}_1$',xy = (5,13),fontsize = 16)
ax.annotate(r'$\alpha^{-1}_2$',xy = (5,30),fontsize = 16)
ax.annotate(r'$\alpha^{-1}_3$',xy = (5,55),fontsize = 16)
plt.title(r'Running Gauge Couplings for Standard Model') 
plt.xlabel(r'$\mu$ (GeV)', fontsize = 18)
plt.ylabel(r'$\alpha^{-1}$', fontsize = 18)
plt.xticks(xlab,labels,fontsize = 14)

#SO(10)
x1 = np.arange(2,11.114,0.1)
x2 = np.arange(11.114,16.378,0.1)
y1,y2,y3 = [],[],[]
y4c,y2l,y2r = [],[],[]
labels = []
a1 = 0.016946
a2 = 0.033812
a3 = 0.1176
for xi in x1:
	y1.append(alpha(a1,b1,10**xi,10**2))
	y2.append(alpha(a2,b2,10**xi,10**2))
	y3.append(alpha(a3,b3,10**xi,10**2))
a4 = 0.03136
a2l = 0.02491
a2r = 0.01843
b4 = -7./3.
b2l = 2.
b2r = 28./3.
for xi in x2:
	y4c.append(alpha(a4,b4,10**xi,1.3*10**11))
	y2l.append(alpha(a2l,b2l,10**xi,1.3*10**11))
	y2r.append(alpha(a2r,b2r,10**xi,1.3*10**11))
for xi in xlab:
	string = r"$10^{" + (str) (xi) + r"}$"
	labels.append(string)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x1,y1,label = r'$\alpha^{-1}_1$',color = 'r')
ax.plot(x1,y2,label = r'$\alpha^{-1}_2$',color = 'r')
ax.plot(x1,y3,label = r'$\alpha^{-1}_3$',color = 'r')
ax.plot(x2,y4c,label = r'$\alpha^{-1}_{4C}$',color = 'b')
ax.plot(x2,y2l,label = r'$\alpha^{-1}_{2L}$',color = 'b')
ax.plot(x2,y2r,label = r'$\alpha^{-1}_{2R}$',color = 'b')
ax.annotate(r'$\alpha^{-1}_1$',xy = (5,13),fontsize = 16)
ax.annotate(r'$\alpha^{-1}_2$',xy = (5,30),fontsize = 16)
ax.annotate(r'$\alpha^{-1}_3$',xy = (5,55),fontsize = 16)
ax.annotate(r'$\alpha^{-1}_{4}$',xy = (13,30),fontsize = 16)
ax.annotate(r'$\alpha^{-1}_{2L}$',xy = (13,40),fontsize = 16)
ax.annotate(r'$\alpha^{-1}_{2R}$',xy = (13,50),fontsize = 16)
plt.title(r'Running Gauge Couplings for Non-SUSY SO(10)') 
plt.xlabel(r'$\mu$ (GeV)', fontsize = 18)
plt.ylabel(r'$\alpha^{-1}$', fontsize = 18)
plt.xticks(xlab,labels,fontsize = 14)
plt.xlim(xmax = 16.7)
plt.show()
