"""
Script for extracting different measurements from model runs
"""

import numpy as np
import ORdmm_Land as model

def adp_values(hf_type, cell_type, percentage=0.9, index=False):
    # fetch model run
    y = np.load(f"init_values/{hf_type}_{cell_type}_ordmm.npy")
    # extract membrane potential
    V_idx = model.state_indices('v')
    V = y.T[V_idx]
    V_max_idx = np.argmax(V)
    V_tmp = V[V_max_idx:]

    # find value of range [min V, max V] at % repolarization
    V_adp = (1-percentage)*(max(V)-min(V))+min(V)

    # find the index
    adp_idx_tmp = (np.abs(V_tmp - V_adp)).argmin() 
    adp_idx = V_max_idx + adp_idx_tmp
    if index == True:
        return adp_idx 
    else:
        #time in ms
        return adp_idx/10

def catd_values(hf_type, cell_type, percentage=0.8, index=False):
    # fetch model run
    y = np.load(f"init_values/{hf_type}_{cell_type}_ordmm.npy")
    # extract membrane potential
    Cai_idx = model.state_indices('cai')
    Cai = y.T[Cai_idx]
    Cai_max_idx = np.argmax(Cai)
    Cai_tmp = Cai[Cai_max_idx:]

    # find value of range [min V, max V] at % repolarization
    CaTD = (1-percentage)*(max(Cai)-min(Cai))+min(Cai)

    # find the index
    CaTD_idx_tmp = (np.abs(Cai_tmp - CaTD)).argmin() 
    CaTD_idx = Cai_max_idx + CaTD_idx_tmp
    if index == True:
        return CaTD_idx 
    else:
        #time in ms
        return CaTD_idx/10


def ap_max(hf_type, cell_type, time=False):
    y = np.load(f"init_values/{hf_type}_{cell_type}_ordmm.npy")
    V_idx = model.state_indices('v')
    V = y.T[V_idx]

    if time == True:
        V_max_idx = np.argmax(V)
        return V_max_idx/10 #time in ms
    else:
        return max(V)

def cat_max(hf_type, cell_type, time=False):
    y = np.load(f"init_values/{hf_type}_{cell_type}_ordmm.npy")
    Cai_idx = model.state_indices('cai')
    Cai = y.T[Cai_idx]

    if time == True:
        Cai_max_idx = np.argmax(Cai)
        return Cai_max_idx/10 #time in ms
    else:
        return max(Cai)

def ta_max(hf_type, cell_type, time=False):
    """
    WRONG
    """
    y = np.load(f"init_values/{hf_type}_{cell_type}_ordmm.npy")
    tsteps = np.arange(0.0, y.shape[0]/10, 0.1)
    parameters = model.init_parameter_values(celltype=0)
    monitor = np.array([model.monitor(r, t, parameters) for r, t in zip(y, tsteps)])
    # find a way to extract monitored values without running everything again
    # because monitored needs parameters, but this results in a math domain error
    Ta_idx = model.monitor_indices('Ta')
    Ta = monitor.T[Ta_idx]

    if time == True:
        Ta_max_idx = np.argmax(Ta)
        return Ta_max_idx/10 #time in ms
    else:
        return max(Ta)


if __name__ == "__main__":
    """ 
    adp90 = adp_values('gomez', 'endo')
    adp50 = adp_values('gomez', 'endo', percentage=0.5)
    print(adp90)
    print(adp50)

    CaTD80 = catd_values('gomez', 'endo')
    CaTD50 = adp_values('gomez', 'endo', percentage=0.5)
    print(CaTD80)
    print(CaTD50)
    """
    tester = ta_max('gomez', 'epi')
    print(tester)