flag = False


in_roll = input("Enter Roll No.: ")

with open("./Exp1/student_info.txt", 'r') as src:
    while True:
        name_value = src.readline().strip()
        if not name_value:
            break  
        name_value = name_value.split(": ")[1]
        roll_value = src.readline().strip().split(": ")[1]
        div_value = src.readline().strip().split(": ")[1]
        group_value = src.readline().strip().split(": ")[1]
        src.readline()  
        
        if in_roll == roll_value:
            print(f"Name: {name_value}\nDivision: {div_value}\nGroup: {group_value}")
            flag = True
            break
    
if not flag:
    print("Roll No. not found")
