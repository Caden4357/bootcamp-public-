#Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
#Example: countdown(5) should return [5,4,3,2,1,0]
def countdown(num):
    my_list = []
    for num in range(num,-1,-1):
        my_list.append(num)
    return my_list
print(countdown(29))
#Create a function that will receive a list with two numbers. Print the first value and return the second.
#Example: print_and_return([1,2]) should print 1 and return 2
def print_and_return(lst):
    print(lst[0])
    return lst[1]
print(print_and_return([1,2]))
#Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
#Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
def sum_first_and_last(lst):
    return lst[0] + len(lst)
print(sum_first_and_last([1,2,3,4,10]))
#Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
#Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
#Example: values_greater_than_second([3]) should return False
def values_greater_than_second(arr):
    new_arr = []
    if len(arr) < 2:
        return False
    for i in range(len(arr)):
        if arr[i] > arr[1]:
            new_arr.append(arr[i])
    print(len(new_arr))
    return new_arr
print(values_greater_than_second([5]))
#Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
#Example: length_and_value(4,7) should return [7,7,7,7]
#Example: length_and_value(6,2) should return [2,2,2,2,2,2]
def size_value(size, value):
    new_list = []
    for val in range(size):
        new_list.append(value)
    return new_list
print(size_value(11,7))

#Another way to write the two functions above:
#Print values greater than second value and return the length of the new list
def values_greater_than_second(lst):
    new_lst= []
    if len(lst) < 2:
        return False
    for i in range(len(lst)):
        if lst[i] > lst[1]:
            new_lst = new_lst + [lst[i]]
    return new_lst
print(values_greater_than_second([5,3,2,4,5,2]))

#Size And Value 
def size_value(size, value):
    new_lst = []
    for i in range(size):
        new_lst = new_lst + [value]
    return new_lst
print(size_value(5,10))

#Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
#Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse_list(list):
    list.reverse()
    return list
print(reverse_list([5,4,3,6,77,5,4,8]))
#another way to reverse a list without functions 

def reverse_list2(lst):
    length = len(lst)-1
    x = length
    for i in range(len(lst)//2):
        lst[i], lst[x-i] = lst[x-i], lst[i]
    return lst
print(reverse_list2([0,1,2,3]))

#Calculate years to days

def years_to_days(age):
    year = 365
    days = 0 
    days = age * year
    return days
print(years_to_days(100))

#Implement function sigma(num) that given a number, returns the sum of all positive integers up to number (inclusive). Ex.:sigma(3)=6(or1 + 2 + 3); sigma(5)=15(or1 + 2 + 3 + 4 + 5).

def sigma(num):
    new_list = []
    total = 0
    for i in range(1,num+1,1):
        new_list.append(i)
    for j in range(len(new_list)):
        total = total + new_list[j]
    return total    
print(sigma(100))

#sorting a list from smallest to greatest

def sorting(lst):
    for j in range(len(lst)-1):
        for i in range(len(lst)-1-j):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst
print(sorting([6,5,7,4,1,3,2]))

#Create threesFives(n) that adds values from 1 and n (inclusive) if that value is not divisible by 3 or 5. Return the final sum.

#For example, threesFives(10) returns 22 as it only returns the sum of 1, 2, 4, 7, and 8. On that example, it skips 3, 6, 9 as those are divisible by 3. It also skips 5, and 10 as it's divisible by 5.

def threeFive(num):
    sum = 0
    new_list = []
    for i in range(1,num+1,1):
        if i % 3 != 0 and i % 5 !=0:
            sum += i
    return sum
print(threeFive(10))



