source_file="X.txt"
destination_file="Y.txt"

with open(source_file, 'r') as src:
    content = src.read()
with open(destination_file, 'w') as dest:
    dest.write(content)
    
print(f"Content copied from {source_file} to {destination_file} successfully.")