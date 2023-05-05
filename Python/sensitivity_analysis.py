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
#lamval = [0.9, 0.95, 1, 1.05, 1.1]  #0.9, 0.95,
#lamfile = ["100", "105", "110"] # "090", "095",


def adp(V, percentage, index=False):
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

def catd(Cai, percentage=0.8, index=False):
    # extract Ca_i
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


def tad(Ta, percentage=0.5, index=False):
    # extract Ta
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



def sensitivity_df(hf_type, mech_type, param):
    
    all_values = np.load(f'sens/sens_{mech_type}_{hf_type}_endo_{param}.npy', allow_pickle=True)

    V = all_values.item().get("V")
    Cai = all_values.item().get("Cai")
    Ta = all_values.item().get("Ta")
    CaTrpn = all_values.item().get("CaTrpn")

    d = []

    if mech_type=='iso':
        lamval = [0.9, 0.95, 1, 1.05, 1.1]
    else: 
        lamval = [1, 1.05, 1.1]

    for l in range(len(lamval)):
        for i in range(len(inc)):
            if inc[i] in [0.80, 1.00, 1.20]:
                max_V = max(V[l][i])
                max_Cai = max(Cai[l][i])
                max_Ta = max(Ta[l][i])
                max_CaTrpn = max(CaTrpn[l][i])

                min_V = min(V[l][i])
                min_Cai = min(Cai[l][i])
                min_Ta = min(Ta[l][i])
                min_CaTrpn = min(CaTrpn[l][i])

                max_V_t = np.argmax(V[l][i]) / 10
                max_Cai_t = np.argmax(Cai[l][i]) / 10
                max_Ta_t = np.argmax(Ta[l][i]) / 10
                max_CaTrpn_t = np.argmax(CaTrpn[l][i]) / 10


                ADP40 = adp(V[l][i], 0.4)
                ADP90 = adp(V[l][i], 0.9)
                CATD30 = catd(Cai[l][i], 0.3)
                CATD90 = catd(Cai[l][i], 0.9)
                TAD50 = catd(Ta[l][i], 0.5)
                TAD90 = catd(Ta[l][i], 0.9)

                data = {
                    "hf": hf_type,
                    "mech": mech_type,
                    "parameter": param,
                    "inc": inc[i],
                    "lambda": lamval[l],
                    "max V": max_V,
                    "max Cai": max_Cai,
                    "max Ta": max_Ta,
                    "max CaTrpn": max_CaTrpn,
                    "TT max V": max_V_t,
                    "TT max Cai": max_Cai_t,
                    "TT max Ta": max_Ta_t,
                    "TT max CaTrpn": max_CaTrpn_t,
                    "min V": min_V,
                    "min Cai": min_Cai,
                    "min Ta": min_Ta,
                    "min CaTrpn": min_CaTrpn,
                    "ADP40": ADP40,
                    "ADP90": ADP90,
                    "CATD30": CATD30,
                    "CATD90": CATD90,
                    "TAD50": TAD50,
                    "TAD90": TAD90,
                    }
                
                d.append(data)
        
    df = pd.DataFrame(data=d)

    return df

def conc_all_df(hf_type, mech_type):
    params = [
        'ku', 'kuw', 'kws', 'ktrpn', 'Trpn50', 'gammaw', 
        'gammas', 'rs', 'rw', 'Tref', 'cat50ref', 'ntm'
        ] 

    all_frames = []

    for p in params:
        df = sensitivity_df(
            hf_type=hf_type, 
            mech_type=mech_type, 
            param=p)
        
        all_frames.append(df)

    result = pd.concat(all_frames)

    result.to_csv(f'sens/df_sens_{mech_type}_{hf_type}.csv')

    print(result.head(20))


def blabla(mech_type, hf_type):

    df = pd.read_csv(f'sens/df_sens_{mech_type}_{hf_type}.csv')

    if mech_type=='iso':
        lamval = [0.9, 0.95, 1, 1.05, 1.1]
    else: 
        lamval = [1, 1.05, 1.1]

    params = [
        'ku', 'kuw', 'kws', 'ktrpn', 'Trpn50', 'gammaw', 
        'gammas', 'rs', 'rw', 'Tref', 'cat50ref', 'ntm'
        ] 

    for l in lamval:
        for p in params:
             new_df = df[((df['inc'] == 1.00) & (df['lambda'] == l))]
             print(new_df.head())

            
if __name__ == "__main__":
    type_hf = ['gomez', 'control']
    mech_type = ['iso','dyn']

    #blabla(mech_type='iso', hf_type='control')

    df = pd.read_csv(f'sens/df_sens_iso_gomez.csv')

    print(df[['max V', 'max Cai', 'max Ta', 'max CaTrpn', 'TT max V', 'TT max Cai', 'TT max Ta', 'TT max CaTrpn']].describe())


