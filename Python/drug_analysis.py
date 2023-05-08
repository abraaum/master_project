"""
Analysis of all drug biomarkers.
"""

import ORdmm_Land_em_coupling as model
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import tqdm
import sys
import seaborn as sns
import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

from joypy import joyplot


drug_h = [
        "dofetilide",
        "quinidine",
        "bepridil",
        "sotalol",
        "azimilide",
        "ibutilide",
        "vandetanib",
        "disopyramide",
    ]
drug_i = [
    "chlorpromazine",
    "cisapride",
    "ondansetron",
    "terfenadine",
    "astemizole",
    "clozapine",
    "domperidone",
    "droperidol",
    "pimozide",
    "risperidone",
]
drug_n = [
    "verapamil",
    "diltiazem",
    "mexiletine",
    "ranolazine",
    "loratadine",
    "metoprolol",
    "nifedipine",
    "nitrendipine",
    "tamoxifen",
    "clarithromycin",
]
drugs = [
    'azimilide',
    'bepridil',
    'disopyramide',
    'dofetilide',
    'ibutilide',
    'quinidine',
    'sotalol',
    'vandetanib',
    'astemizole',
    'chlorpromazine',
    'cisapride',
    'clozapine',
    'domperidone',
    'droperidol',
    'ondansetron',
    'pimozide',
    'risperidone',
    'terfenadine',
    'clarithromycin',
    'diltiazem',
    'loratadine',
    'metoprolol',
    'mexiletine',
    'nifedipine',
    'nitrendipine',
    'ranolazine',
    'tamoxifen',
    'verapamil'
    ]

drugs_val = [
    'azimilide',
    'disopyramide',
    'ibutilide',
    'vandetanib',
    'astemizole',
    'clozapine',
    'domperidone',
    'droperidol',
    'pimozide',
    'risperidone',
    'clarithromycin',
    'loratadine',
    'metoprolol',
    'nifedipine',
    'nitrendipine',
    'tamoxifen',
    ]

drugs_train = [
    'bepridil',
    'dofetilide',
    'quinidine',
    'sotalol',
    'chlorpromazine',
    'cisapride',
    'ondansetron',
    'terfenadine',
    'clarithromycin',
    'diltiazem',
    'mexiletine',
    'ranolazine',
    'verapamil'
    ]

def box_plot_biomarker(biomarker, mech_type, hf_type):
    """Get boxplot of selected biomarker for drugs in same risk category.
    """

    data_frames = []

    for drug in drugs:

        df = pd.read_csv(f'drug/df_drug_{drug}_{mech_type}_{hf_type}.csv')
        data_frames.append(df)

    
    result = pd.concat(data_frames)
    

    #palette = sns.color_palette('RdYlGn')
    plt.figure(figsize=(12,8))
    ax = sns.boxplot(data=result, x=biomarker, y='drug_type', hue='risk', palette='RdYlBu', dodge=False)
    ax.set_title(f'{biomarker} boxplot for population ({mech_type}, {hf_type})', fontsize='x-large')
    #ax.axvline(x = 180, ymin = 0, ymax = 1)
    #ax.axvline(x = 440, ymin = 0, ymax = 1)
    #plt.show()

    plt.savefig(f'plots/drug_boxplots/boxplot_{mech_type}_{hf_type}_{biomarker}.png')


def bar_plot_biomarkers(biomarker, mech_type, hf_type):
    data_frames = []

    for drug in drugs:

        df = pd.read_csv(f'drug/df_drug_{drug}_{mech_type}_{hf_type}.csv')
        data_frames.append(df)

    
    result = pd.concat(data_frames)

    ax = sns.countplot(data=result, y='drug_type', hue='EAD')

    plt.show()


def scatter_plot(mech_type, hf_type):

    data_frames = []

    for drug in drugs:

        df = pd.read_csv(f'drug/df_drug_{drug}_{mech_type}_{hf_type}.csv')
        data_frames.append(df)

    
    result = pd.concat(data_frames)

    df = result[[
            'APD_90',
            'CaTD_80',
            'RT90',
            #'RT50',
            #'TTP',
            #'Ta_max', 
            #'CaTA',
            #'DevF',
            'qNet',
            'risk']]

    df.iloc[:,0:-1] = df.iloc[:,0:-1].apply(lambda x: (x-x.mean())/ x.std(), axis=0)

    #ax = sns.scatterplot(data=result, x=biomarker1, y=biomarker2, hue='risk')

    ax = sns.pairplot(
        data=df,
        hue='risk',
        plot_kws={"s": 2}
        )

    plt.show()
    #plt.savefig(f'plots/pairplot_{mech_type}_{hf_type}.png')


def test_simple_classification():
    
    train = []
    test = []

    for drug in drugs_val:
        df = pd.read_csv(f'drug/df_drug_{drug}_{mech_type}_{hf_type}.csv')
        test.append(df)
    
    for drug in drugs_train:
        df = pd.read_csv(f'drug/df_drug_{drug}_{mech_type}_{hf_type}.csv')
        train.append(df)
    
    df_train = pd.concat(train)
    df_test = pd.concat(test)

    X_train = df_train[['APD_30',
        'APD_40',
        'APD_50',
        'APD_90',
        'Tri90_30',
        'Tri90_40',
        'Tri90_50',
        'CaTD_50',
        'CaTD_80',
        'CaTD_90',
        'RT50',
        'RT90',
        'TTP', 
        'Ta_min', 
        'Ta_max', 
        'dvdt_max', 
        'RMP', 
        'V_peak', 
        'diast_Ca', 
        'syst_Ca',
        'CaTA',
        'DevF',
        'qNet']]
    y_train = df_train['risk']
    X_test = df_test[['APD_30',
        'APD_40',
        'APD_50',
        'APD_90',
        'Tri90_30',
        'Tri90_40',
        'Tri90_50',
        'CaTD_50',
        'CaTD_80',
        'CaTD_90',
        'RT50',
        'RT90',
        'TTP', 
        'Ta_min', 
        'Ta_max', 
        'dvdt_max', 
        'RMP', 
        'V_peak', 
        'diast_Ca', 
        'syst_Ca',
        'CaTA',
        'DevF',
        'qNet']]
    y_test = df_test['risk']

    cls = SVC().fit(X_train, y_train)

    accuracy_train = accuracy_score(y_train, cls.predict(X_train))
    accuracy_test = accuracy_score(y_test, cls.predict(X_test))
    print('\nTrain Accuracy:{: .2f}%'.format(accuracy_train*100))
    print('Test Accuracy:{: .2f}%'.format(accuracy_test*100))

    

def test_ridgeline(mech_type, hf_type, biomarker, drugs):
    dfs = []
    baseline_df = pd.read_csv(f'drug/df_drug_baseline_{mech_type}_{hf_type}.csv')
    dfs.append(baseline_df)

    for d in drugs:
        drug_df = pd.read_csv(f'drug/df_drug_{d}_{mech_type}_{hf_type}.csv')
        dfs.append(drug_df)
    
    df_huge = pd.concat(dfs)

    joyplot(
        df_huge, 
        by='drug_type',
        column=biomarker, 
        colormap=sns.color_palette("Reds", as_cmap=True) if 'drug_type' in drug_h else sns.color_palette("crest", as_cmap=True))
    plt.xlabel(f'{biomarker}')
    plt.title("Ridgeline Plot, multiple groups")

    plt.show()






if __name__ == "__main__":

    mech_type = 'dyn'
    hf_type = 'gomez'
    all_bio = [
        'APD_30',
        'APD_40',
        'APD_50',
        'APD_90',
        'Tri90_30',
        'Tri90_40',
        'Tri90_50',
        'CaTD_50',
        'CaTD_80',
        'CaTD_90',
        'RT50',
        'RT90',
        'TTP', 
        'Ta_min', 
        'Ta_max', 
        'dvdt_max', 
        'RMP', 
        'V_peak', 
        'diast_Ca', 
        'syst_Ca',
        'CaTA',
        'DevF',
        'qNet'

    ]

    #scatter_plot(mech_type='dyn', hf_type='control')


    #for b in all_bio:
    #    box_plot_biomarker(biomarker=b, mech_type=mech_type, hf_type=hf_type)

    #bar_plot_biomarkers('EAD', 'iso', 'gomez')

    #test_simple_classification()

    bio = [
    #'APD_90',
    #'Tri90_30',
    #'CaTD_80',
    'RT50',
    #'CaTA',
    #'DevF',
    #'qNet'
    ]

    for b in bio:
        test_ridgeline(mech_type='iso', hf_type='control', biomarker=b,  drugs=drugs)
