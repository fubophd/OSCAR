def find_larger_region(region):
    '''
    Find the lager reion index of input region index.
    
    Input:
    ------
    region (int)       The region index (14 samll region)

    Output:
    -------
    (int)              The larger reion index (5 big region)
    '''
    if region in [0]:
        return 0  
    elif region in [1,6,7,8]:
        return 1
    elif region in [2,9]:
        return 2
    elif region in [3]:
        return 3
    elif region in [4,10,11,12,13,14]:
        return 4
    elif region in [5,15]:
        return 5
    else:
        print('Error imput')
        return -1

def group_region(For_hist,For_hist_reg14):
    '''
    Find the lager reion index of input region index.
    
    Input:
    ------
    For_hist (xr.DataSet)             The For Dataset (in 5 samll regions)
    For_hist_reg14 (xr.DataSet)       The For Dataset (in 14 samll regions)

    Output:
    -------
    (xr.DataSet)              The grouped For Dataset (in 5 regions)
    '''
    for VAR in For_hist:
        print(VAR)
        if 'reg_land' not in For_hist[VAR].dims:
            continue
        For_hist[VAR].values[:] =0
        for region in For_hist_reg14.reg_land.values[:]:
            For_hist[VAR].isel(reg_land=find_larger_region(region)).values[:] += For_hist_reg14[VAR].isel(reg_land=region).values[:] 
    return For_hist
