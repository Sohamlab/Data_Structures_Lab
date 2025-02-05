# Chaining in Hashtable 

hashtable = []
bucket = []

def create():
  print("Enter the Number of elements to be entered: ")
  n = int(input())
  
  for i in range(n):
    hashtable.append([None,-1])
    bucket.append(-1)
    
def insert(key):
  n = len(hashtable)
  hashv = key % n
  
  if(hashtable[hashv][0] == None):
    hashtable[hashv][0] = key
    bucket[hashv] = hashv
    
  else:
    for i in range(n):
      new_hash = (hashv + i) % n
      if(hashtable[new_hash][0] == None):
        if(bucket[hashv] != -1):
          hashtable[bucket[hashv]][1] = new_hash
          
        bucket[hashv] = new_hash
        hashtable[new_hash][0] = key
        break

def display(hashtable):
  n = len(hashtable)
  print("The Hashtable is as Follows: ")
  for i in range(n):
    print(hashtable[i][0]," - ",hashtable[i][1])

def search(hashtable,key):
  flag = 0
  n = len(hashtable)
  hashv = key % 10
  if(hashtable[hashv][0] == key):
    print("element found at index - ",hashv)
    flag = 1
    
  else:
    link = hashtable[hashv][1]
    while(link != -1):
      if(hashtable[link][0] == key):
        print("Element found at index - ",link)
        flag = 1
        break
      else:
        link = hashtable[link][1]

  if(flag):
    return
  else:
    for i in range(n):
      if(hashtable[hashv][0] == key):
        print("Element found at index - ",hashv)
    print("Element not Found")
      

  
def main():
  create()
  insert(10)
  insert(11)
  insert(21)
  insert(31)
  insert(42)
  display(hashtable)
  search(hashtable,31)
  search(hashtable,42)

main()
