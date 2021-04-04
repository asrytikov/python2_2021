import os

f = open('example.txt', 'w+')
f.write("lololo")
f.close()

f = open('example.txt', 'r+')
print(*f)
f.close()

p = os.getcwd()

print(os.path.exists(p+'\example.txt'))


print(os.listdir('C:\\Users'))