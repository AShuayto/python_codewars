# Cat Years
# 15 cat years for first year
# +9 cat years for second year
# +4 cat years for each year after that

# Dog Years
# 15 dog years for first year
# +9 dog years for second year
# +5 dog years for each year after that


def human_years_cat_years_dog_years(human_years):
    i = 3
    cat = 24
    dog = 24


    if human_years == 1:
        cat = 15
        dog = 15
        return([human_years,cat,dog])
    elif human_years == 2:
        cat = 24
        dog = 24
        return([human_years,cat,dog])
    else:
        while i <= human_years:
                cat = cat + 4
                dog = dog + 5
                i += 1
        return([human_years,cat,dog])







print(human_years_cat_years_dog_years(1))
print(human_years_cat_years_dog_years(2))
print(human_years_cat_years_dog_years(10))