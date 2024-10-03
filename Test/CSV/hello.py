f = open("a.txt", 'w') 
line = 'Welcome to python.mykvs.in\nRegularly visit python.mykvs.in'  
f.write(line) 
f.close()  
f = open("a.txt", 'rb+')  
print(f.tell())  
print(f.read(7)) # read seven characters  
print(f.tell())  
print(f.read())  
print(f.tell())  
f.seek(13,0) # moves to 9 position from begining 
print(f.read(5))  
f.seek(1, 1) # moves to 4 position from current location 
print(f.read(5))  
f.seek(-8, 2) # Go to the 5th byte before the end 
print(f.read(5))  
f.close() 