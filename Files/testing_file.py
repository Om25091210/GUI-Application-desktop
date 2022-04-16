import os

fol='C:/Users/Mustafa/Desktop'
todir=os.path.join(fol,'bank management') ######## join one or more path compoonents intelligently ,concatenation of path
m=os.path.basename(todir)########## returns folder or fiile name
n=os.path.abspath(todir)########### returns folder name in standard form
b=os.path.dirname(todir)########### returns directory except folder name
c=os.path.exists(todir)############# returns true if file or folder exists
r=os.path.lexists(todir)########### returns true if path refers to an existing path
p=os.path.expanduser(todir)########33 returns the path
w=os.path.expandvars(todir)######### same as above
q=os.path.getatime(todir) ########### returns the time of last access of path.returns floating seconds and exception if not exist
a=os.path.getmtime(todir) ######### time of last modification
z=os.path.getsize(todir) ########## returns the size, in bytes of path
d=os.path.isfile(todir) ########## returns if it is path
l=os.path.isdir(todir) ######### returns true if path is an existing directory
y=os.path.normpath(todir) ###### normalize the path removing extra slases
o=os.path.samefile(todir,'C:/Users/Mustafa/Desktop/bank management') #Returns true if both file path is same
t=os.path.split(todir) ######### returns tuple containing directory head and tail. 

print(os.getcwd())
