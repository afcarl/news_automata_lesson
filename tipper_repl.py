from tipper import tip, tip2, tip3

# simple example
print('\n~~ simple example ~~\n')
total = tip(100)
print('Your total is {0}'.format(total))


# list example
print('\n~~ list example ~~\n')
bills = [13, 76, 16, 22]

for bill in bills:
    total = tip(bill)
    print('Your total is {0}'.format(total))


# conditionals example
print('\n~~ conditionals example ~~\n')

print( tip2(100) )
print( tip2(-20) )


# dict example
print('\n~~ dict example ~~\n')

bill = {
    'amount': 100,
    'paid': False
}
print( tip3(bill) )
