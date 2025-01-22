
def linear_prob(hash_table):
  n = len(hash_table)
  print("Insering using Linear Probing ")
  for i in range(n):
    ele = []
    print("Enter the Name: ")
    name = input()
    print("Enter the Telephone no: ")
    tel = int(input())
    ele.append(name)
    ele.append(tel)
    hash_val = tel % n
  
    if(hash_table[hash_val] == -1):
      hash_table[hash_val] = ele
    else:
      for j in range(1,n):
        new_hash = (hash_val + j)%n
        if(hash_table[new_hash] == -1):
          hash_table[new_hash] = ele
          break
        else:
          continue
          
def quad_prob(hash_table):
  n = len(hash_table)
  print("Insering using Quadratic Probing ")
  for i in range(n):
    ele = []
    print("Enter the Name: ")
    name = input()
    print("Enter the Telephone no: ")
    tel = int(input())
    ele.append(name)
    ele.append(tel)
    hash_val = tel % n
  
    if(hash_table[hash_val] == -1):
      hash_table[hash_val] = ele
    else:
      for j in range(1,n):
        new_hash = (hash_val + (j**2))%n
        if(hash_table[new_hash] == -1):
          hash_table[new_hash] = ele
          break
        else:
          continue
          
def prime(n):
  prime = 2
  for i in range(n):
    flag = 0
    for j in range(2,n)
      if(i%j == 0):
        flag = 1
            
    if(flag == 0):
      prime = i
    
  return prime      
          
def double_hashing(hash_table):
  n = len(hash_table)
  p = prime(n)
  print("Insering using Double Hashing ")
  for i in range(n):
    ele = []
    print("Enter the Name: ")
    name = input()
    print("Enter the Telephone no: ")
    tel = int(input())
    ele.append(name)
    ele.append(tel)
    hash_val = tel % n
  
    if(hash_table[hash_val] == -1):
      hash_table[hash_val] = ele
    else:
      hash_val2 = (p - (tel%p))%n
      for j in range(1,n):
        new_hash = (hash_val + hash_val2*j)%n
        if(hash_table[new_hash] == -1):
          hash_table[new_hash] = ele
          break
        else:
          continue
         
def display(hash_table):
  n = len(hash_table)  	    
  print("THE HASHTABLE IS AS FOLLOWS: ")
  for i in range(n):
    if(hash_table[i] != -1):
      print(hash_table[i][0],"  ",hash_table[i][1]) 
    else:
      print("NULL")   

def main():
  print("Enter the Number of Entries to be made: ")
  n = int(input())
  hash_table = [-1 for i in range(n)]
  print(hash_table)
  
  /*linear_prob(hash_table)
  display(hash_table)
  quad_prob(hash_table)
  display(hash_table)*/
  double_hashing(hash_table)
  display(hash_table)
  
main()

