
from pylab import *
#from pyclaw.plotters.data import ClawPlotData
from clawpack.visclaw.data import ClawPlotData
import tidegauge

g_obs=tidegauge.read_tide_gauge('1617760__2011-03-11_to_2011-03-13.csv')
outdir = '../Runs/HAI1125-26/_output'

tsec = g_obs[1]
thour = tsec / 3600.
eta = g_obs[3]

figure(3)
clf()
plot(thour,eta,'k',linewidth=1)
plot(thour,eta,'k.',linewidth=1,label='Observed')

# computed results:
plotdata = ClawPlotData()
plotdata.outdir = outdir
print "Looking for GeoClaw results in ",plotdata.outdir
g7760 = plotdata.getgauge(7760)

# shift by 10 minutes:
thour = (g7760.t + 600.) / 3600.
plot(thour, g7760.q[3,:],'r',linewidth=2,label='GeoClaw')
xlim(7.5,13)
ylim(-2,1.5)
legend(loc='lower right')
xticks(range(8,14),fontsize=15)
yticks(fontsize=15)
title('Surface elevation at Gauge 7760',fontsize=15)

if 1:
    fname = "TG7760.jpg"
    savefig(fname)
    print "Created ",fname
