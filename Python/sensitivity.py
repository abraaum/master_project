import ORdmm_Land_em_coupling as model
from scipy.integrate import odeint
import numpy as np

# import pylab
import matplotlib.pyplot as plt
import tqdm
import pandas as pd

# TODO:
# make small function to save everything from test_with_load_iso
# into npy/maybe json files for easier testing of plots/tables etc


inc = np.arange(0.8,1.201, 0.05).round(decimals=2)  # real run 0.01
num_beats = 100  # real run 100-1000
tsteps = np.arange(0.0, 1000.0, 0.1)  # real run 1000
lamval = [0.9, 0.95, 1, 1.05, 1.1]  
lamfile = ['090', '095', '100', '105', '110']

def test_with_load_iso(hf_type, cell_type):
    V_list, Cai_list, Ta_list, CaTrpn_list = [], [], [], []

    for l in range(len(lamval)):
        Vs, Cais, Tas, CaTrpns = [], [], [], []
        for i in range(len(inc)):
            y_load = np.load(f"init_values/coupled/{hf_type}_{cell_type}_coupled_iso_{lamfile[l]}.npy")
            y0 = y_load[-1]
            parameters = model.init_parameter_values(
                # CHANGE MANUALLY
                celltype=0 if cell_type=='endo' else 1 if cell_type=='epi' else 2,
                isometric=1,
                lmbda_set=lamval[l], 
                # ku_rate=inc[i],
                # kuw_rate=inc[i],
                # kws_rate=inc[i],
                ktrpn_rate=inc[i],
                # ntrpn_rate=inc[i],
                # Trpn50_rate=inc[i],
                # gammaw_rate=inc[i],
                # gammas_rate=inc[i],
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

    return V_list, Cai_list, Ta_list, CaTrpn_list


def isometric_sensitivity():
    """Sensitivity analysis, isometric run
    """
    V_list, Cai_list, Ta_list, CaTrpn_list = [], [], [], []

    for l in range(len(lamval)):
        Vs, Cais, Tas, CaTrpns = [], [], [], []
        for i in range(len(inc)):
            y0 = model.init_state_values(lmbda=lamval[l])
            parameters = model.init_parameter_values(
                # CHANGE MANUALLY
                celltype=0,
                isometric=1,
                lmbda_set=lamval[l], 
                # ku_rate=inc[i],
                # kuw_rate=inc[i],
                # kws_rate=inc[i],
                ktrpn_rate=inc[i],
                # ntrpn_rate=inc[i],
                # Trpn50_rate=inc[i],
                # gammaw_rate=inc[i],
                # gammas_rate=inc[i],
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
            n = f"Lambda: {lamval[l]}, % ktrpn: {inc[i]}" # CHANGE MANUALLY
            index_names.append(n)

    df = pd.DataFrame(data=data, index=index_names)

    if latex_table == True:
        df = df.to_latex()

    return df


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
        ax[3].set_xlabel(f"%ktrpn") # CHANGE MANUALLY

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
        ax[3].set_xlabel(f"%ktrpn") # CHANGE MANUALLY

        l += 1

    plt.legend()
    plt.show()


if __name__ == "__main__":
    # isometric_sensitivity_markdown()
    V, Cai, Ta, CaTrpn = test_with_load_iso(hf_type='control', cell_type='endo')

    df = isometric_sensitivity_df(V=V, Cai=Cai, Ta=Ta, CaTrpn=CaTrpn, latex_table=True)
    print(df)
    plot_isometric_sensitivity(V=V, Cai=Cai, Ta=Ta, CaTrpn=CaTrpn)
