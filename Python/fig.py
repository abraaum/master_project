import new_model_lambda as model_mm
import new_model as model
from scipy.integrate import odeint
import numpy as np 
import pylab
import matplotlib.pyplot as plt
import tqdm

import importlib
importlib.reload(model_mm)
importlib.reload(model)


t = np.arange(0.0, 1000.0, 0.1)
num_beats = 10


SLvals = np.linspace(1.8,2.3,6)
lmbdavals = SLvals/1.85
#[0.97297297 1.02702703 ! 1.08108108 1.13513514 1.18918919 1.24324324]
#lmbdavals = [1.08108108, 1.13513514, 1.18918919, 1.24324324]
force_ind = model.monitor_indices("Ta")     

def run_lam_mm(lambda_0=True):
    for l in lmbdavals:
        force = []
        if lambda_0 == True:
            p = model_mm.init_parameter_values(
                lmbda_0=1,
                )
        else: 
            p = model_mm.init_parameter_values(
                lmbda_0=l,
                )
        init = model_mm.init_state_values(lmbda=l)
        for i in tqdm.tqdm(range(num_beats)):
            s = odeint(model_mm.rhs, init, t, (p,))
            init = s[-1] 
        for tn,sn in zip(t,s):
            m = model_mm.monitor(sn, tn, p)
            force.append(m[force_ind])
        pylab.plot(t, force, label=l)
    pylab.legend()
    pylab.show()


def run_lam():
    for l in lmbdavals:
        force = []
        p = model.init_parameter_values(
            lmbda=l,
            )
        init = model.init_state_values()
        for i in tqdm.tqdm(range(num_beats)):
            s = odeint(model.rhs, init, t, (p,))
            init = s[-1] 
        for tn,sn in zip(t,s):
            m = model.monitor(sn, tn, p)
            force.append(m[force_ind])
        pylab.plot(t, force, label=l)
    pylab.legend()
    pylab.show()



def run_lam_plots(lmbda=1.18918919, lambda_0=True):
    init = model.init_state_values(lmbda=lmbda)
    if lambda_0 == True:
        p = model.init_parameter_values(lmbda_0=lmbda)
    else: 
        p = model.init_parameter_values()

    for i in tqdm.tqdm(range(num_beats)):
        s = odeint(model.rhs, init, t, args=(p,))
        init = s[-1]

    V_idx = model.state_indices('v')
    V = s.T[V_idx]
    Cai_idx = model.state_indices('cai')
    Cai = s.T[Cai_idx]
    lam_idx = model.state_indices('lmbda')
    lam = s.T[lam_idx]

    monitor = np.array([model.monitor(rr, tt, p) for rr, tt in zip(s, t)])
    Ta_idx = model.monitor_indices('Ta')
    Ta = monitor.T[Ta_idx]

    fig, ax = plt.subplots(4, 1, sharex=True)
    ax[0].plot(t, V)
    ax[0].set_title('Voltage')
    ax[1].plot(t, Cai)
    ax[1].set_title('Cai')
    ax[2].plot(t, lam)
    ax[2].set_title('Lambda')
    ax[3].plot(t, Ta)
    ax[3].set_title('Ta')
    ax[3].set_xlabel(f'Time (ms), lambda={lmbda}')
    plt.show()

def compare_isometric():
    for l in lmbdavals:
        force_dyn = []
        force_stat = []
        p_dyn = model_mm.init_parameter_values(
            lmbda_0=l,Kse=1e6
            )
        p_stat = model.init_parameter_values(lmbda=l)
        init_dyn = model_mm.init_state_values(lmbda=l)
        init_stat = model.init_state_values()
        for i in tqdm.tqdm(range(num_beats)):
            s_dyn = odeint(model_mm.rhs, init_dyn, t, (p_dyn,))
            init_dyn = s_dyn[-1]
            s_stat = odeint(model.rhs, init_stat, t, (p_stat,))
            init_stat = s_stat[-1] 
        for tn,sn in zip(t,s_dyn):
            m = model_mm.monitor(sn, tn, p_dyn)
            force_dyn.append(m[force_ind])
        pylab.plot(t, force_dyn, label=f'Dynamic, $\lambda$={l:3.2f}')
        for tn,sn in zip(t,s_stat):
            m = model.monitor(sn, tn, p_stat)
            force_stat.append(m[force_ind])
        pylab.plot(t, force_stat,':', label=f'Static, $\lambda$={l:3.2f}')
    pylab.legend()
    pylab.show()



if __name__ == "__main__":
    #for l in lmbdavals:
    #    run_lam_plots(lmbda=l)
    compare_isometric()
    #run_lam_mm(True)
    #run_lam_mm(False)
    #run_lam()

