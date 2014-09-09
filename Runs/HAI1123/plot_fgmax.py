"""
Plot fgmax output from GeoClaw run.

"""


from pylab import *
import matplotlib as mpl
import os
from clawpack.geoclaw import fgmax_tools


def add_gauges(label=True):
    plot([203.52825],[20.9021333],'ko',markersize=8)
    if label: text(203.529,20.9023,'1123',fontsize=15)
    plot([203.530944],[20.895],'ko',markersize=8)
    if label: text(203.5293,20.8951,'TG',fontsize=15)

fg = fgmax_tools.FGmaxGrid()
fg.read_input_data('fgmax1.txt')
fg.read_output(outdir='_mocha_1sep14')

figure(1, figsize=(10,7))


bounds = [0,1,2,3,4,5,6]
bounds = [0,0.5,1,2,3,4,5]
cmap = mpl.colors.ListedColormap([[1,1,1],[.8,.8,1],[.5,.5,1],[.2,.2,1],[0,0,1],\
                 [1,.7,.7], [1,.4,.4], [1,0,0]])

bounds = [0,.25,.5,.75,1,2,4,5]
cmap = mpl.colors.ListedColormap([[1,1,1],[.8,.8,1],[.5,.5,1],[0,0,1],\
                 [1,.7,.7], [1,.4,.4], [1,0,0]])
ax1 = axes()
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
contourf(fg.x,fg.y,fg.s,bounds,cmap=cmap,norm=norm,extend='max')
cb = colorbar(extend='max')
cb.set_label('meters / sec')

contour(fg.x,fg.y,fg.s,bounds,colors='w')
contour(fg.x,fg.y,fg.B,[0],colors='k')

ticklabel_format(format='plain',useOffset=False)
#title('Maximum speed s')
xticks(rotation=20,fontsize=15)
yticks(fontsize=15)
ax1.set_aspect(1./cos(21*pi/180.))
xlim(203.515,203.5443)

add_gauges(False)

show()

# Plot gauges and topo:

bounds = [-1e10,0,1e10]
cmap = mpl.colors.ListedColormap([[1,1,1],[0,1,0]])
figure(2, figsize=(10,7))
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
contourf(fg.x,fg.y,fg.B,bounds,cmap=cmap,norm=norm,extend='max')
contour(fg.x,fg.y,fg.B,[0],colors='k')
ticklabel_format(format='plain',useOffset=False)
xticks(rotation=20,fontsize=15)
yticks(fontsize=15)
ax1.set_aspect(1./cos(21*pi/180.))
xlim(203.515,203.5443)

add_gauges()

show()

if 1:
    figure(2)
    fname = 'Kahului_gauges.png'
    savefig(fname)
    print 'Created ', fname

    figure(1)
    fname = 'Kahului_smax.png'
    savefig(fname)
    print 'Created ', fname
