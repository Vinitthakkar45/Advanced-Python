# import zipfile

# with zipfile.ZipFile('example.zip','w') as zf:
#     zf.write('data.txt',compress_type=zipfile.ZIP_DEFLATED)
#     zf.write('data1.txt',compress_type=zipfile.ZIP_DEFLATED)
# with zipfile.ZipFile('example.zip','r') as zf:
#     zf.extractall('./example')

# import tarfile

# with tarfile.open('example_tar.tar.gz','w:gz') as zf:
#     zf.add('data.txt')
#     zf.add('data1.txt')
# with tarfile.open('example_tar.tar.gz','r:gz') as zf:
#     zf.extractall('./example_tar')

# import gzip
# import shutil
# with open('data.txt','rb') as f_in:
#     with gzip.open('data.txt.gz','wb') as f_out:
#         shutil.copyfileobj(f_in,f_out)
        
# with gzip.open('data.txt.gz','rb') as f_in:
#     with open('data_gz.txt','wb') as f_out:
#         shutil.copyfileobj(f_in,f_out)
# import shutil
# import os
# os.makedirs('test',exist_ok=True)
# # shutil.rmtree('test')
# print(os.listdir())
# # os.chdir('C:/')
# # print(os.getcwd())

# shutil.move('data.txt','./test')



# from pathlib import Path
# import os

# # path=Path(os.getcwd())
# # # path.mkdir(parents=True,exist_ok=True)

# # for item in path.iterdir():
# #     print(item)
# # path = path / "test"   
# Path('test3.txt').unlink()
# # path.rmdir()

import os

cwd=os.getcwd()

f=[]
d=[]

for item in os.listdir():
    if os.path.isfile(item):
        f.append(item)
    elif os.path.isdir(item):
        d.append(item)
        
print(f)
print(d)