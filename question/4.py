array = [1,4,6,3,10,2,5,22,47,21,3,6]

'''
Fastest way

array.sort()
array.reverse()
print(array)
'''

#sorting whithout sort() 
array2 = []

while array:
        bigger_num = array[0]
        for item in array:
            if item > bigger_num:
                bigger_num = item
        array2.append(bigger_num)
        array.remove(bigger_num)

print(array2)