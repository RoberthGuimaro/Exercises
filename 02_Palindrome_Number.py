x = input('Type something to test if it is palindrome: ')

if x == x[::-1]:
    print(f'{x}, is palindrome!')
else:
    print(f'{x}, it is not palindrome!')