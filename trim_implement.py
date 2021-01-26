# implement strip() to remove the white spaces in the head and tail of a string.

def strip(s):
    while len(s) != 0 and (s[0] == ' ' or s[-1] == ' '):
        s = s[1:] if s[0] == ' ' else s
        s = s[:-1] if s[-1] == ' ' else s
    return s


if __name__ == "__main__":
    if strip('hello  ') != 'hello':
        print('fail!')
    elif strip('  hello') != 'hello':
        print('fail!')
    elif strip('  hello  ') != 'hello':
        print('fail!')
    elif strip('  hello  world  ') != 'hello  world':
        print('fail!')
    elif strip('') != '':
        print('fail!')
    elif strip('    ') != '':
        print('fail!')
    else:
        print('success!')
