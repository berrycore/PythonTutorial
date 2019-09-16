chars = []
data = input("Input data : ")

for i in range(len(data)):
    chars.append(data[i:i+1])

print(chars)