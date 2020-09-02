# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 11:21:40 2020

@author: Fub
绘制第四章节的图，包括：

"""
import numpy as np
import xarray as xr
import matplotlib.pylab as plt

plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.rcParams['axes.unicode_minus']=False   #这两行需要手动设置

filepath = './'
filename = '4.1_RF'
fileformat = '.jpg'
############################
RF_list = ['RF_CO2','RF_CH4','RF_N2O']+['RF_H2Os']+\
    ['RF_SO4','RF_BC','RF_POA','RF_NO3','RF_SOA']+\
    ['RF_Xhalo','RF_O3t','RF_O3s']+\
    ['RF_lcc','RF_BCsnow','RF_cloud']
RF_label = ['RF_{CO_2}','RF_{CH_4}','RF_{N_2O}']+['RF_{H_2Os}']+\
    ['RF_{SO_4}','RF_{BC}','RF_{POA}','RF_{NO_3}','RF_{SOA}']+\
    ['RF_{Xhalo}','RF_{O_3t}','RF_{O_3s}']+\
    ['RF_{lcc}','RF_{BCsnow}','RF_{cloud}'] 
RF_color = ['#e91f22','#ef7015','#fecf1a']+['#ef7015']+\
    ['#3abeef','#c80065','#591381','#194d9f','#591381']+\
    ['#f2999b','#7fbf51','#7fbf51']+\
    ['#00682b','#c80065','#0067ff']
RF_linestyle = ['-','-','-']+['--']+\
    ['-','-','-','-','--']+\
    ['-','-','--']+\
    ['-','--','-']
############################

f=plt.figure(figsize=[8,8])
ax0 = plt.subplot2grid((1,1),(0,0),colspan=1)

with xr.open_dataset('../../results/base_Out_hist.nc') as TMP: base_Out_hist = TMP.load()

# ax0.plot([0,1,2],[0,1,0.2])

for rf in RF_list:
    # legend
    ax0.plot([0],[0],color=RF_color[RF_list.index(rf)],
             linestyle=RF_linestyle[RF_list.index(rf)],
             label='$'+RF_label[RF_list.index(rf)]+'$')
    ax0.plot(base_Out_hist.year,np.nanmean(base_Out_hist[rf],1),
             color=RF_color[RF_list.index(rf)],
             linestyle=RF_linestyle[RF_list.index(rf)],
             linewidth=3)
ax0.legend(loc='upper left',ncol=3)
ax0.set_xlim([1850,2014])
ax0.set_xlabel('年份')
ax0.set_ylabel('辐射强迫($W/m^2$)')
f.savefig(filepath+filename+fileformat,dpi=300)