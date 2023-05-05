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
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")


from drug_values import drug_dict
from population_func import apd_values, catd_values, tad_values, state_biomarkers, monitored_biomarkers , extra_biomarkers_drug

tsteps = np.arange(0.0, 1000.0, 0.1)  # real run 1000
pop_size = 1000

drug_h = [
        "dofetilide",
        "quinidine",
        "bepridil",
        "sotalol",
        "azimilide",
        "ibutilide",
        "vandetanib",
        "disopyramide",
    ]
drug_i = [
    "clarithromycin",
    "chlorpromazine",
    "cisapride",
    "ondansetron",
    "terfenadine",
    "astemizole",
    "clozapine",
    "domperidone",
    "droperidol",
    "pimozide",
    "risperidone",
]
drug_n = [
    "verapamil",
    "diltiazem",
    "mexiletine",
    "ranolazine",
    "loratadine",
    "metoprolol",
    "nifedipine",
    "nitrendipine",
    "tamoxifen",
]
drug_all = [
    'azimilide',
    'bepridil',
    'disopyramide',
    'dofetilide',
    'ibutilide',
    'quinidine',
    'sotalol',
    'vandetanib',
    'astemizole',
    'chlorpromazine',
    'cisapride',
    'clozapine',
    'domperidone',
    'droperidol',
    'ondansetron',
    'pimozide',
    'risperidone',
    'terfenadine',
    'clarithromycin',
    'diltiazem',
    'loratadine',
    'metoprolol',
    'mexiletine',
    'nifedipine',
    'nitrendipine',
    'ranolazine',
    'tamoxifen',
    'verapamil'
    ]


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



def df_pop_baseline(mech_type, hf_type, cell_type='endo'):
    """Run the population model with different drugs.
    """
    # load random sampling values
    rand_val = np.load(f'init_pop/rand_sample_iso_control.npy')
    # load specific population
    y0s = np.load(f'init_pop/population_{mech_type}_{hf_type}.npy') 

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
                'drug_type': 'baseline',
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

    df_biomarkers.to_csv(f'drug/df_drug_baseline_{mech_type}_{hf_type}.csv')
    


def df_diff_latex(mech_type, hf_type):

    dfs = []
    baseline_df = pd.read_csv(f'drug/df_drug_baseline_{mech_type}_{hf_type}.csv')
    dfs.append(baseline_df)

    drugs = [
        'azimilide','bepridil','disopyramide','dofetilide','ibutilide','quinidine',
        'sotalol','vandetanib','astemizole','chlorpromazine','cisapride','clozapine',
        'domperidone','droperidol','ondansetron','pimozide','risperidone','terfenadine',
        'clarithromycin','diltiazem','loratadine','metoprolol','mexiletine','nifedipine',
        'nitrendipine','ranolazine','tamoxifen','verapamil'
    ]

    for d in drugs:
        drug_df = pd.read_csv(f'drug/df_drug_{d}_{mech_type}_{hf_type}.csv')
        dfs.append(drug_df)

    diff_d = []

    for i in range(len(dfs)):
        current_df = dfs[i]

        EmWs = current_df['CaTD_90'] - current_df['APD_90']

        mean_vals = current_df.mean()
        sd_vals = current_df.std()

        APD_90_mean = round(mean_vals['APD_90'], 1)
        APD_90_sd =  round(sd_vals['APD_90'], 1) 

        Tri_90_30_mean = round(mean_vals['Tri90_30'], 1)
        Tri_90_30_sd = round(sd_vals['Tri90_30'], 1)

        CaTA_mean =  round((mean_vals['CaTA'])*1000, 2)
        CaTA_sd =  round((sd_vals['CaTA'])*1000, 3) 

        CaTD_80_mean = round(mean_vals['CaTD_80'], 1) 
        CaTD_80_sd =  round(sd_vals['CaTD_80'], 1) 

        DevF_mean = round(mean_vals['DevF'], 2) 
        DevF_sd = round(sd_vals['DevF'], 2) 

        RT50_mean = round(mean_vals['RT50'], 1) 
        RT50_sd = round(sd_vals['RT50'], 1) 

        EmW_mean = round(EmWs.mean(), 1)
        EmW_sd = round(EmWs.std(), 1)

        qNet_mean = round(mean_vals['qNet'], 1) 
        qNet_sd = round(sd_vals['qNet'], 2) 

    
        new_d = {
            'Drug': 'baseline' if i==0 else drugs[i-1],
            'APD90': f'{APD_90_mean} ({APD_90_sd})',
            'Tri90-30': f'{Tri_90_30_mean} ({Tri_90_30_sd})',
            'CaTA': f'{CaTA_mean} ({CaTA_sd})',
            'CaTD80': f'{CaTD_80_mean} ({CaTD_80_sd})',
            'DevF': f'{DevF_mean} ({DevF_sd})',
            'RT50': f'{RT50_mean} ({RT50_sd})',
            'EmW': f'{EmW_mean} ({EmW_sd})',
            'qNet': f'{qNet_mean} ({qNet_sd})',         
            
        }

        diff_d.append(new_d)
    
    full_diff_df = pd.DataFrame(diff_d)

    print(full_diff_df.to_latex(index=False))


def df_diff_csv(mech_type, hf_type):

    dfs = []
    baseline_df = pd.read_csv(f'drug/df_drug_baseline_{mech_type}_{hf_type}.csv')
    dfs.append(baseline_df)

    drugs = [
        'azimilide','bepridil','disopyramide','dofetilide','ibutilide','quinidine',
        'sotalol','vandetanib','astemizole','chlorpromazine','cisapride','clozapine',
        'domperidone','droperidol','ondansetron','pimozide','risperidone','terfenadine',
        'clarithromycin','diltiazem','loratadine','metoprolol','mexiletine','nifedipine',
        'nitrendipine','ranolazine','tamoxifen','verapamil'
    ]

    for d in drugs:
        drug_df = pd.read_csv(f'drug/df_drug_{d}_{mech_type}_{hf_type}.csv')
        dfs.append(drug_df)

    diff_d = []

    for i in range(len(dfs)):
        current_df = dfs[i]

        EmWs = current_df['CaTD_90'] - current_df['APD_90']

        mean_vals = current_df.mean()
        sd_vals = current_df.std()
        min_vals = current_df.min()
        max_vals = current_df.max()


        APD_90_mean = round(mean_vals['APD_90'], 4)
        APD_90_sd =  round(sd_vals['APD_90'], 4) 
        APD_90_min = round(min_vals['APD_90'], 4)
        APD_90_max =  round(max_vals['APD_90'], 4) 

        Tri_90_30_mean = round(mean_vals['Tri90_30'], 4)
        Tri_90_30_sd = round(sd_vals['Tri90_30'], 4)
        Tri_90_30_min = round(min_vals['Tri90_30'], 4)
        Tri_90_30_max = round(max_vals['Tri90_30'], 4)

        CaTA_mean =  round((mean_vals['CaTA'])*1000, 4)
        CaTA_sd =  round((sd_vals['CaTA'])*1000, 4) 
        CaTA_min =  round((min_vals['CaTA'])*1000, 4) 
        CaTA_max =  round((max_vals['CaTA'])*1000, 4) 

        CaTD_80_mean = round(mean_vals['CaTD_80'], 4) 
        CaTD_80_sd =  round(sd_vals['CaTD_80'], 4) 
        CaTD_80_min =  round(min_vals['CaTD_80'], 4) 
        CaTD_80_max =  round(max_vals['CaTD_80'], 4) 

        DevF_mean = round(mean_vals['DevF'], 4) 
        DevF_sd = round(sd_vals['DevF'], 4) 
        DevF_min = round(min_vals['DevF'], 4) 
        DevF_max = round(max_vals['DevF'], 4) 

        RT50_mean = round(mean_vals['RT50'], 4) 
        RT50_sd = round(sd_vals['RT50'], 4) 
        RT50_min = round(min_vals['RT50'], 4)
        RT50_max = round(max_vals['RT50'], 4)

        EmW_mean = round(EmWs.mean(), 4)
        EmW_sd = round(EmWs.std(), 4)
        EmW_min = round(EmWs.min(), 4)
        EmW_max = round(EmWs.max(), 4)

        qNet_mean = round(mean_vals['qNet'], 4) 
        qNet_sd = round(sd_vals['qNet'], 4) 
        qNet_min = round(min_vals['qNet'], 4) 
        qNet_max = round(max_vals['qNet'], 4) 

    
        new_d = {
            'Drug': 'baseline' if i==0 else drugs[i-1],
            'APD90_m': f'{APD_90_mean}',
            'APD90_sd': f'{APD_90_sd}',
            'APD90_min': f'{APD_90_min}',
            'APD90_max': f'{APD_90_max}',

            'Tri90-30_m': f'{Tri_90_30_mean}',
            'Tri90-30_sd': f'{Tri_90_30_sd}',
            'Tri90-30_min': f'{Tri_90_30_min}',
            'Tri90-30_max': f'{Tri_90_30_max}',

            'CaTA_m': f'{CaTA_mean}',
            'CaTA_sd': f'{CaTA_sd}',
            'CaTA_min': f'{CaTA_min}',
            'CaTA_max': f'{CaTA_max}',

            'CaTD80_m': f'{CaTD_80_mean}',
            'CaTD80_sd': f'{CaTD_80_sd}',
            'CaTD80_min': f'{CaTD_80_min}',
            'CaTD80_max': f'{CaTD_80_max}',

            'DevF_m': f'{DevF_mean}',
            'DevF_sd': f'{DevF_sd}',
            'DevF_min': f'{DevF_min}',
            'DevF_max': f'{DevF_max}',

            'RT50_m': f'{RT50_mean}',
            'RT50_sd': f'{RT50_sd}',
            'RT50_min': f'{RT50_min}',
            'RT50_max': f'{RT50_max}',
            
            'EmW_m': f'{EmW_mean}',
            'EmW_sd': f'{EmW_sd}',
            'EmW_min': f'{EmW_min}',
            'EmW_max': f'{EmW_max}',

            'qNet_m': f'{qNet_mean}', 
            'qNet_sd': f'{qNet_sd}', 
            'qNet_min': f'{qNet_min}', 
            'qNet_max': f'{qNet_max}',        
            
        }

        diff_d.append(new_d)
    
    full_diff_df = pd.DataFrame(diff_d)
    
    full_diff_df.to_csv(f'diff_drug_full_{mech_type}_{hf_type}.csv')


def histograms(mech_type, hf_type, drug_type):
    baseline_df = pd.read_csv(f'drug/df_drug_baseline_{mech_type}_{hf_type}.csv')
    drug_df = pd.read_csv(f'drug/df_drug_{drug_type}_{mech_type}_{hf_type}.csv')

    biomarkers = [
        'APD_30','APD_90','Tri90_40','Tri90_50',
        'CaTD_50','CaTD_80','CaTD_90','RT50','RT90','TTP', 'Ta_min', 'Ta_max', 
        'dvdt_max', 'RMP', 'V_peak', 'diast_Ca', 'syst_Ca','CaTA','DevF','qNet']
    
    fig, axis = plt.subplots(4,5, figsize=(16,8), sharey=False, sharex=False)
    m = 0
    for i in range(len(axis)):
        for j in range(len(axis[0])):
            axis[i][j].set_title(biomarkers[m])
            sns.distplot(ax=axis[i, j], x =baseline_df[f'{biomarkers[m]}'], kde=True, color='tab:blue')
            sns.distplot(ax=axis[i, j], x =drug_df[f'{biomarkers[m]}'], kde=True, color='tab:orange')
            m += 1
            axis[i][j].set_xticks([])
            axis[i][j].set_yticks([])
    
    fig.suptitle(f'Distribution with {drug_type} ({mech_type},{hf_type})')
    plt.legend(labels=['baseline', f'{drug_type}'], loc='upper right')
    plt.savefig(f'plots/drug_trial/dist_{mech_type}_{hf_type}_{drug_type}.png')


def biomarkers_paired_smd(mech_type, hf_type, drugs, get_mean=False):

    dfs = []
    baseline_df = pd.read_csv(f'drug/df_drug_baseline_{mech_type}_{hf_type}.csv')

    for d in drugs:
            drug_df = pd.read_csv(f'drug/df_drug_{d}_{mech_type}_{hf_type}.csv')
            dfs.append(drug_df)
    
    APD_90_base = baseline_df['APD_90']
    Tri_90_30_base = baseline_df['Tri90_30']
    CaTA_base = baseline_df['CaTA']
    CaTD_80_base = baseline_df['CaTD_80']
    DevF_base = baseline_df['DevF']
    RT50_base = baseline_df['RT50']
    qNet_base = baseline_df['qNet']
    EmW_base = baseline_df['CaTD_90']-baseline_df['APD_90']

    paired_diff = []
    paired_diff_mean = []

    for i in range(len(dfs)):

        diff_APD_90 = APD_90_base - dfs[i]['APD_90']
        diff_Tri90_30 = Tri_90_30_base - dfs[i]['Tri90_30']
        diff_CaTA = (CaTA_base - dfs[i]['CaTA'])*1000
        diff_CaTD_80 = CaTD_80_base - dfs[i]['CaTD_80']
        diff_DevF = DevF_base - dfs[i]['DevF']
        diff_RT50 = RT50_base - dfs[i]['RT50']
        diff_qNet = qNet_base - dfs[i]['qNet']
        diff_EmW = EmW_base - (dfs[i]['CaTD_90']-dfs[i]['APD_90'])

        new_d = {
            'Drug': dfs[i]['drug_type'][1],
            'APD90_SMD': f'{round((diff_APD_90.mean()/diff_APD_90.std()), 1)}',
            'Tri90-30_SMD': f'{round((diff_Tri90_30.mean()/diff_Tri90_30.std()), 1)}',
            'CaTA_SMD': f'{round((diff_CaTA.mean()/diff_CaTA.std()), 1)}',
            'CaTD80_SMD': f'{round((diff_CaTD_80.mean()/diff_CaTD_80.std()), 1)}',
            'DevF_SMD': f'{round((diff_DevF.mean()/diff_DevF.std()), 1)}',
            'RT50_SMD': f'{round((diff_RT50.mean()/diff_RT50.std()), 1)}',
            'EmW_SMD': f'{round((diff_qNet.mean()/diff_qNet.std()), 1)}',
            'qNet_SMD': f'{round((diff_EmW.mean()/diff_EmW.std()), 1)}',
        }
        paired_diff.append(new_d)

        if get_mean==True:
            new_m = {
                'Drug': dfs[i]['drug_type'][1],
                'APD90_m': f'{round(diff_APD_90.mean(),1)}',
                'APD90_sd': f'{round(diff_APD_90.std(),2)}',

                'Tri90-30_m': f'{round(diff_Tri90_30.mean(),1)}',
                'Tri90-30_sd': f'{round(diff_Tri90_30.std(),2)}',

                'CaTA_m': f'{round(diff_CaTA.mean(),2)}',
                'CaTA_sd': f'{round(diff_CaTA.std(),2)}',

                'CaTD80_m': f'{round(diff_CaTD_80.mean(),1)}',
                'CaTD80_sd': f'{round(diff_CaTD_80.std(),2)}',

                'DevF_m': f'{round(diff_DevF.mean(),1)}',
                'DevF_sd': f'{round(diff_DevF.std(),2)}',

                'RT50_m': f'{round(diff_RT50.mean(),1)}',
                'RT50_sd': f'{round(diff_RT50.std(),2)}',
                
                'EmW_m': f'{round(diff_qNet.mean(),1)}',
                'EmW_sd': f'{round(diff_qNet.std(),2)}',

                'qNet_m': f'{round(diff_EmW.mean(),1)}', 
                'qNet_sd': f'{round(diff_EmW.std(),2)}', 
                }
            paired_diff_mean.append(new_m)

    paired_diff_df = pd.DataFrame(paired_diff)
    print(paired_diff_df.to_latex(index=False))

    if get_mean==True:
        paired_diff_mean_df = pd.DataFrame(paired_diff_mean)
        print(paired_diff_mean_df.to_latex(index=False))




if __name__ == '__main__':
    """  
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
    """
    #df_diff_csv(mech_type='dyn', hf_type='control')
    biomarkers_paired_smd(mech_type='dyn', hf_type='gomez', drugs=drug_all)
    
    """
    drugs = [
    'azimilide',
    'bepridil',
    'disopyramide',
    'dofetilide',
    'ibutilide',
    'quinidine',
    'sotalol',
    'vandetanib',
    'astemizole',
    'chlorpromazine',
    'cisapride',
    'clozapine',
    'domperidone',
    'droperidol',
    'ondansetron',
    'pimozide',
    'risperidone',
    'terfenadine',
    'clarithromycin',
    'diltiazem',
    'loratadine',
    'metoprolol',
    'mexiletine',
    'nifedipine',
    'nitrendipine',
    'ranolazine',
    'tamoxifen',
    'verapamil'
    ]
    mech = ['iso', 'dyn']
    hf = ['control', 'gomez']

    #df_diff('dyn', 'gomez')
    for m in mech:
        for h in hf:
            for d in drugs:
                histograms(mech_type=m, hf_type=h, drug_type=d)

    """

    