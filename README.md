# Master project

Master project description

### Installation and dependencies

To install the dependencies:
```
python -m pip install -r requirements.txt
```

### Python

Changes implemented from original code:

**Ordmm_Land.py**:
- Added scaling for the maximum conductance, meaning all Gs where s is the ion. Variable name in the code for each ion s is Gs_rate.
- Added celltypes (used Matlab code for reference). In the code, celltype=0 is endo, 1 is epi, and 2 is m.
- 

**Ordmm_Land_em_coupling.py**:
- Added scaling for the maximum conductance, meaning all Gs where s is the ion. Variable name in the code for each ion s is Gs_rate.
- 


### MatLab

No files have been changed from the original code.

### Gotran

Convert the gotran model to python:
```
python -m gotran gotran2py ORdmm_Land_em_coupling.ode
```

No files have been changed from the original code.