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

num_beats = 70  # real run 100-1000
tsteps = np.arange(0.0, 1000.0, 0.1)  # real run 1000

kse_value = [0.0, 5, 10, 20] # kse  0.5, 1.0, 1.5,

lambdafile = ['100', '105', '110']
lambdas  =[1, 1.05, 1.10]

Tas = [[], [], []]
Cais = [[], [], []]
CaTrpns = [[], [], []]
Ls = [[], [], []]

for l in range(len(lambdafile)):
    for i in range(len(kse_value)):
        y0 = np.load(
                    f"init_values/coupled/control_endo_coupled_dyn_{lambdafile[l]}.npy"
                )
        
        parameters = model.init_parameter_values(
            # CHANGE MANUALLY
            celltype=0,
            lmbda_set=lambdas[l],
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
        CaTrpn = y.T[model.state_indices('CaTrpn')]
        Cai = y.T[model.state_indices('cai')]
        L = y.T[model.state_indices('lmbda')]
        monitor = np.array([model.monitor(r, t, parameters) for r, t in zip(y, tsteps)])
        Ta = monitor.T[model.monitor_indices('Ta')]

        
        CaTrpns[l].append(list(CaTrpn))
        Cais[l].append(list(Cai))
        Tas[l].append(list(Ta))
        Ls[l].append(list(L))




fig, ax = plt.subplots(2, 2, sharex=True, figsize=(14,8))
col_list = ['b', 'g', 'm']
widths = [1, 0.8, 0.6, 0.4]



for i in range(len(lambdafile)):
    for j in range(len(kse_value)):
        Cai_t = Cais[i][j]
        CaTrpn_t = CaTrpns[i][j]
        Ta_t = Tas[i][j]
        L_t = Ls[i][j]
        fig.suptitle(f'Sensitivity of Kse (Control)')

        ax[0][0].plot(
            tsteps, 
            Cai_t, 
            linewidth=widths[j], 
            color=col_list[i], 
            label=f"$\lambda$:{lambdas[i]}" if j==0 else None)
        ax[0][0].grid(linewidth=0.3)
        ax[0][0].set_title("Cai")
        ax[1][0].plot(
            tsteps, 
            L_t, 
            linewidth=widths[j], 
            color=col_list[i])
        ax[1][0].grid(linewidth=0.3)
        ax[1][0].set_title("Lambda")
        ax[1][1].plot(
            tsteps, 
            Ta_t, 
            linewidth=widths[j],  
            color=col_list[i])
        ax[1][1].grid(linewidth=0.3)
        ax[1][1].set_title("Ta")
        ax[0][1].plot(
            tsteps, 
            CaTrpn_t, 
            linewidth=widths[j],  
            color=col_list[i])
        ax[0][1].grid(linewidth=0.3)
        ax[0][1].set_title("CaTRPN")

fig.legend(loc=7, ncol=1)   
plt.show()

