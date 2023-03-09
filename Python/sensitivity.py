"""
Funcitons for running mechanical sensitivity analysis.

TODO:
1. Add dynamic run
2. make dict or another file to load different parameter sets (?)
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
lamfile = ["090", "095", "100", "105", "110"]

lamval_dyn = [1, 1.05, 1.1]
lamfile_dyn = ["100", "105", "110"]


def isometric_sensitivity(hf_type, cell_type, mech_param, out=None):
    V_list, Cai_list, Ta_list, CaTrpn_list = [], [], [], []

    for l in range(len(lamval)):
        Vs, Cais, Tas, CaTrpns = [], [], [], []
        for i in range(len(inc)):
            y0 = np.load(
                f"init_values/coupled/{hf_type}_{cell_type}_coupled_iso_{lamfile[l]}.npy"
            )
            parameters = model.init_parameter_values(
                celltype=0 if cell_type == "endo" else 1 if cell_type == "epi" else 2,
                isometric=1,
                lmbda_set=lamval[l],
                #mechanical parameters
                ku_rate=inc[i] if mech_param=='ku' else 1,
                kuw_rate=inc[i] if mech_param=='kuw' else 1,
                kws_rate=inc[i] if mech_param=='kws' else 1,
                ktrpn_rate=inc[i] if mech_param=='ktrpn' else 1,
                Trpn50_rate=inc[i] if mech_param=='Trpn50' else 1,
                gammaw_rate=inc[i] if mech_param=='gammaw' else 1,
                gammas_rate=inc[i] if mech_param=='gammas' else 1,
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

            monitor = np.array(
                [model.monitor(r, t, parameters) for r, t in zip(y, tsteps)]
            )

            V = y.T[model.state_indices("v")]
            Cai = y.T[model.state_indices("cai")]
            Ta = monitor.T[model.monitor_indices("Ta")]
            CaTrpn = y.T[model.state_indices("CaTrpn")]

            Vs.append(V)
            Cais.append(Cai)
            Tas.append(Ta)
            CaTrpns.append(CaTrpn)

        V_list.append(Vs)
        Cai_list.append(Cais)
        Ta_list.append(Tas)
        CaTrpn_list.append(CaTrpns)

    if out != None:
        # save value to file in specific folder
        # sens/...
        if not os.path.isdir("sens"):
            os.mkdir("sens")

        d = {
            "L": lamval_dyn,
            "num_beats": num_beats,
            "V": V_list,
            "Cai": Cai_list,
            "Ta": Ta_list,
            "CaTrpn": CaTrpn_list,
        }

        path = os.path.join("sens", out)
        np.save(path, d, allow_pickle=True)
        print(f'Finished and saved {out}.')

    return V_list, Cai_list, Ta_list, CaTrpn_list


def dynamic_sensitivity(hf_type, cell_type, mech_param, out=None):
    V_list, Cai_list, Ta_list, CaTrpn_list, lmbda_list = [], [], [], [], []

    for l in range(len(lamval_dyn)):
        Vs, Cais, Tas, CaTrpns, lmbdas = [], [], [], [], []
        for i in range(len(inc)):
            y0 = np.load(
                f"init_values/coupled/{hf_type}_{cell_type}_coupled_dyn_{lamfile_dyn[l]}.npy"
            )
            parameters = model.init_parameter_values(
                celltype=0 if cell_type == "endo" else 1 if cell_type == "epi" else 2,
                isometric=0,
                lmbda_set=lamval_dyn[l],
                #mechanical parameters
                ku_rate=inc[i] if mech_param=='ku' else 1,
                kuw_rate=inc[i] if mech_param=='kuw' else 1,
                kws_rate=inc[i] if mech_param=='kws' else 1,
                ktrpn_rate=inc[i] if mech_param=='ktrpn' else 1,
                Trpn50_rate=inc[i] if mech_param=='Trpn50' else 1,
                gammaw_rate=inc[i] if mech_param=='gammaw' else 1,
                gammas_rate=inc[i] if mech_param=='gammas' else 1,
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

            monitor = np.array(
                [model.monitor(r, t, parameters) for r, t in zip(y, tsteps)]
            )

            V = y.T[model.state_indices("v")]
            Cai = y.T[model.state_indices("cai")]
            Ta = monitor.T[model.monitor_indices("Ta")]
            CaTrpn = y.T[model.state_indices("CaTrpn")]
            lmbda = y.T[model.state_indices("lmbda")]

            Vs.append(V)
            Cais.append(Cai)
            Tas.append(Ta)
            CaTrpns.append(CaTrpn)
            lmbdas.append(lmbda)

        V_list.append(Vs)
        Cai_list.append(Cais)
        Ta_list.append(Tas)
        CaTrpn_list.append(CaTrpns)
        lmbda_list.append(lmbdas)

    if out != None:
        # save value to file in specific folder
        # sens/...
        if not os.path.isdir("sens"):
            os.mkdir("sens")

        d = {
            "L": lamval_dyn,
            "num_beats": num_beats,
            "V": V_list,
            "Cai": Cai_list,
            "Ta": Ta_list,
            "CaTrpn": CaTrpn_list,
            "Lambda": lmbda_list,
        }

        path = os.path.join("sens", out)
        np.save(path, d, allow_pickle=True)
        print(f'Finished and saved {out}.')

    return V_list, Cai_list, Ta_list, CaTrpn_list, lmbda_list


if __name__ == "__main__":
    type_hf = ['control', 'gomez',] 
    params = ['ku', 'kuw', 'kws', 'ktrpn', 'Trpn50', 'gammaw', 'gammas'] # 


    for i in range(len(type_hf)):
        for j in range(len(params)):
            V, Cai, Ta, CaTrpn, lam = dynamic_sensitivity(
                hf_type=type_hf[i], 
                cell_type='endo', 
                mech_param=params[j], 
                out=f'sens_dyn_{type_hf[i]}_endo_{params[j]}.npy')


    #V, Cai, Ta, CaTrpn = load_sensitivity_values("test.npy")

    #df = isometric_sensitivity_df(V=V, Cai=Cai, Ta=Ta, CaTrpn=CaTrpn, latex_table=True)
    #print(df)
    # plot_isometric_sensitivity(V=V, Cai=Cai, Ta=Ta, CaTrpn=CaTrpn)
