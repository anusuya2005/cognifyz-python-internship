def email_validator():
    email=input("Enter Email :")
    if "@" in email and "." in email:
        at_index=email.index("@")
        dot_index=email.rindex(".")
        if at_index>0 and dot_index>at_index and dot_index<len(email)-1:
            print("email is in correct format")
        else:
            print("Invalid email format")
    else:
        print("Invalid email format")    
email_validator()
        
                            
