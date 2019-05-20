'''
inspo: https://www.reddit.com/r/cscareerquestions/comments/bojrrb/hiring_managers_what_projects_stood_out_in_a_bad/enhmnu6/?utm_source=share&utm_medium=web2x
This all came from a post from reddit user GhostBond. All funny comments below
are theirs. The code is mine.

A lot of this could be improved. I've only been working in Python for 6 months.
If you see something that could be improved please let me know.

Thanks to u/GhostBond for the idea! This was fun practice. :)
'''

'''
O(1) Optimization Sort: Delete the whole list, an empty list is sorted list.
'''
def optimizationSort(arr):
    arr =  ''
    return arr

'''
O(-1) Sort: Fuck off, I'm not sorting your list.
'''
def qminus1Sort(arr):
    return "Fuck Off! I'm not sorting your list"

'''
StalinSort: You iterate down the list of elements checking if they're in order.
An element which is out of order is eliminated.
At the end you have a sorted list.
(this one took awhile to figure out! -ns)
'''
def stalinSort(arr):
    arr2 = []
    max = ''
    if len(arr) <= 1:
        return arr
    try:
        for i in range(0,len(arr),1):
            if i == 0:
                max = arr[i]
                arr2.append(arr[i])
            else:
                if (arr[i] > arr[i-1]) and (arr[i] > max):
                    max = arr[i]
                    arr2.append(arr[i])
    except IndexError:
        if arr[i] > arr[i-1]:
            arr2.append(arr[i])
    return arr2

'''
GenghisKhanSort: delete all elements except for the first,
repopulate the list with successors of the first element.
'''
def gengkhiskhanSort(arr):
    gk = ''
    for i in range(0,len(arr)):
        gk = arr[0]
        for j in range(0,len(arr)):
            arr[i] = gk
    return arr
#
# list1 = [0,-2,-4,-3,-1,-2,-23,1,4,2,4,5,4124,4,6]
# print(gengkhiskhanSort(list1))

'''
HitlerSort: pick the value that you like,
declare it as the highest, and then delete all other values.
'''
def hitlerSort(arr):
    value=input("Which value do you like the most? ")
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            arr[i] = value
    print('Excellent choice, ma\'am')
    return arr

'''
AmishSort: Turn off computer, then you won't even need sorting.
'''
# def amishSort(arr):
#     import os
#     os.system("shutdown /s /t 1")
# amishSort(list1)
# COMMENTED OUT TO AVOID DISASTER!

'''
Communist Sort: Wait for the list to sort itself.
Act upset when it doesn't happen until a tyrannical dictatorship shows up
and forces the list into sorted order.
'''
def communistSort(arr):
    import time
    value = input("Is the vanguard ready? (y/n)")
    if value == 'n':
        time.sleep(2)
        communistSort(arr)
    elif value == 'y':
        print('Comrades, it is time!')
        for i in range(len(arr)):
            min = i
            for j in range(i + 1, len(arr)):
                if arr[min] > arr[j]:
                    min = j
            arr[i],arr[min] = arr[min], arr[i]
    else:
        print("I'm sorry I didn't hear you.")
        communistSort(arr)
    return arr


'''
Capitalist Sort: The first 3 elements in the list remain in their position,
every iteration through they subtract 1 from all of the other elements and add it to themselves,
until the rest of the list is destroyed and they are the only ones left.
'''
# def capitalistSort(arr)

'''
Thanos Sort: Randomly delete half the elements in the list over
and over until the list happens to be sorted.
'''
def thanosSort(arr):
    import random
    random.shuffle(arr)
    snap = len(arr)//2
    return arr[snap:]

# print(thanosSort(list1))

'''
trumpSort O(0): the array is always sorted.
Anyone who says otherwise is fake news.
'''
def trumpSort(arr):
    print(arr)
    value = print("The list is now sorted. It\'s so lucky for you that I was here to help. I've been such a bigly help.")
    return arr

# trumpSort(list1)

'''
LiberalSort: each element is declared to be out of order for moral reasons
and committing moral crimes, elements have 1 subtracted from them at semi-random.
The sort never actually ends as the narrative needs to keep going to maintain political power.
'''

def liberalSort(arr):
    from random import randrange,randint
    import random
    counter = 0
    rand = random.randint(1,101)
    print(rand)
    while counter <= rand:
        for i in range(0,randrange(len(arr)+1)):
            arr[i] -= 1
            counter += 1
    return arr

# print(liberalSort(list1))

'''
Republican Sort: Look at the first 5 elements.
Choose the highest one no matter how much lower that is than
other elements in the list past that.
Declare that the new top value, the list never gets sorted
because it would upset the newly declared top element.
'''

def republicanSort(arr):
    counter = 0
    max = 0
    list2= []
    while counter <= 5:
        for i in range(0,len(arr)):
            list2 += arr[i]
            counter += 1
    return list2


list1 = [1,4,6,2,7,10,1,243]
print(republicanSort(list1))
