# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


"""
Given a list of strings, return the count of the number of strings
where the string length is 2 or more and the first and last chars
of the string are the same.
"""

def match_ends(words):
    count=0

    for word in words:
        if len(word) >= 2 and word[0]==word[len(word)-1]:
            count +=1

    return count

#Test Functions
print match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
print match_ends(['', 'x', 'xy', 'xyx', 'xx'])
print match_ends(['aaa', 'be', 'abc', 'hello'])



"""
Given a list of strings, return a list with the strings in sorted
order, except group all the strings that begin with 'x' first.
e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].
"""

def front_x(words):
    ind=0
    words.sort()

    for word in words:
        if word[0].lower()=="x":
            words.remove(word)
            words.insert(ind,word)
            ind += 1

    return words

#Test Functions
print front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']) #['xaa', 'xzz', 'axx', 'bbb', 'ccc']
print front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']) # ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
print front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']) #['xanadu', 'xyz', 'aardvark', 'apple' 


def sort_last(tuples):
    """
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].

    >>> sort_last([(1, 3), (3, 2), (2, 1)])
    [(2, 1), (3, 2), (1, 3)]
    >>> sort_last([(2, 3), (1, 2), (3, 1)])
    [(3, 1), (1, 2), (2, 3)]
    >>> sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
    [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    """
    raise NotImplementedError



"""
Given a list of numbers, return a list where all adjacent equal
elements have been reduced to a single element, so [1, 2, 2, 3]
returns [1, 2, 3]. You may create a new list or modify the passed
in list.
"""

def remove_adjacent(nums):
    temp_list=[]

    for i in range(0,len(nums)):
        if i==0 or nums[i] != nums[i-1]:
            temp_list.append(nums[i])

    return temp_list


#Test Function;
print remove_adjacent([1, 2, 2, 3]) #[1, 2, 3]
print remove_adjacent([2, 2, 3, 3, 3]) # [2, 3]
print remove_adjacent([3, 2, 3, 3, 3]) #[3, 2, 3]
print remove_adjacent([]) #[]


"""
Given two lists sorted in increasing order, create and return a
merged list of all the elements in sorted order. You may modify
the passed in lists. Ideally, the solution should work in "linear"
time, making a single pass of both lists.
"""

def linear_merge(list1, list2):
    merged_list=[]

    i=0
    j=0

    while :
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i+=1
        else:
            merged_list.append(list2[j])
            j+=1




    if len(list1) < len(list2):
        short_list=list1
        long_list=list2
    else:
        short_list=list2
        long_list=list1

    j=0

    for i in range(0,len(long_list)):
        if long_list[i] >= short_list[j]:
            long_list.insert(i,short_list[j])
            j+=1

    return long_list

print linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']) #['aa', 'bb', 'cc', 'xx', 'zz']
print linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']) #['aa', 'bb', 'cc', 'xx', 'zz']
print linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']) #['aa', 'aa', 'aa', 'bb', 'bb']
 
