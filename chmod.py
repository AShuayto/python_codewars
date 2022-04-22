# Octal output given key value pair.
# Octal Permission:
# Read: 4
# Write: 2
# Execute: 1
# User,Group,Other


def chmod_calculator(perm):
    a = []
    for item in perm:
        a.append((perm.get(item)))
    return(a)



print(chmod_calculator({"user": 'rwx', "group": 'r-x', "other": 'r-x'}))