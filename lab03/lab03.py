import urllib.request
import unittest
from typing import TypeVar, Callable, List

T = TypeVar('T')
S = TypeVar('S')



#################################################################################
# EXERCISE 1
#################################################################################
def mysort(lst: List[T], compare: Callable[[T, T], int]) -> List[T]:
    for x in range (1,len(lst)):
      pos = x
      comp = compare(lst[x-1],lst[x])
      while pos >0 and comp>0:
        temp = lst[pos]
        lst[pos] = lst[pos -1]
        lst[pos-1]=temp
        pos = pos -1
        comp = compare(lst[pos-1],lst[pos])
    return (lst)



def mybinsearch(lst: List[T], elem: S, compare: Callable[[T, S], int]) -> int:
    for x in range (0,len(lst)):
      comp = compare(lst[x],elem)
      if (comp == 0):
        return x
    return -1

class Student():
    """Custom class to test generic sorting and searching."""
    def __init__(self, name: str, gpa: float):
        self.name = name
        self.gpa = gpa

    def __eq__(self, other):
        return self.name == other.name

# 30 Points (total)
def test1():
    """Tests for generic sorting and binary search."""
    print(80 * "#" + "\nTests for generic sorting and binary search.")
    test1_1()
    test1_2()
    test1_3()
    test1_4()
    test1_5()

# 6 Points
def test1_1():
    """Sort ints."""
    print("\t-sort ints")
    tc = unittest.TestCase()
    ints = [ 4, 3, 7, 10, 9, 2 ]
    intcmp = lambda x,y:  0 if x == y else (-1 if x < y else 1)
    sortedints = mysort(ints, intcmp)
    tc.assertEqual(sortedints, [2, 3, 4, 7, 9, 10])

# 6 Points
def test1_2():
    """Sort strings based on their last character."""
    print("\t-sort strings on their last character")
    tc = unittest.TestCase()
    strs = [ 'abcd', 'aacz',  'zasa' ]
    suffixcmp = lambda x,y: 0 if x[-1] == y[-1] else (-1 if x[-1] < y[-1] else 1)
    sortedstrs = mysort(strs,suffixcmp)
    tc.assertEqual(sortedstrs, [ 'zasa', 'abcd', 'aacz' ])

# 6 Points
def test1_3():
    """Sort students based on their GPA."""
    print("\t-sort students on their GPA.")
    tc = unittest.TestCase()
    students = [ Student('Josh', 3.0), Student('Angela', 2.5), Student('Vinesh', 3.8),  Student('Jia',  3.5) ]
    sortedstudents = mysort(students, lambda x,y: 0 if x.gpa == y.gpa else (-1 if x.gpa < y.gpa else 1))
    expected = [ Student('Angela', 2.5), Student('Josh', 3.0), Student('Jia',  3.5), Student('Vinesh', 3.8) ]
    tc.assertEqual(sortedstudents, expected)

# 6 Points
def test1_4():
    """Binary search for ints."""
    print("\t-binsearch ints")
    tc = unittest.TestCase()
    ints = [ 4, 3, 7, 10, 9, 2 ]
    intcmp = lambda x,y:  0 if x == y else (-1 if x < y else 1)
    sortedints = mysort(ints, intcmp)
    tc.assertEqual(mybinsearch(sortedints, 3, intcmp), 1)
    tc.assertEqual(mybinsearch(sortedints, 10, intcmp), 5)
    tc.assertEqual(mybinsearch(sortedints, 11, intcmp), -1)

# 6 Points
def test1_5():
    """Binary search for students by gpa."""
    print("\t-binsearch students")
    tc = unittest.TestCase()
    students = [ Student('Josh', 3.0), Student('Angela', 2.5), Student('Vinesh', 3.8),  Student('Jia',  3.5) ]
    stcmp = lambda x,y: 0 if x.gpa == y.gpa else (-1 if x.gpa < y.gpa else 1)
    stbincmp = lambda x,y: 0 if x.gpa == y else (-1 if x.gpa < y else 1)
    sortedstudents = mysort(students, stcmp)
    tc.assertEqual(mybinsearch(sortedstudents, 3.5, stbincmp), 2)
    tc.assertEqual(mybinsearch(sortedstudents, 3.7, stbincmp), -1)




class PrefixSearcher():

    def __init__(self, document, k):
      pos = 0
      self.list = []
      suffixcmp = lambda x,y: 0 if x == y else (-1 if x < y else 1)
      for x in range(len(document)-k):
          val = document[pos:pos+k]
          self.list.append(val)
          pos = pos +1
      while (pos < len(document)):
        self.list.append(document[pos:])
        pos = pos + 1
      self.list = mysort(self.list,suffixcmp)
      

    def search(self, q): 
        suffixcmp = lambda x,y: 0 if x[0:len(y)] == y else (-1 if x < y else 1)
        if (mybinsearch(self.list,q,suffixcmp)!= -1):
          return True
        return False


# 30 Points
def test2():
    print("#" * 80 + "\nSearch for substrings up to length n")
    test2_1()
    test2_2()

# 15Points
def test2_1():
    print("\t-search in hello world")
    tc = unittest.TestCase()
    p = PrefixSearcher("Hello World!", 1)
    tc.assertTrue(p.search("l"))
    tc.assertTrue(p.search("e"))
    tc.assertFalse(p.search("h"))
    tc.assertFalse(p.search("Z"))
    tc.assertFalse(p.search("Y"))
    p = PrefixSearcher("Hello World!", 2)
    tc.assertTrue(p.search("l"))
    tc.assertTrue(p.search("ll"))
    tc.assertFalse(p.search("lW"))

# 20 Points
def test2_2():
    print("\t-search in Moby Dick")
    tc = unittest.TestCase()
    md_url = 'https://www.gutenberg.org/files/2701/2701-0.txt'
    md_text = urllib.request.urlopen(md_url).read().decode()
    p = PrefixSearcher(md_text[0:1000],4)
    tc.assertTrue(p.search("Moby"))
    tc.assertTrue(p.search("Dick"))

class SuffixArray():

    def __init__(self, document: str):
        self.suff = []
        self.numList = []

        numPos = 0
        suffixcmp = lambda x,y: 0 if x == y else (-1 if x < y else 1)
        for x in range (0,len(document)):
          self.suff.append(document[x:])
        self.suff = mysort(self.suff,suffixcmp)
        for t in range (0,len(document)):
          for y in range (0,len(document)-1):
            if document[y:]== self.suff[numPos]:
              self.numList.append(y)
          numPos = numPos +1
            
        


    def positions(self, searchstr: str):

        poses = []
        high = len(self.suff)
        low = 0
        mid = (high + low)//2
        while (low<high):  
          val = self.suff[mid]
          if val[0:len(searchstr)]<searchstr:
            low = mid+1
            
          elif val[0:len(searchstr)]>searchstr:
            high = mid-1
            
          else:
            val = self.suff[mid]
            #print (val[0:10])
            #print (self.numList[mid])
            break
            low = mid +1
          mid = (high + low)//2
        val = self.suff[mid]
        while val[0:len(searchstr)]==searchstr:
          mid = mid -1
          #print (val[0:10])
          val = self.suff[mid]
        #print (val[0:10])
        #print (self.numList[mid])
        mid = mid +1
        val = self.suff[mid]
        #print (valf[0:10])
        #print (self.numList[mid+2])
        while val[0:len(searchstr)]==searchstr:
          #print (val[0:10])
          #print (self.numList[mid])
          #print(mid)
          poses.append(mid)
          return(poses)
          #mid = mid +1
          #val = self.suff[mid]
        #return (poses)
        

    def contains(self, searchstr: str):  
        high = len(self.suff)
        low = 0
        mid = (high + low)//2
        while (low<high):  
          val = self.suff[mid]
          if val[0:len(searchstr)]<searchstr:
            low = mid+1
            
          elif val[0:len(searchstr)]>searchstr:
            high = mid-1
            
          else:
            return True
          mid = (high + low)//2
        val = self.suff[mid]
        if (high == low and val[0:len(searchstr)]==searchstr):
          return True
        return False


# 40 Points
def test3():
    """Test suffix arrays."""
    print(80 * "#" + "\nTest suffix arrays.")
    test3_1()
    test3_2()


# 20 Points
def test3_1():
    print("\t-suffixarray on Hello World!")
    tc = unittest.TestCase()
    s = SuffixArray("Hello World!")
    tc.assertTrue(s.contains("l"))
    tc.assertTrue(s.contains("e"))
    tc.assertFalse(s.contains("h"))
    tc.assertFalse(s.contains("Z"))
    tc.assertFalse(s.contains("Y"))
    tc.assertTrue(s.contains("ello Wo"))


# 20 Points
def test3_2():
    print("\t-suffixarray on Moby Dick!")
    tc = unittest.TestCase()
    md_url = 'https://www.gutenberg.org/files/2701/2701-0.txt'
    md_text = urllib.request.urlopen(md_url).read().decode()
    s = SuffixArray(md_text[0:1000])
    tc.assertTrue(s.contains("Moby Dick"))
    tc.assertTrue(s.contains("Herman Melville"))
    tc.assertEqual(s.positions("Moby Dick"), [427])


#################################################################################
# TEST CASES
#################################################################################
def main():
    test1()
    test2()
    test3()

if __name__ == '__main__':
    main()
