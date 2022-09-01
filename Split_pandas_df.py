import pandas as pd
import snowflake.connector as snow
from snowflake.connector.pandas_tools import write_pandas

conn = snow.connect(
    user = 'AMAN22JULY',
    password='*****',
    account = '****',
    warehouse = 'COMPUTE_WH',
    database = 'DEMO',
    schema = 'DATA_LOAD' 
)

curr = conn.cursor()

sql = "select C_CUSTKEY from CUSTOMERS"

curr.execute(sql)
df=curr.fetch_pandas_all()

#'C:\Users\Documents\Python_code\dataset\dplit\name'
S = 5000
N = int(len(df)/S)

frames = [df.iloc[i*S:(i+1)*S] for i in range(N+1)]

frames
# batch = []

# for i in range(N+1):
#     batch.append(df.iloc[i*S:(i+1)*S])
#     batch.copy()


for i in range(0,len(frames)):
    tempdf = pd.DataFrame(frames[i])
    if tempdf.empty:
        pass
    else: 
        print("filed copied to the location")  
        tempdf.to_csv(r'C:\Users\Documents\Python_code\dataset\dplit\name_{}.csv'.format(i), index = False, header = None)
   

