from functools import reduce

li=[2,3,4,5]

sum=reduce(lambda x,y:x+y,li,1)
print(sum)