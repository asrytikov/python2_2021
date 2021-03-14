a=int(input())

sum=0
pr=1

while (a>0):
    dig = a % 10
    if dig !=0:
        sum += dig
        pr *= dig
    a = a // 10

print("Summa =", sum)
print ("Proiz = ", pr)
