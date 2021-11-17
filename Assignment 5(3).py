def life_stage_of_person():
    Age = int(input("Enter your age: "))
    if Age > -1 and Age <= 12:
        print ("KID")
    elif Age >= 13 and Age <= 17:
        print ("TEEN")
    elif Age == 18:
        print ("DEBUT")
    else:
        print("ADULT")
Stage_of_life = life_stage_of_person()

