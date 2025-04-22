#odd and even used  with random
import random

odd = [random.randrange(1, 100, 2) for _ in range(5)]
even = [random.randrange(0, 100, 2) for _ in range(4)]
print("Odd:", odd)
print("Even:", even)

odd[2:3] = even  # Replace 3rd odd with all evens
print("Modified List:", odd)

flat_sorted = sorted(odd)
print("Flattened & Sorted:", flat_sorted)
'''
output:
Odd: [11, 59, 79, 23, 81]
Even: [10, 4, 12, 54]
Modified List: [11, 59, 10, 4, 12, 54, 23, 81]
Flattened & Sorted: [4, 10, 11, 12, 23, 54, 59, 81]
'''


#20 random no.s stored in a list,user input,print position of all occurrences
import random
lst = [random.randint(1, 100) for _ in range(20)]
print(lst)
n = int(input("Enter number to search: "))
for i in range(len(lst)):
    if lst[i] == n:
        print("Found at index", i)
'''
output:
[56, 37, 63, 20, 33, 95, 20, 66, 48, 78, 67, 17, 74, 86, 38, 18, 1, 52, 87, 39]
Enter number to search: 52
Found at index 17
'''


        
