import pandas as pd

data={
    'Name':['Jai','Prince','Gaurav','Anuj'],
    'Age':[27,24,22,32],
    'Qualification':['Msc','MA','MCA','phd']
}

myval = pd.DataFrame(data)

print(myval)