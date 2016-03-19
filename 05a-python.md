# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both lists and tuples are Python data structures containing a sequence of values. Both lists and tuples can contain values of multiple types (e.g. stings, integers, and floats). Both are indexed, and specific elements within a list or tuple can be called using the object[index] syntax.

>> The major difference between lists and tuples is that tuples are immutable. Unlike with lists, you cannot add, delete, or modify elements in a tuple after the tuple has been created. The constant nature of tuples allow them to be used as keys in dictionaries. Python dictionaries use hash values to assign keys to specific lookup locations; thus, if keys were allowed to be mutable, modifications to keys may lead to Python re-assigning hash values for these keys, interfering with the dictionary's lookup algorithm and preventing the dictionary from functioning properly.

>> Another more subtle difference is that python lists are often used to store homogeneous elements (e.g. the number of GitHub commits to a specific repo per user), while tuples are often used to store heterogeneous elements (e.g. a specific GitHub user's user name and number of commits to a specific repo). Although using lists to store heterogeneous data is not syntactically incorrect, using tuples instead makes python code easier for other Python coders to understand.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Both lists and sets are python data structures containing a sequence of values of any type . Lists and sets are also both mutable (unless you specifically create an immutable set), allowing coders to add, remove, and modify elements. However, unlike a list, a set is unordered (i.e. indices are not assigned to the specific elements within a set). A set also cannot contain duplicate elements, while a list can. Further, while a set as a whole is mutable, the specific elements within a set must be hashable and hence immutable; elements of lists, by contrast, may be mutable. Finally, Python provides functions to test the union, intersection, and difference of elements in sets; no such functions are provided for lists.

>> Lists are best used when you need your data to be ordered. For example, when I did the GitHub coding challenge, I wanted to look the accumulating number of d3.js commits over time. In order to correctly calculate cumulating commits, I needed to write a function that would loop through the sequence and, for each week, add the total number of commits that week to the previous week's total commit count. In order to correctly calculate the accumulation for each week, I needed to loop through the data in order from earliest to latest. As such, I needed to use an ordered list. By contrast, I would use a set to test the which elements are common between two different sequences, as only sets support the python "union" function that returns elements in common between two sequences. Sets are also useful for de-duplicating data sequences-as a set cannot have duplicates, converting a list to a set automatically de-duplicates the data.

>> It is faster to test whether or not a specific element belongs to a set than to a list. Like dictionaries, sets use hash values to store elements in specific "slots". Hence, when testing for element membership in a set, Python only has to look for the element in that particular "slot" as defined by its hash value. On the other hand, when testing for element membership in a set, python has to look through the entire list.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Python's `lambda` is an operator used to create single-line, unnamed python functions. Lambda allows coders to create and implement simple functions without having to formally create a new function using a `def` command.

>> Lambda's are handy when using the `filter` function, as they allow coders to define a filtering condition within `filter` itself. For example, if I wanted to filter a list to only even values, I could write:

>> ` filtered = filter(lambda x: x%2==0, list)`

>> Within a `sorted` function, I could use a lambda operator in the key to sort the list by descending values, without using the reverse=true option. I would so this by multiplying each list value by -1 in the `key` statement:

>> `reversed=sorted(list, key=lambda x: x*-1)`

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> Python list comprehensions provide an easy way to create python lists using well-known mathematical(ish) notation. In many ways, list comprehensions provide the same functionality as `map` and `filter` functions using `lambdas`. For example:

>>`up=[x.upper() for x in ["a","b","c"]]` is equivalent to `up=map(lambda x: x.upper(), ["a","b","c"])`

>>`evens=[x for x in [1,2,3,4,5] if x%2==0]` is equivalent to `evens=filter(lambda x: x%2==0, [1,2,3,4,5])`

>>Both `map`/`filter` and list comprehensions have similar capabilities, and which method a python coder chooses to use is often a matter of personal preference. Personally, I prefer list comprehensions as I find the syntax to be more intuitive. Further, I find list comprehensions to be more general/ flexible - a coder can use the same list comprehension mechanisms to implement a variety of list functions (mapping, filtering, and more), while the `map` and `filter` functions provide only one capability each.

>>Set comprehensions work in the same way as list comprehensions, but syntactically use curly brackets as opposed to square ones. Since sets cannot contain duplicate entries, one can use set comprehension to remove duplicates from a list, like so:

>>`deduped={x for x in [1,1,2,3,3,3,4,5]}`

>>You can also use much of the same list/set comprehension logic to create dictionaries. For example, I can create a dictionary with each number 0-24 as keys and the square of the key as values like so:

>>`sqaures={x:x**2 for x in range(0,25)}`


---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> There are 937 days between 1/2/2013 and 7/28/2015

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> There are 513 days between 12/31/2013 and 05/28/2015

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> There are 7,850 days betwene 1/15/1994 and 7/14/2015


Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





