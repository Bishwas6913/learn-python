#guessing the fruit

print("yes is 1 no is 0)")
small = bool(int(input("is it small? 1 for yes, 0 for no: ")))
green = bool(int(input("is it green? 1 for yes, 0 for no: ")))

if small :
    if green :
        print("it must be green peas")

    else :
        print("it must be cherry")

else :
    if green :
        print("it must be watermelon")

    else :
        print("it must be pumpkin")