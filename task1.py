#!python3

"""
Create a list that contains the following strings, in order:
Cat
Fish
Dog
Bear
Turtle

Sort the list into alphabetical order and and then ask the user to enter a number corresponding
to the index of an element.  Print the element associated with that index.

inputs:
integer number

outputs:
string animal

example:
Enter the index for an animal:2
The animal at that index is Dog
"""



animals =("Cat","Fish","Dog","Bear","Turtle")
def SortTuple(animals): 
      
    n = len(animals) 
      
    for i in range(n): 
        for j in range(n-i-1): 
              
            if animals[j][0] > animals[j + 1][0]: 
                animals[j], animals[j + 1] = animals[j + 1], animals[j] 
                  
    return animals
     
          
print(SortTuple(animals))
