'''
inspo: https://www.reddit.com/r/cscareerquestions/comments/bojrrb/hiring_managers_what_projects_stood_out_in_a_bad/enhmnu6/?utm_source=share&utm_medium=web2x
This all came from a post from reddit user GhostBond. All funny comments below
are theirs. The code is mine.
A lot of this could be improved. I've only been working in Python for 6 months.
If you see something that could be improved please let me know.
Thanks to u/GhostBond for the idea! This was fun practice. :)
'''

# print('''
# Please select a sort:
# 1.  Optimization
# 2.  Big O Minus 1
# 3.  Stalin
# 4.  Genghis Khan
# 5.  Hitler
# 6.  Communist
# 7.  Capitalist
# 8.  Thanos
# 9.  Trump
# 10. Liberal
# 11. Republican
#     ''')

'''
O(1) Optimization Sort:
Delete the whole list, an empty list is sorted list.
'''

def optimizationSort(arr):
    print('Optimization Sort:')
    print('List: 'arr)
    arr =  ''
    print('All Done:',arr, '[  ]')
    return arr



'''
O(-1) Sort:
Fuck off, I'm not sorting your list.
'''
def ominus1Sort(arr):
    print('Big O Minus 1 Sort:')
    print('List: 'arr)
    print("Fuck Off! I'm not sorting your list")



'''
StalinSort:
You iterate down the list of elements checking if they're in order.
An element which is out of order is eliminated.
At the end you have a sorted list.
(this one took awhile to figure out! -ns)
'''
def stalinSort(arr):
    print('Stalin Sort:')
    print('List: 'arr)
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
    result = print(arr2)
    return result

'''
GenghisKhanSort:
Delete all elements except for the first,
repopulate the list with successors of the first element.
'''
def gengkhiskhanSort(arr):
    print('Genkhis Khan Sort:')
    print('List: 'arr)

    gk = ''
    for i in range(0,len(arr)):
        gk = arr[0]
        for j in range(0,len(arr)):
            arr[i] = gk
    result = print(arr)
    return result

'''
HitlerSort:
Pick the value that you like,
declare it as the highest,
and then delete all other values.
'''
def hitlerSort(arr):
    print('Hitler Sort:')
    print('List: 'arr)
    value=input("Which value do you like the most? ")
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            arr[i] = value
    print('Excellent choice, Mr. Hitler \n Here\'s your new list: ')
    result = print(arr)
    return result


'''
AmishSort:
Turn off computer, then you won't even need sorting.
'''
#### Commented out due to safety concerns
####
#### def amishSort(arr):
####     print('Amish Sort:')
####     print('List: 'arr)
####     import os
####     os.system("shutdown /s /t 1")
####

'''
Communist Sort:
Wait for the list to sort itself.
Act upset when it doesn't happen until a tyrannical dictatorship shows up
and forces the list into sorted order.
'''
def communistSort(arr):
    import time
    print('Communist Sort:')
    print('List: 'arr)

    value = input("Is the vanguard ready yet? (y/n)")
    if value == 'n':
        print(1)
        print("Man, I can't wait for Communism to start.")
        time.sleep(2)
        communistSort(arr)
    elif value == 'y':
        print(2)
        print('Comrades, it is time!')
        for i in range(len(arr)):
            min = i
            for j in range(i + 1, len(arr)):
                if arr[min] > arr[j]:
                    min = j
            arr[i],arr[min] = arr[min], arr[i]
    else:
        print(3)
        print("I\'m sorry what?")
        communistSort(arr)
    print(arr)

list1 = [20,40,50,10,60,10]


'''
# TODO: THIS
# TODO: THIS
# TODO: THIS
Capitalist Sort:
The first 3 elements in the list remain in their position,
every iteration through they subtract 1 from all of the other elements and add it to themselves,
until the rest of the list is destroyed and they are the only ones left.
'''

def capitalistSort(arr):
    print('Capitalist Sort:')
    print('List: 'arr)
    titans = [] #of industry
    counter = 0
    try:
        for i in arr[0:3]:
            titans.append(arr[i])
            print(arr)
    except IndexError:
        print("IndexError")

# capitalistSort(list1)

'''
Thanos Sort: Randomly delete half the elements in the list over
and over until the list happens to be sorted.
'''

def thanosSort(arr):
    from random import shuffle
    print('Thanos Sort:')
    print('List: 'arr)
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
trump Sort:
The array is always sorted.
Anyone who says otherwise is fake news.
'''
def trumpSort(arr):
    print('Trump Sort:')
    print('List: 'arr)
    value = print('''
     The list is now sorted.
     It\'s so lucky for you that I was here to help
     before brown people came and murdered your entire family or whatever.
     ''',arr)
    return arr

'''
Liberal Sort:
Each element is declared to be out of order for moral reasons and committing moral crimes,
elements have 1 subtracted from them at semi-random.
The sort never actually ends as the narrative needs to keep going to maintain political power.
'''

def liberalSort(arr):
    from random import randrange,randint
    print('Liberal Sort')
    print("Morally, I just don't know about these ",arr)
    counter = 0
    rand = randint(1,101)

    print(rand)
    while counter <= rand:
        for i in range(0,randrange(len(arr)+1)):
            arr[i] -= 1
            counter += 1
    result = print("I hope everyone's learned a valuable lesson about sharing and the value of being nice to each other.",arr)
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
    print('Republican Sort:')
    print('List: 'arr)
    max = 0
    arr1= []
    arr1=arr[:5]
    for i in range(0,len(arr1)):
        if arr[i] > max:
            max = arr[i]
    result = print("The highest number in: ",arr,"\n is...",max,"!")
    return result



list1 = [5,4,6,8,9,1,2,55,1,1337,1336,1338]
hitlerSort(list1)

# optimizationSort(list1)
# ominus1Sort(list1)
# stalinSort(list)
# gengkhiskhanSort(list1)
# hitlerSort(list1)
# ######## #amisishSort(list1)
# communistSort(list1)
# thanosSort(list1)
# trumpSort(list1)
# liberalSort(list1)
# republicanSort(list1)
