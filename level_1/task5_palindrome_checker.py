def palindrome_checker():
    word=input("Enter word :")
    word=word.lower()
    reverse_word=word[::-1]
    if word==reverse_word:
        print("The given word is Palindrome")
    else:
        print("The given word is not Palindrome")
palindrome_checker()
