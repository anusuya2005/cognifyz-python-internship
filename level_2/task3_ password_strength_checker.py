def  Password_Strength_Checker():
    password=input("Enter password :")
    password_len=len(password)
    upper_case=False
    lower_case=False
    digit=False
    special_char=False
    length=password_len>=8
    for ch in password:
        if ch.isupper():
            upper_case=True
        if ch.islower():
            lower_case=True
        if ch.isdigit():
            digit=True
        if not ch.isalnum():
            special_char=True
    if (upper_case and lower_case and length and digit and special_char):
        print("the password is strong")
    else:
        print("it was not strong password try another password")
Password_Strength_Checker()


