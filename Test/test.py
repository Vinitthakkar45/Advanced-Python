# Python code to illustrate read() mode character wise
file = open("output.txt", "r")
# print (file.read())
print (file.read(5))
print (file.readline())
file.close()