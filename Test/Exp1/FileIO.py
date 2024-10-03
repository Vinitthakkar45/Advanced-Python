while True:
    res = input("If you want to exit enter 'exit' else press Enter: ")
    if res == 'exit':
        break
    print("---Enter the student details---")
    name = input("Enter Name: ")
    roll = input("Enter Roll No.: ")
    div = input("Enter Division: ")
    group = input("Enter Group: ")
    
    with open("./Exp1/student_info.txt", 'a') as dest:
        dest.write(f"Name: {name}\nRoll No.: {roll}\nDivision: {div}\nGroup: {group}\n\n")
