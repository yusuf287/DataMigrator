import pandas as pd
from pyspark.sql.types import *

#===========Utility function=====================#
# Auxiliar functions
def equivalent_type(f):
    if f == 'datetime64[ns]': return DateType()
    elif f == 'int64': return LongType()
    elif f == 'int32': return IntegerType()
    elif f == 'float64': return FloatType()
    else: return StringType()

def define_structure(string, format_type):
    try: typo = equivalent_type(format_type)
    except: typo = StringType()
    return StructField(string, typo)

def pandas_to_spark(spark, pandas_df):
    columns = list(pandas_df.columns)
    types = list(pandas_df.dtypes)
    struct_list = []
    for column, typo in zip(columns, types): 
        struct_list.append(define_structure(column, typo))
        p_schema = StructType(struct_list)
    return spark.createDataFrame(pandas_df, p_schema)
#===========Utility function=====================#

def csv(param, spark):
    print('Reading CSV...')
    path= param['path']
    header= param['distributed_header']
    
    if (header.lower()=="true"):
        header = True
    else:
        header = False
        
    inferSchema= param['inferSchema']
    
    if (inferSchema.lower()=="true"):
        inferSchema = True
    else:
        inferSchema = False
        
    mode= param['mode']
  
    data = spark.read.csv(path, header=header, inferSchema = inferSchema, mode=mode)

    return data

def excel(param, spark):
    print('Reading EXCEL...')
    
    path=param['path']
    sheet_name= param['sheet_name']
    header= param['header']

    data = pd.read_excel(path, sheet_name=sheet_name, header=header)
    data = pandas_to_spark(spark, data)
    return data

def json(param, spark):
    print('Reading JSON...')
    path= param['path']
    mode= param['mode']

    data=pd.read_json(path)
    data = pandas_to_spark(spark, data)
    return data

def pickle(param, spark):
    print('Reading PICKLE...')
    path= param['path']

    data= pd.read_pickle(path)
    data = pandas_to_spark(spark, data)
    return data

def parquet(param, spark):
    print('Reading PARQUET...')
    path=param['path']

    data= spark.read.parquet(path)
    return data
