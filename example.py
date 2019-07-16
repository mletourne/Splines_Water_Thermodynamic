import th_spl
import numpy
import matplotlib.pyplot as plt


# ----------------------------------------------------------------------------------------------------------------------
# EXAMPLE 1: Contour plots of the different thermodynamic properties
# ----------------------------------------------------------------------------------------------------------------------

# We wish to sample following an uniform grid covering the whole thermodynamic domain
PMIN = 611.657
PMAX = 1e8

HMIN = 1e3
HMAX = 4.5e6

PCRIT = 22064000.0 #critical pressure

H, P = numpy.meshgrid(numpy.linspace(HMIN,HMAX,100), numpy.linspace(PMIN,PMAX,100))
HH, PP = H.flatten(), P.flatten()

# Let's call our thermodynamic library to compute the properties for the desired samples
properties = th_spl.properties(HH, PP)

D = numpy.array([sample[2] for sample in properties]).reshape(H.shape)
T = numpy.array([sample[3] for sample in properties]).reshape(H.shape)
V = numpy.array([sample[4] for sample in properties]).reshape(H.shape)

# Let's also build the boiling and dew curve for the plots
bdcp = numpy.linspace(1041., PCRIT, 100)
bch = numpy.array([th_spl._hl_p(pi) for pi in bdcp])
dch = numpy.array([th_spl._hv_p(pi) for pi in bdcp])

f1 = plt.figure("Density")
s1 = f1.add_subplot(111)
c1 = s1.contourf(H * 1e-3, P * 1e-6, D, 25)
b1 = plt.colorbar(c1)
s1.plot(bch * 1e-3, bdcp * 1e-6, c='r', label="boiling curve")
s1.plot(dch * 1e-3, bdcp * 1e-6, c='b', label="dew curve")
b1.ax.set_ylabel("Density (kg/m3)", fontsize=16, weight="bold")
for l in b1.ax.yaxis.get_ticklabels():
    l.set_weight("bold")
    l.set_fontsize(12)
plt.xticks(weight="bold", fontsize=12)
plt.yticks(weight="bold", fontsize=12)
plt.xlabel("Enthalpy (kJ/kg)", weight="bold", fontsize=16)
plt.ylabel("Pressure (MPa)", weight="bold", fontsize=16)
plt.title('d(H,P)', weight="bold", fontsize=20)
plt.legend(loc='best')

f2 = plt.figure("Temperature")
s2 = f2.add_subplot(111)
c2 = s2.contourf(H * 1e-3, P * 1e-6, T, 25)
b2 = plt.colorbar(c2)
s2.plot(bch * 1e-3, bdcp * 1e-6, c='r', label="boiling curve")
s2.plot(dch * 1e-3, bdcp * 1e-6, c='b', label="dew curve")
b2.ax.set_ylabel("Temperature (K)", fontsize=16, weight="bold")
for l in b2.ax.yaxis.get_ticklabels():
    l.set_weight("bold")
    l.set_fontsize(12)
plt.xticks(weight="bold", fontsize=12)
plt.yticks(weight="bold", fontsize=12)
plt.xlabel("Enthalpy (kJ/kg)", weight="bold", fontsize=16)
plt.ylabel("Pressure (MPa)", weight="bold", fontsize=16)
plt.title('T(H,P)', weight="bold", fontsize=20)
plt.legend(loc='best')

f3 = plt.figure("Viscosity")
s3 = f3.add_subplot(111)
c3 = s3.contourf(H * 1e-3, P * 1e-6, V, 25)
b3 = plt.colorbar(c3)
s3.plot(bch * 1e-3, bdcp * 1e-6, c='r', label="boiling curve")
s3.plot(dch * 1e-3, bdcp * 1e-6, c='b', label="dew curve")
b3.ax.set_ylabel("1/viscosity (s/mPa)", fontsize=16, weight="bold")
for l in b3.ax.yaxis.get_ticklabels():
    l.set_weight("bold")
    l.set_fontsize(12)
plt.xticks(weight="bold", fontsize=12)
plt.yticks(weight="bold", fontsize=12)
plt.xlabel("Enthalpy (kJ/kg)", weight="bold", fontsize=16)
plt.ylabel("Pressure (MPa)", weight="bold", fontsize=16)
plt.title('v(H,P)', weight="bold", fontsize=20)
plt.legend(loc='best')

plt.show()

# ----------------------------------------------------------------------------------------------------------------------
# EXAMPLE 1: Partial derivative of the Temperature with respect to Enthalpy
# ----------------------------------------------------------------------------------------------------------------------

P = [80e6, 23e6, 1e6]
H = numpy.linspace(HMIN,HMAX,1000)

plt.figure("Cross_Sections")

for p in P:
    properties = th_spl.temperature(H, p, dx=1)
    Tdh = numpy.array([sample[4] for sample in properties])
    plt.plot(H * 1e-3, Tdh, label= "P= {} MPa".format(p*1e-6))

plt.xticks(weight="bold", fontsize=12)
plt.yticks(weight="bold", fontsize=12)
plt.xlabel("Enthalpy (kJ/kg)", weight="bold", fontsize=16)
plt.ylabel("Pressure (MPa)", weight="bold", fontsize=16)
plt.title('dT/dh', weight="bold", fontsize=20)
plt.legend(loc='best')
plt.show()