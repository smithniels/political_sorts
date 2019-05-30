'''
inspo: https://www.reddit.com/r/cscareerquestions/comments/bojrrb/hiring_managers_what_projects_stood_out_in_a_bad/enhmnu6/?utm_source=share&utm_medium=web2x
This all came from a post from reddit user GhostBond. Most funny comments below
are theirs. The code is mine.

I'm sure this code could be improved, so if you see something that could be improved please let me know!

Someone on Reddit mentioned doing list comprehensions for some of those For loops, but I'm not sure how to assign
local variables within those comprehensions. I believe it involves a "nested generator expression" according to someone on
stack overflow, but I haven't looked into it yet. (TODO:)

Thanks to u/GhostBond for the idea! This was fun practice. :)
'''

list1 = [1,2,3,4,6,5,20,30,40,50,400,2,5,1,2,50,520,124,512,5134,10000]

'''
O(1) Optimization Sort:
Delete the whole list, an empty list is sorted list.
'''
def optimizationSort(arr):
    arr =  ''
    return arr

'''
O(-1) Sort:
Fuck off, I'm not sorting your list.
'''
def ominus1Sort(arr):
    return "Fuck Off! I'm not sorting your list"

'''
StalinSort:
You iterate down the list of elements checking if they're in order.
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
GenghisKhanSort:
Delete all elements except for the first,
repopulate the list with successors of the first element.
'''
def gengkhiskhanSort(arr):
    gk = ''
    for i in range(0,len(arr)):
        gk = arr[0]
        for j in range(0,len(arr)):
            arr[i] = gk
    return arr

'''
HitlerSort:
Pick the value that you like,
declare it as the highest,
and then delete all other values.
'''
def hitlerSort(arr):
    value=input("Which value do you like the most? ")
    list2 = []
    for i in range(0,len(arr)):
        i = value
        list2.append(i)
    print('Excellent choice, ma\'am')
    result = print(list2)
    return result

'''
AmishSort:
Turn off computer, then you won't even need sorting.
'''
# def amishSort(arr):
#     import os
#     os.system("shutdown /s /t 1")
# amishSort(list1)
# COMMENTED OUT TO AVOID DISASTER!

'''
Communist Sort:
Wait for the list to sort itself.
Act upset when it doesn't happen until a tyrannical dictatorship shows up
and forces the list into sorted order.
'''
def communistSort(arr):
    import time
    value = input("Is the vanguard ready? (y/n) ")
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
    result = print(arr)
    return result

'''
Capitalist Sort:
The first 3 elements in the list remain in their position,
every iteration through they subtract 1 from all of the other elements and add it to themselves,
until the rest of the list is destroyed and they are the only ones left.


TODO: I need to switch this, so it isn't adding all of the plebs and repeatedly putting them into titans. 
    at the moment if plebs is 100 and titans is [1,2,3] titans wi2ll become [101,102,103]. 
    it should be closer to [35,35,37] (34+1,33+2,33+3]
'''
def capitalistSort(arr):
    titans = []
    plebs  = []
    sum = 0
    for i in range(0,3):
        titans.append(arr[i])
    print("Titans:",titans)
    for i in range(3,(len(arr))):
        plebs.append(arr[i])
        arr[i] -= 1
    print("Plebs: ",plebs)
    for i in range(0,len(plebs)):
        while plebs[i] > 0:
            plebs[i] -= 1
            sum += 1
    sum2 = sum
    for j in range(0,len(titans)):
        titans[j] += sum2
    final = titans + plebs
    print(" This is fair: \n",final)

'''
Thanos Sort: Randomly delete half the elements in the list over
and over until the list happens to be sorted.
# TODO: snap then check if order
        if that's false ^ "snap"
'''
def thanosSort(arr):
    from random import shuffle
    print('Thanos Sort:')
    print('List: ',arr)
    def order(arr):
        if sorted(arr) == arr:
            print(arr,"It is done. ")
        else:
            print(arr, " This isn't complete.")
            snap(arr)

    def snap(arr):
        print('*snap*')
        x = 0
        try:
            x = 0
            shuffle(arr)
            snap = len(arr)//2
            x = arr[:(snap)]
            order(x)
        except IndexError:
            if arr[i] > arr[i-1]:
                print('IndexError')
                order(x)

    if len(arr) <= 1:
        arr = arr[0]/2
        return arr
    else:
        return snap(arr)

'''
trumpSort O(0):
The array is always sorted.
Anyone who says otherwise is fake news.
'''
def trumpSort(arr):
    print(arr)
    value = print("The list is now sorted. It\'s so lucky for you that I was here to help before the brown people \n showed up to steal our right to bear arms or whatever")
    return arr

'''
LiberalSort:
Each element is declared to be out of order for moral reasons
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
    result = print(arr)
    return result

'''
Republican Sort:
Look at the first 5 elements.
Choose the highest one no matter how much lower that is than
other elements in the list past that.
Declare that the new top value, the list never gets sorted
because it would upset the newly declared top element.
'''
def republicanSort(arr):
    max = 0
    arr1= []
    arr1=arr[:5]
    for i in range(0,len(arr1)):
        if arr[i] >max:
            max = arr[i]
    print("The highest number in: "+str(arr)+"\n is... "+str(max)+"! Do you have a problem with that?")
