
'''A Binary search is an algorithm which searches a target value in a list of
numbers. We use for loop to iterate through the list and then we print the
True or False if the algorithm finds that number and when it doesnot respectively'''
import random
# data = Put that in a variable`
data = [1,2,3,4,5,6]

target = int(input('Enter the number between 0 to 10 '))
def linear_search(data,target): #Enter the two necessary parameters
    for i in data: #The two brackets denotes two missing function
        if i == target:
            return True
        else:
            return False


print(data)
print(target)
a=linear_search(data,target)
print(a)
