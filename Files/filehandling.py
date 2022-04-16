file=open("plasma_T.txt",'r')
for i in file:
    h=file.readline()
for i in m:
                if i[:6]=="NAME:-":
                   m=use.get()
                   x=m.upper()
                   n=""
                   z=0
                   y=6
                   for g in range(len(i[6:])):
                       if i[y:y+1]==x[z:z+1]:
                          y=y+1
                          z=z+1
                          n=n+i[y-1:y]
                          b=i[6:]
                          sb=b.rstrip()
                          if n==sb:
                              y=0
                              z=5
                              print("yeah")
                              print(i[:6]) 
                              if i[:10]=="PASSWORD:-":
                                  print("in")
                              break
                       else:
                            print("NOT FOUND")
                            break  
   
