import ORdmm_Land_em_coupling as model
from scipy.integrate import odeint
import numpy as np
import os

# import pylab
import matplotlib.pyplot as plt
import tqdm
import pandas as pd

# TODO:
# 1. make dict or another file to load different parameter sets


inc = np.arange(0.8, 1.201, 0.05).round(decimals=2)  # real run 0.01
num_beats = 10  # real run 100-1000
tsteps = np.arange(0.0, 1000.0, 0.1)  # real run 1000
lamval = [0.9, 0.95, 1, 1.05, 1.1]
lamfile = ["090", "095", "100", "105", "110"]


def isometric_sensitivity(hf_type, cell_type, mech_param, out=None):
    V_list, Cai_list, Ta_list, CaTrpn_list = [], [], [], []

    for l in range(len(lamval)):
        Vs, Cais, Tas, CaTrpns = [], [], [], []
        for i in range(len(inc)):
            y_load = np.load(
                f"init_values/coupled/{hf_type}_{cell_type}_coupled_iso_{lamfile[l]}.npy"
            )
            y0 = y_load[-1]
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
            "L": lamval,
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


def isometric_sensitivity_max(V, Cai, Ta, CaTrpn, time_2_max=False):
    """Blablabla
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


def isometric_sensitivity_df(V, Cai, Ta, CaTrpn, latex_table=False):
    """Blablabla 
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
            n = f"Lambda: {lamval[l]}, % ktrpn: {inc[i]}"  # CHANGE MANUALLY
            index_names.append(n)

    df = pd.DataFrame(data=data, index=index_names)

    if latex_table == True:
        df = df.to_latex()

    return df


def load_sensitivity_values(filename):
    """Blablabla
    """
    path = os.path.join("sens", filename)
    all_values = np.load(path, allow_pickle=True)

    L = all_values.item().get("L")
    N = all_values.item().get("num_beats")

    if L != [0.9, 0.95, 1.0, 1.05, 1.1]:
        raise ValueError(
            f"This is a test run, the lambda values ({L}) should be equal to [0.9, 0.95, 1.0, 1.05, 1.1]"
        )
    if N != 2:
        raise ValueError(
            f"This is a test run, the # of beats ({N}) should be equal to 100"
        )

    V = all_values.item().get("V")
    Cai = all_values.item().get("Cai")
    Ta = all_values.item().get("Ta")
    CaTrpn = all_values.item().get("CaTrpn")

    return V, Cai, Ta, CaTrpn


def plot_isometric_sensitivity(V, Cai, Ta, CaTrpn):
    Vs, Cais, Tas, CaTrpns = isometric_sensitivity_max(
        V=V, Cai=Cai, Ta=Ta, CaTrpn=CaTrpn, time_2_max=False
    )
    Vs_t, Cais_t, Tas_t, CaTrpns_t = isometric_sensitivity_max(
        V=V, Cai=Cai, Ta=Ta, CaTrpn=CaTrpn, time_2_max=True
    )
    fig, ax = plt.subplots(4, 1, sharex=True)
    l = 0
    for i in range(0, len(Vs), len(inc)):
        V = Vs[i : i + len(inc)]
        Cai = Cais[i : i + len(inc)]
        Ta = Tas[i : i + len(inc)]
        CaTrpn = CaTrpns[i : i + len(inc)]

        ax[0].plot(inc, V, label=f"lambda {lamval[l]}")
        ax[0].set_title("Voltage")
        ax[1].plot(inc, Cai, label=f"lambda {lamval[l]}")
        ax[1].set_title("Cai")
        ax[2].plot(inc, Ta, label=f"lambda {lamval[l]}")
        ax[2].set_title("Ta")
        ax[3].plot(inc, CaTrpn, label=f"lambda {lamval[l]}")
        ax[3].set_title("CaTrpn")
        ax[3].set_xlabel(f"%ktrpn")  # CHANGE MANUALLY

        l += 1

    plt.legend()
    plt.show()

    fig, ax = plt.subplots(4, 1, sharex=True)
    l = 0
    for i in range(0, len(Vs), len(inc)):
        V_t = Vs_t[i : i + len(inc)]
        Cai_t = Cais_t[i : i + len(inc)]
        Ta_t = Tas_t[i : i + len(inc)]
        CaTrpn_t = CaTrpns_t[i : i + len(inc)]

        ax[0].plot(inc, V_t, label=f"lambda {lamval[l]}")
        ax[0].set_title("Voltage")
        ax[1].plot(inc, Cai_t, label=f"lambda {lamval[l]}")
        ax[1].set_title("Cai")
        ax[2].plot(inc, Ta_t, label=f"lambda {lamval[l]}")
        ax[2].set_title("Ta")
        ax[3].plot(inc, CaTrpn_t, label=f"lambda {lamval[l]}")
        ax[3].set_title("CaTrpn")
        ax[3].set_xlabel(f"%ktrpn")  # CHANGE MANUALLY

        l += 1

    plt.legend()
    plt.show()


if __name__ == "__main__":
    type_hf = ['gomez', 'control'] #, 
    params = ['ku', 'kuw', 'kws', 'ktrpn', 'Trpn50', 'gammaw', 'gammas'] #
    # missing control: nothing
    # missing HF: everything

    for i in range(len(type_hf)):
        for j in range(len(params)):
            V, Cai, Ta, CaTrpn = isometric_sensitivity(
                hf_type=type_hf[i], 
                cell_type='endo', 
                mech_param=params[j], 
                out=f'sens_iso_{type_hf[i]}_endo_{params[j]}.npy')


    #V, Cai, Ta, CaTrpn = load_sensitivity_values("test.npy")

    #df = isometric_sensitivity_df(V=V, Cai=Cai, Ta=Ta, CaTrpn=CaTrpn, latex_table=True)
    #print(df)
    # plot_isometric_sensitivity(V=V, Cai=Cai, Ta=Ta, CaTrpn=CaTrpn)
