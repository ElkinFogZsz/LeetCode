"""
小美有两个数字，其中第一个数字是任意的正整数，第二个数字是一位仅可能为0到9间的整数。

小美希望能将第二个插入第一个数字中，以得到最大的数字。具体可参见输入输出样例。
"""


def maxValue():
    data = read_multi_line()
    sumarry = []
    for i in range(len(data)):
        first_num = data[i][0]
        second_num = data[i][1]
        result = str(first_num)
        temp = ''
        flag = True
        for single_num in result:
            if int(single_num) <= second_num and flag:
                temp += str(second_num)
                temp += str(single_num)
                flag = False
            else:
                temp += str(single_num)
        if len(temp) != len(result) + 1:
            temp += str(second_num)
        print(temp)


def read_multi_line():
    n = int(input().strip())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().strip().split())))
    return arr


if __name__ == '__main__':
    maxValue()
