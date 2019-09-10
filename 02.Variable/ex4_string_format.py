# lower()
msg1 = "HelloWorld!".lower()
print(msg1)

# upper()
msg2 = "HelloWorld!".upper()
print(msg2)

# format()
date = "{}Year, {}Month, {}Day".format(2019, 9, 4)
print(date)

# strip()
msg3 = "H e l l o ~ !"
print(msg3.strip())

# lsplit()
msg4 = "   Hello   "
print(msg4.lstrip())

# rsplit()
print(msg4.rstrip())

# find()
print("ABCDEFG".find("C"))  # 2 (3rd)

# find()
print("ABCDEFG".find("Y")) # not found : -1

# X in XYZ
print("B" in "ABCDEFG")    # True

# split(" ")
msg5 = "Hello World !!!"
print(msg5.split(" "))  # ['Hello', 'World', '!!!']

 