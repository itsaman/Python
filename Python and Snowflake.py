#Connecting to snowflake by python
import snowflake.connector

crr = snowflake.connector.connect(
    user = '###',
    password='###',
    account = 'vy13440.ap-south-1.aws'
)

cs = crr.cursor()

cs.execute("use database azure_db")
cs.execute("use schema loading")
cs.execute("select * from world_bank")
one_row = cs.fetchone()
print(one_row)

#USING WRITE PANDAS METHOD

import pandas as pd
import snowflake.connector as snow
from snowflake.connector.pandas_tools import write_pandas

#connection
conn = snow.connect(
    user = '###',
    password='###',
    account = 'vy13440.ap-south-1.aws',
    warehouse = 'COMPUTE_WH',
    database = 'AZURE_DB',
    schema = 'LOADING' 
)
cur = conn.cursor()

sql = "select * from world_bank limit 10"
cur.execute(sql)
cur.close()

original = r"C:\Users\anshi\Documents\Python_code\dataset\World_Bank_Projects_new.csv"
delimiter = ','

total = pd.read_csv(original, delimiter)

total.drop(columns = ['envassesmentcategorycode','esrc_ovrl_risk_rate','sector1','sector2','sector3','theme1','theme2'], inplace = True)

total.columns

total.drop(columns =['pdo', 'impagency', 'cons_serv_reqd_ind', 'url',
       'boardapprovaldate', 'closingdate', 'projectfinancialtype',
       'curr_project_cost', 'curr_ibrd_commitment', 'curr_ida_commitment',
       'curr_total_commitment', 'grantamt', 'borrower', 'lendinginstr'], inplace = True)

total.columns = map(lambda x: str(x).upper(), total.columns)

total.rename(columns ={'REGIONNAME':'REGION_NAME',
                        'COUNTRYNAME':'COUNTRY_NAME',
                        'PROJECTSTATUSDISPLAY':'PROJECTSTATUS'
}, inplace = True)

total.head()

write_pandas(conn, total, "SNOWPY")



#ANOTHER WRITE PANDAS

#cursor
cur = conn.cursor()

cur.execute("select * from esg_data")
one_row = cur.fetchone()

#read csv path
path = r'C:\Users\anshi\Documents\Python_code\dataset\archive (2)\ESGData.csv'
delimiter = ','


esg = pd.read_csv(path, delimiter)

#transformation
esg.drop(columns = ['1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968',
       '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977',
       '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986',
       '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
       '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004',
       '2005', '2006', '2007', '2008', '2009','Unnamed: 66'], inplace = True)

esg.columns = map(lambda x: str(x).upper(), esg.columns)

esg.rename(columns ={'COUNTRY NAME':'COUNTRY_NAME',
                      'COUNTRY CODE':'COUNTRY_CODE',
                      'INDICATOR NAME':'INDICATOR_NAME',
                      'INDICATOR CODE':'INDICATOR_CODE',
                      '2010':'YEAR_2010',
                      '2011':'YEAR_2011',
                      '2012':'YEAR_2012',
                      '2013':'YEAR_2013',
                      '2014':'YEAR_2014',
                      '2015':'YEAR_2015',
                      '2016':'YEAR_2016',
                      '2017':'YEAR_2017',
                      '2018':'YEAR_2018',
                      '2019':'YEAR_2019',
                      '2020':'YEAR_2020',
                      '2050':'YEAR_2050'
}, inplace= True)


esg.head()

write_pandas(conn, esg, "ESG_DATA")





