import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
	if file == "Encrypt.py" or file == "Key.key" or file == "Decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)
print(files)

with open("Key.key", "rb") as key:
	newkey = key.read()


for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_decrypted = Fernet(newkey).decrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_decrypted)


