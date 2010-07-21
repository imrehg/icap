#!/usr/bin/env python

from numpy import loadtxt, linspace, sqrt
from scipy.interpolate import UnivariateSpline
import pylab as pl

d1 = loadtxt("data_CW.txt", skiprows=1)
d2 = loadtxt("data_comb.txt", skiprows=1)

x = UnivariateSpline(d1[:,0],d1[:,2],s=2)
p = linspace(min(d1[:,0]), max(d1[:,0]))


fig_width_pt = 510.0  # Get this from LaTeX using \showthe\columnwidth
inches_per_pt = 1.0/72.27               # Convert pt to inch
golden_mean = (sqrt(5)-1.0)/2.0         # Aesthetic ratio
fig_width = fig_width_pt*inches_per_pt  # width in inches
fig_height = fig_width*golden_mean      # height in inches
fig_size =  [fig_width,fig_height]
params = {'backend': 'ps',
          'axes.labelsize': 20,
          'text.fontsize': 10,
          'legend.fontsize': 10,
          'xtick.labelsize': 18,
          'ytick.labelsize': 18,
          'text.usetex': True,
          'figure.figsize': fig_size}
pl.rcParams.update(params)

pl.axes([0.125,0.2,0.95-0.125,0.95-0.2])


#pl.plot(d1[:,0], d1[:,2], '--', label="CW", linewidth=2)
pl.semilogy(p, x(p), '--', label="CW", linewidth=2)
pl.semilogy(d2[:,0], d2[:,2], '-', label="mode-locked", linewidth=2)
pl.ylabel('Light shift $\mathrm{Hz}$')
pl.xlabel('Average laser intensiy $\mu\mathrm{W}$')
pl.legend(loc='best')
pl.savefig("lightshift.pdf")
pl.show()

