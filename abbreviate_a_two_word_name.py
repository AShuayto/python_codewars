'''

Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot seperating them.

It should look like this:

Sam Harris => S.H

Patrick Feeney => P.F

'''

def abbrevName(name):
    return (".".join(k[0] for k in name.split()).upper())
    

# You can use Test.describe and Test.it to write BDD style test groupings
Test.assert_equals(abbrevName("Sam Harris"), "S.H");
Test.assert_equals(abbrevName("Patrick Feenan"), "P.F");
Test.assert_equals(abbrevName("Evan Cole"), "E.C");
Test.assert_equals(abbrevName("P Favuzzi"), "P.F");
Test.assert_equals(abbrevName("David Mendieta"), "D.M");