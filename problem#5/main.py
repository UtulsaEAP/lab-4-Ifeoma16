'''
Name: Ifeoma Ogwu
Lab time: Thursday, 2pm - 3:15pm
'''

def swap_values(user_val1, user_val2, user_val3, user_val4):   
   #write your code here
   user_val1, user_val2, user_val3, user_val4 = user_val2, user_val1, user_val4, user_val3
   return user_val1, user_val2, user_val3, user_val4

if __name__ == '__main__':   
   user_input1 = int(input())
   user_input2 = int(input())
   user_input3 = int(input())
   user_input4 = int(input())
   #store output for every input here
   #print those output
   swapped_values = swap_values(user_input1, user_input2, user_input3, user_input4)
   print(" ".join(map(str, swapped_values)))

 