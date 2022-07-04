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
