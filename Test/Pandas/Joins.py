import pandas as pd

df1=pd.DataFrame({'ID':[1,2,3],'Name':["Ankit","Anshul","Ankur"]})
df2=pd.DataFrame({'ID':[1,3,4],'Age':[5,7,8]})

print(pd.merge(df1,df2,on='ID',how='outer'))