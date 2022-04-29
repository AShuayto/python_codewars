
NATO = {'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 
        'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray', 'Y': 'Yankee', 'Z': 'Zulu'}

def to_nato(words):
    final_list=[]
    a = [char for char in words.replace(" ", "")]
    print(a)
    for letter in a:
        if letter.isalpha():
            letter = letter.upper()
            final_list.append((NATO.get(letter)))
        else:
            final_list.append(letter)
    return " ".join(final_list)


print(to_nato("If you can! read"))




def to_nato2(words):
    words = words.replace(' ','').upper()
    return ' '.join([db[i] if i in db else i for i in list(words)])