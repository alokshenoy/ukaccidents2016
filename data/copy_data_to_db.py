import pandas as pd
from sqlalchemy import create_engine
import os, glob, re

username = 'accidentdata'
password = '2016'
database = 'ukaccidents_2016'

engine = create_engine('postgresql://{0}:{1}@localhost/{2}'.format(username, password, database))
connection = engine.connect()

#os.chdir("/data")
files = [i.split(".")[0] for i in glob.glob('*.csv')]

for file in files:
    data = pd.read_csv("{0}.csv".format(file))
    # There is a column called Engine_Capacity_(CC), which throws an error. 
    # To fix this, we're using str.replace() to get rid of the parentheses.
    data.columns = [column.replace("(","").replace(")","") for column in data.columns]
    print("Uploading {0} to Database".format(file))
    data.to_sql("{0}".format(file), con=connection, index=False, if_exists="replace")


connection.close()




