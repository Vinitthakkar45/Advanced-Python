import csv

input_file = "student_grades.csv"
output_file = "student_average_grades.csv"
student_Roll = {}

with open(input_file, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    
    for row in csvreader:
        name = row['Name']
        math = row['Maths']
        science = row['Science']
        english = row['English']
        
        if math and science and english:
            math = int(math)
            science = int(science)
            english = int(english)
            
            score = math + science + english
            average = score / 3
            
            student_Roll[name] = average
            
        else:
            print(f"Skipping row with missing data: {row}")

with open(output_file, 'w', newline='') as outfile:
    csvwriter = csv.writer(outfile)
    csvwriter.writerow(['Name', 'Average'])
    
    for row in student_Roll:
        csvwriter.writerow([row,round(student_Roll[row],2)])
        