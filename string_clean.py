def string_clean(s):
    """
    Function will return the cleaned string
    """
    final_list = []
    for item in s:
        if item.isdigit():
            pass
        else:
            final_list.append(item)
    return ''.join(final_list)


print(string_clean("This looks5 grea8t!"))




# BEST PRACTICE
def string_clean1(s):
    return ''.join(x for x in s if not x.isdigit())