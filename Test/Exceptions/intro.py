# class AgeNotValid(Exception):
#     def __init__(self, age):
#         self.age=age
#     def __str__(self):
#         return f"Invalid Age : {self.age} "
    
# def checkAge(age):
#     if(not(age>=20 and age<=30 )):
#         raise AgeNotValid(age)
    
# if __name__=="__main__":
#     try:
#         date=int(input("Enter your DOB year: "))
#         checkAge(2024-date)
#     except AgeNotValid as e:
#         print(f"Error Occured \n{e}")
from datetime import datetime    
date="2027-05-31"
date_obj=datetime.strptime(date, "%Y-%m-%d")
print(date_obj)