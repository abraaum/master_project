"""
Dictonaries with IC50, hill, etc for drug trial on population model. From Llopis-Lorente (2022)
"""

# control, no drug
control = {
    'drug_INa':0, 'IC50_INa':0, 'h_INa':0,
    'drug_IKr':0, 'IC50_IKr':0, 'h_IKr':0,
    'drug_ICaL':0, 'IC50_ICaL':0, 'h_ICaL':0,
    'drug_INaL':0, 'IC50_INaL':0, 'h_INaL':0,
    'drug_IKs':0, 'IC50_IKs':0, 'h_IKs':0,
    'drug_Ito':0, 'IC50_Ito':0, 'h_Ito':0,
    'drug_IK1':0, 'IC50_IK1':0, 'h_IK1':0
    }

# drugs targeting EP
dofetilide = {
    'drug_INa':2, 'IC50_INa':1460000, 'h_INa':5.1,
    'drug_IKr':2, 'IC50_IKr':75, 'h_IKr':1,
    'drug_ICaL':2, 'IC50_ICaL':2300, 'h_ICaL':5.4,
    'drug_INaL':2, 'IC50_INaL':837000, 'h_INaL':4.6,
    'drug_IKs':2, 'IC50_IKs':100000, 'h_IKs':1,
    'drug_Ito':2, 'IC50_Ito':18.8, 'h_Ito':0.8,
    'drug_IK1':0, 'IC50_IK1':0, 'h_IK1':0
    }

verapamil = {
    'drug_INa':81, 'IC50_INa':2480000, 'h_INa':5.1,
    'drug_IKr':81, 'IC50_IKr':452, 'h_IKr':1,
    'drug_ICaL':81, 'IC50_ICaL':202, 'h_ICaL':1.1,
    'drug_INaL':81, 'IC50_INaL':982, 'h_INaL':1.2,
    'drug_IKs':81, 'IC50_IKs':29880, 'h_IKs':0.93,
    'drug_Ito':81, 'IC50_Ito':13429, 'h_Ito':0.8,
    'drug_IK1':81, 'IC50_IK1':3.5e8, 'h_IK1':0.3
    }

quinidine = {
    'drug_INa':3237, 'IC50_INa':14600, 'h_INa':1.22,
    'drug_IKr':3237, 'IC50_IKr':971, 'h_IKr':1,
    'drug_ICaL':3237, 'IC50_ICaL':51592, 'h_ICaL':1,
    'drug_INaL':3237, 'IC50_INaL':2360, 'h_INaL':0.91,
    'drug_IKs':3237, 'IC50_IKs':58665, 'h_IKs':1.17,
    'drug_Ito':3237, 'IC50_Ito':3487, 'h_Ito':1.3,
    'drug_IK1':3237, 'IC50_IK1':4.0e7, 'h_IK1':0.4
    }

drug_dict = {'dofetilide': dofetilide, 'verapamil': verapamil, 'quinidine': quinidine}
