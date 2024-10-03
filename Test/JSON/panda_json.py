import json
import os
import pandas as pd
import matplotlib.pyplot as plt

def read_json(file_path):
    all_covid_data = []
    for root, _, files in os.walk(file_path):
        for file in files:
            if file.endswith(".json"):
                with open(os.path.join(root, file)) as f:
                    data = json.load(f)
                    all_covid_data.append(data)
    return all_covid_data

def calculate_cases(all_covid_data):
    all_cases = []
    for data in all_covid_data:
        cases = data.get('cases', {})
        all_cases.append(cases)
    return all_cases

def create_dataframe(all_cases):
    df = pd.DataFrame(all_cases)
    # Convert all columns to numeric, forcing errors to NaN
    df = df.apply(pd.to_numeric, errors='coerce')
    return df

def plot_cases(df):
    if df.empty:
        print("DataFrame is empty. No data to plot.")
        return
    
    # Check if DataFrame contains numeric data
    if df.select_dtypes(include=['number']).empty:
        print("No numeric data to plot.")
        return

    df.plot(kind='bar')
    plt.xlabel('Date')
    plt.ylabel('Cases')
    plt.title('COVID-19 Cases Over Time')
    plt.show()

def main():
    file_path = "JSON/Covid-19.json"  # Adjust this if needed
    all_covid_data = read_json(file_path)
    
    # Print the loaded data to debug
    print("Loaded data:")
    for item in all_covid_data:
        print(item)
    
    all_cases = calculate_cases(all_covid_data)
    
    # Print all_cases to debug
    print("All cases:")
    print(all_cases)
    
    df = create_dataframe(all_cases)
    
    # Print DataFrame content to debug
    print("DataFrame content:")
    print(df.head())
    
    plot_cases(df)

if __name__ == "__main__":
    main()
