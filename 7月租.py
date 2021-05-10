mon=int(input("輸入月租類型:"))
mint=int(input("通話秒數:"))
if mon == 186:
    if mint *0.09  <= 186:
        print("通話費為",round(mint*0.09*0.9))
    else:
        print("通話費為",round(mint*0.09*0.8))
elif mon == 386:
    if mint *0.08  <= 386:
        print("通話費為",round(mint*0.08*0.8))
    else:
        print("通話費為",round(mint*0.08*0.7))
elif mon == 586:
    if mint *0.07  <= 586:
        print("通話費為",round(mint*0.07*0.7))
    else:
        print("通話費為",round(mint*0.07*0.6))
elif mon == 986:
    if mint *0.06 <= 986:
        print("通話費為",round(mint*0.06*0.6))
    else:
        print("通話費為",round(mint*0.07*0.5))
else:
    print("錯誤")