# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 11:21:40 2020

@author: Fub
绘制第四章节的图，包括：

"""
# %%
import numpy as np
import xarray as xr
import matplotlib.pylab as plt

plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.rcParams['axes.unicode_minus']=False   #这两行需要手动设置
# %%
############################
'''
所有物质的辐射强迫的历史序列
'''
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


for rf in RF_list:
    # legend
    ax0.plot([0],[0],color=RF_color[RF_list.index(rf)],
             linestyle=RF_linestyle[RF_list.index(rf)],
             label='$'+RF_label[RF_list.index(rf)]+'$')
    if rf in ['RF_Xhalo']:
        plot_data = np.nanmean(base_Out_hist[rf].sum('spc_halo'),1)
    else:
        plot_data = np.nanmean(base_Out_hist[rf],1)
    ax0.plot(base_Out_hist.year,plot_data,
             color=RF_color[RF_list.index(rf)],
             linestyle=RF_linestyle[RF_list.index(rf)],
             linewidth=3)
ax0.legend(loc='upper left',ncol=3)
ax0.set_xlim([1850,2014])
ax0.set_xlabel('年份')
ax0.set_ylabel('辐射强迫($W/m^2$)')
f.savefig(filepath+filename+fileformat,dpi=300)
# %%
############################
'''
温室气体的辐射强迫与不确定性
'''
filepath = './'
filename = '4.2_RFGHG'
fileformat = '.jpg'
############################
f=plt.figure(figsize=[8,8])

alpha = 0.5

ax0 = plt.subplot2grid((2,2),(0,0),colspan=1)
rf = 'RF_CO2'
data = np.nanmean(base_Out_hist[rf],1)
data_std = np.nanstd(base_Out_hist[rf],1)
ax0.plot(base_Out_hist.year,data,
         color=RF_color[RF_list.index(rf)],
         linestyle=RF_linestyle[RF_list.index(rf)],
         linewidth=3,label='$'+RF_label[RF_list.index(rf)]+'$')
ax0.fill_between(base_Out_hist.year,data-data_std,data+data_std,
                 color=RF_color[RF_list.index(rf)],
                 alpha=alpha,label='1倍标准差')
ax0.legend(loc='upper left')
ax0.set_xlim([1850,2014])
ax0.set_xlabel('年份')
ax0.set_ylabel('辐射强迫($W/m^2$)')
ax0.set_title('a',fontweight='bold')

ax0 = plt.subplot2grid((2,2),(0,1),colspan=1)
rf = 'RF_CH4'
data = np.nanmean(base_Out_hist[rf],1)
data_std = np.nanstd(base_Out_hist[rf],1)
ax0.plot(base_Out_hist.year,data,
         color=RF_color[RF_list.index(rf)],
         linestyle=RF_linestyle[RF_list.index(rf)],
         linewidth=3,label='$'+RF_label[RF_list.index(rf)]+'$')
ax0.fill_between(base_Out_hist.year,data-data_std,data+data_std,
                 color=RF_color[RF_list.index(rf)],
                 alpha=alpha,label='1倍标准差')
ax0.legend(loc='upper left')
ax0.set_xlim([1850,2014])
ax0.set_xlabel('年份')
ax0.set_ylabel('辐射强迫($W/m^2$)')
ax0.set_title('b',fontweight='bold')

ax0 = plt.subplot2grid((2,2),(1,0),colspan=1)
rf = 'RF_N2O'
data = np.nanmean(base_Out_hist[rf],1)
data_std = np.nanstd(base_Out_hist[rf],1)
ax0.plot(base_Out_hist.year,data,
         color=RF_color[RF_list.index(rf)],
         linestyle=RF_linestyle[RF_list.index(rf)],
         linewidth=3,label='$'+RF_label[RF_list.index(rf)]+'$')
ax0.fill_between(base_Out_hist.year,data-data_std,data+data_std,
                 color=RF_color[RF_list.index(rf)],
                 alpha=alpha,label='1倍标准差')
ax0.legend(loc='upper left')
ax0.set_xlim([1850,2014])
ax0.set_xlabel('年份')
ax0.set_ylabel('辐射强迫($W/m^2$)')
ax0.set_title('c',fontweight='bold')

ax0 = plt.subplot2grid((2,2),(1,1),colspan=1)
rf = 'RF_Xhalo'

data = np.nanmean(base_Out_hist[rf].sum('spc_halo'),1)
data_std = np.nanstd(base_Out_hist[rf].sum('spc_halo'),1)
ax0.plot(base_Out_hist.year,data,
         color=RF_color[RF_list.index(rf)],
         linestyle=RF_linestyle[RF_list.index(rf)],
         linewidth=3,label='$'+RF_label[RF_list.index(rf)]+'$')
ax0.fill_between(base_Out_hist.year,data-data_std,data+data_std,
                 color=RF_color[RF_list.index(rf)],
                 alpha=alpha,label='1倍标准差')
ax0.legend(loc='upper left')
ax0.set_xlim([1850,2014])
ax0.set_xlabel('年份')
ax0.set_ylabel('辐射强迫($W/m^2$)')
ax0.set_title('d',fontweight='bold')


f.tight_layout()
f.savefig(filepath+filename+fileformat,dpi=300)

# %%
############################
'''
短生命物质的辐射强迫与不确定性
'''
filepath = './'
filename = '4.3_RFSLCF'
fileformat = '.jpg'
############################
f=plt.figure(figsize=[8,8])

alpha = 0.5

ax0 = plt.subplot2grid((3,3),(0,0),colspan=1)
rf = 'RF_SO4'
data = np.nanmean(base_Out_hist[rf],1)
data_std = np.nanstd(base_Out_hist[rf],1)
ax0.plot(base_Out_hist.year,data,
         color=RF_color[RF_list.index(rf)],
         linestyle=RF_linestyle[RF_list.index(rf)],
         linewidth=3,label='$'+RF_label[RF_list.index(rf)]+'$')
ax0.fill_between(base_Out_hist.year,data-data_std,data+data_std,
                 color=RF_color[RF_list.index(rf)],
                 alpha=alpha,label='1倍标准差')
ax0.legend(loc='lower left')
ax0.set_xlim([1850,2014])
ax0.set_xlabel('年份')
ax0.set_ylabel('辐射强迫($W/m^2$)')
ax0.set_title('a',fontweight='bold')

ax0 = plt.subplot2grid((3,3),(0,1),colspan=1)
rf = 'RF_BC'
data = np.nanmean(base_Out_hist[rf],1)
data_std = np.nanstd(base_Out_hist[rf],1)
ax0.plot(base_Out_hist.year,data,
         color=RF_color[RF_list.index(rf)],
         linestyle=RF_linestyle[RF_list.index(rf)],
         linewidth=3,label='$'+RF_label[RF_list.index(rf)]+'$')
ax0.fill_between(base_Out_hist.year,data-data_std,data+data_std,
                 color=RF_color[RF_list.index(rf)],
                 alpha=alpha,label='1倍标准差')
ax0.legend(loc='upper left')
ax0.set_xlim([1850,2014])
ax0.set_xlabel('年份')
ax0.set_ylabel('辐射强迫($W/m^2$)')
ax0.set_title('b',fontweight='bold')


ax0 = plt.subplot2grid((3,3),(0,2),colspan=1)
rf = 'RF_POA'
data = np.nanmean(base_Out_hist[rf],1)
data_std = np.nanstd(base_Out_hist[rf],1)
ax0.plot(base_Out_hist.year,data,
         color=RF_color[RF_list.index(rf)],
         linestyle=RF_linestyle[RF_list.index(rf)],
         linewidth=3,label='$'+RF_label[RF_list.index(rf)]+'$')
ax0.fill_between(base_Out_hist.year,data-data_std,data+data_std,
                 color=RF_color[RF_list.index(rf)],
                 alpha=alpha,label='1倍标准差')
ax0.legend(loc='lower left')
ax0.set_xlim([1850,2014])
ax0.set_xlabel('年份')
ax0.set_ylabel('辐射强迫($W/m^2$)')
ax0.set_title('c',fontweight='bold')

ax0 = plt.subplot2grid((3,3),(0,2),colspan=1)
rf = 'RF_POA'
data = np.nanmean(base_Out_hist[rf],1)
data_std = np.nanstd(base_Out_hist[rf],1)
ax0.plot(base_Out_hist.year,data,
         color=RF_color[RF_list.index(rf)],
         linestyle=RF_linestyle[RF_list.index(rf)],
         linewidth=3,label='$'+RF_label[RF_list.index(rf)]+'$')
ax0.fill_between(base_Out_hist.year,data-data_std,data+data_std,
                 color=RF_color[RF_list.index(rf)],
                 alpha=alpha,label='1倍标准差')
ax0.legend(loc='lower left')
ax0.set_xlim([1850,2014])
ax0.set_xlabel('年份')
ax0.set_ylabel('辐射强迫($W/m^2$)')
ax0.set_title('d',fontweight='bold')


ax0 = plt.subplot2grid((3,3),(1,0),colspan=1)
rf = 'RF_NO3'
data = np.nanmean(base_Out_hist[rf],1)
data_std = np.nanstd(base_Out_hist[rf],1)
ax0.plot(base_Out_hist.year,data,
         color=RF_color[RF_list.index(rf)],
         linestyle=RF_linestyle[RF_list.index(rf)],
         linewidth=3,label='$'+RF_label[RF_list.index(rf)]+'$')
ax0.fill_between(base_Out_hist.year,data-data_std,data+data_std,
                 color=RF_color[RF_list.index(rf)],
                 alpha=alpha,label='1倍标准差')
ax0.legend(loc='lower left')
ax0.set_xlim([1850,2014])
ax0.set_xlabel('年份')
ax0.set_ylabel('辐射强迫($W/m^2$)')
ax0.set_title('e',fontweight='bold')


ax0 = plt.subplot2grid((3,3),(1,1),colspan=1)
rf = 'RF_SOA'
data = np.nanmean(base_Out_hist[rf],1)
data_std = np.nanstd(base_Out_hist[rf],1)
ax0.plot(base_Out_hist.year,data,
         color=RF_color[RF_list.index(rf)],
         linestyle=RF_linestyle[RF_list.index(rf)],
         linewidth=3,label='$'+RF_label[RF_list.index(rf)]+'$')
ax0.fill_between(base_Out_hist.year,data-data_std,data+data_std,
                 color=RF_color[RF_list.index(rf)],
                 alpha=alpha,label='1倍标准差')
ax0.legend(loc='lower left')
ax0.set_xlim([1850,2014])
ax0.set_xlabel('年份')
ax0.set_ylabel('辐射强迫($W/m^2$)')
ax0.set_title('f',fontweight='bold')


ax0 = plt.subplot2grid((3,3),(1,2),colspan=1)
rf = 'RF_O3t'
data = np.nanmean(base_Out_hist[rf],1)
data_std = np.nanstd(base_Out_hist[rf],1)
ax0.plot(base_Out_hist.year,data,
         color=RF_color[RF_list.index(rf)],
         linestyle=RF_linestyle[RF_list.index(rf)],
         linewidth=3,label='$'+RF_label[RF_list.index(rf)]+'$')
ax0.fill_between(base_Out_hist.year,data-data_std,data+data_std,
                 color=RF_color[RF_list.index(rf)],
                 alpha=alpha,label='1倍标准差')
ax0.legend(loc='upper left')
ax0.set_xlim([1850,2014])
ax0.set_xlabel('年份')
ax0.set_ylabel('辐射强迫($W/m^2$)')
ax0.set_title('g',fontweight='bold')


ax0 = plt.subplot2grid((3,3),(2,0),colspan=1)
rf = 'RF_O3s'
data = np.nanmean(base_Out_hist[rf],1)
data_std = np.nanstd(base_Out_hist[rf],1)
ax0.plot(base_Out_hist.year,data,
         color=RF_color[RF_list.index(rf)],
         linestyle=RF_linestyle[RF_list.index(rf)],
         linewidth=3,label='$'+RF_label[RF_list.index(rf)]+'$')
ax0.fill_between(base_Out_hist.year,data-data_std,data+data_std,
                 color=RF_color[RF_list.index(rf)],
                 alpha=alpha,label='1倍标准差')
ax0.legend(loc='lower left')
ax0.set_xlim([1850,2014])
ax0.set_xlabel('年份')
ax0.set_ylabel('辐射强迫($W/m^2$)')
ax0.set_title('h',fontweight='bold')


f.tight_layout()
f.savefig(filepath+filename+fileformat,dpi=300)

# %%





