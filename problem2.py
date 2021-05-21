# Write a function that checks if a given word is a palindrome. Character case should be ignored.


def is_palindrome(word):
    if not isinstance(word, str):
        print('Required string input')
        return False
    if not word:
        return True
    word = word.lower()
    return word == word[::-1]


# if __name__ == '__main__':
#     print(is_palindrome("Test"))
#     print(is_palindrome("abcba"))
#     print(is_palindrome("aBcba"))
#     print(is_palindrome("aBcbA"))
