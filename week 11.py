import re

handle = open('regex_sum_2002804.txt')
context = handle.read()
lst = re.findall('[0-9]+', context)         #finall all the numbers in the context#
sum_lst = sum(map(int, lst))    #the sum of all the numbers in the context#
print(sum_lst)
