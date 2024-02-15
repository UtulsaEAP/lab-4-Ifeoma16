'''
Name: Ifeoma Ogwu
Lab time: Thursday, 2pm - 3:15pm
'''

def feet_to_steps(user_feet):
   #write your code here
    steps = int(user_feet/2.5)
    return(steps)

if __name__ == '__main__':
    #take input feet steps here
    #store it into the function
    feet = float(input())
    #print your steps here
    print(feet_to_steps(feet))