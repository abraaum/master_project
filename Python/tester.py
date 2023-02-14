"""
Testing sensitivity analysis for dynamic lambda, coupled model
"""

import ORdmm_Land_em_coupling as model
from scipy.integrate import odeint
import numpy as np
import os
import matplotlib.pyplot as plt
import tqdm
import pandas as pd

num_beats = 50  # real run 100-1000
tsteps = np.arange(0.0, 650.0, 0.1)  # real run 1000

#lst_value = [0.9, 0.95, 1.0, 1.05, 1.1] # lam
lst_value = [0.0, 0.5, 1.0, 1.5, 2, 5] # kse

Tas = []
Vs =[]
Ls = []

for i in range(len(lst_value)):
    y0 = model.init_state_values() # lmbda=lst_value[i]
    parameters = model.init_parameter_values(
        # CHANGE MANUALLY
        celltype=0,
        #lmbda_set=lst_value[i],
        Kse = lst_value[i],
    )

    for n in tqdm.tqdm(range(num_beats)):
        y = odeint(model.rhs, y0, tsteps, args=(parameters,))
        y0 = y[-1]

    # Extract the membrane potential
    V = y.T[model.state_indices('v')]
    L = y.T[model.state_indices('lmbda')]
    monitor = np.array([model.monitor(r, t, parameters) for r, t in zip(y, tsteps)])
    Ta = monitor.T[model.monitor_indices('Ta')]
    
    Vs.append(V)
    Tas.append(Ta)
    Ls.append(L)


fig, ax = plt.subplots(3, 1, sharex=True)
for i in range(len(lst_value)):
    V_t = Vs[i]
    Ta_t = Tas[i]
    L_t = Ls[i]

    ax[0].plot(tsteps, V_t, label=f"val:{lst_value[i]}")
    ax[0].set_title("Voltage")
    ax[1].plot(tsteps, L_t, label=f"val:{lst_value[i]}")
    ax[1].set_title("Lambda")
    ax[2].plot(tsteps, Ta_t, label=f"val:{lst_value[i]}")
    ax[2].set_title("Ta")
   


plt.legend()
plt.show()

