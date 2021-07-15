def check_palindrome(word):
    palindrome = word.lower()
    if palindrome == palindrome[::-1]:
        return True
    else:
        return False

print(check_palindrome('Kajak'))
print(check_palindrome('moc'))
