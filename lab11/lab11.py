from unittest import TestCase
import random

def quicksort(lst,pivot_fn):
    #print('x')
    qsort(lst,0,len(lst) - 1,pivot_fn)

def qsort(lst,low,high,pivot_fn):
    ### BEGIN SOLUTION
    #print('w')
    #print(lst)
    #print(low)
    #print(high)
    #print('k')
    if low < high: 
      p = pivot_fn(lst,low,high)
      qsort(lst,low,p-1,pivot_fn)
      qsort(lst,p+1,high,pivot_fn)
    ### END SOLUTION

def pivot_first(lst,low,high):
    ### BEGIN SOLUTION
    pivot = lst[low]
    i = low
    j = high
    #print("j")
    #print(lst[0])
    #print(low)
    #print(high)
    while True:
      #print(i)
      #print(j)
      if i>=j:
        break
      while i<len(lst):
        if lst[i]>=pivot:
          break
        i = i +1
        
      while j>=0:
        if lst[j]<=pivot:
          break
        j = j-1
      if i<j:
        #print ('i')
        #print(i)
        #print(j)
        lst[i],lst[j]=lst[j],lst[i]
    return j
    ### END SOLUTION

def pivot_random(lst,low,high):
    ### BEGIN SOLUTION
    n = random.randrange(0,high)
    pivot = lst[n]
    i = low
    j = high
    #print("j")
    #print(lst[0])
    #print(low)
    #print(high)
    while True:
      #print(i)
      #print(j)
      if i>=j:
        break
      while i<len(lst):
        if lst[i]>=pivot:
          break
        i = i +1
        
      while j>=0:
        if lst[j]<=pivot:
          break
        j = j-1
      if i<j:
        #print ('i')
        #print(i)
        #print(j)
        lst[i],lst[j]=lst[j],lst[i]
    return j
    ### END SOLUTION

def pivot_median_of_three(lst,low,high):
    ### BEGIN SOLUTION
    def med (lst,low,high):
      lo = lst[low]
      hi = lst[high]
      me = lst[(low+high)//2]
      if lo > me and lo<hi or lo < me and lo>hi:
        return lo
      elif me <hi and me>lo or me>hi and me<lo:
        return me
      else:
        return hi
    #n = random.randrange(0,high)
    pivot = med(lst,low,high)
    i = low
    j = high
    #print("j")
    #print(lst[0])
    #print(low)
    #print(high)
    while True:
      #print(i)
      #print(j)
      if i>=j:
        break
      while i<len(lst):
        if lst[i]>=pivot:
          break
        i = i +1
        
      while j>=0:
        if lst[j]<=pivot:
          break
        j = j-1
      if i<j:
        #print ('i')
        #print(i)
        #print(j)
        lst[i],lst[j]=lst[j],lst[i]
    return j
    ### END SOLUTION

################################################################################
# TEST CASES
################################################################################
def randomize_list(size):
    lst = list(range(0,size))
    for i in range(0,size):
        l = random.randrange(0,size)
        r = random.randrange(0,size)
        lst[l], lst[r] = lst[r], lst[l]
    return lst

def test_lists_with_pfn(pfn):
    lstsize = 20
    tc = TestCase()
    exp = list(range(0,lstsize))

    lst = list(range(0,lstsize))
    quicksort(lst, pivot_first)
    tc.assertEqual(lst,exp)

    lst = list(reversed(range(0,lstsize)))
    quicksort(lst, pivot_first)
    tc.assertEqual(lst,exp)

    for i in range(0,100):
        lst = randomize_list(lstsize)
        quicksort(lst, pfn)
        tc.assertEqual(lst,exp)

# 30 points
def test_first():
    test_lists_with_pfn(pivot_first)

# 30 points
def test_random():
    test_lists_with_pfn(pivot_random)

# 40 points
def test_median():
    test_lists_with_pfn(pivot_median_of_three)

################################################################################
# TEST HELPERS
################################################################################
def say_test(f):
    print(80 * "#" + "\n" + f.__name__ + "\n" + 80 * "#" + "\n")

def say_success():
    print("----> SUCCESS")

################################################################################
# MAIN
################################################################################
def main():
    for t in [test_first,
              test_random,
              test_median]:
        say_test(t)
        t()
        say_success()
    print(80 * "#" + "\nALL TEST CASES FINISHED SUCCESSFULLY!\n" + 80 * "#")

if __name__ == '__main__':
    main()
