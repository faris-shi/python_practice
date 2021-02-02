"""
The operator.itemgetter() function takes as arguments the lookup indices used to extract the desired 
values from the records in rows. It can be a dictionary key name, a numeric list element, 
or any value that can be fed to an object’s __getitem__() method.

The functionality of itemgetter() is sometimes replaced by lambda expressions. 
However,  the solution involving itemgetter() typically runs a bit faster
"""
from operator import itemgetter

rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1002},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]


print(sorted(rows, key=itemgetter('uid', 'fname')))


"""
The operator.attrgetter() taks as arguments that some objects did not support comparison operation.
"""

from operator import attrgetter

class User:

    def __init__(self, user_id):
        self.user_id = user_id
    
    def __repr__(self):
        return f'User({self.user_id})'

users = [User(2), User(1), User(3)]
print(sorted(users, key=attrgetter('user_id')))