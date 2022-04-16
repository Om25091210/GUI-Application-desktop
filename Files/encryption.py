from cryptography.fernet import Fernet
key=Fernet.generate_key()          ###############     generate a random key each time its called
print(key)
file=open("file.txt",'wb')
file.write(key) ####### the key is type bytes ,,,,,write the data after b===
file.close()
