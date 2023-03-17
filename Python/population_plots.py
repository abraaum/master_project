import ORdmm_Land_em_coupling as model
from scipy.integrate import odeint
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
import tqdm
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

num_beats = 100
tsteps = np.arange(0.0, 1000.0, 0.1)  # real run 1000
pop_size = 1000

def plot_population_dist(hf_type='control', mech_type='iso', out=None):
    """Plot differennce between distributions of original and refined population parameters"""

    initial_pop = np.load(f'init_pop/rand_sample_iso_control.npy')
    clean_pop = np.load(f'init_pop/rand_sample_{mech_type}_{hf_type}_clean.npy')

    fig, axis = plt.subplots(3,4, figsize=(16,8), sharey=True, sharex=True)
    fig.suptitle('Distribution of parameter scaling for population model (iso control)')

    mech_names = ['Ku', 'Kuw', 'Kws', 'ktrpn', 'Trpn50', 'gammaw', 'gammas', 'rs', 'rw', 'Tref', 'Cat50ref', 'ntm']

    m = 0
    for i in range(len(axis)):
        for j in range(len(axis[0])):
            axis[i][j].set_title(mech_names[m])
            sns.distplot(ax=axis[i, j], x =initial_pop[:,m], kde=True, color='tab:blue')
            sns.distplot(ax=axis[i, j], x =clean_pop[:,m], kde=True, color='tab:orange')
            m += 1

    plt.figlegend(title='Population', labels=['original', 'refined'], loc=7)
    
    if out != None:
        plt.savefig(f'plots/pop_dist_{hf_type}_{mech_type}.png')
    else:
        plt.show()


def plot_population_diff(hf_type='control', cell_type='endo', mech_type='iso', out=None):
    """Plot difference in accepted and rejected cells in population."""
    # load random sampling values
    rand_val = np.load(f'init_pop/rand_sample_iso_control.npy') 
    # load population
    y0s = np.load(f'init_pop/population_{mech_type}_{hf_type}.npy') 
    # find difference of populations
    removed_rand_index = np.load(f'init_pop/population_{mech_type}_{hf_type}_remove.npy', allow_pickle=True) 

    fig, ax = plt.subplots(2, 2, sharex=True, figsize=(14,8))

    for i in range(pop_size):
        y0 = y0s[i]

        parameters = model.init_parameter_values(
            celltype=0 if cell_type == "endo" else 1 if cell_type == "epi" else 2,
            isometric=1 if mech_type=='iso' else 0,
            lmbda_set=1,
            #mechanical parameters
            ku_rate=rand_val[i][0],
            kuw_rate=rand_val[i][1],
            kws_rate=rand_val[i][2],
            ktrpn_rate=rand_val[i][3],
            Trpn50_rate=rand_val[i][4],
            gammaw_rate=rand_val[i][5],
            gammas_rate=rand_val[i][6],
            rs_rate=rand_val[i][7],
            rw_rate=rand_val[i][8],
            Tref_rate=rand_val[i][9],
            cat50ref_rate=rand_val[i][10],
            ntm_rate=rand_val[i][11],
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

        y = odeint(model.rhs, y0, tsteps, args=(parameters,))
        monitor = np.array(
                [model.monitor(r, t, parameters) for r, t in zip(y, tsteps)]
            )
        
        V = y.T[model.state_indices("v")]
        Cai = y.T[model.state_indices("cai")]
        Ta = monitor.T[model.monitor_indices("Ta")]
        CaTrpn = y.T[model.state_indices("CaTrpn")]

        if i in removed_rand_index:
            alpha = 0.5
            col = 'lightskyblue'
            z = 1
        else:
            alpha = 1
            col = 'blue'
            z = 2
        
        ax[0][0].plot(tsteps, V, linewidth=0.7, alpha=alpha, color=col, zorder=z)
        ax[0][0].set_title("Voltage")
        ax[0][0].set_ylabel("Voltage (mV)")
        ax[0][0].set_xlabel("Time (ms)")
        ax[0][0].grid(linewidth=0.3)

        ax[0][1].plot(tsteps, Cai, linewidth=0.7, alpha=alpha, color=col, zorder=z)
        ax[0][1].set_title("Cai")
        ax[0][1].set_ylabel("Ca_i (mM)")
        ax[0][1].set_xlabel("Time (ms)")
        ax[0][1].grid(linewidth=0.3)

        ax[1][0].plot(tsteps, Ta, linewidth=0.7, alpha=alpha, color=col, zorder=z)
        ax[1][0].set_title("Ta")
        ax[1][0].set_ylabel("Ta (kPa)")
        ax[1][0].set_xlabel("Time (ms)")
        ax[1][0].grid(linewidth=0.3)

        ax[1][1].plot(tsteps, CaTrpn, linewidth=0.7, alpha=alpha, color=col, zorder=z)
        ax[1][1].set_title("CaTrpn")
        ax[1][1].set_ylabel("CaTrpn (?)")
        ax[1][1].set_xlabel("Time (ms)")
        ax[1][1].grid(linewidth=0.3)

    leg = plt.figlegend(title='Population', labels=['rejected', 'accepted'], loc=7)
    leg.legendHandles[0].set_color('lightskyblue')
    leg.legendHandles[1].set_color('blue')


    if out != None:
        plt.savefig(f'plots/pop_diff_{hf_type}_{mech_type}.png')
        plt.show()
    else:
        plt.show()



if __name__ == "__main__":

    #plot_population_dist(hf_type='control', mech_type='iso',out=None)
    plot_population_diff(hf_type='control', cell_type='endo', mech_type='iso', out=True)




