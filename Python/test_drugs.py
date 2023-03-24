import ORdmm_Land_em_coupling as model
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import tqdm


num_beats = 10
tsteps = np.arange(0.0, 1000.0, 0.1)  # real run 1000
#pop_size = 1000

# sequence in list:
# INa, IKr, ICaL, INaL, IKs, Ito, IK1

og = {'drug_INa':0, 'IC50_INa':0, 'h_INa':0,
              'drug_IKr':0, 'IC50_IKr':0, 'h_IKr':0,
              'drug_ICaL':0, 'IC50_ICaL':0, 'h_ICaL':0,
              'drug_INaL':0, 'IC50_INaL':0, 'h_INaL':0,
              'drug_IKs':0, 'IC50_IKs':0, 'h_IKs':0,
              'drug_Ito':0, 'IC50_Ito':0, 'h_Ito':0,
              'drug_IK1':0, 'IC50_IK1':0, 'h_IK1':0}

dofetilide_1 = {'drug_INa':0.0021, 'IC50_INa':31.9, 'h_INa':0.54,
              'drug_IKr':0.0021, 'IC50_IKr':0.013, 'h_IKr':1.56,
              'drug_ICaL':0.0021, 'IC50_ICaL':201, 'h_ICaL':1,
              'drug_INaL':0, 'IC50_INaL':0, 'h_INaL':0,
              'drug_IKs':0.0021, 'IC50_IKs':135, 'h_IKs':1,
              'drug_Ito':0.0021, 'IC50_Ito':300, 'h_Ito':1,
              'drug_IK1':0, 'IC50_IK1':0, 'h_IK1':0}

verapamil_1 = {'drug_INa':0.088, 'IC50_INa':32.5, 'h_INa':1.33,
             'drug_IKr':0.088, 'IC50_IKr':0.25, 'h_IKr':0.89,
             'drug_ICaL':0.088, 'IC50_ICaL':0.2, 'h_ICaL':0.8,
             'drug_INaL':0, 'IC50_INaL':0, 'h_INaL':0,
             'drug_IKs':0, 'IC50_IKs':0, 'h_IKs':0,
             'drug_Ito':0, 'IC50_Ito':0, 'h_Ito':0,
             'drug_IK1':0, 'IC50_IK1':0, 'h_IK1':0}

quinidine_1 = {'drug_INa':3.237, 'IC50_INa':14.6, 'h_INa':1.22,
             'drug_IKr':3.237, 'IC50_IKr':0.72, 'h_IKr':1.06,
             'drug_ICaL':3.237, 'IC50_ICaL':6.4, 'h_ICaL':0.68,
             'drug_INaL':0, 'IC50_INaL':0, 'h_INaL':0,
             'drug_IKs':0, 'IC50_IKs':0, 'h_IKs':0,
             'drug_Ito':0, 'IC50_Ito':0, 'h_Ito':0,
             'drug_IK1':0, 'IC50_IK1':0, 'h_IK1':0}

dofetilide_2 = {'drug_INa':2, 'IC50_INa':1460000, 'h_INa':5.1,
              'drug_IKr':2, 'IC50_IKr':75, 'h_IKr':1,
              'drug_ICaL':2, 'IC50_ICaL':2300, 'h_ICaL':5.4,
              'drug_INaL':2, 'IC50_INaL':837000, 'h_INaL':4.6,
              'drug_IKs':2, 'IC50_IKs':100000, 'h_IKs':1,
              'drug_Ito':2, 'IC50_Ito':18.8, 'h_Ito':0.8,
              'drug_IK1':0, 'IC50_IK1':0, 'h_IK1':0}

verapamil_2 = {'drug_INa':81, 'IC50_INa':2480000, 'h_INa':5.1,
              'drug_IKr':81, 'IC50_IKr':452, 'h_IKr':1,
              'drug_ICaL':81, 'IC50_ICaL':202, 'h_ICaL':1.1,
              'drug_INaL':81, 'IC50_INaL':982, 'h_INaL':1.2,
              'drug_IKs':81, 'IC50_IKs':29880, 'h_IKs':0.93,
              'drug_Ito':81, 'IC50_Ito':13429, 'h_Ito':0.8,
              'drug_IK1':81, 'IC50_IK1':3.5e8, 'h_IK1':0.3}

quinidine_2 = {'drug_INa':3237, 'IC50_INa':14600, 'h_INa':1.22,
              'drug_IKr':3237, 'IC50_IKr':971, 'h_IKr':1,
              'drug_ICaL':3237, 'IC50_ICaL':51592, 'h_ICaL':1,
              'drug_INaL':3237, 'IC50_INaL':2360, 'h_INaL':0.91,
              'drug_IKs':3237, 'IC50_IKs':58665, 'h_IKs':1.17,
              'drug_Ito':3237, 'IC50_Ito':3487, 'h_Ito':1.3,
              'drug_IK1':3237, 'IC50_IK1':4.0e7, 'h_IK1':0.4}

drug_lst = [og, dofetilide_1, verapamil_1, quinidine_1, dofetilide_2, verapamil_2, quinidine_2]
drugs = ['Control', 'dofetilide_1', 'verapamil_1', 'quinidine_1', 'dofetilide_2', 'verapamil_2', 'quinidine_2']

fig, ax = plt.subplots(2, 2, sharex=True, figsize=(14,8))
# control
for i in range(len(drug_lst)):
    y0 = np.load(f'init_values/coupled/control_endo_coupled_iso_100.npy')

    parameters = model.init_parameter_values(
            celltype=0,
            isometric=1,
            lmbda_set=1,
            # drug parameters
            drug_INa=drug_lst[i]['drug_INa'],
            IC50_INa=drug_lst[i]['IC50_INa'],
            h_INa=drug_lst[i]['h_INa'],
            #
            drug_IKr=drug_lst[i]['drug_IKr'],
            IC50_IKr=drug_lst[i]['IC50_IKr'],
            h_IKr=drug_lst[i]['h_IKr'],
            #
            drug_ICaL=drug_lst[i]['drug_ICaL'],
            IC50_ICaL=drug_lst[i]['IC50_ICaL'],
            h_ICaL=drug_lst[i]['h_ICaL'],
            #
            drug_INaL=drug_lst[i]['drug_INaL'],
            IC50_INaL=drug_lst[i]['IC50_INaL'],
            h_INaL=drug_lst[i]['h_INaL'],
            #
            drug_IKs=drug_lst[i]['drug_IKs'],
            IC50_IKs=drug_lst[i]['IC50_IKs'],
            h_IKs=drug_lst[i]['h_IKs'],
            #
            drug_Ito=drug_lst[i]['drug_Ito'],
            IC50_Ito=drug_lst[i]['IC50_Ito'],
            h_Ito=drug_lst[i]['h_Ito'],
            #
            drug_IK1=drug_lst[i]['drug_IK1'],
            IC50_IK1=drug_lst[i]['IC50_IK1'],
            h_IK1=drug_lst[i]['h_IK1'],

        )

    for n in tqdm.tqdm(range(num_beats)):
        y = odeint(model.rhs, y0, tsteps, args=(parameters,))
        y0 = y[-1]
    
    monitor = np.array([model.monitor(r, t, parameters) for r, t in zip(y, tsteps)])
    V = y.T[model.state_indices("v")]
    Cai = y.T[model.state_indices("cai")]
    Ta = monitor.T[model.monitor_indices("Ta")]
    CaTrpn = y.T[model.state_indices("CaTrpn")]

    ax[0][0].plot(tsteps, V, linewidth=0.9, label=f"{drugs[i]}")
    ax[0][0].set_title("Voltage")
    ax[0][0].set_ylabel("Voltage (mV)")
    ax[0][0].set_xlabel("Time (ms)")
    ax[0][0].grid(linewidth=0.3)

    ax[0][1].plot(tsteps, Cai, linewidth=0.9)
    ax[0][1].set_title("Cai")
    ax[0][1].set_ylabel("Ca_i (mM)")
    ax[0][1].set_xlabel("Time (ms)")
    ax[0][1].grid(linewidth=0.3)

    ax[1][0].plot(tsteps, Ta, linewidth=0.9)
    ax[1][0].set_title("Ta")
    ax[1][0].set_ylabel("Ta (kPa)")
    ax[1][0].set_xlabel("Time (ms)")
    ax[1][0].grid(linewidth=0.3)

    ax[1][1].plot(tsteps, CaTrpn, linewidth=0.9)
    ax[1][1].set_title("CaTrpn")
    ax[1][1].set_ylabel("CaTrpn")
    ax[1][1].set_xlabel("Time (ms)")
    ax[1][1].grid(linewidth=0.3)


fig.legend(loc=7, ncol=1)
plt.show()
