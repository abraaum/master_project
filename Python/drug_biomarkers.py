from multiprocessing import Process
import time

import ORdmm_Land_em_coupling as model
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import tqdm
import sys
import os
import pandas as pd


from drug_values import drug_dict
from population_func import apd_values, catd_values, tad_values, state_biomarkers, monitored_biomarkers , extra_biomarkers_drug

tsteps = np.arange(0.0, 1000.0, 0.1)  # real run 1000
pop_size = 1000

def df_pop_drug(mech_type, hf_type, drug_type, cell_type='endo'):
    """Run the population model with different drugs.
    """
    # load random sampling values
    rand_val = np.load(f'init_pop/rand_sample_iso_control.npy')
    # load specific population
    y0s = np.load(f'init_pop_drug/population_{mech_type}_{hf_type}_{drug_type}.npy') 

    biomarkers = []

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

        APD_30 = apd_values(y=y, percentage=0.3)
        APD_40 = apd_values(y=y, percentage=0.4)
        APD_50 = apd_values(y=y, percentage=0.5)
        APD_90 = apd_values(y=y, percentage=0.9)
        Tri90_30 = APD_90 - APD_30
        Tri90_40 = APD_90 - APD_40
        Tri90_50 = APD_90 - APD_50
        CaTD_50 = catd_values(y=y, percentage=0.5)
        CaTD_80 = catd_values(y=y, percentage=0.8)
        CaTD_90 = catd_values(y=y, percentage=0.9)
        RT50 = tad_values(monitor=monitor, percentage=0.5, index=False)
        RT90 = tad_values(monitor=monitor, percentage=0.90, index=False)

        TTP, Ta_min, Ta_max, dvdt_max = monitored_biomarkers(monitor=monitor)

        RMP, V_peak, diast_Ca, syst_Ca = state_biomarkers(y=y)

        #mssing
        # CaTA, EAD, repol_fail, qNet, DevF
        CaTA = abs(diast_Ca-syst_Ca)
        DevF = abs(Ta_min-Ta_max)
        EAD, pos_calc, repol_fail, qNet = extra_biomarkers_drug(monitor, y)

        biomarkers.append(
            {
                'mech_type': mech_type,
                'hf_type': hf_type,
                'drug_type': drug_type,
                'APD_30': APD_30,
                'APD_40': APD_40,
                'APD_50': APD_50,
                'APD_90': APD_90,
                'Tri90_30': Tri90_30,
                'Tri90_40': Tri90_40,
                'Tri90_50': Tri90_50,
                'CaTD_50': CaTD_50,
                'CaTD_80': CaTD_80,
                'CaTD_90': CaTD_90,
                'RT50': RT50,
                'RT90': RT90,
                'TTP': TTP, 
                'Ta_min': Ta_min, 
                'Ta_max': Ta_max, 
                'dvdt_max': dvdt_max, 
                'RMP': RMP, 
                'V_peak': V_peak, 
                'diast_Ca': diast_Ca, 
                'syst_Ca': syst_Ca,
                'CaTA': CaTA,
                'DevF': DevF,
                'EAD': EAD,
                'pos_calc': pos_calc,
                'repol_fail': repol_fail,
                'qNet': qNet

            }
        )

    df_biomarkers = pd.DataFrame(biomarkers)

    df_biomarkers.to_csv(f'drug/df_drug_{drug_type}_{mech_type}_{hf_type}.csv')


    

if __name__ == '__main__':
    drug = sys.argv[1]
    mech = ['iso', 'dyn']
    hf = ['control', 'gomez'] 

    proc = []
    for m in mech:
        for h in hf:
            p = Process(target=df_pop_drug, args=(m, h, drug))
            p.start()
            proc.append(p)
    for p in proc:
        p.join()
    