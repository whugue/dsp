# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0

import copy as cp

"""
Given an int count of a number of donuts, return a string of the
form 'Number of donuts: <count>', where <count> is the number
passed in. However, if the count is 10 or more, then use the word
'many' instead of the actual count.
"""

def donuts(count):
    if count < 10:
        return "Number of donuts: %s" % (str(count))
    else:
        return "Number of donuts: many"

#Test Function
#print donuts(4)
print donuts(9)
print donuts(10)
print donuts(99)


"""
Given a string s, return a string made of the first 2 and the last
2 chars of the original string, so 'spring' yields 'spng'.
However, if the string length is less than 2, return instead the
empty string.
"""

def both_ends(s):
    if len(s) < 2:
        return ""
    else:
        return s[0:2]+s[(len(s)-2):len(s)]

#Test Function
print both_ends("Spring") #spng
print both_ends("Hello") #helo
print both_ends("a") # null
print both_ends("xyz") # xyyz

"""
Given a string s, return a string where all occurences of its
first char have been changed to '*', except do not change the
first char itself. e.g. 'babble' yields 'ba**le' Assume that the
 string is length 1 or more.
"""

def fix_start(s):
    temp_list=[]

    for i in range(0,len(s)):
        if i != 0 and s[i]==s[0]:
            temp_list.append("*")
        else:
            temp_list.append(s[i])

    return "".join(temp_list)

#Test Function
print fix_start("babble")
print fix_start("aardvark")
print fix_start("google")
print fix_start("donut")

"""
Given strings a and b, return a single string with a and b
separated by a space '<a> <b>', except swap the first 2 chars of
each string. Assume a and b are length 2 or more.
"""

def mix_up(a, b):
    new_a=b[0:2]+a[2:len(a)]
    new_b=a[0:2]+b[2:len(b)]

    return new_a+" "+new_b

#Test Function
print mix_up("mix", "pod")
print mix_up("dog", "dinner")
print mix_up("gnash", "sport")
print mix_up("pezzy", "firm")


"""
Given a string, if its length is at least 3, add 'ing' to its end.
Unless it already ends in 'ing', in which case add 'ly' instead.
If the string length is less than 3, leave it unchanged. Return
the resulting string.
"""

def verbing(s):
    if len(s) < 3:
        return s
    else:
        if s[(len(s)-3):len(s)]=="ing":
            return s+"ly"
        else:
            return s+"ing"

#Test Function
print verbing("hail")
print verbing("Swiming")
print verbing("do")


"""
Given a string, find the first appearance of the substring 'not'
and 'bad'. If the 'bad' follows the 'not', replace the whole
'not'...'bad' substring with 'good'. Return the resulting string.
So 'This dinner is not that bad!' yields: 'This dinner is
good!
"""

def not_bad(s):
    word_list=s.split()
    new_word_list=[]

    not_i=-1
    bad_i=-1

    for i in range(0,len(word_list)):
        if word_list[i].lower()=="not":
            not_i=i
        elif word_list[i].lower()=="bad":
            bad_i=i

    if not_i > 0 and bad_i > 0 and not_i < bad_i:
        new_word_list=word_list[0:not_i]
        new_word_list.append("good")
        new_word_list+=new_word_list[bad_i+1:]

    else:
        new_word_list=cp.copy(word_list)

    return " ".join(new_word_list)

#Test Function
print not_bad("This movie is not so bad") #This movie is good
print not_bad("This dinner is not that bad") #This dinner is good
print not_bad("This tea is not hot") #this tea is not hot
print not_bad("It's bad yet not") #It's bad yet not
print not_bad("This movie is not so bad I think") #This movie is good I think

"""
Consider dividing a string into two halves. If the length is even,
the front and back halves are the same length. If the length is
odd, we'll say that the extra char goes in the front half. e.g.
'abcde', the front half is 'abc', the back half 'de'. Given 2
strings, a and b, return a string of the form a-front + b-front +
a-back + b-back
"""

def front_back(a, b):
    front_a=""
    front_b=""
    back_a=""
    back_b=""

    if len(a) % 2 == 0:
        front_a=a[0:(len(a)/2)]
        back_a=a[(len(a)/2):len(a)]
    else:
        front_a=a[0:((len(a)/2)+1)]
        back_a=a[((len(a)/2)+1):len(a)]

    if len(b) % 2 == 0:
        front_b=b[0:(len(b)/2)]
        back_b=b[(len(b)/2):len(b)]
    else:
        front_b=b[0:((len(b)/2)+1)]
        back_b=b[((len(b)/2)+1):len(b)]

    return front_a+front_b+back_a+back_b

#Test Function
print front_back("abcd", "xy")
print front_back("abcde", "xyz")
print front_back("Kitten", "Donut")



