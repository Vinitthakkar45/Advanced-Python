import pandas as pd

def calculate_average(*args):
    return [sum(scores) / len(scores) for scores in zip(*args)]
	
input_files = ['student_grades.csv']
    
df=pd.concat([pd.read_csv(file) for file in input_files])
calculate_average(df['Maths'], df['Science'], df['English'])
df['Total'] = df['Maths'] + df['Science'] + df['English']
df['Average'] = df['Total'] / 3

df.to_csv('summaryPandas.csv', index=False)