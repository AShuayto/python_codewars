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

    if perm.get("user"):
        for item in list(perm.get('user')):
            if item == 'r':
                user = user + 4
            if item == 'w':
                user = user + 2
            if item == 'x':
                user = user + 1

    if perm.get("group"):
        for item in list(perm.get('group')):
            if item == 'r':
                group = group + 4
            if item == 'w':
                group = group + 2
            if item == 'x':
                group = group + 1
    if perm.get("other"):
        for item in list(perm.get('other')):
            if item == 'r':
                other = other + 4
            if item == 'w':
                other = other + 2
            if item == 'x':
                other = other + 1

    return str(user) + str(group) + str(other)

            



print(chmod_calculator({"user": 'rwx', "group": 'r-x', "other": 'r--'}))
#chmod_calculator({"user": 'rwx', "group": 'r-x', "other": 'r--'})
#print(chmod_calculator({"group": 'rwx'})) #070


# BEST PRACTICE
def chmod_calculator1(perm):
    perms = { "r": 4, "w": 2, "x": 1 }
    value = ""
    for permission in ["user", "group", "other"]:
        value += str(sum(perms.get(x, 0) for x in perm.get(permission, "")))
        
    return value