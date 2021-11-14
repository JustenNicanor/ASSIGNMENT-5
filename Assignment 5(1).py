grade = float(input("Enter your grade: "))
if grade > 96.4 and grade <= 100:
    print (1.0)
    print ("EXCELLENT")
else:
    if grade > 93.4 and grade <= 96:
        print (1.25)
        print ("EXCELLENT")
    else:
        if grade > 90.4 and grade <= 93:
            print (1.5)
            print ("VERY GOOD")
        else:
            if grade > 87.4 and grade <= 90:
                print (1.75)
                print ("VERY GOOD")
            else:
                if grade > 84.4 and grade <= 87:
                    print (2.0)
                    print ("GOOD")
                else:
                    if grade > 81.4 and grade <= 84:
                        print (2.25)
                        print ("GOOD")
                    else:
                        if grade > 78.4 and grade <= 81:
                            print (2.50)
                            print ("SATISFACTORY")
                        else:
                            if grade > 75.4 and grade <= 78:
                                print (2.75)
                                print ("SATISFACTORY")
                            else:
                                if grade > 74.4:
                                    print (3.0)
                                    print ("PASSING")
                                else:
                                    if grade > 64.4 and grade < 75:
                                        print (5.0)
                                        print ("FAILURE")
                                    else:
                                        if grade <=64:
                                            print ("Inc / W / D")
                                            print ("INCOMPLETE / WITHDRAWN / DROPPED")






