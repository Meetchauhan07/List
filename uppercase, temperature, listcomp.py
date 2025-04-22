#A list contains 5 strings. Convert all these strings to uppercase.
lst = ['apple', 'banana', 'mango', 'grape', 'peach']
for i in range(len(lst)):
    s = ''
    for ch in lst[i]:
        if 'a' <= ch <= 'z':
            s += chr(ord(ch) - 32)
        else:
            s += ch
    lst[i] = s
print(lst)
'''
output:
['APPLE', 'BANANA', 'MANGO', 'GRAPE', 'PEACH']
'''
#Convert list of temperatures in Fahrenheit degrees to equivalent Celsius degrees.
temps = [32, 68, 77, 104]
celsius = [(f - 32) * 5 / 9 for f in temps]
print("Celsius:", celsius)
'''
output:
Celsius: [0.0, 20.0, 25.0, 40.0]
'''
#Take two lists of numbers.Create third list of numbers from first list which are not there in 2nd list.
l1 = [1, 2, 3, 4, 5]
l2 = [3, 5, 7]
l3 = [x for x in l1 if x not in l2]
print("Result:", l3)
'''
output:
Result: [1, 2, 4]

'''
