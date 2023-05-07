import pandas as pd

# simple example
dataset = {
    'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

mavar = pd.DataFrame(dataset)

print(mavar.loc[0])
 
# read a csv file

mFile = pd.read_csv('addresses.csv')
print(mFile )