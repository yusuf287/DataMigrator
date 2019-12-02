import pandas as pd


def csv(param, spark):
    print('Reading CSV...')
    
    path= param['path']
    header= param['header']
    encoding= param['encoding']
    sep= param['sep']
    nrows= param['nrows']
    prefix= param['prefix']
    engine= param['engine']

    data=pd.read_csv(path, header=header, encoding=encoding, sep=sep, nrows=nrows, prefix=prefix, engine=engine)
    return data

def excel(param, spark):
    print('Reading EXCEL...')
    
    path=param['path']
    sheet_name= param['sheet_name']
    header= param['header']

    data = pd.read_excel(path, sheet_name=sheet_name, header=header)
    
    return data

def json(param, spark):
    print('Reading JSON...')
    
    path= param['path']
    encoding= param['encoding']
    compression= param['compression']

    data=pd.read_json(path, encoding=encoding, compression=compression)
    return data

def pickle(param, spark):
    print('Reading PICKLE...')
    path= param['path']
    compression= param['compression']

    data= pd.read_pickle(path, compression=compression)
    return data

def parquet(param, spark):
    print('Reading PARQUET...')
    
    path=param['path']
    engine= param['engine']

    data= pd.read_parquet(path, engine=engine)
    return data
