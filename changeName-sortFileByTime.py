#!/usr/bin/env python
# coding: utf-8

# In[7]:


import os
from functools import cmp_to_key

filePath="C:\\Users\\20441\\Desktop\\fin_data"

if not os.path.exists(filePath):
    print("目录不存在")
#st_mtime:最后一次修改文件的时间   写文件的时候会改变
#st_ctime:最后一次修改文件权限的时间
#st_atime：time of last access
     #最后一次访问时间，如果使用read函数读某个文件，会改变文件的这个时间
def compare(x, y):
    stat_x = os.stat(filePath + "\\" + x)
    stat_y = os.stat(filePath + "\\" + y)
    if stat_x.st_mtime < stat_y.st_mtime:
        return -1
    elif stat_x.st_mtime > stat_y.st_mtime:
        return 1
    else:
        return 0

filenames = os.listdir(filePath)
filenames.sort(key=cmp_to_key(compare))
i=1
for file in filenames:
    print(file)
    newpath="C:\\Users\\20441\\Desktop\\fin_list_data"
    origin_name="Oriana_Export_"
    os.rename(filePath+"\\"+file,newpath+"\\"+origin_name+str(i)+".xlsx")
    i=i+1
    print(i)


# In[ ]:





# In[ ]:





# In[ ]:




