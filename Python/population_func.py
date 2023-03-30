"""
Script for extracting different biomarkers for cleaning populaiton model.

TODO:
1. Fix repeating code, put in one func
"""
import ORdmm_Land_em_coupling as model
import numpy as np

def apd_values(y, percentage=0.9, index=False):
    # extract membrane potential
    V = y.T[model.state_indices('v')]
    V_max_idx = np.argmax(V)
    V_tmp = V[V_max_idx:]

    # find value of range [min V, max V] at % repolarization
    V_adp = (1-percentage)*(max(V)-min(V))+min(V)

    # find the index
    apd_idx_tmp = (np.abs(V_tmp - V_adp)).argmin() 
    apd_idx = V_max_idx + apd_idx_tmp
    if index == True:
        return apd_idx 
    else:
        #time in ms
        return apd_idx/10


def catd_values(y, percentage=0.8, index=False):
    # extract Ca_i
    Cai = y.T[model.state_indices('cai')]
    Cai_max_idx = np.argmax(Cai)
    Cai_tmp = Cai[Cai_max_idx:]

    # find value of range [min Cai, max Cai] at % repolarization
    CaTD = (1-percentage)*(max(Cai)-min(Cai))+min(Cai)

    # find the index
    CaTD_idx_tmp = (np.abs(Cai_tmp - CaTD)).argmin() 
    CaTD_idx = Cai_max_idx + CaTD_idx_tmp
    if index == True:
        return CaTD_idx 
    else:
        #time in ms
        return CaTD_idx/10


# monitored
def tad_values(monitor, percentage=0.5, index=False):
    # extract Ta
    Ta = monitor.T[model.monitor_indices("Ta")]
    Ta_max_idx = np.argmax(Ta)
    Ta_tmp = Ta[Ta_max_idx:]

    # find value of range [min Ta, max Ta] at % repolarization
    TaD = (1-percentage)*(max(Ta)-min(Ta))+min(Ta)

    # find the index
    TaD_idx_tmp = (np.abs(Ta_tmp - TaD)).argmin() 
    TaD_idx = Ta_max_idx + TaD_idx_tmp
    if index == True:
        return TaD_idx-Ta_max_idx
    else:
        #time in ms
        return (TaD_idx-Ta_max_idx)/10


def state_biomarkers(y):
    """Simplified ap/cai max/min values for population.
    """
    V = y.T[model.state_indices('v')]
    Cai = y.T[model.state_indices('cai')]

    return min(V), max(V), min(Cai), max(Cai)


def monitored_biomarkers(monitor):
    """Simplified dv_dt/Ta values for population.
    """
    Ta = monitor.T[model.monitor_indices("Ta")]
    Ta_max_idx = np.argmax(Ta)/10 # ms

    dvdt = monitor.T[model.monitor_indices("dv_dt")]

    return Ta_max_idx, min(Ta), max(Ta), max(dvdt)

def extra_biomarkers_drug(monitor):
    dvdt = monitor.T[model.monitor_indices("dv_dt")]
    dcaidt = monitor.T[model.monitor_indices("dcai_dt")]
    inet = monitor.T[model.monitor_indices("Inet")]



#################################
# Specific (repetative) functions
#################################

def ap_max(y, time=False):
    V = y.T[model.state_indices('v')]
    if time == True:
        V_max_idx = np.argmax(V)
        return V_max_idx/10 #time in ms
    else:
        return max(V)


def ap_min(y, time=False):
    V = y.T[model.state_indices('v')]
    if time == True:
        V_min_idx = np.argmin(V)
        return V_min_idx/10 #time in ms
    else:
        return min(V)


def max_cai(y, time=False):
    # systolic
    Cai = y.T[model.state_indices('cai')]
    if time == True:
        Cai_max_idx = np.argmax(Cai)
        return Cai_max_idx/10 #time in ms
    else:
        return max(Cai)


def min_cai(y, time=False):
    # diastolic
    Cai = y.T[model.state_indices('cai')]
    if time == True:
        Cai_min_idx = np.argmin(Cai)
        return Cai_min_idx/10 #time in ms
    else:
        return min(Cai)

#monitored
def ta_max(monitor, time=False):
    Ta = monitor.T[model.monitor_indices("Ta")]
    if time == True:
        Ta_max_idx = np.argmax(Ta)
        return Ta_max_idx/10 #time in ms
    else:
        return max(Ta)

# monitored
def ta_min(monitor, time=False):
    Ta = monitor.T[model.monitor_indices("Ta")]
    if time == True:
        Ta_min_idx = np.argmin(Ta)
        return Ta_min_idx/10 #time in ms
    else:
        return min(Ta)

# monitored
def dvdt_max(monitor, time=False):
    dvdt = monitor.T[model.monitor_indices("dv_dt")]
    if time == True:
        dvdt_max_idx = np.argmax(dvdt)
        return dvdt_max_idx/10 #time in ms
    else:
        return max(dvdt)


