#################### use them in software with style
import os
import shutil
from_dir=input('ENTER THE DIR OF FOLDER TO PROTECT')
fname=input('Enter folder name to create')
pasw=input('Enter the password')

todir='C:/Users/Mustafa/Desktop'
todir=os.path.join(todir,fname)
os.mkdir(todir)

for i in pasw:
    for j in range(1,11):
        path=os.path.join(todir,str(j))
        try:
            os.mkdir(path)
        except:
            print('error1')
        

    todir=todir+'/'+i

try:
    shutil.move(from_dir,todir)
except:
    print()
