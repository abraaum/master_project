"""
Funcitons for plotting/summarizing results from mechanical sensitivity analysis. 
Just isometric results for now.

TODO:
1. Add dynamic run
2. Fix repeating code
3. Finish full plot + save
4. Make full plot interactive (?)
"""

import ORdmm_Land_em_coupling as model
from scipy.integrate import odeint
import numpy as np
import os
import matplotlib.pyplot as plt
import tqdm
import pandas as pd


inc = np.arange(0.8, 1.201, 0.05).round(decimals=2)  # real run 0.01
num_beats = 100  # real run 100-1000
tsteps = np.arange(0.0, 1000.0, 0.1)  # real run 1000
lamval = [0.9, 0.95, 1, 1.05, 1.1]  
lamfile = ["090", "095", "100", "105", "110"] #


def isometric_sensitivity_max(V, Cai, Ta, CaTrpn, time_2_max=False):
    """Find peak value/time 2 peak for different states from isometric sensitivity analysis.
    """
    maxVs, maxCais, maxTas, maxCatrpns = [], [], [], []
    for l in range(len(lamval)):
        for i in range(len(inc)):

            if time_2_max == False:
                max_V = max(V[l][i])
                max_Cai = max(Cai[l][i])
                max_Ta = max(Ta[l][i])
                max_CaTrpn = max(CaTrpn[l][i])

            else:
                # calculate time 2 peak
                max_V = np.argmax(V[l][i]) / 10
                max_Cai = np.argmax(Cai[l][i]) / 10
                max_Ta = np.argmax(Ta[l][i]) / 10
                max_CaTrpn = np.argmax(CaTrpn[l][i]) / 10

            maxVs.append(max_V)
            maxCais.append(max_Cai)
            maxTas.append(max_Ta)
            maxCatrpns.append(max_CaTrpn)

    return maxVs, maxCais, maxTas, maxCatrpns


def isometric_sensitivity_df(V, Cai, Ta, CaTrpn, param, latex_table=False):
    """Make summarizing table of isometric sensitivivity analysis.
    """
    V_max, Cai_max, Ta_max, CaTrpn_max = isometric_sensitivity_max(
        V=V, Cai=Cai, Ta=Ta, CaTrpn=CaTrpn, time_2_max=False
    )
    V_max_t, Cai_max_t, Ta_max_t, CaTrpn_max_t = isometric_sensitivity_max(
        V=V, Cai=Cai, Ta=Ta, CaTrpn=CaTrpn, time_2_max=True
    )

    data = {
        "max V": V_max,
        "T2P V": V_max_t,
        "max Ca_i": Cai_max,
        "T2P Ca_i": Cai_max_t,
        "max Ta": Ta_max,
        "T2P Ta": Ta_max_t,
        "max CaTrpn": CaTrpn_max,
        "T2P CaTrpn": CaTrpn_max_t,
    }

    index_names = []
    for l in range(len(lamval)):
        for i in range(len(inc)):
            n = f"L: {lamval[l]}, % {param}: {inc[i]}"  # CHANGE MANUALLY
            index_names.append(n)

    df = pd.DataFrame(data=data, index=index_names)

    if latex_table == True:
        df = df.to_latex()

    return df


def load_sensitivity_values(filename):
    """Load .npy file from sens/ folder.
    """
    path = os.path.join("sens", filename)
    all_values = np.load(path, allow_pickle=True)

    L = all_values.item().get("L")
    N = all_values.item().get("num_beats")

    if L != [0.9, 0.95, 1.0, 1.05, 1.1]: #
        #raise ValueError(
        #    f"This is a test run, the lambda values ({L}) should be equal to [0.9, 0.95, 1.0, 1.05, 1.1] for iso"
        #)
        pass
    if N != 100:
        raise ValueError(
            f"This is a test run, the # of beats ({N}) should be equal to 100"
        )

    V = all_values.item().get("V")
    Cai = all_values.item().get("Cai")
    Ta = all_values.item().get("Ta")
    CaTrpn = all_values.item().get("CaTrpn")

    return V, Cai, Ta, CaTrpn



def plot_isometric_sensitivity(V, Cai, Ta, CaTrpn, hf_type, param, save_fig=False):
    """Plot results from isometric sensitivity analysis. 
    """
    Vs, Cais, Tas, CaTrpns = isometric_sensitivity_max(
        V=V, Cai=Cai, Ta=Ta, CaTrpn=CaTrpn, time_2_max=False
    )
    Vs_t, Cais_t, Tas_t, CaTrpns_t = isometric_sensitivity_max(
        V=V, Cai=Cai, Ta=Ta, CaTrpn=CaTrpn, time_2_max=True
    )
    fig, ax = plt.subplots(2, 2, sharex=True, figsize=(12,8))
    l = 0
    for i in range(0, len(Vs), len(inc)):
        V = Vs[i : i + len(inc)]
        Cai = Cais[i : i + len(inc)]
        Ta = Tas[i : i + len(inc)]
        CaTrpn = CaTrpns[i : i + len(inc)]

        fig.suptitle(f'Sensitivity analysis on {param} ({hf_type})')
        ax[0][0].plot(inc, V, label=f"λ: {lamval[l]}")
        ax[0][0].set_title("Voltage")
        ax[0][0].set_ylabel(f"max")
        ax[0][0].set_xlabel(f"% {param}")
        ax[0][0].grid(linewidth=0.3)

        ax[0][1].plot(inc, Cai)
        ax[0][1].set_title("Cai")
        ax[0][1].set_ylabel(f"max")
        ax[0][1].set_xlabel(f"% {param}")
        ax[0][1].grid(linewidth=0.3)

        ax[1][0].plot(inc, Ta)
        ax[1][0].set_title("Ta")
        ax[1][0].set_ylabel(f"max")
        ax[1][0].set_xlabel(f"% {param}")
        ax[1][0].grid(linewidth=0.3)

        ax[1][1].plot(inc, CaTrpn)
        ax[1][1].set_title("CaTrpn")
        ax[1][1].set_ylabel(f"max")
        ax[1][1].set_xlabel(f"% {param}")
        ax[1][1].grid(linewidth=0.3)        

        l += 1

    fig.legend(loc=7, ncol=1)

    if save_fig==True:
        plt.savefig(f'plots/iso_mech_sens_{hf_type}_endo_{param}_max.png')
    else:
        plt.show()


    fig, ax = plt.subplots(2, 2, sharex=True, figsize=(12,8))
    l = 0
    for i in range(0, len(Vs), len(inc)):
        V_t = Vs_t[i : i + len(inc)]
        Cai_t = Cais_t[i : i + len(inc)]
        Ta_t = Tas_t[i : i + len(inc)]
        CaTrpn_t = CaTrpns_t[i : i + len(inc)]

        fig.suptitle(f'Sensitivity analysis on {param} ({hf_type})')
        ax[0][0].plot(inc, V_t, label=f"λ: {lamval[l]}")
        ax[0][0].set_title("Voltage")
        ax[0][0].set_ylabel(f"T2P (ms)")
        ax[0][0].set_xlabel(f"% {param}")
        ax[0][0].grid(linewidth=0.3)

        ax[0][1].plot(inc, Cai_t)
        ax[0][1].set_title("Cai")
        ax[0][1].set_ylabel(f"T2P (ms)")
        ax[0][1].set_xlabel(f"% {param}")
        ax[0][1].grid(linewidth=0.3)

        ax[1][0].plot(inc, Ta_t)
        ax[1][0].set_title("Ta")
        ax[1][0].set_ylabel(f"T2P (ms)")
        ax[1][0].set_xlabel(f"% {param}")
        ax[1][0].grid(linewidth=0.3)

        ax[1][1].plot(inc, CaTrpn_t)
        ax[1][1].set_title("CaTrpn")
        ax[1][1].set_ylabel(f"T2P (ms)")
        ax[1][1].set_xlabel(f"% {param}")
        ax[1][1].grid(linewidth=0.3)   

        l += 1

    fig.legend(loc=7, ncol=1)
    
    if save_fig==True:
        plt.savefig(f'plots/iso_mech_sens_{hf_type}_endo_{param}_t2p.png')
    else:
        plt.show()

        

def plot_isometric_full(param, hf_type, mech_type):
    Vs, Cais, Tas, CaTrpns = load_sensitivity_values(f'sens_{mech_type}_{hf_type}_endo_{param}.npy')
    fig, ax = plt.subplots(2, 2, sharex=True, figsize=(14,8))
    col_list = ['b', 'g', 'm', 'c', 'r'] 
    lamval = [0.9, 0.95, 1, 1.05, 1.1] 

    if mech_type=='dyn':
        col_list = ['b', 'g', 'm'] 
        lamval = [1, 1.05, 1.1]
     

    for l in range(len(lamval)):
        for i in range(len(inc)):
            V = Vs[l][i]
            Cai = Cais[l][i]
            Ta = Tas[l][i]
            CaTrpn = CaTrpns[l][i]

            fig.suptitle(f'Sensitivity analysis on {param} ({hf_type})')
            ax[0][0].plot(tsteps, V, linewidth=0.7 if inc[i]==1 else 0.3, color=col_list[l], label=f"λ: {lamval[l]}" if inc[i]==1 else None)
            ax[0][0].set_title("Voltage")
            ax[0][0].set_ylabel("Voltage (mV)")
            ax[0][0].set_xlabel("Time (ms)")
            ax[0][0].grid(linewidth=0.3)

            ax[0][1].plot(tsteps, Cai, linewidth=0.7 if inc[i]==1 else 0.3, color=col_list[l])
            ax[0][1].set_title("Cai")
            ax[0][1].set_ylabel("Ca_i (mM)")
            ax[0][1].set_xlabel("Time (ms)")
            ax[0][1].grid(linewidth=0.3)

            ax[1][0].plot(tsteps, Ta, linewidth=0.7 if inc[i]==1 else 0.3, color=col_list[l])
            ax[1][0].set_title("Ta")
            ax[1][0].set_ylabel("Ta ()")
            ax[1][0].set_xlabel("Time (ms)")
            ax[1][0].grid(linewidth=0.3)

            ax[1][1].plot(tsteps, CaTrpn, linewidth=0.7 if inc[i]==1 else 0.3, color=col_list[l])
            ax[1][1].set_title("CaTrpn")
            ax[1][1].set_ylabel("CaTrpn ()")
            ax[1][1].set_xlabel("Time (ms)")
            ax[1][1].grid(linewidth=0.3)        


    fig.legend(loc=7, ncol=1)
    plt.show()



if __name__ == "__main__":
    """
    type_hf = ['control', 'gomez'] #, 
    params = ['rs', 'rw', 'Tref', 'cat50ref', 'ntm'] #'ku', 'kuw', 'kws', 'ktrpn', 'Trpn50', 'gammaw', 'gammas'

    for i in range(len(type_hf)):
        for j in range(len(params)):
            V, Cai, Ta, CaTrpn = load_sensitivity_values(f'sens_iso_{type_hf[i]}_endo_{params[j]}.npy')
            plot_isometric_sensitivity(V=V, Cai=Cai, Ta=Ta, CaTrpn=CaTrpn, hf_type=type_hf[i], param=params[j], save_fig=True)
    
    """
    type_hf = ['control'] #, 'control', 
    params = ['cat50ref'] # , 'kuw', 'kws', 'ktrpn', 'Trpn50', 'gammaw', 'gammas', 'rs', 'rw', 'Tref', 'cat50ref', 'ntm'
    for i in range(len(type_hf)):
        for j in range(len(params)):
            plot_isometric_full(param=params[j], hf_type=type_hf[i], mech_type='iso')