"""
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

    Example 1:

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    Example 2:

    Input: nums = [3,2,4], target = 6
    Output: [1,2]
    Example 3:

    Input: nums = [3,3], target = 6
    Output: [0,1]


    Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.
"""

def two_Sum():
    list = []
    j = 1
    dic = {}
    while True:
        if j >= 1:
            j = int(input('Digite valores para que sejam utilizados: '))
            list.append(j)
            print('Para sair digite: "00"')
        else:
            num = int(input('Digite um numero para a soma: '))
            break

    for i in range(len(list)):
        sum = num - list[i]
        if sum in dic:
            print(f'O par para somar {num} é: {list[i]}, {sum}')
        dic[list[i]] = list[i]

two_Sum()



