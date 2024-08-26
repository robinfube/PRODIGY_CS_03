#Password strength checker


def checker():
    password=input("Enter the password? ")
    score=0
    
    if(password=="exit"):
        exit()
    
    #Check Uppercase and Lowercase
    def caseChecker():
        nonlocal score
        has_upper = False
        has_lower = False
        
        for i in password:
            ascii_value = ord(i)

            if ascii_value>=65 and ascii_value<=90:
                has_upper=True
            elif ascii_value>=97 and ascii_value<=122:
                has_lower=True

        if has_upper and has_lower:
            print("--Password contains both uppercase and lowercase characters--")
            score += 1
            numberChecker()
        else:
            print("--Password should contain both uppercase and lowercase characters--")
    

    #Check for Length
    def length_checker():
        count=0
        nonlocal score
        for i in password:
            count+=1
        
        if count>8 and count<=12 or count>12:
            print("---Length is fantastic---")
            score=score+2
            caseChecker()

        elif count==8:
            print("--Length is OK--")
            score+=1
            caseChecker()
            
        else:
            print("--Password cannot be empty or less than 8 characters--")
            checker()
  


    #Check for numbers 
    def numberChecker():
        nonlocal score
        has_number=False
        for i in password:
            ascii_value=ord(i)
            if ascii_value>=48 and ascii_value<=57:
                has_number=True
        
        if has_number==True:
            print("--Password contains numbers--")
            score+=1
            specialChecker()
        else:
            print("--Password should contain numbers--")
            checker()

    #Check for special characters
    def specialChecker():
        nonlocal score
        has_special=False
        for i in password:
            ascii_value=ord(i)
            if ascii_value>=33 and ascii_value<=47 or ascii_value>=58 and ascii_value<=64 or ascii_value>=91 and ascii_value<=96 or ascii_value>=123 and ascii_value<=126:
                has_special=True
            
        if has_special==True:
            print("--Password contains special characters--")
            score+=1

    length_checker()
    print(f'---Score is {score}---')
   

    #Check for password strength
    if score==5:
        print("Password is very strong")
    elif score==4:
        print("Password is strong")
    elif score==3:
        print("Password is medium")
    elif score==2:
        print("Password is weak")
    else:
        print("Password is too weak or cannot be empty")

if __name__=="__main__":

    checker()
   