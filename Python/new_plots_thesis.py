import ORdmm_Land_em_coupling as model
from scipy.integrate import odeint
import numpy as np
import os
import matplotlib.pyplot as plt
import tqdm
import pandas as pd
import sys


tsteps = np.arange(0.0, 1000.0, 0.1)  # real run 1000
pop_size = 1000
num_beats = 1

def hf_vs_control_plot():
    hf_types = ['control', 'gomez']

    fig, axs = plt.subplots(1, 2, figsize=(14,6))

    for hf_type in hf_types:
        y0 = np.load(
            f"init_values/coupled/{hf_type}_endo_coupled_iso_100.npy"
        )
        parameters = model.init_parameter_values(
            celltype=0,
            isometric=1,
            lmbda_set=1,
            #mechanical parameters
            cat50ref_rate=0.7 if hf_type=='gomez' else 1,
            #HF parameters
            GNaL_rate=1.80 if hf_type=='gomez' else 1,
            Gto_rate=0.40 if hf_type=='gomez' else 1,
            GK1_rate=0.68 if hf_type=='gomez' else 1,
            Gncx_rate=1.750 if hf_type=='gomez' else 1,
            Jleak_rate=1.30 if hf_type=='gomez' else 1,
            Jserca_rate=0.5 if hf_type=='gomez' else 1,
            CaMKa_rate=1.50 if hf_type=='gomez' else 1,
            Pnak_rate=0.70 if hf_type=='gomez' else 1,
            Pnab_rate=1,
            Pcab_rate=1,
            thl_rate=1.80 if hf_type=='gomez' else 1,
            Jrel_inf_sensitivity=0.80 if hf_type=='gomez' else 1,
            Jrel_infp_sensitivity=0.80 if hf_type=='gomez' else 1,
        )


        for n in tqdm.tqdm(range(num_beats)):
            y = odeint(model.rhs, y0, tsteps, args=(parameters,))
            y0 = y[-1]

        if hf_type=='control':
            c = 'tab:blue'
        else:
            c = 'tab:red'

        V = y.T[model.state_indices('v')]
        Cai = y.T[model.state_indices('cai')]

        axs[0].plot(tsteps[:5000], V[:5000], color=c)
        axs[1].plot(tsteps, Cai, color=c)
    
    axs[0].set_title("Voltage")
    axs[0].set_ylabel("Voltage (mV)")
    axs[0].set_xlabel("Time (ms)")
    axs[1].set_title(f"Calcium transient")
    axs[1].set_ylabel(f"$Ca_i$ (mM)")
    axs[1].set_xlabel("Time (ms)")

    axs[0].legend((r"Control", r"HF"))
    axs[1].legend((r"Control", r"HF"))
    plt.show()
        
if __name__ == "__main__":
    hf_vs_control_plot()
        






