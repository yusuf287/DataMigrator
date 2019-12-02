import pandas as pd

def csv(data, param, spark):
    print('Writing CSV...')
    
    path = param['path']
    file_name = param['file_name']
    sep = param['sep']
    header = param['header']
    index = param['index']
    mode = param['mode']
    encoding = param['encoding']
    compression = param['compression']

    data.to_csv(path + file_name, sep=sep, header=header, index=index, mode = mode, encoding=encoding, compression=compression )
    return None

        
def excel(data, param, spark):
    print('Writing EXCEL...')
    
    path = param['path']
    file_name = param['file_name']    
    sheet_name = param['sheet_name']
    index = param['index']
    
    header = param['header']
    encoding = param['encoding']
    
    if (index.lower()=='false'):
        index = False
    else:
        index = True
        
    with pd.ExcelWriter(path + file_name) as xwriter:
        data.to_excel(xwriter, sheet_name=sheet_name, index=index, header=header, encoding=encoding)
    return None

def json(data, param, spark):
    print('Writing JSON...')
    
    path = param['path']
    file_name = param['file_name']
    compression = param['compression']

    data.to_json(path + file_name, compression=compression)
    return None

def pickle(data, param, spark):
    print('Writing PICKLE...')
    
    path = param['path']
    file_name = param['file_name']
    compression= param['compression']
    
    data.to_pickle(path + file_name, compression=compression)
    return None

def parquet(data, param, spark):
    print('Writing PARQUET...')
    
    path = param['path']
    file_name = param['file_name']
    compression = param['compression']

    data.to_parquet(path + file_name, compression=compression)
    return None
