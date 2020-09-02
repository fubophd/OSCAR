# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 08:52:59 2020

@author: Fub

用于生成整个Phd论文模拟的历史初始条件、参数和驱动（Ini_hist, Par, For_hist）

"""
import numpy as np
import xarray as xr

import datetime
from time import perf_counter

from core_fct.fct_loadP import load_all_param
from core_fct.fct_loadD import load_all_hist,load_all_scen
from core_fct.fct_genMC import generate_config, generate_drivers
from core_fct.fct_genD import create_hist_drivers, create_scen_drivers
from core_fct.fct_process import OSCAR

from fb_fct.fct_region import find_larger_region,group_region

print (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

nMC = nMC_hist = nMC_scen = 3000#20  ##模特卡罗模拟次数

model = OSCAR
LCC = 'gross'
inds = (1750, 1750, 2014)
mod_region = 'RCP_5reg'
var_keep = ['D_Eluc', 'D_Focean', 'D_Fland', 'D_Epf'] + [var for var in list(OSCAR._processes.keys()) if 'RF' in var]

alpha = 0.01#0.001
# %%
########################################
#create initial state from historical
########################################
print(model.name + ' loading (historical)')
t0 = perf_counter()

Par0 = load_all_param(mod_region)
Par = generate_config(Par0, nMC=nMC)
For0 = load_all_hist(mod_region, LCC=LCC)

For_hist = generate_drivers(create_hist_drivers(For0, inds=inds), nMC=nMC)
## move parameters from For to Par (normally, Aland_0)
Par = xr.merge([Par, For_hist.drop([VAR for VAR in For_hist if 'year' in For_hist[VAR].dims])])
For_hist = For_hist.drop([VAR for VAR in For_hist if 'year' not in For_hist[VAR].dims])

## create initial steady state
Ini_hist = xr.Dataset()
for VAR in list(model.var_prog):
    if len(model[VAR].core_dims) == 0:
        Ini_hist[VAR] = xr.DataArray(0.)
    elif len(model[VAR].core_dims) == 1:
        Ini_hist[VAR] = [xr.zeros_like(Par[dim], dtype=float) if dim in Par.coords else xr.zeros_like(For_hist[dim], dtype=float) for dim in model[VAR].core_dims][0]
    else: Ini_hist[VAR] = sum([xr.zeros_like(Par[dim], dtype=float) if dim in Par.coords else xr.zeros_like(For_hist[dim], dtype=float) for dim in model[VAR].core_dims])
print('time: {:.0f} seconds'.format(perf_counter() - t0))

Par.to_netcdf('parameters/' + 'hist_' + 'Par.nc', encoding={var:{'zlib':True, 'dtype':np.float32} for var in Par})
For_hist.to_netcdf('parameters/' + 'hist_' + 'For.nc', encoding={var:{'zlib':True, 'dtype':np.float32} for var in For_hist})
Ini_hist.to_netcdf('parameters/' + 'hist_' + 'Ini.nc', encoding={var:{'zlib':True, 'dtype':np.float32} for var in Ini_hist})


print (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# %%
Out_hist = model(Ini_hist, Par, For_hist
    ,var_keep=var_keep)
#with xr.open_dataset('results/SSP_fb_Out_hist.nc') as TMP: Out_hist = TMP.load()
filename = 'base'
Out_hist.to_netcdf('results/'+ filename + '_Out_hist.nc', encoding={var:{'zlib':True, 'dtype':np.float32} for var in Out_hist})