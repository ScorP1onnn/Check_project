import numpy as np
from uncertainties import ufloat
from astropy.io import fits
import matplotlib.pyplot as plt
from lmfit import Model
from matplotlib.ticker import ScalarFormatter
from math import *


source=np.asarray(["Hyde","9io9","AzTEC-1","Aztec-3","ID141","SPT2132-58","BR-1202-SMG","BRI-1335-0417","BR-1202-QSO",
                   "PSSJ2322+1944","pisco","APM 08279+5255","MM 18423+5938"])

type=np.asarray(["DSFG","SMG","SMG","SMG","SMG","SMG","SMG","QSO","QSO","QSO","QSO","QSO","QSO"])

z=np.asarray([3.7087,2.5543,4.342,5.29795,4.24,4.768,4.7,4.407,4.7,4.12,7.5413,3.911,3.93])

"""Without pisco,APM,MM"""
source_reduced=np.asarray(["Hyde","9io9","AzTEC-1","Aztec-3","ID141","SPT2132-58","BR-1202-SMG","BRI-1335-0417","BR-1202-QSO",
                   "PSSJ2322+1944","APM 08279+5255","MM 18423+5938"])

n=source_reduced.shape[0]
print(f"n = {n}")
z_reduced=np.asarray([3.7087,2.5543,4.342,5.29795,4.24,4.768,4.7,4.407,4.7,4.12,3.911,3.93])
type_reduced=np.asarray(["DSFG","SMG","SMG","SMG","SMG","SMG","SMG","QSO","QSO","QSO","QSO","QSO"])

nitrogen_line_luminosity=np.asarray([ufloat(7.5e7,2e7),ufloat(7.0e8,0.7e8),ufloat(2.14e8,0.23e8),ufloat(2.0e8,0.9e8),
                                    ufloat(1.54e9,0.12e9)/20,ufloat(1.06e9,0.15e9)/ufloat(5.7,0.5),ufloat(6.1e8,0.5e8),ufloat(4.4e8,0.4e8),ufloat(3.97e8,0.3e8),
                                     ufloat(5.7e8,2.1e8)/ufloat(5.3,0.3),ufloat(1.11e9,0.30e9)/80,ufloat(8.2e8,1.1e8)/20])

nitrogen_FWHM=np.asarray([ufloat(611.9961821753315,165.66828877047436),ufloat(750.4640017248616,63.79647223941275),
                          ufloat(374.6595074546333,43.81585606973786),ufloat(684.6079623818567,294.51606096402105),
                          ufloat(844.8951682753528,64.40967081681306),ufloat(259.0981118043234,39.31305882412342),
                          ufloat(870.2236682099431,70.18793751724704), ufloat(282.5754293914247,28.203072749204143),
                          ufloat(428.4675327547311,34.78995674375571),ufloat(309.5092398615353,120.76559186526976),
                          ufloat(560.7054955333228,154.06325625592365),ufloat(199.40162854008864,30.22939390964306)])

print(f"{source_reduced.shape[0]} : {nitrogen_line_luminosity.shape[0]} : {nitrogen_FWHM.shape[0]} : {type_reduced.shape[0]}")




carbon_line_luminosity=np.asarray([ufloat(8.4e8,1.0e8),ufloat(0,0),ufloat(7.8e9,1.1e9),ufloat(6.69e9,0.23e9),ufloat(61.6e9,9.8e9)/20,ufloat(21e9,4e9)/ufloat(5.7,0.5),
                   ufloat(10.0e9,1.5e9),ufloat(16.4e9,2.6e9),ufloat(6.5e9,1.0e9),ufloat(1.7e9,1e9),ufloat(0,0),ufloat(0,0)])

carbon_FWHM=np.asarray([ufloat(781,292),ufloat(0,0),ufloat(366,0),ufloat(421,19),ufloat(690,80),ufloat(212,43),
                         ufloat(722,12),ufloat(340,140),ufloat(328,6),ufloat(0,0),ufloat(0,0),ufloat(0,0)])



IR_luminosities=np.asarray([ufloat(1.1e12,0.4e12),ufloat(1.1e13,0.2e13),ufloat(1.9e13,0.3e13),ufloat(2.8e13,0),
                            ufloat(5.4e12,0.3e12)/20,ufloat(6.4e13,1e13)/ufloat(5.7,0.5),ufloat(6.7e13,0),ufloat(49.6e12,3.8e12),
                            ufloat(5.0e13,0),ufloat(17.8e12,1.7e12)/ufloat(5.3,0.3),ufloat(16.0e12,0.4e12)/80,ufloat(10.2e12,1e12)/20])

FIR_luminosities = np.asarray([ufloat(0.67e12,0.25e12),ufloat(8.2e12,1.5e12),ufloat(6.6e12,1.0e12),ufloat(1.1e13,0.6e13),
                             ufloat(4.3e12,0.2e12)/20,ufloat(3.9e13,0.6e13)/ufloat(5.7,0.5),ufloat(2.4e13,0),ufloat(3.1e13,0),ufloat(2.3e13,0),
                             ufloat(5.3e12,0.5e12)/ufloat(5.3,0.3),ufloat(3.6e12,0.1e12)/80,ufloat(5e12,0.5e12)/20])




for i in range(n):
    print(f"source:{source_reduced[i]}; Type:{type_reduced[i]};   L_[NII]:{nitrogen_line_luminosity[i]};     FWHM:{nitrogen_FWHM[i]};  L_[CII]: {carbon_line_luminosity[i]}; FWHM:{carbon_FWHM[i]}  L_IR:{IR_luminosities[i]}  "
          f"L_FIR = {FIR_luminosities[i]}   ")




print("")
print("")
print("")
NLL_IR=[]
CLL_NLL=[]
NitrogenFWHM=[]
CarbonFWHM=[]
CarbonFWHM_NitrogenFWHM=[]
NLL_FIR=[]
NLL_NitrogenFWHM=[]

for i in range(n):
    a=nitrogen_line_luminosity[i]/IR_luminosities[i]
    b=carbon_line_luminosity[i]/nitrogen_line_luminosity[i]
    c=nitrogen_FWHM[i]
    d=carbon_FWHM[i]
    e=carbon_FWHM[i]/nitrogen_FWHM[i]
    f=nitrogen_line_luminosity[i]/FIR_luminosities[i]
    g=nitrogen_FWHM[i]/nitrogen_line_luminosity[i]

    NLL_IR.append(a)
    CLL_NLL.append(b)
    NitrogenFWHM.append(c)
    CarbonFWHM.append(d)
    CarbonFWHM_NitrogenFWHM.append(e)
    NLL_FIR.append(f)
    NLL_NitrogenFWHM.append(g)



NLL_IR=np.asarray(NLL_IR)
CLL_NLL=np.asarray(CLL_NLL)
NitrogenFWHM=np.asarray(NitrogenFWHM)
CarbonFWHM=np.asarray(CarbonFWHM)
CarbonFWHM_NitrogenFWHM=np.asarray(CarbonFWHM_NitrogenFWHM)
NLL_FIR=np.asarray(NLL_FIR)
NLL_NitrogenFWHM=np.asarray(NLL_NitrogenFWHM)

NitrogenFWHM_nominal_value=[]
for i in range(len(NitrogenFWHM)):
    NitrogenFWHM_nominal_value.append(NitrogenFWHM[i].n)

NitrogenFWHM_nominal_value=np.asarray(NitrogenFWHM_nominal_value)

NitrogenFWHM_nominal_value_SMG=[]
NitrogenFWHM_nominal_value_QSO=[]


for i in range(7):
    NitrogenFWHM_nominal_value_SMG.append(NitrogenFWHM_nominal_value[i])
for i in range(7,n):
    NitrogenFWHM_nominal_value_QSO.append(NitrogenFWHM_nominal_value[i])

NitrogenFWHM_nominal_value_SMG=np.asarray(NitrogenFWHM_nominal_value_SMG)
NitrogenFWHM_nominal_value_QSO=np.asarray(NitrogenFWHM_nominal_value_QSO)

print("*******************************************SMG*****************************************************")
for i in range(7):

    print(f"{source_reduced[i]} : {NitrogenFWHM_nominal_value_SMG[i]}")
print("**************************************QSO*******************************************************")
for i in range(5):

    print(f"{source_reduced[i+7]} : {NitrogenFWHM_nominal_value_QSO[i]}")



print("")
print("")
print("")
print("L_[NII]/L_IR")
for i in range(n):
    print(f"{source_reduced[i]} : {NLL_IR[i]}")

print("")
print("")
print("")
print("L_[CII]/L_[NII]")
for i in range(n):
    print(F"{source_reduced[i]} : {CLL_NLL[i]}")

print("")
print("")
print("")
print("Nitrogen FWHM")
for i in range(n):
    print(f"{source_reduced[i]} : {NitrogenFWHM[i]}")

print("")
print("")
print("")
print("Carbon FWHM")
for i in range(n):
    print(f"{source_reduced[i]} : {CarbonFWHM[i]}")

print("")
print("")
print("")
print("Carbon FWHM/Nitrogen FWHM")
for i in range(n):
    print(f"{source_reduced[i]} : {CarbonFWHM_NitrogenFWHM[i]}")

print("")
print("")
print("")
print("L_[NII]/L_FIR")
for i in range(n):
    print(f"{source_reduced[i]} : {NLL_FIR[i]}")








"""For SMG"""
NLL_IR_SMG=[]
CLL_NLL_SMG=[]
NitrogenFWHM_SMG=[]
CarbonFWHM_SMG=[]
CarbonFWHM_NitrogenFWHM_SMG=[]
IR_luminosities_SMG=[]
FIR_luminosities_SMG=[]
NLL_FIR_SMG=[]
NLL_NitrogenFWHM_SMG=[]

for i in range(7):
    NLL_IR_SMG.append(NLL_IR[i])
    CLL_NLL_SMG.append(CLL_NLL[i])
    NitrogenFWHM_SMG.append(NitrogenFWHM[i])
    CarbonFWHM_SMG.append(CarbonFWHM[i])
    CarbonFWHM_NitrogenFWHM_SMG.append(CarbonFWHM_NitrogenFWHM[i])
    IR_luminosities_SMG.append(IR_luminosities[i])
    FIR_luminosities_SMG.append(FIR_luminosities[i])
    NLL_FIR_SMG.append(NLL_FIR[i])
    NLL_NitrogenFWHM_SMG.append(NLL_NitrogenFWHM[i])

NLL_IR_SMG=np.asarray(NLL_IR_SMG)
CLL_NLL_SMG=np.asarray(CLL_NLL_SMG)
NitrogenFWHM_SMG=np.asarray(NitrogenFWHM_SMG)
CarbonFWHM_SMG = np.asarray(CarbonFWHM_SMG)
CarbonFWHM_NitrogenFWHM_SMG=np.asarray(CarbonFWHM_NitrogenFWHM_SMG)
IR_luminosities_SMG=np.asarray(IR_luminosities_SMG)
FIR_luminosities_SMG=np.asarray(FIR_luminosities_SMG)
NLL_FIR_SMG=np.asarray(NLL_FIR_SMG)
NLL_NitrogenFWHM_SMG=np.asarray(NLL_NitrogenFWHM_SMG)
print("For SMG")
print("")
print(NLL_IR_SMG)
print("")
print(CLL_NLL_SMG)
print("")
print(NitrogenFWHM_SMG)
print("")
print(CarbonFWHM_SMG)
print("")
print(IR_luminosities_SMG)
print("")






"""For QSO"""
NLL_IR_QSO=[]
CLL_NLL_QSO=[]
NitrogenFWHM_QSO=[]
CarbonFWHM_QSO=[]
CarbonFWHM_NitrogenFWHM_QSO=[]
IR_luminosities_QSO=[]
FIR_luminosities_QSO=[]
NLL_FIR_QSO=[]
NLL_NitrogenFWHM_QSO=[]
for i in range(7,n):
    NLL_IR_QSO.append(NLL_IR[i])
    CLL_NLL_QSO.append(CLL_NLL[i])
    NitrogenFWHM_QSO.append(NitrogenFWHM[i])
    CarbonFWHM_QSO.append(CarbonFWHM[i])
    CarbonFWHM_NitrogenFWHM_QSO.append(CarbonFWHM_NitrogenFWHM[i])
    IR_luminosities_QSO.append(IR_luminosities[i])
    FIR_luminosities_QSO.append(FIR_luminosities[i])
    NLL_FIR_QSO.append(NLL_FIR[i])
    NLL_NitrogenFWHM_QSO.append(NLL_NitrogenFWHM[i])
NLL_IR_QSO=np.asarray(NLL_IR_QSO)
CLL_NLL_QSO=np.asarray(CLL_NLL_QSO)
NitrogenFWHM_QSO=np.asarray(NitrogenFWHM_QSO)
CarbonFWHM_QSO = np.asarray(CarbonFWHM_QSO)
CarbonFWHM_NitrogenFWHM_QSO=np.asarray(CarbonFWHM_NitrogenFWHM_QSO)
IR_luminosities_QSO=np.asarray(IR_luminosities_QSO)
FIR_luminosities_QSO=np.asarray(FIR_luminosities_QSO)
NLL_FIR_QSO=np.asarray(NLL_FIR_QSO)
NLL_NitrogenFWHM_QSO=np.asarray(NLL_NitrogenFWHM_QSO)
print("For QSO")
print("")
print(NLL_IR_QSO)
print("")
print(CLL_NLL_QSO)
print("")
print(NitrogenFWHM_QSO)
print("")
print(CarbonFWHM_QSO)
print("")
print(IR_luminosities_QSO)
print("")






"""FOR SMG"""
NLL_IR_SMG_nominal_value=[]
CLL_NLL_SMG_nominal_value=[]
NitrogenFWHM_SMG_nominal_value=[]
CarbonFWHM_SMG_nominal_value=[]
CarbonFWHM_NitrogenFWHM_SMG_nominal_value=[]
IR_luminosities_SMG_nominal_value=[]
FIR_luminosities_SMG_nominal_value=[]
NLL_FIR_SMG_nominal_value=[]
NLL_NitrogenFWHM_SMG_nominal_value=[]

NLL_IR_SMG_error=[]
CLL_NLL_SMG_error=[]
NitrogenFWHM_SMG_error=[]
CarbonFWHM_SMG_error=[]
CarbonFWHM_NitrogenFWHM_SMG_error=[]
NLL_FIR_SMG_error=[]
NLL_NitrogenFWHM_SMG_error=[]

for i in range(7):
    NLL_IR_SMG_nominal_value.append(NLL_IR_SMG[i].n)
    CLL_NLL_SMG_nominal_value.append(CLL_NLL_SMG[i].n)
    NitrogenFWHM_SMG_nominal_value.append(NitrogenFWHM_SMG[i].n)
    CarbonFWHM_SMG_nominal_value.append(CarbonFWHM_SMG[i].n)
    CarbonFWHM_NitrogenFWHM_SMG_nominal_value.append(CarbonFWHM_NitrogenFWHM_SMG[i].n)
    IR_luminosities_SMG_nominal_value.append(IR_luminosities_SMG[i].n)
    FIR_luminosities_SMG_nominal_value.append(FIR_luminosities_SMG[i].n)
    NLL_FIR_SMG_nominal_value.append(NLL_FIR_SMG[i].n)
    NLL_NitrogenFWHM_SMG_nominal_value.append(NLL_NitrogenFWHM_SMG[i].n)

    NLL_IR_SMG_error.append(NLL_IR_SMG[i].s)
    CLL_NLL_SMG_error.append(CLL_NLL_SMG[i].s)
    NitrogenFWHM_SMG_error.append(NitrogenFWHM_SMG[i].s)
    CarbonFWHM_SMG_error.append(CarbonFWHM_SMG[i].s)
    CarbonFWHM_NitrogenFWHM_SMG_error.append(CarbonFWHM_NitrogenFWHM_SMG[i].s)
    NLL_FIR_SMG_error.append(NLL_FIR_SMG[i].s)
    NLL_NitrogenFWHM_SMG_error.append(NLL_NitrogenFWHM_SMG[i].s)


NLL_IR_SMG_nominal_value=np.asarray(NLL_IR_SMG_nominal_value)
CLL_NLL_SMG_nominal_value=np.asarray(CLL_NLL_SMG_nominal_value)
NitrogenFWHM_SMG_nominal_value=np.asarray(NitrogenFWHM_SMG_nominal_value)
CarbonFWHM_SMG_nominal_value=np.asarray(CarbonFWHM_SMG_nominal_value)
CarbonFWHM_NitrogenFWHM_SMG_nominal_value=np.asarray(CarbonFWHM_NitrogenFWHM_SMG_nominal_value)
IR_luminosities_SMG_nominal_value=np.asarray(IR_luminosities_SMG_nominal_value)
FIR_luminosities_SMG_nominal_value=np.asarray(FIR_luminosities_SMG_nominal_value)
NLL_FIR_SMG_nominal_value=np.asarray(NLL_FIR_SMG_nominal_value)
NLL_NitrogenFWHM_SMG_nominal_value=np.asarray(NLL_NitrogenFWHM_SMG_nominal_value)

NLL_IR_SMG_error=np.asarray(NLL_IR_SMG_error)
CLL_NLL_SMG_error=np.asarray(CLL_NLL_SMG_error)
NitrogenFWHM_SMG_error=np.asarray(NitrogenFWHM_SMG_error)
CarbonFWHM_SMG_error=np.asarray(CarbonFWHM_SMG_error)
CarbonFWHM_NitrogenFWHM_SMG_error=np.asarray(CarbonFWHM_NitrogenFWHM_SMG_error)
NLL_FIR_SMG_error=np.asarray(NLL_FIR_SMG_error)
NLL_NitrogenFWHM_SMG_error=np.asarray(NLL_NitrogenFWHM_SMG_error)


for i in range(7):
    print(f"{NLL_IR_SMG_nominal_value[i]} : {NLL_IR_SMG_error[i]}")
    print(f"{CLL_NLL_SMG_nominal_value[i]} : {CLL_NLL_SMG_error[i]}")
    print(f"{NitrogenFWHM_SMG_nominal_value[i]} : {NitrogenFWHM_SMG_error[i]}")
    print(f"{CarbonFWHM_SMG_nominal_value[i]} : {CarbonFWHM_SMG_error[i]}")
    print(f"{CarbonFWHM_NitrogenFWHM_SMG_nominal_value[i]} : {CarbonFWHM_NitrogenFWHM_SMG_error[i]}")
    print("")
print(IR_luminosities_SMG_nominal_value)
print(FIR_luminosities_SMG_nominal_value)



"""FOR QSO"""
NLL_IR_QSO_nominal_value=[]
CLL_NLL_QSO_nominal_value=[]
NitrogenFWHM_QSO_nominal_value=[]
CarbonFWHM_QSO_nominal_value=[]
CarbonFWHM_NitrogenFWHM_QSO_nominal_value=[]
IR_luminosities_QSO_nominal_value=[]
FIR_luminosities_QSO_nominal_value=[]
NLL_FIR_QSO_nominal_value=[]
NLL_NitrogenFWHM_QSO_nominal_value=[]

NLL_IR_QSO_error=[]
CLL_NLL_QSO_error=[]
NitrogenFWHM_QSO_error=[]
CarbonFWHM_QSO_error=[]
CarbonFWHM_NitrogenFWHM_QSO_error=[]
NLL_FIR_QSO_error=[]
NLL_NitrogenFWHM_QSO_error=[]

for i in range(5):
    NLL_IR_QSO_nominal_value.append(NLL_IR_QSO[i].n)
    CLL_NLL_QSO_nominal_value.append(CLL_NLL_QSO[i].n)
    NitrogenFWHM_QSO_nominal_value.append(NitrogenFWHM_QSO[i].n)
    CarbonFWHM_QSO_nominal_value.append(CarbonFWHM_QSO[i].n)
    CarbonFWHM_NitrogenFWHM_QSO_nominal_value.append(CarbonFWHM_NitrogenFWHM_QSO[i].n)
    IR_luminosities_QSO_nominal_value.append(IR_luminosities_QSO[i].n)
    FIR_luminosities_QSO_nominal_value.append(FIR_luminosities_QSO[i].n)
    NLL_FIR_QSO_nominal_value.append(NLL_FIR_QSO[i].n)
    NLL_NitrogenFWHM_QSO_nominal_value.append(NLL_NitrogenFWHM_QSO[i].n)

    NLL_IR_QSO_error.append(NLL_IR_QSO[i].s)
    CLL_NLL_QSO_error.append(CLL_NLL_QSO[i].s)
    NitrogenFWHM_QSO_error.append(NitrogenFWHM_QSO[i].s)
    CarbonFWHM_QSO_error.append(CarbonFWHM_QSO[i].s)
    CarbonFWHM_NitrogenFWHM_QSO_error.append(CarbonFWHM_NitrogenFWHM_QSO[i].s)
    NLL_FIR_QSO_error.append(NLL_FIR_QSO[i].s)
    NLL_NitrogenFWHM_QSO_error.append(NLL_NitrogenFWHM_QSO[i].s)



NLL_IR_QSO_nominal_value=np.asarray(NLL_IR_QSO_nominal_value)
CLL_NLL_QSO_nominal_value=np.asarray(CLL_NLL_QSO_nominal_value)
NitrogenFWHM_QSO_nominal_value=np.asarray(NitrogenFWHM_QSO_nominal_value)
CarbonFWHM_QSO_nominal_value=np.asarray(CarbonFWHM_QSO_nominal_value)
CarbonFWHM_NitrogenFWHM_QSO_nominal_value=np.asarray(CarbonFWHM_NitrogenFWHM_QSO_nominal_value)
IR_luminosities_QSO_nominal_value=np.asarray(IR_luminosities_QSO_nominal_value)
FIR_luminosities_QSO_nominal_value=np.asarray(FIR_luminosities_QSO_nominal_value)
NLL_FIR_QSO_nominal_value=np.asarray(NLL_FIR_QSO_nominal_value)
NLL_NitrogenFWHM_QSO_nominal_value=np.asarray(NLL_NitrogenFWHM_QSO_nominal_value)

NLL_IR_QSO_error=np.asarray(NLL_IR_QSO_error)
CLL_NLL_QSO_error=np.asarray(CLL_NLL_QSO_error)
NitrogenFWHM_QSO_error=np.asarray(NitrogenFWHM_QSO_error)
CarbonFWHM_QSO_error=np.asarray(CarbonFWHM_QSO_error)
CarbonFWHM_NitrogenFWHM_QSO_error=np.asarray(CarbonFWHM_NitrogenFWHM_QSO_error)
NLL_FIR_QSO_error=np.asarray(NLL_FIR_QSO_error)
NLL_NitrogenFWHM_QSO_error=np.asarray(NLL_NitrogenFWHM_QSO_error)


for i in range(5):
    print(f"{NLL_IR_QSO_nominal_value[i]} : {NLL_IR_QSO_error[i]}")
    print(f"{CLL_NLL_QSO_nominal_value[i]} : {CLL_NLL_QSO_error[i]}")
    print(f"{NitrogenFWHM_QSO_nominal_value[i]} : {NitrogenFWHM_QSO_error[i]}")
    print(f"{CarbonFWHM_QSO_nominal_value[i]} : {CarbonFWHM_QSO_error[i]}")
    print(f"{CarbonFWHM_NitrogenFWHM_QSO_nominal_value} : {CarbonFWHM_NitrogenFWHM_QSO_error}")
    print("")
print(IR_luminosities_QSO_nominal_value)
print(FIR_luminosities_QSO_nominal_value)


print(len(NitrogenFWHM_nominal_value_SMG))
print(len(NitrogenFWHM_nominal_value_QSO))


print(len(NLL_IR_SMG_nominal_value))
print(len(NLL_IR_QSO_nominal_value))

"""PLOTS"""



print("")
print("PLOTS")

print(r'log$\frac{L_{[NII]}}{L_{IR}}$ vs $ log FWHM_{[NII]}$')
for i in range(7):
    print(f"{i+1}) {source_reduced[i]} : {np.log10(NLL_IR[i].n)} : {NitrogenFWHM_nominal_value_SMG[i]}")
for i in range(5):
    print(f"{i + 1}) {source_reduced[i+7]} : {np.log10(NLL_IR[i+7].n)} : {NitrogenFWHM_nominal_value_QSO[i]}")
plt.errorbar(np.log10(NitrogenFWHM_nominal_value_SMG),np.log10(NLL_IR_SMG_nominal_value),yerr=0,fmt='s',color='orange',label='SMG')
plt.errorbar(np.log10(NitrogenFWHM_nominal_value_QSO),np.log10(NLL_IR_QSO_nominal_value),yerr=0,fmt='*',color='red',label='QSO')
plt.xlabel(r'$log FWHM$')
plt.ylabel(r'$log \frac{L_{[NII]}}{L_{IR}}$')
plt.legend()
plt.title(r'$log\frac{L_{[NII]}}{L_{IR}}$ vs $log FWHM_{[NII]}$')
plt.axhline(y = -3.5, color = 'grey', linestyle = '--')
plt.show()
print("")
print("")

print(r'log$\frac{L_{[NII]}}{L_{IR}}$ vs log$ L_{IR}$') #IMP
for i in range(NLL_IR.shape[0]):
    print(f"{i+1}) {source_reduced[i]} : {np.log10(NLL_IR[i].n)} : {np.log10(IR_luminosities[i].n)}")
plt.errorbar(np.log10(IR_luminosities_SMG_nominal_value),np.log10(NLL_IR_SMG_nominal_value),yerr=0,fmt='s',color='orange',label='SMG')
plt.errorbar(np.log10(IR_luminosities_QSO_nominal_value),np.log10(NLL_IR_QSO_nominal_value),yerr=0,fmt='*',color='red',label='QSO')
plt.xlabel(r'$log L_{IR}$')
plt.ylabel(r'$log \frac{L_{[NII]}}{L_{IR}}$')
plt.legend()
plt.title(r'$log\frac{L_{[NII]}}{L_{IR}}$ vs $logL_{IR}$')
plt.axhline(y = -3.5, color = 'grey', linestyle = '--')
plt.show()
print("")
print("")



print(r'$\frac{L_{[NII]}}{L_{IR}}$ vs $L_{IR}$')
for i in range(NLL_IR.shape[0]):
    print(f"{i+1}) {source_reduced[i]} : {NLL_IR[i]} : {IR_luminosities[i]}")
plt.errorbar(IR_luminosities_SMG_nominal_value,NLL_IR_SMG_nominal_value,yerr=NLL_IR_SMG_error,fmt='s',ecolor='grey',color='orange',capsize=5,label='SMG')
plt.errorbar(IR_luminosities_QSO_nominal_value,NLL_IR_QSO_nominal_value,yerr=NLL_IR_QSO_error,fmt='*',ecolor='grey',color='red',capsize=5,label='QSO')
plt.xlabel(r'$L_{IR}$')
plt.ylabel(r'$\frac{L_{[NII]}}{L_{IR}}$')
plt.legend()
plt.title(r'$\frac{L_{[NII]}}{L_{IR}}$ vs $L_{IR}$')
plt.axhline(y = 0, color = 'grey', linestyle = '--')
plt.show()
print("")
print("")


print(r'$\frac{L_{[NII]}}{L_{FIR}}$ vs $L_{IR}$')
for i in range(NLL_FIR.shape[0]):
    print(f"{i+1}) {source_reduced[i]} : {NLL_FIR[i]} : {IR_luminosities[i]}")
plt.errorbar(IR_luminosities_SMG_nominal_value,NLL_FIR_SMG_nominal_value,yerr=NLL_FIR_SMG_error,fmt='s',ecolor='grey',color='orange',capsize=5,label='SMG')
plt.errorbar(IR_luminosities_QSO_nominal_value,NLL_FIR_QSO_nominal_value,yerr=NLL_FIR_QSO_error,fmt='*',ecolor='grey',color='red',capsize=5,label='QSO')
plt.xlabel(r'$L_{IR}$')
plt.ylabel(r'$\frac{L_{[NII]}}{L_{FIR}}$')
plt.legend()
plt.title(r'$\frac{L_{[NII]}}{L_{FIR}}$ vs $L_{IR}$')
plt.axhline(y = 0, color = 'grey', linestyle = '--')
plt.show()
print("")
print("")


print(r'$\frac{L_{[NII]}}{L_{FIR}}$ vs $L_{FIR}$')
for i in range(NLL_FIR.shape[0]):
    print(f"{i+1}) {source_reduced[i]} : {NLL_FIR[i]} : {FIR_luminosities[i]}")
plt.errorbar(FIR_luminosities_SMG_nominal_value,NLL_FIR_SMG_nominal_value,yerr=NLL_FIR_SMG_error,fmt='s',ecolor='grey',color='orange',capsize=5,label='SMG')
plt.errorbar(FIR_luminosities_QSO_nominal_value,NLL_FIR_QSO_nominal_value,yerr=NLL_FIR_QSO_error,fmt='*',ecolor='grey',color='red',capsize=5,label='QSO')
plt.xlabel(r'$L_{FIR}$')
plt.ylabel(r'$\frac{L_{[NII]}}{L_{FIR}}$')
plt.legend()
plt.title(r'$\frac{L_{[NII]}}{L_{FIR}}$ vs $L_{FIR}$')
plt.axhline(y = 0, color = 'grey', linestyle = '--')
plt.show()
print("")
print("")

print(r'$log\frac{L_{[NII]}}{L_{FIR}}$ vs $logL_{FIR}$')
for i in range(NLL_FIR.shape[0]):
    print(f"{i+1}) {source_reduced[i]} : {np.log10(NLL_FIR[i].n)} : {np.log10(FIR_luminosities[i].n)}")
plt.errorbar(np.log10(FIR_luminosities_SMG_nominal_value),np.log10(NLL_FIR_SMG_nominal_value),fmt='s',color='orange',capsize=5,label='SMG')
plt.errorbar(np.log10(FIR_luminosities_QSO_nominal_value),np.log10(NLL_FIR_QSO_nominal_value),fmt='*',color='red',capsize=5,label='QSO')
plt.xlabel(r'$logL_{FIR}$')
plt.ylabel(r'$log\frac{L_{[NII]}}{L_{FIR}}$')
plt.legend()
plt.title(r'$log\frac{L_{[NII]}}{L_{FIR}}$ vs $logL_{FIR}$')
plt.axhline(y = -3.25, color = 'grey', linestyle = '--')
plt.show()
print("")
print("")

print("C/N vs IR")
for i in range(NLL_IR.shape[0]):
    print(f"{i+1}) {source_reduced[i]} : {CLL_NLL[i]} : {IR_luminosities[i]}")
plt.errorbar(IR_luminosities_SMG_nominal_value,CLL_NLL_SMG_nominal_value,yerr=CLL_NLL_SMG_error,fmt='s',ecolor='grey',color='orange',capsize=5,label='SMG')
plt.errorbar(IR_luminosities_QSO_nominal_value,CLL_NLL_QSO_nominal_value,yerr=CLL_NLL_QSO_error,fmt='*',ecolor='grey',color='red',capsize=5,label='QSO')
plt.xlabel(r'$L_{IR}$')
plt.ylabel(r'$\frac{L_{[CII]}}{L_{[NII]}}$')
plt.legend()
plt.title(r'$\frac{L_{[CII]}}{L_{[NII]}}$ vs $L_{IR}$')
plt.axhline(y = 0, color = 'grey', linestyle = '--')
plt.show()
print("")
print("")


print("log C/N vs log IR")
for i in range(NLL_IR.shape[0]):
    print(f"{i+1}) {source_reduced[i]} : {np.log10(CLL_NLL[i].n)} : {np.log10(IR_luminosities[i].n)}")
plt.errorbar(np.log10(IR_luminosities_SMG_nominal_value),np.log10(CLL_NLL_SMG_nominal_value),yerr=0,fmt='s',color='orange',label='SMG')
plt.errorbar(np.log10(IR_luminosities_QSO_nominal_value),np.log10(CLL_NLL_QSO_nominal_value),yerr=0,fmt='*',color='red',label='QSO')
plt.xlabel(r' $logL_{IR}$')
plt.ylabel(r' $log\frac{L_{[CII]}}{L_{[NII]}}$')
plt.legend()
plt.title(r' $log\frac{L_{[CII]}}{L_{[NII]}}$ vs  $logL_{IR}$')
plt.axhline(y = 0.4, color = 'grey', linestyle = '--')
plt.show()
print("")
print("")


print("FWHM_[NII] vs log_IR")
for i in range(NLL_IR.shape[0]):
    print(f"{i+1}) {source_reduced[i]} : {NitrogenFWHM[i]} : {IR_luminosities[i]}")
plt.errorbar(np.log10(IR_luminosities_SMG_nominal_value),NitrogenFWHM_SMG_nominal_value,yerr=NitrogenFWHM_SMG_error,fmt='s',ecolor='grey',color='orange',capsize=5,label='SMG')
plt.errorbar(np.log10(IR_luminosities_QSO_nominal_value),NitrogenFWHM_QSO_nominal_value,yerr=NitrogenFWHM_QSO_error,fmt='*',ecolor='grey',color='red',capsize=5,label='QSO')
plt.xlabel(r'$logL_{IR}$')
plt.ylabel(r'$FWHM_{[NII]}$')
plt.legend()
plt.title(r'$FWHM_{[NII]}$ vs  $logL_{IR}$')
plt.show()
print("")
print("")


print("FWHM_[CII] vs log_IR")
for i in range(NLL_IR.shape[0]):
    print(f"{i+1}) {source_reduced[i]} : {CarbonFWHM[i]} : {IR_luminosities[i]}")
plt.errorbar(np.log10(IR_luminosities_SMG_nominal_value),CarbonFWHM_SMG_nominal_value,yerr=CarbonFWHM_SMG_error,fmt='s',ecolor='grey',color='orange',capsize=5,label='SMG')
plt.errorbar(np.log10(IR_luminosities_QSO_nominal_value),CarbonFWHM_QSO_nominal_value,yerr=CarbonFWHM_QSO_error,fmt='*',ecolor='grey',color='red',capsize=5,label='QSO')
plt.xlabel(r'log $L_{IR}$')
plt.ylabel(r'$FWHM_{[CII]}$')
plt.legend()
plt.title(r'$FWHM_{[CII]}$ vs log $L_{IR}$')
plt.axhline(y = 0, color = 'grey', linestyle = '--')
plt.show()
print("")
print("")

print(r'$\frac{FWHM_{[CII}}{FWHM_{[NII]}}$ vs log_IR')
for i in range(NLL_IR.shape[0]):
    print(f"{i+1}) {source_reduced[i]} : {CarbonFWHM_NitrogenFWHM[i]} : {IR_luminosities[i]}")
plt.errorbar(np.log10(IR_luminosities_SMG_nominal_value),CarbonFWHM_NitrogenFWHM_SMG_nominal_value,yerr=CarbonFWHM_NitrogenFWHM_SMG_error,fmt='s',ecolor='grey',color='orange',capsize=5,label='SMG')
plt.errorbar(np.log10(IR_luminosities_QSO_nominal_value),CarbonFWHM_NitrogenFWHM_QSO_nominal_value,yerr=CarbonFWHM_NitrogenFWHM_QSO_error,fmt='*',ecolor='grey',color='red',capsize=5,label='QSO')
plt.xlabel(r' $logL_{IR}$')
plt.ylabel(r'$\frac{FWHM_{[CII}}{FWHM_{[NII]}}$')
plt.legend()
plt.title(r'$\frac{FWHM_{[CII}}{FWHM_{[NII]}}$ vs  $logL_{IR}$')
plt.axhline(y = 0, color = 'grey', linestyle = '--')
plt.show()
print("")
print("")

print(r'$log\frac{FWHM_{[NII]}}{L_{NII}}$ vs log_IR')
for i in range(NLL_IR.shape[0]):
    print(f"{i+1}) {source_reduced[i]} : {CarbonFWHM_NitrogenFWHM[i]} : {IR_luminosities[i]}")
plt.errorbar(np.log10(IR_luminosities_SMG_nominal_value),np.log10(NLL_NitrogenFWHM_SMG_nominal_value),yerr=0,fmt='s',ecolor='grey',color='orange',capsize=5,label='SMG')
plt.errorbar(np.log10(IR_luminosities_QSO_nominal_value),np.log10(NLL_NitrogenFWHM_QSO_nominal_value),yerr=0,fmt='*',ecolor='grey',color='red',capsize=5,label='QSO')
plt.xlabel(r'log $L_{IR}$')
plt.ylabel(r'$log\frac{FWHM_{[NII]}}{L_{N[II]}}$')
plt.legend()
plt.title(r'$log\frac{FWHM_{[NII]}}{L_{N[II]}}$ vs log $L_{IR}$')
plt.axhline(y = 0, color = 'grey', linestyle = '--')
plt.show()
print("")
print("")

print(r'$log\frac{FWHM_{[NII]}/L_{NII}}{L_{IR}}$ vs log_IR')
for i in range(NLL_IR.shape[0]):
    print(f"{i+1}) {source_reduced[i]} : {CarbonFWHM_NitrogenFWHM[i]} : {IR_luminosities[i]}")
plt.errorbar(np.log10(IR_luminosities_SMG_nominal_value),np.log10(NLL_NitrogenFWHM_SMG_nominal_value/IR_luminosities_SMG_nominal_value),yerr=0,fmt='s',ecolor='grey',color='orange',capsize=5,label='SMG')
plt.errorbar(np.log10(IR_luminosities_QSO_nominal_value),np.log10(NLL_NitrogenFWHM_QSO_nominal_value/IR_luminosities_QSO_nominal_value),yerr=0,fmt='*',ecolor='grey',color='red',capsize=5,label='QSO')
plt.xlabel(r'log $L_{IR}$')
plt.ylabel(r'$log\frac{FWHM_{[NII]}/L_{N[II]}}{L_{IR}}$')
plt.legend()
plt.title(r'$log\frac{FWHM_{[NII]}/L_{N[II]}}{L_{IR}}$ vs log $L_{IR}$')
plt.axhline(y = 0, color = 'grey', linestyle = '--')
plt.show()
print("")
print("")

"""
print(r'$L_{FIR} vs L_{IR}')
plt.errorbar(IR_luminosities_SMG_nominal_value,FIR_luminosities_SMG_nominal_value,yerr=0,fmt='s',ecolor='grey',color='orange',capsize=5,label='SMG')
plt.errorbar(IR_luminosities_QSO_nominal_value,FIR_luminosities_QSO_nominal_value,yerr=0,fmt='*',ecolor='grey',color='red',capsize=5,label='QSO')
plt.xlabel(r'$L_{IR}$')
plt.ylabel(r'$L_{FIR}$')
plt.legend()
plt.title(r'$L_{FIR} vs L_{IR}$')
plt.show()
print("")
print("")
"""


print(r'$\frac{L_{[NII]}}{L_{IR}}$ vs $FWHM_{[NII]}$')
for i in range(NLL_IR.shape[0]):
    print(f"{i+1}) {source_reduced[i]} : {NLL_IR[i]/NitrogenFWHM[i]} : {IR_luminosities[i]}")
plt.errorbar(IR_luminosities_SMG_nominal_value,NLL_IR_SMG_nominal_value/NitrogenFWHM_nominal_value_SMG,yerr=0,fmt='s',ecolor='grey',color='orange',capsize=5,label='SMG')
plt.errorbar(IR_luminosities_QSO_nominal_value,NLL_IR_QSO_nominal_value/NitrogenFWHM_nominal_value_QSO,yerr=0,fmt='*',ecolor='grey',color='red',capsize=5,label='QSO')
plt.xlabel(r'$FWHM_{[NII]}$')
plt.ylabel(r'$\frac{L_{[NII]}}{L_{IR}}$')
plt.legend()
plt.title(r'$\frac{L_{[NII]}}{L_{IR}}$ vs $FWHM_{[NII]}$')
plt.axhline(y = 0, color = 'grey', linestyle = '--')
plt.show()
print("")
print("")


"""**************************************************HISTOGRAM**************************************"""
def histogram_redshift():
    f = np.linspace(2, 8, endpoint=True, num=7)
    z_SMG = np.asarray([2.5543, 4.342, 5.29795, 4.24, 4.768, 4.7])
    z_QSO = np.asarray([4.407, 4.7, 4.12, 7.5413, 3.991, 3.93])
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.hist(z_SMG, f, ec="black", color="orange", alpha=0.5, label="SMG")
    ax.hist(z_QSO, f, ec="black", color="red", alpha=0.5, label="QSO")
    plt.xlabel("Redshift")
    plt.ylabel("Number of Galaxies")
    plt.legend()
    plt.show()
"""print(histogram_redshift())"""


"""************************************************** L_FIR_M_H2 **************************************"""
def L_FIR_M_H2():
    molecular_gas_mass_QSO = np.asarray(
        [ufloat(6.4e10, 0e10), ufloat(8e10, 0e10), ufloat(4e10, 0e10), ufloat(1e10, 0e10), ufloat(0.325e11, 0.225e11)])
    molecular_gas_mass_SMG = np.asarray(
        [ufloat(3.6e10, 3.1e10), ufloat(7.5e10, 0.1e10), ufloat(1.4e11, 0.2e11), ufloat(5.3e10, 0e10),
         ufloat(3.8e10, 1.2e10), ufloat(7e10, 0e10)])

    fir_luminosities_SMG = np.asarray(
        [ufloat(0.67e12, 0.25e12), ufloat(8.2e12, 1.5e12), ufloat(6.6e12, 1.0e12), ufloat(1.1e13, 0.6e13)
            , ufloat(3.9e13, 0.6e13), ufloat(2.4e13, 0)])
    fir_luminosities_QSO = np.asarray(
        [ufloat(3.1e13, 0), ufloat(2.3e13, 0), ufloat(5.3e12, 0.5e12), ufloat(3.6e12, 0.1e12), ufloat(5e12, 0.5e12)])

    type_reduced_SMG = np.asarray(["DSFG", "SMG", "SMG", "SMG", "SMG", "SMG", ])
    type_reduced_QSO = np.asarray(["QSO", "QSO", "QSO", "QSO", "QSO"])

    source_reduced_SMG = np.asarray(["Hyde", "9io9", "AzTEC-1", "Aztec-3", "SPT2132-58", "BR-1202-SMG"])

    source_reduced_QSO = np.asarray(["BRI-1335-0417", "BR-1202-QSO",
                                     "PSSJ2322+1944", "APM 08279+5255", "MM 18423+5938"])

    nitrogen_line_luminosity_SMG = np.asarray(
        [ufloat(7.5e7, 2e7), ufloat(7.0e8, 0.7e8), ufloat(2.14e8, 0.23e8), ufloat(2.0e8, 0.9e8)
            , ufloat(1.06e9, 0.15e9), ufloat(6.1e8, 0.5e8)])

    nitrogen_line_luminosity_QSO = np.asarray([ufloat(4.4e8, 0.4e8), ufloat(3.97e8, 0.3e8), ufloat(5.7e8, 2.1e8),
                                               ufloat(1.11e9, 0.30e9), ufloat(8.2e8, 1.1e8)])

    nll_ID141 = 0.000285

    fir_M_SMG = fir_luminosities_SMG / molecular_gas_mass_SMG
    fir_M_QSO = fir_luminosities_QSO / molecular_gas_mass_QSO

    nll_FIR_SMG = nitrogen_line_luminosity_SMG / fir_luminosities_SMG
    nll_FIR_QSO = nitrogen_line_luminosity_QSO / fir_luminosities_QSO

    fir_M_SMG_nominal_value = []
    fir_M_QSO_nominal_value = []
    nll_FIR_SMG_nominal_value = []
    nll_FIR_QSO_nominal_value = []
    fir_luminosities_SMG_nominal_value = []
    fir_luminosities_QSO_nominal_value = []

    for i in range(len(fir_M_SMG)):
        fir_M_SMG_nominal_value.append(fir_M_SMG[i].n)
        nll_FIR_SMG_nominal_value.append(nll_FIR_SMG[i].n)
        fir_luminosities_SMG_nominal_value.append(fir_luminosities_SMG[i].n)

    for i in range(len(fir_M_QSO)):
        fir_M_QSO_nominal_value.append(fir_M_QSO[i].n)
        nll_FIR_QSO_nominal_value.append(nll_FIR_QSO[i].n)
        fir_luminosities_QSO_nominal_value.append(fir_luminosities_QSO[i].n)

    fir_M_SMG_nominal_value = np.asarray(fir_M_SMG_nominal_value)
    fir_M_QSO_nominal_value = np.asarray(fir_M_QSO_nominal_value)
    nll_FIR_SMG_nominal_value = np.asarray(nll_FIR_SMG_nominal_value)
    nll_FIR_QSO_nominal_value = np.asarray(nll_FIR_QSO_nominal_value)
    fir_luminosities_SMG_nominal_value = np.asarray(fir_luminosities_SMG_nominal_value)
    fir_luminosities_QSO_nominal_value = np.asarray(fir_luminosities_QSO_nominal_value)
    print("***********************************************************************************************************")
    for i in range(len(nitrogen_line_luminosity_SMG)):
        print(
            f"source: {source_reduced_SMG[i]} & {molecular_gas_mass_SMG[i]/1e10} &  {fir_M_SMG[i]/1e2}")

    for i in range(len(nitrogen_line_luminosity_QSO)):
        print(
            f"{source_reduced_QSO[i]} & {molecular_gas_mass_QSO[i]/1e10} &  {fir_M_QSO[i]/1e2}")
    print("***********************************************************************************************************")
    plt.errorbar(np.log10(fir_luminosities_SMG_nominal_value), np.log10(nll_FIR_SMG_nominal_value), yerr=0, fmt='s',
                 ecolor='grey', color='orange', capsize=5, label='SMG')
    plt.errorbar(12.633468455579587, -3.4459477347431235, yerr=0, fmt='s', ecolor='grey', color='orange', capsize=5,
                 label='SMG')
    plt.errorbar(np.log10(fir_luminosities_QSO_nominal_value), np.log10(nll_FIR_QSO_nominal_value), yerr=0, fmt='*',
                 ecolor='grey', color='red', capsize=5, label='QSO')
    plt.xlabel(r'$L_{FIR}$')
    plt.ylabel(r'$L_{[NII]}/L_{FIR}$')
    plt.title(r'$L_{[NII]}/L_{FIR}$ vs $L_{FIR}$')

    plt.legend()
    plt.show()

    plt.errorbar(fir_M_SMG_nominal_value, nll_FIR_SMG_nominal_value*1e4, yerr=0, fmt='s', ecolor='grey', color='orange',
                 capsize=5, label='SMG')
    plt.errorbar(fir_M_QSO_nominal_value, nll_FIR_QSO_nominal_value*1e4, yerr=0, fmt='*', ecolor='grey', color='red',
                 capsize=5, label='QSO')
    plt.errorbar(230, 0.000358*1e4, yerr=0, fmt='s', ecolor='grey', color='orange', capsize=5)
    plt.axvline(x=80, color='grey', linestyle='--')
    plt.xlabel(r'$L_{FIR}/M_{H_2}$')
    plt.ylabel(r'$L_{[NII]}/L_{FIR}$')
    plt.title(r'$L_{[NII]}/L_{FIR}$ vs $L_{FIR}/M_{H_2}$')
    yfmt = ScalarFormatter()
    yfmt.set_useOffset(1e4)
    plt.legend()
    plt.show()

    plt.errorbar(fir_M_SMG_nominal_value, np.log10(nll_FIR_SMG_nominal_value), yerr=0, fmt='s', ecolor='grey',
                 color='orange', capsize=5, label='SMG')
    plt.errorbar(fir_M_QSO_nominal_value, np.log10(nll_FIR_QSO_nominal_value), yerr=0, fmt='*', ecolor='grey',
                 color='red', capsize=5, label='QSO')
    plt.errorbar(230, np.log10(0.000358), yerr=0, fmt='s', ecolor='grey', color='orange', capsize=5)
    plt.axvline(x=80, color='grey', linestyle='--')
    plt.xlabel(r'$L_{FIR}/M_{H_2}$')
    plt.ylabel(r'$L_{[NII]}/L_{FIR}$')
    plt.title(r'$L_{[NII]}/L_{FIR}$ vs $L_{FIR}/M_{H_2}$')
    plt.legend()
    plt.show()

    for i in range(len(nitrogen_line_luminosity_SMG)):
        print(
            f"source: {source_reduced_SMG[i]} ; L_[FIR]/M: {fir_M_SMG[i]}")

    for i in range(len(nitrogen_line_luminosity_QSO)):
        print(
            f"source: {source_reduced_QSO[i]} ; L_[FIR]/M: {fir_M_QSO[i]}")

print(L_FIR_M_H2())



"""***************************including local galaxies**************************************************"""


data1=np.loadtxt(open(r"C:\Users\kolup\Desktop\new_local_galaxies.csv"),delimiter=',')
data2=np.loadtxt(open(r"C:\Users\kolup\Desktop\local_galaxies_2.csv"),delimiter=',')

def local_galaxies_1(data1):
    def luminosity_distance(x):
        z = x
        W_R = 0.  # Omega Radiation
        W_K = 0.  # Omega curvature
        c = 299792.458  # speed of light in km/s
        H_0 = 69.6  # Hubbles constant
        W_M = 0.286  # Omega matter
        W_V = 1 - W_M  # Omega vacuum
        Tyr = 977.8  # coefficent for converting 1/H into Gyr

        h = H_0 / 100
        W_R = 4.165e-5 / (h * h)
        W_K = 1 - W_M - W_R - W_V
        a_z = 1.0 / (1 + 1.0 * z)
        age = 0
        n = 1000

        for i in range(n):
            a = a_z * (i + 0.5) / n
            a_dot = np.sqrt(W_K + (W_M / a) + (W_R / (a * a)) + (W_V * a * a))
            age = age + 1. / a_dot
        z_age = a_z * age / n
        z_age_Gyr = (Tyr / H_0) * z_age

        DTT = 0.0
        DCMR = 0.0

        # do integral over a=1/(1+z) from az to 1 in n steps, midpoint rule
        for i in range(n):
            a = a_z + (1 - a_z) * (i + 0.5) / n
            adot = np.sqrt(W_K + (W_M / a) + (W_R / (a * a)) + (W_V * a * a))
            DTT = DTT + 1. / adot
            DCMR = DCMR + 1. / (a * adot)

        DTT = (1. - a_z) * DTT / n
        DCMR = (1. - a_z) * DCMR / n
        age = DTT + z_age
        age_Gyr = age * (Tyr / H_0)
        DTT_Gyr = (Tyr / H_0) * DTT
        DCMR_Gyr = (Tyr / H_0) * DCMR
        DCMR_Mpc = (c / H_0) * DCMR

        # tangential comoving distance

        ratio = 1.00
        x = sqrt(abs(W_K)) * DCMR
        if x > 0.1:
            if W_K > 0:
                ratio = 0.5 * (exp(x) - exp(-x)) / x
            else:
                ratio = sin(x) / x
        else:
            y = x * x
            if W_K < 0: y = -y
            ratio = 1. + y / 6. + y * y / 120.
        DCMT = ratio * DCMR
        DA = a_z * DCMT
        DA_Mpc = (c / H_0) * DA
        kpc_DA = DA_Mpc / 206.264806
        DA_Gyr = (Tyr / H_0) * DA
        DL = DA / (a_z * a_z)
        DL_Mpc = (c / H_0) * DL
        return DL_Mpc

    f_N = []
    z = []
    fwhm = []
    IR_luminosity_log = []

    for i in range(data1.shape[0]):
        f_N.append(ufloat(data1[i][0], data1[i][1]))
        z.append(data1[i][2])
        fwhm.append(data1[i][3])
        IR_luminosity_log.append(data1[i][4])

    f_N = np.asarray(f_N)
    z = np.asarray(z)
    fwhm = np.asarray(fwhm)
    IR_luminosity_log = np.asarray(IR_luminosity_log)

    print(f" median redhsift = {np.median(z)}")

    constant = (4 * np.pi * ((3.086e22) ** 2) * (1e-17)) / (3.846e26)

    f_N_luminosity = []

    for i in range(data1.shape[0]):
        f_N_luminosity.append(constant * f_N[i] * (luminosity_distance(z[i]) ** 2))
    f_N_luminosity = np.asarray(f_N_luminosity)

    for i in range(data1.shape[0]):
        print(f"{i} : {f_N_luminosity[i]}")

    a = []
    for i in range(data1.shape[0]):
        a.append(np.log10(f_N_luminosity[i].n) - IR_luminosity_log[i])  # converting to [NII]205
    a = np.asarray(a)
    print(a)

    plt.scatter(IR_luminosity_log, a)
    plt.show()
    return IR_luminosity_log, a




def local_galaxies_2(data):
    print(data)

    fir = []
    f_N = []
    D_L = []

    print(data.shape[0])

    for i in range(data.shape[0]):
        fir.append(data[i][0])
        f_N.append(data[i][1])
        D_L.append(data[i][2])

    print(f_N)

    constant = (4 * np.pi * ((3.086e22) ** 2) * (1e-14)) / (3.846e26)

    print(constant)

    fir_luminosity = []
    for i in range(data.shape[0]):
        fir_luminosity.append(constant * data[i][0] * (data[i][2] ** 2))

    fir_luminosity = np.asarray(fir_luminosity)
    print(fir_luminosity)
    print("")

    ir_luminosity=fir_luminosity/0.75

    f_N_luminosity = []

    for i in range(data.shape[0]):
        f_N_luminosity.append(constant * data[i][1] * (data[i][2] ** 2))

    f_N_luminosity = np.asarray(f_N_luminosity)
    print(f_N_luminosity)
    print("")

    f_N_luminosity = f_N_luminosity / 5

    for i in range(data.shape[0]):
        print(f"{fir_luminosity[i]} : {f_N_luminosity[i]} : {f_N_luminosity[i] / fir_luminosity[i]}")

    f_N_IR_luminoisty = []

    for i in range(data.shape[0]):
        f_N_IR_luminoisty.append(f_N_luminosity[i] / ir_luminosity[i])

    f_N_IR_luminoisty = np.asarray(f_N_IR_luminoisty)
    print(f_N_IR_luminoisty)



    plt.scatter(np.log10(ir_luminosity), np.log10(f_N_IR_luminoisty))
    plt.xlabel(r'$L_{IR}$')
    plt.ylabel(r'$\frac{L_{[NII]}}{L_{IR}}$')
    plt.show()

    return ir_luminosity,f_N_IR_luminoisty



#combined plot

a,b=local_galaxies_1(data1)
c,d=local_galaxies_2(data2)


plt.scatter(a,b,color='blue')
plt.scatter(np.log10(c),np.log10(d),color='blue')
plt.show()

plt.scatter(a,b,color='blue')
plt.scatter(np.log10(c),np.log10(d),color='green')
plt.show()




print(r'log$\frac{L_{[NII]}}{L_{IR}}$ vs log$ L_{IR}$')
for i in range(NLL_IR.shape[0]):
    print(f"{i+1}) {source_reduced[i]} : {np.log10(NLL_IR[i].n)} : {np.log10(IR_luminosities[i].n)}")
plt.errorbar(np.log10(IR_luminosities_SMG_nominal_value),np.log10(NLL_IR_SMG_nominal_value),yerr=0,fmt='s',color='orange',label='SMG')
plt.errorbar(np.log10(IR_luminosities_QSO_nominal_value),np.log10(NLL_IR_QSO_nominal_value),yerr=0,fmt='*',color='red',label='QSO')
plt.errorbar(a,b,yerr=0,fmt='^',color='green',label='Local galaxies')
plt.errorbar(np.log10(c),np.log10(d),yerr=0,fmt='^',color='green')
plt.xlabel(r'$log L_{IR}$')
plt.ylabel(r'$log \frac{L_{[NII]}}{L_{IR}}$')
plt.legend()
plt.title(r'$log\frac{L_{[NII]}}{L_{IR}}$ vs $logL_{IR} $ ')
#plt.axhline(y = -3.5, color = 'grey', linestyle = '--')
plt.show()
print("")
print("")

"""
ir_luminosity_of_my_galaxies=np.asarray(np.concatenate((np.log10(IR_luminosities_SMG_nominal_value),np.log10(IR_luminosities_QSO_nominal_value)),axis=None))
nll_ir_of_my_galaxies=np.asarray(np.concatenate((np.log10(NLL_IR_SMG_nominal_value),np.log10(NLL_IR_QSO_nominal_value)),axis=None))
ir_luminosity_of_local_galaxies=np.asarray(np.concatenate((a,np.log10(c)),axis=None))
nll_ir_of_local_galaxies=np.asarray(np.concatenate((b,np.log10(d)),axis=None))

def straight_line(x,m,c):
    y=m*x+c
    return y

gm_sl=Model(straight_line)
params_sl1=gm_sl.make_params(m=-3,c=-9)
params_sl2=gm_sl.make_params(m=-1.5,c=-4.5)


out1=gm_sl.fit(nll_ir_of_my_galaxies,params_sl1,method='Leastsq',x=ir_luminosity_of_my_galaxies)
out2=gm_sl.fit(nll_ir_of_local_galaxies,params_sl2,method='Leastsq',x=ir_luminosity_of_local_galaxies)

print(out1.fit_report())
print(out2.fit_report())

plt.errorbar(np.log10(IR_luminosities_SMG_nominal_value),np.log10(NLL_IR_SMG_nominal_value),yerr=0,fmt='s',color='orange',label='SMG')
plt.errorbar(np.log10(IR_luminosities_QSO_nominal_value),np.log10(NLL_IR_QSO_nominal_value),yerr=0,fmt='*',color='red',label='QSO')
plt.errorbar(a,b,yerr=0,fmt='^',color='green',label='Local galaxies')
plt.errorbar(np.log10(c),np.log10(d),yerr=0,fmt='^',color='green')
plt.errorbar(ir_luminosity_of_my_galaxies,out1.best_fit)
plt.errorbar(ir_luminosity_of_local_galaxies,out2.best_fit)
plt.show()


total_ir_luminosity=np.asarray(np.concatenate((ir_luminosity_of_my_galaxies,ir_luminosity_of_local_galaxies),axis=None))

plt.errorbar(np.log10(IR_luminosities_SMG_nominal_value),np.log10(NLL_IR_SMG_nominal_value),yerr=0,fmt='s',color='orange',label='SMG')
plt.errorbar(np.log10(IR_luminosities_QSO_nominal_value),np.log10(NLL_IR_QSO_nominal_value),yerr=0,fmt='*',color='red',label='QSO')
plt.errorbar(a,b,yerr=0,fmt='^',color='green',label='Local galaxies')
plt.errorbar(np.log10(c),np.log10(d),yerr=0,fmt='^',color='green')
plt.errorbar(np.concatenate((total_ir_luminosity,14),axis=None),straight_line(np.concatenate((total_ir_luminosity,14),axis=None),-0.75376223,5.42896592),color='grey')
plt.errorbar(np.concatenate((total_ir_luminosity,14),axis=None),straight_line(np.concatenate((total_ir_luminosity,14),axis=None),-0.17890571,-2.46116105),color='grey')
plt.xlim([8,14])
plt.ylim([-5.2,-3.5])
plt.show()"""


"""**************************Values****************"""
print("****************************************************************************************************************")
print("source : [NII] luminosity : [NII] FWHM : IR : FIR")
for i in range(n):
    print(f"{source_reduced[i]}    & {nitrogen_line_luminosity[i]}  & {IR_luminosities[i]} &{FIR_luminosities[i]}  ")

print("****************************************************************************************************************")
print("source : [NII] luminosity : [NII] FWHM : IR : FIR")
for i in range(n):
    print(f"{source_reduced[i]}    & {nitrogen_line_luminosity[i]/1e9}  & {IR_luminosities[i]/1e13} &{FIR_luminosities[i]/1e13}  ")

print("****************************************************************************************************************")

print("source : [NII]/IR : [NII]/FIR : L_C/L_N : FWHM_C/FWHM_N")
for i in range(n):
    print(f"{source_reduced[i]} & {np.round(np.log10(NLL_IR[i].n),decimals=3)} & {np.round(np.log10(NLL_FIR[i].n),decimals=3)} & {CLL_NLL[i]} & {CarbonFWHM_NitrogenFWHM[i]}")

print("****************************************************************************************************************")