def is_palindrome_1(n):
    return str(n) == str(n)[::-1]

def is_palindrome(n):
    s = str(n)
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True

if __name__ == '__main__':
    print(list(filter(lambda x: is_palindrome_1(x), range(100))))
    print(list(filter(lambda x: is_palindrome(x), range(1000))))