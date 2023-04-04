import ORdmm_Land_em_coupling as model
from scipy.integrate import odeint
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
import tqdm
import pandas as pd
from matplotlib.lines import Line2D

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



def plot_pop_accepted(hf_type='control', mech_type='iso', out=None):
    """Plot difference in accepted and rejected cells in population."""
    # load random sampling values
    rand_val = np.load(f'init_pop/rand_sample_iso_control.npy') 
    # load population
    all_values = np.load(f'init_pop/pop_res_{mech_type}_{hf_type}.npy', allow_pickle=True) 
    # find difference of populations
    removed_rand_index = np.load(f'init_pop/population_iso_control_remove.npy', allow_pickle=True) 

    V = all_values.item().get("V")
    Cai = all_values.item().get("Cai")
    Ta = all_values.item().get("Ta")

    if mech_type=='iso':
        CaTrpn = all_values.item().get("CaTrpn")
    else:
        Lambda = all_values.item().get("Lambda")

    fig, ax = plt.subplots(2, 2, sharex=True, figsize=(14,8))


    for i in range(pop_size):

        if i in removed_rand_index:
            alpha = 0.3 #0.5
            col = 'lightskyblue' if hf_type=='control' else 'lightcoral'
            z = 1
        else:
            alpha = 1
            col = 'tab:blue' if hf_type=='control' else 'tab:red'
            z = 2
        
        ax[0][0].plot(tsteps[::50], V[i], linewidth=0.7, alpha=alpha, color=col, zorder=z)
        ax[0][1].plot(tsteps[::50], Cai[i], linewidth=0.7, alpha=alpha, color=col, zorder=z)
        ax[1][0].plot(tsteps[::50], Ta[i], linewidth=0.7, alpha=alpha, color=col, zorder=z)
        ax[1][1].plot(tsteps[::50], CaTrpn[i] if mech_type=='iso' else Lambda[i], linewidth=0.7, alpha=alpha, color=col, zorder=z)
        
    ax[0][0].set_title("Voltage")
    ax[0][0].set_ylabel("Voltage (mV)")
    ax[0][0].set_xlabel("Time (ms)")
    ax[0][0].grid(linewidth=0.3)

    ax[0][1].set_title("Cai")
    ax[0][1].set_ylabel("Ca_i (mM)")
    ax[0][1].set_xlabel("Time (ms)")
    ax[0][1].grid(linewidth=0.3)

    ax[1][0].set_title("Ta")
    ax[1][0].set_ylabel("Ta (kPa)")
    ax[1][0].set_xlabel("Time (ms)")
    ax[1][0].grid(linewidth=0.3)

    ax[1][1].set_title("CaTrpn" if mech_type=='iso' else "Lambda")
    ax[1][1].set_ylabel("CaTrpn" if mech_type=='iso' else "Lambda")
    ax[1][1].set_xlabel("Time (ms)")
    ax[1][1].grid(linewidth=0.3)

    if hf_type=='control':
        custom_lines = [Line2D([0], [0], color='lightskyblue', ls='-'),
                        Line2D([0], [0], color='tab:blue', ls='-')]
    else:
        custom_lines = [Line2D([0], [0], color='lightcoral', ls='-'),
                        Line2D([0], [0], color='tab:red', ls='-')]
    
    plt.figlegend(custom_lines, ['rejected', 'accepted'], loc=7)
    fig.suptitle(f'Population of models ({mech_type}, {hf_type})', fontsize='x-large')

    if out != None:
        plt.savefig(f'plots/pop_acc_{hf_type}_{mech_type}.png')
        plt.show()
    else:
        plt.show()


def plot_pop_diff_HF_C(mech_type='iso', drug_type=None, out=None):

    if drug_type==None:
        control_values = np.load(f'init_pop/pop_res_{mech_type}_control.npy', allow_pickle=True) 
        hf_values = np.load(f'init_pop/pop_res_{mech_type}_gomez.npy', allow_pickle=True) 
    else:
        control_values = np.load(f'drug/drug_res_{drug_type}_{mech_type}_control.npy', allow_pickle=True) 
        hf_values = np.load(f'drug/drug_res_{drug_type}_{mech_type}_gomez.npy', allow_pickle=True) 
    
    V_hf = hf_values.item().get("V")
    Cai_hf = hf_values.item().get("Cai")
    Ta_hf = hf_values.item().get("Ta")

    V_control = control_values.item().get("V")
    Cai_control = control_values.item().get("Cai")
    Ta_control = control_values.item().get("Ta")

    if mech_type=='iso':
        CaTrpn_hf = hf_values.item().get("CaTrpn")
        CaTrpn_control = control_values.item().get("CaTrpn")
    else:
        Lambda_hf = hf_values.item().get("Lambda")
        Lambda_control = control_values.item().get("Lambda")

    fig, ax = plt.subplots(2, 2, sharex=True, figsize=(14,8))

    for i in range(pop_size): # pop_size
        ax[0][0].plot(tsteps[::50], V_control[i], linewidth=0.5, alpha=0.1, color='tab:blue', zorder=1)
        ax[0][1].plot(tsteps[::50], Cai_control[i], linewidth=0.5, alpha=0.1, color='tab:blue', zorder=1)
        ax[1][0].plot(tsteps[::50], Ta_control[i], linewidth=0.5, alpha=0.1, color='tab:blue', zorder=1)
        ax[1][1].plot(tsteps[::50], CaTrpn_control[i] if mech_type=='iso' else Lambda_control[i], linewidth=0.5, alpha=0.1, color='tab:blue', zorder=1)

    for i in range(pop_size): # pop_size
        ax[0][0].plot(tsteps[::50], V_hf[i], linewidth=0.5, alpha=0.1, color='tab:red', zorder=1)
        ax[0][1].plot(tsteps[::50], Cai_hf[i], linewidth=0.5, alpha=0.1, color='tab:red', zorder=1)
        ax[1][0].plot(tsteps[::50], Ta_hf[i], linewidth=0.5, alpha=0.1, color='tab:red', zorder=1)
        ax[1][1].plot(tsteps[::50], CaTrpn_hf[i] if mech_type=='iso' else Lambda_hf[i], linewidth=0.5, alpha=0.1, color='tab:red', zorder=1)
    

    ax[0][0].plot(tsteps[::50], np.mean(V_control, axis=0), linewidth=1, alpha=1, color='b', zorder=2)
    ax[0][0].plot(tsteps[::50], np.mean(V_hf, axis=0), linewidth=1, alpha=1, color='r', zorder=2)
    ax[0][0].set_title("Voltage")
    ax[0][0].set_ylabel("Voltage (mV)")
    ax[0][0].set_xlabel("Time (ms)")
    ax[0][0].grid(linewidth=0.3)

    ax[0][1].plot(tsteps[::50], np.mean(Cai_control, axis=0), linewidth=1, alpha=1, color='b', zorder=2)
    ax[0][1].plot(tsteps[::50], np.mean(Cai_hf, axis=0), linewidth=1, alpha=1, color='r', zorder=2)
    ax[0][1].set_title("Cai")
    ax[0][1].set_ylabel("Ca_i (mM)")
    ax[0][1].set_xlabel("Time (ms)")
    ax[0][1].grid(linewidth=0.3)

    ax[1][0].plot(tsteps[::50], np.mean(Ta_control, axis=0), linewidth=1, alpha=1, color='b', zorder=2)
    ax[1][0].plot(tsteps[::50], np.mean(Ta_hf, axis=0), linewidth=1, alpha=1, color='r', zorder=2)
    ax[1][0].set_title("Ta")
    ax[1][0].set_ylabel("Ta (kPa)")
    ax[1][0].set_xlabel("Time (ms)")
    ax[1][0].grid(linewidth=0.3)

    ax[1][1].plot(tsteps[::50], np.mean(CaTrpn_control, axis=0) if mech_type=='iso' else np.mean(Lambda_control, axis=0), linewidth=1, alpha=1, color='b', zorder=2)
    ax[1][1].plot(tsteps[::50], np.mean(CaTrpn_hf, axis=0) if mech_type=='iso' else np.mean(Lambda_hf, axis=0), linewidth=1, alpha=1, color='r', zorder=2)
    ax[1][1].set_title("CaTrpn" if mech_type=='iso' else "Lambda")
    ax[1][1].set_ylabel("CaTrpn" if mech_type=='iso' else "Lambda")
    ax[1][1].set_xlabel("Time (ms)")
    ax[1][1].grid(linewidth=0.3)

    custom_lines = [Line2D([0], [0], color='tab:blue', ls='-'),
                    Line2D([0], [0], color='tab:red', ls='-')]

    plt.figlegend(custom_lines, ['control', 'HF'], loc=7)
    if drug_type==None:
        fig.suptitle(f'Population of {mech_type} models', fontsize='x-large')
    else:
        fig.suptitle(f'Population of {mech_type} models ({drug_type})', fontsize='x-large')

    if out != None:
        if drug_type==None:
            plt.savefig(f'plots/pop_diff_hf_c_{mech_type}.png')
        else:
            plt.savefig(f'plots/drug_trial/pop_diff_hf_c_{mech_type}_{drug_type}.png')
    else:
        plt.show()




if __name__ == "__main__":

    #plot_population_dist(hf_type='control', mech_type='iso',out=True)

    #plot_pop_accepted(hf_type='control', mech_type='iso', out=True)
    #plot_pop_accepted(hf_type='control', mech_type='dyn', out=True)
    #plot_pop_accepted(hf_type='gomez', mech_type='dyn', out=True)
    #plot_pop_accepted(hf_type='gomez', mech_type='iso', out=True)

    plot_pop_diff_HF_C(mech_type='iso', out=True)
    plot_pop_diff_HF_C(mech_type='dyn', out=True)




