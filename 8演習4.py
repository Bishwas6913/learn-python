seceret_num = str(6)
num = input(str("type the number"))
num = str(num)

#もともとの変数とnputさせる変数の型を同じに指定しないとばぐる。


if num == seceret_num:
    print("corrct")

elif num < seceret_num:
    print("too small")

else:
    print("too big")


