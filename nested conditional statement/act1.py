medical_cause=input("did you have a medical cause y or n: ")

if medical_cause == 'y': 
    print("you are allowed")
else:
    atten =int(input("enter the attendence of the student: "))
    if atten>=75:
        print("allowed")
    
    else:
        print("not allowed")