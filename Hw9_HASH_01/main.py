#Name: Alejandra Hernandez
#Date: 11/18/2020
#Desc: code demonstrates the working of MD5 hash accepting bytes and output as bytes.

#https://www.geeksforgeeks.org/md5-hash-python/


import hashlib

# initializing string
str2hash = "GeeksforGeeks"

# encoding GeeksforGeeks using encode()
# then sending to md5()
result = hashlib.md5(str2hash.encode())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of hash is : ", end="")
print(result.hexdigest())