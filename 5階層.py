m=int(input("請輸入階層值:"))
num=i=1
while True:
  num*=i
  if num>m:
    break
  i+=1
print("超過M為",m,"最小階層數為:",i)