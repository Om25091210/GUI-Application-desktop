s=input("ENTER YOUR PASSWORD")
st=input("CONFIRM UR PASSWORD")
u=""
for i in s:
    if i=="@" or i=="#" or i=="$" or i=="%" or i=="&" or i=="/" or i=="\\" or i.isdigit()==True or i.isalpha()==True:
       u=u+i 
if s==st:
    print("PROCEED")
else:
    print("PASSWORD DOSEN'T MATCH")

