# simple tip calculator.
def tip(bill):
    total = bill * 1.18
    return total


# tipping with conditionals
def tip2(bill):
    if bill < 0:
        print('A negative bill!!!')
        total = 0
    else:
        total = bill * 1.18
    return total


# tipping with dicts
def tip3(bill):
    if not bill['paid']:
        total = bill['amount'] * 1.18
    else:
        total = 0
    return total

