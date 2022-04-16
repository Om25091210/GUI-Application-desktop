k=open("C:\\Users\\MUSTAFA\\Desktop\\plasma_st.txt",'r')
m=k.readlines()
for i in m:
    if i[:6]=="NAME:-":
       if i[6:7]=="O":
          if i[7:8]=="M":
              if i[8:9]==" ":
                  print("ok")
          
