def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

string1 = "4257304920394478392772938744930294037524"
string2 = "2704702208931031198668911301398022074072"
string3 = "0974101607733149676776769413377061014790"
string4 = "7798338247658278460338648728567428338977"

print("Is string1 a palindrome?", palindrome(string1))
print("Is string2 a palindrome?", palindrome(string2))
print("Is string3 a palindrome?", palindrome(string3))
print("Is string4 a palindrome?", palindrome(string4))