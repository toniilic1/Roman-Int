roman_dict = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}

roman_dict_doubles = {
    'IV' : 4,
    'IX' : 9,
    'XL' : 40,
    'XC' : 90,
    'CD' : 400,
    'CM' : 900
}

enter = input('Input a roman number: ').upper()

final = 0
adds = 0
i = len(enter)

while i > 0:

    if enter[:2] not in roman_dict_doubles:
        adds = adds + roman_dict[enter[:1]]
        replacement = 1
    else:
        final = final + roman_dict_doubles[enter[:2]]
        replacement = 2

    enter = enter[replacement::]
    i = len(enter)


print(final+adds)