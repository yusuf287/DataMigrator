import pandas as pd
import datetime as dt
import numpy as np
import json as j
# import reader_standalone, writer_standalone, reader_distribute, writer_distribute

from . import reader_standalone, writer_standalone, reader_distribute, writer_distribute

import os

cur_dir = os.path.dirname(os.path.abspath(__file__))
input_json_file = os.path.abspath(os.path.join(cur_dir, "../../../../services/data_migrator/src/config/Input/input_csv.json"))
output_json_file = os.path.abspath(os.path.join(cur_dir, "../../../../services/data_migrator/src/config/Output/output_json.json"))


class DataMigrator:
    
    def __init__(self, spark_session=None):
        """
        Reading requirements
        """
        self.input_type = None
        self.output_type = None
        
        self.input_conf_path = None        
        self.output_conf_path = None
        
        self.distribute = None        
        self.input_data = None              

        self.spark= spark_session
    
    def json_reader(self,path):
        '''
        Input is file path
        returns a dictionary        
        '''
        try:
            with open(path) as file:
                param = j.load(file)
        except Exception as e:
            print("Make sure you have correctly formatted config in  place!!\n", e)
            return None
        return param
    
    def assign_values(self, req_conf):
        
        self.input_type = req_conf['input_type']
        self.output_type = req_conf['output_type']
            
        self.input_conf_path = req_conf['input_conf_path']
        self.output_conf_path = req_conf['output_conf_path']
        
        self.distribute = req_conf['distribute']
        
        return req_conf
        
    def extract_dict_values(self, req_conf):
        if (type(req_conf) == dict):            
            self.assign_values(req_conf)           
            self.req_conf = req_conf
        else:
            req_conf = self.json_reader(req_conf)
            self.req_conf = self.assign_values(req_conf)
        
        return self.req_conf
    
    def execute(self, req_conf):
        print("req_conf: ", req_conf)

        #migration input and output config
        self.extract_dict_values(req_conf)

        print("Reading data initiated...")       
        reader = self.get_reader()
        self.input_data = self.read(reader)
        if (type(self.input_data) == int):
            print("Reading input config failed.")
            return -1
        else:
            print("Reading data from ", (self.input_type).upper(), "source type is successfull!!")

        print("-------------------------------------------------------")
        print("-------------------------------------------------------")
        print("Writing data initiated...")
        writer = self.get_writer()
        output_flag = self.write(writer)

        if (output_flag == -1):
            print("Reading output config failed.")
            return -1
        else:
            print("Writing data to ", (self.output_type).upper(), " source type is successfull!!")

        return None
    
    def get_reader(self):
        
        if self.distribute.lower() == 'true':
            reader = reader_distribute
        else:
            reader = reader_standalone
        
        return reader
    
    def get_writer(self):
        if self.distribute.lower() == 'true':
            writer = writer_distribute
        else:
            writer = writer_standalone
        
        return writer
                

    def read(self, reader):
    
        """
        Read Data according to type defined in requirement config file
        some methods will read one file but other may return a list of input files
        """
 
        input_type = self.input_type
        param = self.json_reader(self.input_conf_path)
        if(param == None):
            return -1
        print("Reading config: ", param)
        print(".")
        print(".")
        print(".") 

        spark= self.spark


        if input_type=='csv':
            """CSV Reader"""
            input_data= reader.csv(param, spark)
        elif input_type== 'excel':
            """Excel Reader"""
            input_data= reader.excel(param,spark)
        elif input_type == 'json':
            """Json Reader"""
            input_data= reader.json(param, spark)
        elif input_type == 'pickle':
            """pickle reader"""
            input_data= reader.pickle(param, spark)
        elif input_type == 'parquet':
            """Apache Parquet"""
            input_data= reader.parquet(param, spark)

        return input_data

    def write(self, writer):

        """
        Writes data to any other file type at given location
        """
        output_type = self.output_type
        param = self.json_reader(self.output_conf_path)

        if(param == None):
            return -1
        print("Writing config: ", param)
        print(".")
        print(".")
        print(".") 
        file = self.input_data

        spark = self.spark

        if output_type == 'csv':
            """CSV Reader"""
            writer.csv(file, param, spark)
        elif output_type == 'excel':
            """Excel Reader"""
            writer.excel(file, param, spark)
        elif output_type == 'json':
            """Json Reader"""
            writer.json(file, param, spark)
        elif output_type == 'pickle':
            """pickle reader"""
            writer.pickle(file, param, spark)
        elif output_type == 'parquet':
            """Apache Parquet"""
            writer.parquet(file, param, spark)

        return None
