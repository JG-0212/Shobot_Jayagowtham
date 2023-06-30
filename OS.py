import os
cwd=os.getcwd()
nxtd="Dataset"
path = os.path.join(cwd,nxtd)
list_dir =os.listdir()
url_files=[]
for i in list_dir:
    if i[:-8:-1] == "txt.lru" and not os.path.exists(os.path.join(path,i[:-8])):
        url_files.append(i)
for i in url_files:
    os.mkdir(os.path.join(path,i[:-8]))

