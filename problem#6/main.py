'''
Name: Ifeoma Ogwu
Lab time: Thursday, 2pm - 3:15pm
'''

def fibonacci(n):
    #write your code here
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

if __name__ == '__main__':
    start_num = int(input())
    result = fibonacci(start_num)
    print(f'fibonacci({start_num}) is {result}')