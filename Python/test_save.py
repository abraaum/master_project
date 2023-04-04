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
from matplotlib.lines import Line2D

tsteps = np.arange(0.0, 1000.0, 0.1)  # real run 1000
pop_size = 1000


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


def save_pop_traces(mech_type, hf_type, cell_type='endo'):
    """Run the population model with different drugs.
    """
    # load random sampling values
    rand_val = np.load(f'init_pop/rand_sample_iso_control.npy')
    # load specific population
    y0s = np.load(f'init_pop/population_{mech_type}_{hf_type}.npy') 
    
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
    
    np.save(f'init_pop/pop_res_{mech_type}_{hf_type}.npy', d, allow_pickle=True)


def test_plot_drug(mech_type, hf_type, drug_type, out=None):
    all_values = np.load(f'drug/drug_res_{drug_type}_{mech_type}_{hf_type}.npy', allow_pickle=True)
    control_values = np.load(f'init_pop/res_{mech_type}_control.npy', allow_pickle=True)

    V = all_values.item().get("V")
    Cai = all_values.item().get("Cai")
    Ta = all_values.item().get("Ta")

    V_control = control_values.item().get("V")
    Cai_control = control_values.item().get("Cai")
    Ta_control = control_values.item().get("Ta")

    if mech_type=='iso':
        CaTrpn = all_values.item().get("CaTrpn")
        CaTrpn_control = control_values.item().get("CaTrpn")
    else:
        Lambda = all_values.item().get("Lambda")
        Lambda_control = control_values.item().get("Lambda")

    fig, ax = plt.subplots(2, 2, sharex=True, figsize=(14,8))

    for i in range(pop_size): # pop_size
        ax[0][0].plot(tsteps[::50], V[i], linewidth=0.5, alpha=0.5, color='lightskyblue', zorder=1)
        ax[0][1].plot(tsteps[::50], Cai[i], linewidth=0.5, alpha=0.5, color='lightskyblue', zorder=1)
        ax[1][0].plot(tsteps[::50], Ta[i], linewidth=0.5, alpha=0.5, color='lightskyblue', zorder=1)
        ax[1][1].plot(tsteps[::50], CaTrpn[i] if mech_type=='iso' else Lambda[i], linewidth=0.7, alpha=0.5, color='lightskyblue', zorder=1)
    
    ax[0][0].plot(tsteps[::50], np.mean(V, axis=0), linewidth=1, alpha=1, color='tab:blue', zorder=3)
    ax[0][0].plot(tsteps[::50], V_control, linewidth=1, alpha=1, color='k', ls='--', zorder=3)
    ax[0][0].set_title("Voltage")
    ax[0][0].set_ylabel("Voltage (mV)")
    ax[0][0].set_xlabel("Time (ms)")
    ax[0][0].grid(linewidth=0.3)

    ax[0][1].plot(tsteps[::50], np.mean(Cai, axis=0), linewidth=1, alpha=1, color='tab:blue', zorder=3)
    ax[0][1].plot(tsteps[::50], Cai_control, linewidth=1, alpha=1, color='k', ls='--', zorder=3)
    ax[0][1].set_title("Cai")
    ax[0][1].set_ylabel("Ca_i (mM)")
    ax[0][1].set_xlabel("Time (ms)")
    ax[0][1].grid(linewidth=0.3)

    ax[1][0].plot(tsteps[::50], np.mean(Ta, axis=0), linewidth=1, alpha=1, color='tab:blue', zorder=3)
    ax[1][0].plot(tsteps[::50], Ta_control, linewidth=1, alpha=1, color='k', ls='--', zorder=3)
    ax[1][0].set_title("Ta")
    ax[1][0].set_ylabel("Ta (kPa)")
    ax[1][0].set_xlabel("Time (ms)")
    ax[1][0].grid(linewidth=0.3)

    ax[1][1].plot(tsteps[::50], np.mean(CaTrpn, axis=0) if mech_type=='iso' else np.mean(Lambda, axis=0), linewidth=1, alpha=1, color='tab:blue', zorder=3)
    ax[1][1].plot(tsteps[::50], CaTrpn_control if mech_type=='iso' else Lambda_control, linewidth=1, alpha=1, color='k', ls='--', zorder=3)
    ax[1][1].set_title("CaTrpn" if mech_type=='iso' else "Lambda")
    ax[1][1].set_ylabel("CaTrpn" if mech_type=='iso' else "Lambda")
    ax[1][1].set_xlabel("Time (ms)")
    ax[1][1].grid(linewidth=0.3)


    ax[0][0].set_ylim(-92, 50)
    ax[0][1].set_ylim(0.00005, 0.00085)

    if mech_type=='iso':
        ax[1][0].set_ylim(-0.1, 70)
        ax[1][1].set_ylim(0, 0.4)
    else:
        ax[1][0].set_ylim(-0.1, 3.6)
        ax[1][1].set_ylim(0.7, 1.01)
    
    # plot sd filled line area
    ax[1][0].fill_between(
        tsteps[::50], 
        np.mean(Ta, axis=0)-np.std(Ta, axis=0), 
        np.mean(Ta, axis=0)+np.std(Ta, axis=0), 
        color='tab:blue', alpha=0.3, zorder=2)
    
    ax[0][1].fill_between(
        tsteps[::50], 
        np.mean(Cai, axis=0)-np.std(Cai, axis=0), 
        np.mean(Cai, axis=0)+np.std(Cai, axis=0), 
        color='tab:blue', alpha=0.3, zorder=2)
    
    ax[1][1].fill_between(
        tsteps[::50], 
        (np.mean(CaTrpn, axis=0)-np.std(CaTrpn, axis=0)) if mech_type=='iso' else (np.mean(Lambda, axis=0)-np.std(Lambda, axis=0)), 
        (np.mean(CaTrpn, axis=0)+np.std(CaTrpn, axis=0)) if mech_type=='iso' else (np.mean(Lambda, axis=0)+np.std(Lambda, axis=0)), 
        color='tab:blue', alpha=0.3, zorder=2)


    custom_lines = [Line2D([0], [0], color='lightskyblue', ls='-'),
                    Line2D([0], [0], color='tab:blue', ls='-'),
                    Line2D([0], [0], color='k',  ls='--')]

    plt.figlegend(custom_lines, ['population', 'mean', 'control'], loc=7)
    fig.suptitle(f'{drug_type.capitalize()} (population: {mech_type}, {hf_type})', fontsize='x-large')

    if out != None:
        plt.savefig(f'plots/drug_trial_control/drug_{mech_type}_{hf_type}_{drug_type}.png')
    else:
        plt.show()


def drug_control_save(mech_type, hf_type, cell_type='endo'):
    y0 = np.load(f"init_values/coupled/{hf_type}_{cell_type}_coupled_{mech_type}_100.npy")
    parameters = model.init_parameter_values(
            celltype=0 if cell_type == "endo" else 1 if cell_type == "epi" else 2,
            isometric=1 if mech_type=='iso' else 0,
            lmbda_set=1,
        )
    
    y = odeint(model.rhs, y0, tsteps, args=(parameters,))

    monitor = np.array([model.monitor(r, t, parameters) for r, t in zip(y, tsteps)])
    V = y.T[model.state_indices("v")]
    Cai = y.T[model.state_indices("cai")]
    Ta = monitor.T[model.monitor_indices("Ta")]
    CaTrpn = y.T[model.state_indices("CaTrpn")]

    if mech_type =='dyn':
        Lambda = y.T[model.state_indices("lmbda")]

    d = {
        'V': V[::50],
        'Cai': Cai[::50],
        'Ta':Ta[::50],
        'CaTrpn': CaTrpn[::50]
        }
    
    if mech_type =='dyn':
        d = {
        'V': V[::50],
        'Cai': Cai[::50],
        'Ta':Ta[::50],
        'Lambda': Lambda[::50]
        }
    
    np.save(f'init_pop/res_{mech_type}_{hf_type}.npy', d, allow_pickle=True)



if __name__ == '__main__':
    
    mech = ['iso', 'dyn']
    hf = ['control', 'gomez']
    #drug = sys.argv[1]
    proc = []
    for m in mech:
        for h in hf:
            p = Process(target=save_pop_traces, args=(m, h)) #target=save_pop_drug, args=(m, h, drug)
            p.start()
            proc.append(p)
    for p in proc:
        p.join()
    
    """ 
    mech = ['iso', 'dyn']
    hf = ['control', 'gomez']
    drug = [
        'dofetilide', 'verapamil', 'quinidine','bepridil','sotalol', 'azimilide','ibutilide',
        'vandetanib', 'disopyramide', 'chlorpromazine', 'cisapride', 'ondansetron', 'terfenadine',
        'diltiazem', 'mexiletine', 'ranolazine', 'astemizole', 'clozapine', 'domperidone', 'droperidol', 
        'pimozide', 'risperidone', 'loratadine', 'metoprolol', 'nifedipine', 'nitrendipine', 'tamoxifen',
        'clarithromycin'
        ]
    
    for m in mech:
        for h in hf:
            for d in drug:
                test_plot_drug(mech_type=m, hf_type=h, drug_type=d, out=True)
    """