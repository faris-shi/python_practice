from functools import reduce
"""
write a function str2float to convert convert a string into a floating point 
number by using reduce. such as '123.45' --> 123.45
"""

def str2float(s):
    signal = 1
    if s.startswith('-'):
        signal = -1
        s = s[1:]
    if '.' not in s:
        return signal * reduce(lambda x, y : int(x) * 10 + int(y), s)
    return signal * (
        reduce(lambda x, y : float(x) * 10 + float(y), s[:s.find('.')]) 
        + 
        0.1 * reduce(lambda x, y : float(x) * 0.1 + float(y), s[:s.find('.'):-1])
    )
    
if __name__ == '__main__':
    assert str2float('123') == 123
    assert str2float('-234') == -234
    assert abs(str2float('123.456') - 123.456) < 0.00001
    assert abs(str2float('-123.456') + 123.456) < 0.00001