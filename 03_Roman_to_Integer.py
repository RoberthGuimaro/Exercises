"""
    I = 1
    IV = 4
    V = 5
    IX = 9
    X = 10
    XL = 40
    L = 50
    XC = 90
    C = 100
    CD = 400
    D = 500
    CM = 900
    M = 1000
"""

# Function to convert interger to Roman Values

def convert_Interger_to_Roman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

    roman = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'DM', 'M']

    i = 12

    while number:
        division = number // num[i]
        number %= num[i]

        while division:
            print(roman[i], end = '')
            division -= 1
        i -= 1

#Driver code

if __name__ == '__main__':
    number = 3333
    print('Roman values is: ', end = '')
    convert_Interger_to_Roman(number)
