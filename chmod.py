# Octal output given key value pair.
# Octal Permission:
# Read: 4
# Write: 2
# Execute: 1
# User,Group,Other


def chmod_calculator(perm):

    # Variables
    a = []
    user = 0
    group = 0
    other = 0

    # For Loop
    for item in perm:
        a.append((perm.get(item)))
    
    def get_octal(a, b, part):
        for item in a[b]:
            if item == 'r':
                part = part + 4
            elif item == 'w':
                part = part + 2
            elif item == 'x':
                part = part + 1
        return part

    user = (get_octal(a,0,user))
    group = (get_octal(a,1,group))
    other = (get_octal(a,2,other))

    return (str(user) + str(group) + str(other))

            



print(chmod_calculator({"user": 'rwx', "group": 'r-x', "other": 'r--'}))
#chmod_calculator({"user": 'rwx', "group": 'r-x', "other": 'r--'})

print(chmod_calculator({"group": 'rwx'})) #070