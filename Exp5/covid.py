import json
import os

country_stats = {}

def calculate_country_stats(item):
    confirmed_cases=0
    deaths=0
    recovered=0
    active_cases=0
    for data in item:
        print(data)
        country = data['country']
        confirmed_cases += data['confirmed_cases']['total']+data['confirmed_cases']['new']
        deaths += data['deaths']
        recovered += data['recovered']
        active_cases += confirmed_cases - deaths - recovered
    
    return {
        'country': country,
        'total_confirmed_cases': confirmed_cases,
        'total_deaths': deaths,
        'total_recovered': recovered,
        'total_active_cases': active_cases
    }


for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith('.json'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                data = json.load(f)
                
                stats = calculate_country_stats(data)
                country = stats['country']
                
                if country not in country_stats:
                    country_stats[country] = stats
                else:
                    country_stats[country]['total_confirmed_cases'] += stats['total_confirmed_cases']
                    country_stats[country]['total_deaths'] += stats['total_deaths']
                    country_stats[country]['total_recovered'] += stats['total_recovered']
                    country_stats[country]['total_active_cases'] += stats['total_active_cases']

summary_report = []

for country, stats in country_stats.items():
    summary_report.append(stats)

top_5_highest = sorted(summary_report, key=lambda x: x['total_confirmed_cases'], reverse=True)[:5]
top_5_lowest = sorted(summary_report, key=lambda x: x['total_confirmed_cases'])[:5]

summary_json = {
    'summary': summary_report,
    'top_5_highest': top_5_highest,
    'top_5_lowest': top_5_lowest
}

with open("covid19_summary.json", 'w') as f:
    json.dump(summary_json, f, indent=4)

print("Summary report saved to covid19_summary.json")
