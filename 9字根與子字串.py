a=list(input("輸入S1為:"))
a=set(a)
b=list(input("輸入S2為:"))
b=set(b)
if a.intersection(b) == a:
    print("YES")
else:
    print("NO")
    
