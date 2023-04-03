from multiprocessing import Process
import time

import ORdmm_Land_em_coupling as model
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import itertools

from drug_values import drug_dict

tsteps = np.arange(0.0, 1000.0, 0.1)  # real run 1000
pop_size = 1000

tsteps_new = np.arange(0.0, 1000.0, 1)

def save_pop_drug(mech_type, hf_type, drug_type, cell_type='endo'):
    """Run the population model with different drugs.
    """
    # load random sampling values
    rand_val = np.load(f'init_pop/rand_sample_iso_control.npy')
    # load specific population
    y0s = np.load(f'init_pop_drug/population_{mech_type}_{hf_type}_{drug_type}.npy') 
    
    Vs, Cais, Tas, CaTrpns = [], [], [], []

    if mech_type == 'dyn':
        Lambdas = []

    for i in range(pop_size):
        print(i)
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
            cat50ref_rate=(rand_val[i][10])*0.7 if hf_type=='gomez' else rand_val[i][10],
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
            # drug parameters
            drug_INa=drug_dict[drug_type]['drug_INa'],
            IC50_INa=drug_dict[drug_type]['IC50_INa'],
            h_INa=drug_dict[drug_type]['h_INa'],
            drug_IKr=drug_dict[drug_type]['drug_IKr'],
            IC50_IKr=drug_dict[drug_type]['IC50_IKr'],
            h_IKr=drug_dict[drug_type]['h_IKr'],
            drug_ICaL=drug_dict[drug_type]['drug_ICaL'],
            IC50_ICaL=drug_dict[drug_type]['IC50_ICaL'],
            h_ICaL=drug_dict[drug_type]['h_ICaL'],
            drug_INaL=drug_dict[drug_type]['drug_INaL'],
            IC50_INaL=drug_dict[drug_type]['IC50_INaL'],
            h_INaL=drug_dict[drug_type]['h_INaL'],
            drug_IKs=drug_dict[drug_type]['drug_IKs'],
            IC50_IKs=drug_dict[drug_type]['IC50_IKs'],
            h_IKs=drug_dict[drug_type]['h_IKs'],
            drug_Ito=drug_dict[drug_type]['drug_Ito'],
            IC50_Ito=drug_dict[drug_type]['IC50_Ito'],
            h_Ito=drug_dict[drug_type]['h_Ito'],
            drug_IK1=drug_dict[drug_type]['drug_IK1'],
            IC50_IK1=drug_dict[drug_type]['IC50_IK1'],
            h_IK1=drug_dict[drug_type]['h_IK1'],
        )

        y = odeint(model.rhs, y0, tsteps, args=(parameters,))

        monitor = np.array([model.monitor(r, t, parameters) for r, t in zip(y, tsteps)])
        V = y.T[model.state_indices("v")]
        Cai = y.T[model.state_indices("cai")]
        Ta = monitor.T[model.monitor_indices("Ta")]
        CaTrpn = y.T[model.state_indices("CaTrpn")]

        Vs.append(V[::50])
        Cais.append(Cai[::50])
        Tas.append(Ta[::50])
        CaTrpns.append(CaTrpn[::50])

        if mech_type =='dyn':
            Lambda = y.T[model.state_indices("lmbda")]
            Lambdas.append(Lambda[::50])
    
    d = {
        'V': Vs,
        'Cai': Cais,
        'Ta':Tas,
        'CaTrpn': CaTrpns
        }
    
    if mech_type =='dyn':
        d = {
        'V': Vs,
        'Cai': Cais,
        'Ta':Tas,
        'Lambda': Lambdas
        }
    
    np.save(f'drug/drug_res_{drug_type}_{mech_type}_{hf_type}.npy', d, allow_pickle=True)


def test_plot_drug():
    all_values = np.load('tester_save_50th.npy', allow_pickle=True)

    V = all_values.item().get("V")
    Cai = all_values.item().get("Cai")
    Ta = all_values.item().get("Ta")
    CaTrpn = all_values.item().get("CaTrpn")

    fig, ax = plt.subplots(2, 2, sharex=True, figsize=(14,8))

    for i in range(10): # pop_size
        ax[0][0].plot(tsteps[::50], V[i], linewidth=0.7, alpha=0.5, color='lightskyblue')
        ax[0][1].plot(tsteps[::50], Cai[i], linewidth=0.7, alpha=0.5, color='lightskyblue')
        ax[1][0].plot(tsteps[::50], Ta[i], linewidth=0.7, alpha=0.5, color='lightskyblue')
        ax[1][1].plot(tsteps[::50], CaTrpn[i], linewidth=0.7, alpha=0.5, color='lightskyblue')
    
    ax[0][0].plot(tsteps[::50], np.mean(V, axis=0), linewidth=1, alpha=1, color='tab:blue')
    ax[0][0].set_title("Voltage")
    ax[0][0].set_ylabel("Voltage (mV)")
    ax[0][0].set_xlabel("Time (ms)")
    ax[0][0].grid(linewidth=0.3)

    ax[0][1].plot(tsteps[::50], np.mean(Cai, axis=0), linewidth=1, alpha=1, color='tab:blue')
    ax[0][1].set_title("Cai")
    ax[0][1].set_ylabel("Ca_i (mM)")
    ax[0][1].set_xlabel("Time (ms)")
    ax[0][1].grid(linewidth=0.3)

    ax[1][0].plot(tsteps[::50], np.mean(Ta, axis=0), linewidth=1, alpha=1, color='tab:blue')
    ax[1][0].set_title("Ta")
    ax[1][0].set_ylabel("Ta (kPa)")
    ax[1][0].set_xlabel("Time (ms)")
    ax[1][0].grid(linewidth=0.3)

    ax[1][1].plot(tsteps[::50], np.mean(CaTrpn, axis=0), linewidth=1, alpha=1, color='tab:blue')
    ax[1][1].set_title("CaTrpn")
    ax[1][1].set_ylabel("CaTrpn")
    ax[1][1].set_xlabel("Time (ms)")
    ax[1][1].grid(linewidth=0.3)

    leg = plt.figlegend(labels=['population', 'mean'], loc=7)
    leg.legendHandles[0].set_color('lightskyblue')
    leg.legendHandles[1].set_color('tab:blue')

    plt.show()



if __name__ == '__main__':
    mech = ['iso', 'dyn']
    hf = ['control', 'gomez']
    drug = sys.argv[1]
    proc = []
    for m in mech:
        for h in hf:
            p = Process(target=save_pop_drug, args=(m, h, drug))
            p.start()
            proc.append(p)
    for p in proc:
        p.join()

    #test_plot_drug()