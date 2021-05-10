import urllib
import requests

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

"""def balance(data):
  lg = len(data[1])
  for x in data:
    if len(x)>lg:
      lg = len(x)
  lst1 = []
  for x in data:
    string = ""
    dif = lg - len(x)
    while dif>0:
      string = string +'!'
      dif = dif-1
    lst1.append(string+x)
  #print (lst1)
  return(lst1)
def largest(data):
  lg = len(data[1])
  for x in data:
    if len(x)>lg:
      lg = len(x)
  return lg """

def stringSort(data, pos):
  #print(data)
  #print(data)
  end = False
  dict = {}
  for y in range (0,257):
    dict[y]=[]
  for x in range (0,len(data)):
    y = data[x]
    #print(y)
    #y = y.hex()
    #print(data[x])
    #bo = bytes.fromhex(y)
    #asci = bo.decode("ASCII")
    try:
      r = y[len(y)-2-pos:len(y)-pos]
      #print(r)
      #print(data[x])
      v = int(r,16)
      #print(v)
      #print(dict[ord(r)])
      end = True
      #print (v)
      dict[v].append(y)
    except:
      dict[0].append(y)
  lst = []
  for t in range(0,257):
    if len(dict[t]) >0:
      #print(t)
      #l = dict[t]
      #r = l[::-1]
      temp = lst + dict[t] 
      #temp = lst + r
      lst = temp
  #print (lst)
  if end:
    
    #print("y")
    
    lst = stringSort(lst,pos+2)
  return (lst)





def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
  #bt = urllib.request.urlopen(book_url).read().decode()
  #book = bt.split()
  #l = largest(book)
  #print(l)
  b = book_to_words(book_url)
  lst = []
  for x in b:
    lst.append(x.hex())
  lst1 = stringSort(lst,0)
  lst2 = []
  for y in lst1:
    bo = bytes.fromhex(y)
    asci = bo.decode("ASCII")
    lst2.append(asci)
  return(lst2)
