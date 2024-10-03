import json

data={
    "name":"John",
    "age":30,
    "city":"New York"
}

file_path="output.json"
with open(file_path,"w") as file:
    json.dump(data,file,indent=1)