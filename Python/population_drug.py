import ORdmm_Land_em_coupling as model
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import tqdm
import sys

from drug_values import drug_dict

num_beats = 100
tsteps = np.arange(0.0, 1000.0, 0.1)  # real run 1000
pop_size = 1000

def run_population_drug(mech_type, hf_type, drug_type, part, cell_type='endo'):
    """Run the population model with different drugs.
    """
    # load random sampling values
    rand_val = np.load(f'init_pop/rand_sample_iso_control.npy')
    # load specific population
    y0s = np.load(f'init_pop/population_{mech_type}_{hf_type}.npy') 
    # list for new population
    population_drug = []

    part_dict = {'1': [0,200], '2': [200,400], '3': [400,600], '4': [600,800], '5': [800,1000]}

    for i in range(part_dict[part][0], part_dict[part][1]):
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

        for n in tqdm.tqdm(range(num_beats)):
            y = odeint(model.rhs, y0, tsteps, args=(parameters,))
            y0 = y[-1]
        
        population_drug.append(y0)
    
    np.save(f'init_pop_drug/population_{mech_type}_{hf_type}_{drug_type}_{part}.npy', population_drug, allow_pickle=True) 




if __name__ == "__main__":

    mech = sys.argv[1]
    hf = sys.argv[2]
    drug = sys.argv[3]
    partition = sys.argv[4]

    run_population_drug(mech_type=mech, hf_type=hf, drug_type=drug, part=partition)




    


