"""
Dictonaries with IC50, hill, etc for drug trial on population model. From Llopis-Lorente (2022)
"""

# control, no drug
control = {
    'drug_IKr':0, 'IC50_IKr':0, 'h_IKr':0,
    'drug_INa':0, 'IC50_INa':0, 'h_INa':0,
    'drug_INaL':0, 'IC50_INaL':0, 'h_INaL':0,
    'drug_ICaL':0, 'IC50_ICaL':0, 'h_ICaL':0,
    'drug_IKs':0, 'IC50_IKs':0, 'h_IKs':0,
    'drug_IK1':0, 'IC50_IK1':0, 'h_IK1':0,
    'drug_Ito':0, 'IC50_Ito':0, 'h_Ito':0
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

bepridil = {
    'drug_INa':33, 'IC50_INa':2300, 'h_INa':1.26,
    'drug_IKr':33, 'IC50_IKr':149, 'h_IKr':1,
    'drug_ICaL':33, 'IC50_ICaL':1000, 'h_ICaL':1.28,
    'drug_INaL':33, 'IC50_INaL':1814, 'h_INaL':1.4,
    'drug_IKs':33, 'IC50_IKs':6200, 'h_IKs':1,
    'drug_Ito':33, 'IC50_Ito':8594, 'h_Ito':3.5,
    'drug_IK1':0, 'IC50_IK1':0, 'h_IK1':0
    }

sotalol = {
    'drug_INa':14690, 'IC50_INa':7.0e6, 'h_INa':1,
    'drug_IKr':14690, 'IC50_IKr':2.90e5, 'h_IKr':1,
    'drug_ICaL':14690, 'IC50_ICaL':7.1e7, 'h_ICaL':0.9,
    'drug_INaL':14690, 'IC50_INaL':1.3e8, 'h_INaL':5.9,
    'drug_IKs':14690, 'IC50_IKs':1100000, 'h_IKs':1,
    'drug_Ito':14690, 'IC50_Ito':4.30e7, 'h_Ito':0.7,
    'drug_IK1':14690, 'IC50_IK1':3050260, 'h_IK1':1.2
    }

azimilide = {
    'drug_INa':70, 'IC50_INa':18400, 'h_INa':3.8,
    'drug_IKr':70, 'IC50_IKr':380, 'h_IKr':1,
    'drug_ICaL':70, 'IC50_ICaL':7500, 'h_ICaL':1,
    'drug_INaL':70, 'IC50_INaL':3690, 'h_INaL':1.4,
    'drug_IKs':70, 'IC50_IKs':1400, 'h_IKs':1,
    'drug_Ito':0, 'IC50_Ito':0, 'h_Ito':0,
    'drug_IK1':0, 'IC50_IK1':0, 'h_IK1':0
    }

ibutilide = {
    'drug_IKr':140, 'IC50_IKr':11, 'h_IKr':1,
    'drug_INa':140, 'IC50_INa':8020, 'h_INa':0.78,
    'drug_INaL':140, 'IC50_INaL':820, 'h_INaL':0.96,
    'drug_ICaL':140, 'IC50_ICaL':62500, 'h_ICaL':1.16,
    'drug_IKs':0, 'IC50_IKs':0, 'h_IKs':0,
    'drug_IK1':0, 'IC50_IK1':0, 'h_IK1':0,
    'drug_Ito':0, 'IC50_Ito':0, 'h_Ito':0
    }
   
vandetanib = {
    'drug_IKr':110, 'IC50_IKr':394, 'h_IKr':1,
    'drug_INa':110, 'IC50_INa':5840, 'h_INa':3.3,
    'drug_INaL':110, 'IC50_INaL':4210, 'h_INaL':2.2,
    'drug_ICaL':110, 'IC50_ICaL':3360, 'h_ICaL':4.9,
    'drug_IKs':0, 'IC50_IKs':0, 'h_IKs':0,
    'drug_IK1':0, 'IC50_IK1':0, 'h_IK1':0,
    'drug_Ito':0, 'IC50_Ito':0, 'h_Ito':0
    }

disopyramide = {
    'drug_IKr':742, 'IC50_IKr':4.70e3, 'h_IKr':1,
    'drug_INa':742, 'IC50_INa':302300, 'h_INa':1,
    'drug_INaL':742, 'IC50_INaL':20200, 'h_INaL':0.73,
    'drug_ICaL':742, 'IC50_ICaL':1036700, 'h_ICaL':1,
    'drug_IKs':742, 'IC50_IKs':81800, 'h_IKs':1,
    'drug_IK1':0, 'IC50_IK1':0, 'h_IK1':0,
    'drug_Ito':0, 'IC50_Ito':0, 'h_Ito':0
    }

chlorpromazine = {
    'drug_IKr':38, 'IC50_IKr':650, 'h_IKr':1,
    'drug_INa':38, 'IC50_INa':21200, 'h_INa':2.5,
    'drug_INaL':38, 'IC50_INaL':673, 'h_INaL':1.8,
    'drug_ICaL':38, 'IC50_ICaL':6350, 'h_ICaL':2,
    'drug_IKs':38, 'IC50_IKs':10500, 'h_IKs':1,
    'drug_IK1':38, 'IC50_IK1':9270, 'h_IK1':0.7,
    'drug_Ito':38, 'IC50_Ito':1.80e7, 'h_Ito':0.4
    }

cisapride = {
    'drug_IKr':2.6, 'IC50_IKr':72, 'h_IKr':1,
    'drug_INa':2.6, 'IC50_INa':16800, 'h_INa':2.3,
    'drug_INaL':2.6, 'IC50_INaL':421, 'h_INaL':2.2,
    'drug_ICaL':2.6, 'IC50_ICaL':11800, 'h_ICaL':1,
    'drug_IKs':2.6, 'IC50_IKs':6695, 'h_IKs':1,
    'drug_IK1':2.6, 'IC50_IK1':29498, 'h_IK1':0.5,
    'drug_Ito':2.6, 'IC50_Ito':219112, 'h_Ito':0.2
    }

ondansetron = {
    'drug_IKr':139, 'IC50_IKr':1.20e3, 'h_IKr':1,
    'drug_INa':139, 'IC50_INa':19000, 'h_INa':3.7,
    'drug_INaL':139, 'IC50_INaL':6870, 'h_INaL':1.2,
    'drug_ICaL':139, 'IC50_ICaL':22551, 'h_ICaL':0.8,
    'drug_IKs':139, 'IC50_IKs':15000, 'h_IKs':1,
    'drug_IK1':0, 'IC50_IK1':0, 'h_IK1':0,
    'drug_Ito':139, 'IC50_Ito':1023380, 'h_Ito':1
    }

terfenadine = {
    'drug_IKr':9, 'IC50_IKr':129, 'h_IKr':1,
    'drug_INa':9, 'IC50_INa':1950000, 'h_INa':5.3,
    'drug_INaL':9, 'IC50_INaL':98.3, 'h_INaL':1.1,
    'drug_ICaL':9, 'IC50_ICaL':700, 'h_ICaL':0.7,
    'drug_IKs':9, 'IC50_IKs':2000, 'h_IKs':1,
    'drug_IK1':0, 'IC50_IK1':0, 'h_IK1':0,
    'drug_Ito':9, 'IC50_Ito':239961, 'h_Ito':0.3
    }

diltiazem = {
    'drug_IKr':122, 'IC50_IKr':7.9e3, 'h_IKr':1,
    'drug_INa':122, 'IC50_INa':22400, 'h_INa':1.3,
    'drug_INaL':122, 'IC50_INaL':3040, 'h_INaL':1.1,
    'drug_ICaL':122, 'IC50_ICaL':31600, 'h_ICaL':1.2,
    'drug_IKs':122, 'IC50_IKs':63750, 'h_IKs':1,
    'drug_IK1':0, 'IC50_IK1':0, 'h_IK1':0,
    'drug_Ito':122, 'IC50_Ito':2.80e9, 'h_Ito':0.2
    }

mexiletine = {
    'drug_IKr':4129, 'IC50_IKr':5.30e4, 'h_IKr':1,
    'drug_INa':4129, 'IC50_INa':49700, 'h_INa':0.94,
    'drug_INaL':4129, 'IC50_INaL':8957, 'h_INaL':0.99,
    'drug_ICaL':4129, 'IC50_ICaL':38900, 'h_ICaL':1,
    'drug_IKs':0, 'IC50_IKs':0, 'h_IKs':0,
    'drug_IK1':0, 'IC50_IK1':0, 'h_IK1':0,
    'drug_Ito':0, 'IC50_Ito':0, 'h_Ito':0
    }

ranolazine = {
    'drug_IKr':1948.2, 'IC50_IKr':8.30e3, 'h_IKr':1,
    'drug_INa':1948.2, 'IC50_INa':4115, 'h_INa':0.904,
    'drug_INaL':1948.2, 'IC50_INaL':7884, 'h_INaL':0.99,
    'drug_ICaL':1948.2, 'IC50_ICaL':118300, 'h_ICaL':0.89,
    'drug_IKs':1948.2, 'IC50_IKs':345000, 'h_IKs':1,
    'drug_IK1':0, 'IC50_IK1':0, 'h_IK1':0,
    'drug_Ito':0, 'IC50_Ito':0, 'h_Ito':0
    }

astemizole = {
    'drug_IKr':0.26, 'IC50_IKr':19, 'h_IKr':1,
    'drug_INa':0.26, 'IC50_INa':2300, 'h_INa':1,
    'drug_INaL':0.26, 'IC50_INaL':596, 'h_INaL':3.1,
    'drug_ICaL':0.26, 'IC50_ICaL':988, 'h_ICaL':2.53,
    'drug_IKs':0, 'IC50_IKs':0, 'h_IKs':0,
    'drug_IK1':0, 'IC50_IK1':0, 'h_IK1':0,
    'drug_Ito':0, 'IC50_Ito':0, 'h_Ito':0
    }

clarithromycin = {
    'drug_IKr':1206, 'IC50_IKr':1.50e5, 'h_IKr':1,
    'drug_INa':1206, 'IC50_INa':835000, 'h_INa':4,
    'drug_INaL':1206, 'IC50_INaL':173000, 'h_INaL':2.4,
    'drug_ICaL':1206, 'IC50_ICaL':118000, 'h_ICaL':3,
    'drug_IKs':0, 'IC50_IKs':0, 'h_IKs':0,
    'drug_IK1':0, 'IC50_IK1':0, 'h_IK1':0,
    'drug_Ito':0, 'IC50_Ito':0, 'h_Ito':0
    }

clozapine = {
    'drug_IKr':71, 'IC50_IKr':1.50e3, 'h_IKr':1,
    'drug_INa':71, 'IC50_INa':15100, 'h_INa':1.14,
    'drug_INaL':71, 'IC50_INaL':2240, 'h_INaL':1.4,
    'drug_ICaL':71, 'IC50_ICaL':3600, 'h_ICaL':1,
    'drug_IKs':0, 'IC50_IKs':0, 'h_IKs':0,
    'drug_IK1':0, 'IC50_IK1':0, 'h_IK1':0,
    'drug_Ito':0, 'IC50_Ito':0, 'h_Ito':0
    }

domperidone = {
    'drug_IKr':19, 'IC50_IKr':74, 'h_IKr':1,
    'drug_INa':19, 'IC50_INa':5600, 'h_INa':1,
    'drug_INaL':19, 'IC50_INaL':674, 'h_INaL':0.93,
    'drug_ICaL':19, 'IC50_ICaL':16900, 'h_ICaL':2.2,
    'drug_IKs':0, 'IC50_IKs':0, 'h_IKs':0,
    'drug_IK1':0, 'IC50_IK1':0, 'h_IK1':0,
    'drug_Ito':0, 'IC50_Ito':0, 'h_Ito':0
    }

droperidol = {
    'drug_IKr':16, 'IC50_IKr':118, 'h_IKr':1,
    'drug_INa':16, 'IC50_INa':8220, 'h_INa':1.1,
    'drug_INaL':16, 'IC50_INaL':533, 'h_INaL':1,
    'drug_ICaL':16, 'IC50_ICaL':7600, 'h_ICaL':1.16,
    'drug_IKs':0, 'IC50_IKs':0, 'h_IKs':0,
    'drug_IK1':0, 'IC50_IK1':0, 'h_IK1':0,
    'drug_Ito':0, 'IC50_Ito':0, 'h_Ito':0
    }

pimozide = {
    'drug_IKr':0.5, 'IC50_IKr':19, 'h_IKr':1,
    'drug_INa':0.5, 'IC50_INa':4110, 'h_INa':5.5,
    'drug_INaL':0.5, 'IC50_INaL':5030, 'h_INaL':0.59,
    'drug_ICaL':0.5, 'IC50_ICaL':437, 'h_ICaL':2.2,
    'drug_IKs':0.5, 'IC50_IKs':10000, 'h_IKs':1,
    'drug_IK1':0, 'IC50_IK1':0, 'h_IK1':0,
    'drug_Ito':0, 'IC50_Ito':0, 'h_Ito':0
    }

risperidone = {
    'drug_IKr':1.81, 'IC50_IKr':451, 'h_IKr':1,
    'drug_INa':1.81, 'IC50_INa':43400, 'h_INa':0.98,
    'drug_INaL':1.81, 'IC50_INaL':2930, 'h_INaL':2.7,
    'drug_ICaL':1.81, 'IC50_ICaL':34200, 'h_ICaL':0.79,
    'drug_IKs':1.81, 'IC50_IKs':70979, 'h_IKs':1,
    'drug_IK1':0, 'IC50_IK1':0, 'h_IK1':0,
    'drug_Ito':0, 'IC50_Ito':0, 'h_Ito':0
    }

drug_dict = {
    'dofetilide': dofetilide, 
    'verapamil': verapamil, 
    'quinidine': quinidine,
    'bepridil': bepridil,
    'sotalol': sotalol, 
    'azimilide': azimilide,
    'ibutilide': ibutilide,
    'vandetanib': vandetanib,
    'disopyramide': disopyramide,
    'chlorpromazine': chlorpromazine,
    'cisapride': cisapride,
    'ondansetron': ondansetron,
    'terfenadine': terfenadine,
    'diltiazem': diltiazem,
    'mexiletine': mexiletine,
    'ranolazine': ranolazine,
    'astemizole': astemizole,
    'clozapine': clozapine,
    'domperidone': domperidone}
