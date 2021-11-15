def Lowest_of_three():
    First_num = int(input("First number: "))
    Second_num = int(input("Second number: "))
    Third_num = int(input("Third number: "))
    if First_num < Second_num and First_num < Third_num:
        print(First_num)
    else:
        if Second_num < First_num and Second_num < Third_num:
            print(Second_num)
        else:
            if Third_num < First_num and Third_num < Second_num:
                print (Third_num)
Lowestof3 = Lowest_of_three()
