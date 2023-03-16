import ORdmm_Land_em_coupling as model
from scipy.integrate import odeint
import numpy as np
import os
import matplotlib.pyplot as plt
import tqdm
import pandas as pd
import sys

from population_func import apd_values, catd_values, tad_values, state_biomarkers, monitored_biomarkers #ap_max, dvdt_max

num_beats = 100
tsteps = np.arange(0.0, 1000.0, 0.1)  # real run 1000
pop_size = 1000
# lambda = 1


def random_sampling(pop_size=pop_size, hf_type='control', mech_type='iso'):
    """Random sampling (pop_size x 12 parameters) from normal distribution"""
    #np.random.seed(12) # iso control
    np.random.seed(13) # iso HF
    #np.random.seed(14) # dynamic control
    #np.random.seed(15) # dynamic HF
    selected_val = np.random.normal(loc=1, scale = 0.15, size=(pop_size, 12))
    # save to file
    if not os.path.isdir("init_pop"):
        os.mkdir("init_pop")
    np.save(f"init_pop/rand_sample_{mech_type}_{hf_type}.npy", selected_val)


def make_population(hf_type, cell_type, mech_type, part):
    """Make population of models. (for multiple partitions)
    """
    # load random sampling values
    rand_val = np.load(f'init_pop/rand_sample_{mech_type}_{hf_type}.npy') 
    population = []

    part_dict = {'1': [0,200], '2': [200,400], '3': [400,600], '4': [600,800], '5': [800,1000]}

    for i in range(part_dict[part][0], part_dict[part][1]):
        print(i)
        y0 = np.load(
            f"init_values/coupled/{hf_type}_{cell_type}_coupled_{mech_type}_100.npy"
        )
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
        
        for n in tqdm.tqdm(range(num_beats)):
            y = odeint(model.rhs, y0, tsteps, args=(parameters,))
            y0 = y[-1]

        population.append(y0)

    np.save(f'init_pop/population_{mech_type}_{hf_type}_{part}.npy', population, allow_pickle=True) #AGATHE
    

def plot_population(hf_type='control', cell_type='endo', mech_type='iso'):
    """Load population -> clean data"""
    # load random sampling values
    rand_val = np.load(f'rand_sample_{mech_type}_{hf_type}.npy') 
    # load population
    y0s = np.load('tester_pop.npy') #f'population_{mech_type}_{hf_type}.npy' AGATHE

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
        
        ax[0][0].plot(tsteps, V, linewidth=0.7)
        ax[0][0].set_title("Voltage")
        ax[0][0].set_ylabel("Voltage (mV)")
        ax[0][0].set_xlabel("Time (ms)")
        ax[0][0].grid(linewidth=0.3)

        ax[0][1].plot(tsteps, Cai, linewidth=0.7)
        ax[0][1].set_title("Cai")
        ax[0][1].set_ylabel("Ca_i (mM)")
        ax[0][1].set_xlabel("Time (ms)")
        ax[0][1].grid(linewidth=0.3)

        ax[1][0].plot(tsteps, Ta, linewidth=0.7)
        ax[1][0].set_title("Ta")
        ax[1][0].set_ylabel("Ta ()")
        ax[1][0].set_xlabel("Time (ms)")
        ax[1][0].grid(linewidth=0.3)

        ax[1][1].plot(tsteps, CaTrpn, linewidth=0.7)
        ax[1][1].set_title("CaTrpn")
        ax[1][1].set_ylabel("CaTrpn ()")
        ax[1][1].set_xlabel("Time (ms)")
        ax[1][1].grid(linewidth=0.3)

    plt.show()


def clean_population(hf_type='control', cell_type='endo', mech_type='iso'):
    """NOT FINISHED, missing mechanical check and save
    Load population -> clean data -> new population"""
    # load random sampling values
    rand_val = np.load(f'init_pop/rand_sample_{mech_type}_{hf_type}.npy') 
    # load population
    y0s = np.load(f'init_pop/population_{mech_type}_{hf_type}.npy') # AGATHE

    remove_pop = []

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
        
        # biomarkers from Mora
        APD_40 = apd_values(y=y, percentage=0.4)
        APD_50 = apd_values(y=y, percentage=0.5)
        APD_90 = apd_values(y=y, percentage=0.9)
        Tri90_40 = APD_90 - APD_40
        CaTD_50 = catd_values(y=y, percentage=0.5)
        CaTD_90 = catd_values(y=y, percentage=0.9)
        RT50 = tad_values(monitor=monitor, percentage=0.5, index=False)
        RT95 = tad_values(monitor=monitor, percentage=0.95, index=False) #Says both 90 and 95 in paper
        # eq's beneath can be split into different calls if uncertain, see population_func
        TTP, Ta_min, Ta_max, dvdt_max = monitored_biomarkers(monitor=monitor)
        RMP, V_peak, diast_Ca, syst_Ca = state_biomarkers(y=y)

        # cost function for mechanical biomarkers

        d_TTP = 0 if TTP >= 147 and TTP <= 172 else min(abs(TTP-147), abs(TTP-172)) # 147, 172
        d_RT50 = 0 if RT50 >= 109 and RT50 <= 125 else min(abs(RT50-109), abs(RT50-125)) # 109, 125
        d_RT95 = 0 if RT95 >= 291 and RT95 <= 377 else min(abs(RT95-291), abs(RT95-377)) # 291, 377
        d_Ta_max = 0 if Ta_max >= 15 and Ta_max <= 25 else min(abs(Ta_max-15), abs(Ta_max-25)) # 15, 25

        d_t = d_TTP + d_RT50 + d_RT95 + 10*d_Ta_max + 25*Ta_min

        # check electrophysiological biomarkers
        print(f'Cell number {i}')
        #print(d_t) # AGATHE
        if APD_40 >= 85 and APD_40 <= 320 and \
            APD_50 >= 110 and APD_50 <= 350 and \
            APD_90 >= 180 and APD_90 <= 440 and \
            Tri90_40 >= 50 and Tri90_40 <= 150 and \
            dvdt_max >= 150 and dvdt_max <= 1000 and \
            V_peak >= 10 and V_peak <= 55 and \
            RMP >= -95 and RMP <= -80 and \
            CaTD_50 >= 120 and CaTD_50 <= 420 and \
            CaTD_90 >= 220 and CaTD_90 <= 785 and \
            syst_Ca >= 0.000262 and syst_Ca <= 0.00223 and \
            diast_Ca >= 0 and diast_Ca <= 0.00040 and \
            d_t < 5:

            pass 

        else:
            remove_pop.append(i)
        
        # check mechanical biomarkers
    
    new_parameters = rand_val.copy() #for safety
    new_population = y0s.copy() #for safety

    new_parameters = np.delete(new_parameters, remove_pop, 0)
    new_population = np.delete(new_population, remove_pop, 0)
    print(remove_pop)
    
    np.save(f'init_pop/population_{mech_type}_{hf_type}_clean.npy', new_population)
    np.save(f'init_pop/rand_sample_{mech_type}_{hf_type}_clean.npy', new_parameters)
    np.save(f'init_pop/population_{mech_type}_{hf_type}_remove.npy', remove_pop, allow_pickle=True)
    

        
           


if __name__ == "__main__":
    
    #random_sampling(hf_type='gomez', mech_type='iso')
    partition = sys.argv[1]
    make_population(hf_type='gomez', cell_type='endo', mech_type='iso', part=partition)
    
    #plot_population(hf_type='control', cell_type='endo', mech_type='iso')
    #clean_population()
