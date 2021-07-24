def check_palindrome(string):
    """Check if given text is palindrome.

    :param str text: some text
    :rtype: bool
    :return: True if given text is palindrome False elsewhere
    """
    palindrome = ''.join(string).lower()
    if palindrome == palindrome[::-1]:
        return True
    else:
        return False

if __name__ == '__main__':
    print(check_palindrome('Kayak'))
    print(check_palindrome('cacao'))
    print(check_palindrome('Final fantasy'))
