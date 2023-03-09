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

num_beats = 100  # real run 100-1000
tsteps = np.arange(0.0, 650.0, 0.1)  # real run 1000

kse_value = [0.0, 0.5, 1.0, 1.5, 2, 5, 10] # kse

Tas = []
Vs =[]
Ls = []

for i in range(len(kse_value)):
    y0 = np.load(
                f"init_values/coupled/gomez_endo_coupled_dyn_100.npy"
            )
    parameters = model.init_parameter_values(
        # CHANGE MANUALLY
        celltype=0,
        lmbda_set=1,
        Kse = kse_value[i],
        #GNaL_rate=1.80,
        #Gto_rate=0.40,
        #GK1_rate=0.68,
        #Gncx_rate=1.750,
        #Jleak_rate=1.30,
        #Jserca_rate=0.5,
        #CaMKa_rate=1.50,
        #Pnak_rate=0.70,
        #Pnab_rate=1,
        #Pcab_rate=1,
        #thl_rate=1.80,
        #Jrel_inf_sensitivity=0.80,
        #Jrel_infp_sensitivity=0.80,
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
for i in range(len(kse_value)):
    V_t = Vs[i]
    Ta_t = Tas[i]
    L_t = Ls[i]
    fig.suptitle(f'Sensitivity of Kse (Control)')

    ax[0].plot(tsteps, V_t, label=f"Kse:{kse_value[i]}")
    ax[0].grid(linewidth=0.3)
    ax[0].set_title("Voltage")
    ax[1].plot(tsteps, L_t, label=f"Kse:{kse_value[i]}")
    ax[1].grid(linewidth=0.3)
    ax[1].set_title("Lambda")
    ax[2].plot(tsteps, Ta_t, label=f"Kse:{kse_value[i]}")
    ax[2].grid(linewidth=0.3)
    ax[2].set_title("Ta")
   
plt.legend()
plt.show()

