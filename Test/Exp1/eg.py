from functools import reduce
# import csv
# dict={'ni':3,"vi":4}

# with open('eg.csv','w',newline='') as f:
#     fieldnames=['Name','marks']
#     writer=csv.DictWriter(f,fieldnames)
#     writer.writeheader()
#     for ni,vi in dict.items():
#         writer.writerow({'Name':ni,'marks':vi})


# a=[1,2,3,4]
# b=[1,2,3,8,8]
# sqlist = map(lambda x,y: x+y, a,b)
# print(list(sqlist))

li=[1,2,3,4,5]
res = reduce(lambda x,y: x + y*y, li,0)
print(res)
