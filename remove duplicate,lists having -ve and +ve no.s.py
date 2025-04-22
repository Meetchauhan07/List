#50 random numbers in the range 1 and 30.Remove all duplicate values from list.
import random
lst = [random.randint(1, 30) for _ in range(50)]
print("Original:", lst)
lst = list(set(lst))
print("Unique:", lst)
'''
output:
Original: [7,20,6,4,3,2,26,8,13,12,16,3,6,4,18,24,6,15,23,20, 24, 28, 23, 9, 4, 16, 30, 2, 24, 29, 7, 30, 28, 26, 17, 30, 2, 17, 18, 8, 7, 2, 12, 7, 21, 2, 14, 18, 19, 22]
Unique: [2, 3, 4, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 28, 29, 30]
'''
#30 random no.s and put them in a list.Create two more lists having -ve and +ve no.s
import random
lst = [random.randint(-50, 50) for _ in range(30)]
print("All:", lst)
pos = [x for x in lst if x > 0]
neg = [x for x in lst if x < 0]
print("Positive:", pos)
print("Negative:", neg)
'''
output:
All: [-6, -9, 27, 9, 25, 4, 48, 5, -31, -10, -38, 18, -21, 33, 33, 21, -28, 47, 23, 11, -10, -44, 35, 0, -27, -43, -25, -39, -11, -22]
Positive: [27, 9, 25, 4, 48, 5, 18, 33, 33, 21, 47, 23, 11, 35]
Negative: [-6, -9, -31, -10, -38, -21, -28, -10, -44, -27, -43, -25, -39, -11, -22]

'''

