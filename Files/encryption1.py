from cryptography.fernet import Fernet
file=open("file.txt","rb")
m=file.readline()############ will print the data starting from b
file.close()
print(m)
