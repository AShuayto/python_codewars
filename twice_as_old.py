'''

Your function takes two arguments:

current father's age (years)
current age of his son (years)
Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old).

'''

#SAMPLE TEST

Test.describe("Basic Tests")
Test.assert_equals(twice_as_old(36,7) , 22)
Test.assert_equals(twice_as_old(55,30) , 5)
Test.assert_equals(twice_as_old(42,21) , 0)
Test.assert_equals(twice_as_old(22,1) , 20)
Test.assert_equals(twice_as_old(29,0) , 29)


def twice_as_old(dad_years_old, son_years_old):
    if (son_years_old * 2) > (dad_years_old):
        return(son_years_old * 2 - dad_years_old)
    else:
        return(dad_years_old - son_years_old * 2)
    pass