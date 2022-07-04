import pandas as pd

data = {"A": [420, 380, 390],
  "B": [50, 40, 45]}

df = pd.DataFrame(data)
df['C'] = df['A']*df['B']


# to get names of each columns
for col in df.columns:
    print(col)
#or
list(df.columns)
#or
list(df.columns.values)


#reset index in pandas
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj', 'Geeku'],
        'Age':[27, 24, 22, 32, 15],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj', 'Noida'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd', '10th'] }

newdf  =  pd.DataFrame(data)
newdf

newdf.reset_index()

#Mapping external values to dataframe values in Pandas 
initial_data = {'First_name': ['Ram', 'Mohan', 'Tina', 'Jeetu', 'Meera'], 
        'Last_name': ['Kumar', 'Sharma', 'Ali', 'Gandhi', 'Kumari'], 
        'Age': [42, 52, 36, 21, 23], 
        'City': ['Mumbai', 'Noida', 'Pune', 'Delhi', 'Bihar']}

df = pd.DataFrame(initial_data)
df

new_data = { "Ram":"B.Com",
             "Mohan":"IAS",
             "Tina":"LLB",
             "Jeetu":"B.Tech",
             "Meera":"MBBS" }

df["Qualification"] = df["First_name"].map(new_data)

#to map changed names
changed_name = { "Ram":"Shyam",
             "Tina":"Riya",
             "Jeetu":"Jitender" }


df=df.replace({"First_name":changed_name})
df

#Construct a DataFrame in Pandas using string data
from io import StringIO

StringData =StringIO("""Date;Event;Cost
    10/2/2011;Music;10000
    11/2/2011;Poetry;12000
    12/2/2011;Theatre;5000
    13/2/2011;Comedy;8000
    """)

df = pd.read_csv(StringData, sep = ";")
df

#Clean the string data in the given Pandas Dataframe

df = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
                   'Product':[' UMbreLla', '  maTress', 'BaDmintoN ', 'Shuttle'],
                   'Updated_Price':[1250, 1450, 1550, 400],
                   'Discount':[10, 8, 15, 10],
                   'Quantity':[2,4,5,1]
                   })

def format_name(df):
    for i in range(df.shape[0]):
        df.iat[i, 1] = df.iat[i,1].strip().capitalize()
    return df

format_name(df)

# or we can use apply 

df['Product'] = df['Product'].apply(lambda x: x.strip().capitalize())
df

df['Quantity'] = df['Quantity'].apply(lambda x: x+1)
df
