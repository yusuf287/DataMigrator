import pandas as pd

def csv(file, param, spark):

    path = param['path']
    file_name = param['file_name']
    coalesce_num = param['coalesce_num']
    header = param['header']
        
    if (header.lower()=="true"):
        header = True
    else:
        header = False
        
    inferSchema= param['inferSchema']
    
    if (inferSchema.lower()=="true"):
        inferSchema = True
    else:
        inferSchema = False
        
    file.coalesce(coalesce_num).write.option("inferSchema",inferSchema).csv(path + file_name, header = header)
    return None

def excel(file,param, spark):

    path = param['path']
    file_name = param['file_name']
    sheet_name = param['sheet_name']
    
    with pd.ExcelWriter(path + file_name) as xwriter:
        file.toPandas().to_excel(xwriter, sheet_name=sheet_name)
    return None

def json(file, param, spark):

    path = param['path']
    file_name = param['file_name']
    coalesce_num = param['coalesce_num']
    
    file.coalesce(coalesce_num).write.format('json').save(path + file_name)
    
    return None

def pickle(file, param, spark):

    path = param['path']
    file_name = param['file_name']

  
    file.rdd.saveAsPickleFile(path + file_name)
    return None

def parquet(file, param, spark):

    path = param['path']
    file_name = param['file_name']
    compression_type = param['compression']

    file.write.parquet(path + file_name, mode='overwrite', compression=compression_type)
#     file.to_parquet(path + file_name, compression=compression_type)
    return None
