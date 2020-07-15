from decimal import Decimal

def is_digit(item):
    digit = False

    for i in range(len(item)):
        for n in range(48, 57 + 1):
            if chr(n) == item[i] or item[i] == '.':
                digit = True
        if digit == False:
            return False
        digit = False
    return True

def is_gender(item):
    item = str(item)

    if len(item) == 0:
        return True
    if len(item) == 1 and (item.capitalize() == 'M' or item.capitalize() == 'F'):
        return True
    return False

def is_empty(item):
    if str(item) == "":
        return True
    else:
        return False

def is_contain_between(item, minimum, maximum):
    if is_digit(str(minimum)) and is_digit(str(maximum)) and is_digit(str(item)):
        if int(Decimal(item)) >= int(Decimal(minimum)) and int(Decimal(item)) <= int(Decimal(maximum)):
            return True
        else:
            return False
    else:
        return False

def is_macro(item):
    case = ["0", "0.5", "1", "", "0.0", "1.0"]

    if (str(item) in case):
        return True
    return False
