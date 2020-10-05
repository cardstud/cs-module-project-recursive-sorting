"""RECURSIVE SORTING - Lecture by Tom Tarpley 10/1/2020 6:30pm-8:30pm pacific

AGENDA:
======
1. Talk about Recursion
2. Countdown Debugging
3. Naive Recursive Fibonacci
4. Quick Sort

1. RECURSION
============
A recursive function must end; it does not go on forever - that causes stack overflow
Instead, it requires 3 elements:
    1. The function must call itself
    2. The function must have a base case, which is the simplest version of the problem in which
          the answer is defined or known already
    3. The function must move towards the base case

Purpose - Recursion is hard to get at first but once you understand it, you can write solutions to several problems much
              more cleanly and more quickly
        
    If you can divide a problem into sub-problems,  you can often reduce it to something that you can quickly solve in your head.
    Once you do that, you can use your recursive calls to solve the bigger and bigger versions of that problem for you.

    Recursion is hard so it is also very frequently found in interviews.

DEMONSTRATION 1: BASIC RECURSION
================================

Key Points:
    1. We must have a base case
    2. We must move to that base case or we'll get caught in a loop
    3. The time complexity of a function that recursively calls itself once is O(n)

Example: Counting down from a number - go down from n to zero:
-------
    1.  n-->0 where n = 10, 
    2. then print n
    3. then decrement n -= 1
    4. repeat until you get to the base case where n = 0
    5. use a while loop:  while n is > 0 

"""
# # iterative solution
# n = 10 
# def countdown_i(n):
#     while n>0:
#         print(n)
#         n -= 1
#     print(0, '....Blast off!', '\n')

# countdown_i(n)

# recursive solution

n =10
def countdown(n):
    # condition (base case)
    if n==0:
        print(0, '....Blast off!', '\n') 
    else:
        # body
        print(n)
        # decrement
        countdown(n-1)

countdown(n)

"""
2. COUNTDOWN DEBUGGING
======================

Used the debugging to view above code (4th option down on menu on left)
"""

"""
3. Naive Recursive Fibonacci (a recursive function)
===================================================

Key Points:
    1. It's like fizzbuzz; you're expected to know it by heart
    2. It's also useful; you can solve many combination/permutation problems with similar code
    3. This is an example of a naive approach - solving the problem with the first thing that comes to mind that's simple, or even child-like

Fibonacci sequence is calculated simply by starting with 0 and 1, then adding the last two numbers to get the next one:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

If we dig in a little deeper, we can see how recursion might be an excellent way to solve this. 

What's the 10th Fibonacci number?
    It's the 9th Fibonaci number plus the 8th
What's the 9th Fibonacci number?
    It's the 8th Fibonacci number plus the 7th and so on

Eventually we arrive at the 0th and 1st numbers, which are defined as 0 and 1.
Because this is the smallest version of the problem, with an arbitrary or defined answer, this is the base case.

We can use this understanding to plan our approach to the pseudocode.

Wherever you loop, you can do it recursively
"""


# base case 

def fibn(n): # label
    # condition (base case)
    if n == 0:
        return 0
    if n ==1:
        return 1
    
    # body is our decrement (in this case)
    # return the recursive call to fib(n) on n-1 and add it to the fib of n on n-2 
    # (just add these two together and return them)
    return fibn(n-1) + fibn(n-2)

# can do small numbers but large ones like 40 will either take forever or break it
print(fibn(7))

"""
4. Recursive Sorting
====================

Why are recursive sorting algorithms useful? While Insertion Sort works well if we are only sorting a few books, imagine we have hundreds oor
    thousands of books that need to be sorted according to filters set by the user.

    If we use Insertion Sort, or many of the other iterative sorting algorithms at our disposal, this process will take too long, our app will
        be slow and users will stop using it. We need another sorting algorithm.

Purpose: there are some recursive algorithms that take advantage of the "divide & conquer" strategy. We:
    1. divide a problem into subproblems(of the same type)
    2. solve the subproblems
    3. combine results of subproblems to get solution to original problem

Example, in the real world, there might be a post office where the postmaster has been tasked with the problem:
    * Deliver all of the mail

This is a large problem, as each post office is responsible for regions with many roads, many houses, and many possible routes in between them.
    However, the postmaster can break their region up into sub-regions and assign different employees to deliver the mail for each sub-region.
    Finding a route that allows all mail to be delivered in a particular sub-region is a smaller problem that we can solve more quickly.
    And by solving all of these individual pieces, we also solve the original problem.

In programming, there are many problems that can also be broken up in this way. Sorting is a good example. 
We can break up original datasets in different ways, sort subsets of data, and then put the sorted pieces back together again.

QUICKSORT:
=========
This is not the fastest sort (name fools you)

Lets say you have list of numbers to sort:
    L1 = [5,9,3,7,2,8,16]

    First choose a pivot point: we will choose 0 index (could use middle) but for now:  pivot = L1[0] = 5

    Take the numbers that are less than 5 and put on the left
    Take the numbers that are greater than 5 and put on the right

                               LHS = [3,2,1]     P=[5]      RHS = [9,7,8,6]

    Could call quicksort on LHS and we make pivot= 3        Could call quicksort on RHS and make 9 the pivot
        LHS [2,1]  P[3] [] (empty list on RHS)                       LHS [7,8,6]     P[9]     []  (empty list on RHS
   
    Recursive call: do it again                             Recusive call: do it again          
        LHS [1]    P[2]    [] RHS                                       LHS [6]      P[7]   [8]  RHS           

   Now its pushed up
    
    Left Hand side becomes: [1,2,3]          P[5]                       Right Hand side becomes: [6,7,8,9]

            This gives us as it is concatenated back: [1,2,3,5,6,7,8,9]
"""

# make a quick sort

# helper function conceptual partitioning
def partition(data):
    # takes in a single list and partitions it into 3 lists: (left, pivot, right)
    # create 2 empty lists (left, right) 
    left = []
    right = []

    # create a pivot list containing the first element of the data
    pivot = data[0]

    # for each value in our data starting at index 1
    for value in data[1:]:
        # check if value is less than or equal to the pivot 
        if value <= pivot:
            # append our value to the left list
            left.append(value)
        # otherwise (the value must be greater than the pivot)
        else:
            # append our value to the right list
            right.append(value)

    # returns the tuple of (left, pivot, right)
    return left, pivot, right 

# quick sort that uses the partitioned data
def quicksort(data):
    # if empty list, return empty list (nothing there to sort) which is our base case
    if data == []:  # if data equal to an empty list (base case)
        return data 

    # partition the data into 3 variables (left, pivot, right)
    left, pivot, right = partition(data)

    # recursive call to quicksort using the left
    # recursive call to quicksort using the right
    # return the concatenation quicksort of the LHS + pivot + quicksort of RHS
    return quicksort(left) + [pivot] + quicksort(right)


print(quicksort([5,9,3,7,2,8,1,6]))