'''
Name: Ifeoma Ogwu
Lab time: Thursday, 2pm - 3:15pm
'''

def int_to_reverse_binary(num1):
    binary_val = ''

    while num1 > 0:
        remainder = num1 % 2
        binary_val += str(remainder)
        num1 = num1 // 2

    return binary_val

def string_reverse(input_string):
    reverse_input = ''

    for char in input_string[::-1]:
        reverse_input += char

    return reverse_input

if __name__ == '__main__':
    user_input = int(input())
    
    binary_string = int_to_reverse_binary(user_input)
    reversed_binary_string = string_reverse(binary_string)
    
    print(reversed_binary_string)