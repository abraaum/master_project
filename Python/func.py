"""
Script for running model and saving initial conditions.
"""
import os
import numpy as np
from scipy.integrate import odeint
import ORdmm_Land as model
import ORdmm_Land_em_coupling as model_coup
import tqdm
#from pathlib import Path

def run_Ordmm(parameters, num_beats=1000, out=None):
    """
    Ordmm_Land model

    Args:
        parameters (ndarray):
        num_beats (int):
        max_t (int):
        out (str): 
    
    Returns:
        y:
        tsteps: 
    """
    # inital states
    y0 = model.init_state_values()
    # time steps
    tsteps = np.arange(0.0, 1000, 0.1)

    # solve ODE
    for i in tqdm.tqdm(range(num_beats)):
        y = odeint(model.rhs, y0, tsteps, args=(parameters,))
        y0 = y[-1]
    
    if out != None:
        # save value to file in specific folder
        # inital_values/...
        if not os.path.isdir("init_values"):
            os.mkdir("init_values")
        
        path = os.path.join("init_values", out)
        np.save(path, y)
    
    return y, tsteps


def run_Ordmm_Land(parameters, num_beats=1000, lam=1, out=None):
    """
    NOT FINISHED
    Ordmm_Land coupled model

    Args:
        parameters (ndarray):
        num_beats (int):
        max_t (int):
        out (str): 
    
    Returns:
        y: 
        tsteps:
    """
    # inital states
    y0 = model_coup.init_state_values(lmbda=lam)
    # time steps
    tsteps = np.arange(0.0, 1000, 0.1)

    # solve ODE
    for i in tqdm.tqdm(range(num_beats)):
        y = odeint(model_coup.rhs, y0, tsteps, args=(parameters,))
        y0 = y[-1]
    
    if out != None:
        # save value to file in specific folder
        # inital_values/...
        if not os.path.isdir("init_values/coupled"):
            os.mkdir("init_values/coupled")
        
        path = os.path.join("init_values/coupled", out)
        np.save(path, y)
    
    return y, tsteps


def get_init_param(hf_type='control', cell_type=0):
    """
    Get control values and HF values for different type of cells and HF models.

    Args:
        cell_type (str):
        hf_type (str):
    
    Returns:
        init_param: initial parameter values
    """
    if hf_type == 'control':
        # control parameters
        init_param = model.init_parameter_values(
            celltype=cell_type
            )
    if hf_type == 'gomez':
        # HF ionic remodelling, Gomez 2014 (table 1)
        init_param = model.init_parameter_values(
            celltype=cell_type,
            GNaL_rate=1.80,
            Gto_rate=0.40,
            GK1_rate=0.68,
            Gncx_rate=1.750,
            Jleak_rate=1.30,
            Jserca_rate=0.5,
            CaMKa_rate=1.50,
            Pnak_rate=0.70,
            Pnab_rate=1,
            Pcab_rate=1,
            thl_rate=1.80,
            Jrel_inf_sensitivity=0.80,
            Jrel_infp_sensitivity=0.80,
            )
    if hf_type == 'gomez_hetero':
        # HF heterogenous transmural ionic remodelling, Gomez 2014 (table 2)
        init_param = model.init_parameter_values(
            celltype=cell_type,
            Gncx_rate=1.60,
            Jserca_rate=0.45,
            )
    
    return init_param


def get_init_param_coupled_iso(hf_type='control', cell_type=0, lam=1):
    """
    NOT FINISHED
    Get control values and HF values for different type of cells and HF models.

    Args:
        cell_type (str):
        hf_type (str):
    
    Returns:
        init_param: initial parameter values
    """
    if hf_type == 'control':
        # control parameters
        init_param = model_coup.init_parameter_values(
            celltype=cell_type,
            isometric=1,
            lmbda_set=lam,
            )
    if hf_type == 'gomez':
        # HF ionic remodelling, Gomez 2014 (table 1)
        init_param = model_coup.init_parameter_values(
            celltype=cell_type,
            isometric=1,
            lmbda_set=lam,
            GNaL_rate=1.80,
            Gto_rate=0.40,
            GK1_rate=0.68,
            Gncx_rate=1.750,
            Jleak_rate=1.30,
            Jserca_rate=0.5,
            CaMKa_rate=1.50,
            Pnak_rate=0.70,
            Pnab_rate=1,
            Pcab_rate=1,
            thl_rate=1.80,
            Jrel_inf_sensitivity=0.80,
            Jrel_infp_sensitivity=0.80,
            )
    if hf_type == 'gomez_hetero':
        # HF heterogenous transmural ionic remodelling, Gomez 2014 (table 2)
        init_param = model_coup.init_parameter_values(
            celltype=cell_type,
            isometric=1,
            lmbda_set=lam,
            Gncx_rate=1.60,
            Jserca_rate=0.45,
            )
    
    return init_param


if __name__ == "__main__":

    #params = get_init_param(hf_type='control', cell_type=0)
    #y, tsteps = run_Ordmm(parameters=params, num_beats=1000, out='control_endo_ordmm.npy')
    
    #params = get_init_param(hf_type='control', cell_type=1)
    #y, tsteps = run_Ordmm(parameters=params, num_beats=1000, out='control_epi_ordmm.npy')

    #params = get_init_param(hf_type='control', cell_type=2)
    #y, tsteps = run_Ordmm(parameters=params, num_beats=1000, out='control_m_ordmm.npy')

    params = get_init_param_coupled_iso(hf_type='control', cell_type=0, lam=0.9)
    y, tsteps = run_Ordmm_Land(parameters=params, num_beats=1000, lam=0.9, out='control_endo_coupled_iso_090.npy')
    
    params = get_init_param_coupled_iso(hf_type='control', cell_type=0, lam=0.95)
    y, tsteps = run_Ordmm_Land(parameters=params, num_beats=1000, lam=0.95, out='control_endo_coupled_iso_095.npy')

    params = get_init_param_coupled_iso(hf_type='control', cell_type=0, lam=1.05)
    y, tsteps = run_Ordmm_Land(parameters=params, num_beats=1000, lam=1.05, out='control_endo_coupled_iso_105.npy')

    params = get_init_param_coupled_iso(hf_type='control', cell_type=0, lam=1.10)
    y, tsteps = run_Ordmm_Land(parameters=params, num_beats=1000, lam=1.10, out='control_endo_coupled_iso_110.npy')


 


