def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)
a = int(input("輸入"))
b = int(input("輸入"))
print("最大公因數", gcd(a,b))
