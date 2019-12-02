import os

import findspark
findspark.init()
from pyspark.sql import SparkSession

from .methods.migrator import DataMigrator

import os


def executeMigration(inputs = {}):
    # TODO
    # Send below path from the front-end

    input_type = inputs["input_type"]
    output_type = inputs["output_type"]

    cur_dir = os.path.dirname(os.path.abspath(__file__))
    # inputs['input_conf_path'] = os.path.abspath(os.path.join(cur_dir, "../../../services/data_migrator/src/config/Input/input_csv.json"))
    inputs['input_conf_path'] = os.path.abspath(os.path.join(cur_dir, "../../../services/data_migrator/src/config/Input/input_"+input_type+".json"))
    inputs['output_conf_path'] = os.path.abspath(os.path.join(cur_dir, "../../../services/data_migrator/src/config/Output/output_"+output_type+".json"))

    if (inputs['distribute'].lower()== 'true'):
    	spark = SparkSession.builder.appName("DataMigrator").getOrCreate()
    else:
    	spark = None


    dataMigrator = DataMigrator(spark)
    dataMigrator.execute(inputs)

    print("Mission is Successfull...Congratulations!!" )

    #  logic code goes here

    output = {"Input Type": inputs['input_type'].upper(), \
    		  "Output Type": inputs['output_type'].upper(), \
    		  "Message": "Data Migrated." , "Output folder" : inputs['output_conf_path'], "Status": "Success"}
    return output
	


if __name__ == "__main__":

	pass