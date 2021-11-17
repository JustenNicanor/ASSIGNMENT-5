def Grading():
    print("Type '0' If you are Incomplete, Withdrawn or Dropped")
    grade = float(input("Enter your grade: "))
    if grade > 96.4 and grade <= 100:
       print ("Grade/Mark: 1.0")
       print ("Description: EXCELLENT")
    else:
        if grade > 93.4 and grade <= 96.4:
           print ("Grade/Mark: 1.25")
           print ("Description: EXCELLENT")
        else:
            if grade > 90.4 and grade <= 93.4:
               print ("Grade/Mark: 1.5")
               print ("Description: VERY GOOD")
            else:
                if grade > 87.4 and grade <= 90.4:
                   print ("Grade/Mark: 1.75")
                   print ("Description: VERY GOOD")
                else:
                    if grade > 84.4 and grade <= 87.4:
                       print ("Grade/Mark: 2.0")
                       print ("Description: GOOD")
                    else:
                        if grade > 81.4 and grade <= 84.4:
                           print ("Grade/Mark: 2.25")
                           print ("Description: GOOD")
                        else:
                            if grade > 78.4 and grade <= 81.4:
                               print ("Grade/Mark: 2.50")
                               print ("Description: SATISFACTORY")
                            else:
                                if grade > 75.4 and grade <= 78.4:
                                   print ("Grade/Mark: 2.75")
                                   print ("Description: SATISFACTORY")
                                else:
                                    if grade > 74.4 and grade <= 75.4:
                                       print ("Grade/Mark: 3.0")
                                       print ("Description: PASSING")
                                    else:
                                        if grade <= 74.4 and grade > 64.4:
                                           print ("Grade/Mark: 5.0")
                                           print ("Description: FAILURE")
                                        else:
                                            if grade == 0:
                                                print ("Pls type 'Inc'(Incomplete), 'W' (Withdrawn), and 'D'(dropped) or")
def status_of_grade():
    print ("Type 'ok' in your status if you already have a grade.")
    Status = input("What's your status of grade? ")
    if Status == "Inc":
        print ("Incomplete")
    else:
        if Status == "W":
            print("Withdrawn")
        else:
            if Status == "D":
                print("Dropped")
            else:
                if Status == "ok":
                    print ("Thankyou")


grading = Grading()
grade_status = status_of_grade()


