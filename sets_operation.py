"""
practice the operations of two sets
"""

# assume we have two teams of players who play baseball or basketball.
baseball = {"Jodi", "Carmen", "Aida", "Alicia"}

basketball = {"Eva", "Carmen", "Alicia", "Sarah"}


#intersection
#Display players that play both baseball and basketball
print(baseball & basketball)


#combination
#Display players that play either baseball or basketball
print(baseball | basketball)

#difference
#Display players that play baseball, but not basketball
print(baseball - basketball)

#difference
# Display players that play basketball, but not baseball
print(basketball - baseball)


# Display players that play one sport, but not both
print(basketball ^ baseball)